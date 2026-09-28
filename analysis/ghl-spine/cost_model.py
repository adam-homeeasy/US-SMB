"""GHL spine cost model: all three lines, per plan option, at 1 to 100 paying clients per line.

Run: python3 cost_model.py   (writes 05-cost-model.csv and prints markdown tables)
Every input below is either a GHL price from 01-GHL-TEARDOWN.md (checked 28 Sep 2026)
or a base-case assumption taken from the line reports 02, 03, 04. Change inputs here, not in the CSV.
"""
import csv
from pathlib import Path

N_VALUES = [1, 10, 25, 50, 100]

# GHL plan options, monthly USD [ghl-pricing-page, via 01]
PLANS = {
    "Starter $97": {"fee": 97, "max_subaccounts": 3, "agencies": 1},
    "Unlimited $297": {"fee": 297, "max_subaccounts": None, "agencies": 1},
    # Agency Pro only earns its keep with SaaS mode, which needs a US entity first.
    # US entity running cost: Atlas registered agent $100/yr [stripe-docs, via 01]
    # plus about $50/mo US bookkeeping and Indian ODI/FEMA filings [assumption].
    "Agency Pro $497 + US entity": {"fee": 497 + 100 / 12 + 50, "max_subaccounts": None, "agencies": 1},
    "3 agencies x Unlimited $891": {"fee": 891, "max_subaccounts": None, "agencies": 3},
}

# RevLabs client mix per N paying clients [assumption]
REVLABS_MIX = {"track_b": 0.6, "growth": 0.3, "full": 0.1}

# Internal (non-paying) sub-accounts, monthly usage in USD [assumption, from 03 and 04]
INTERNAL = {
    "RevLabs prospecting, Illinois calling": ("revlabs", 25.0),  # ~600 call min out, 2 numbers, A2P $10, 3k emails
    "RevLabs Texas email lane (no number)": ("revlabs", 3.0),
    "Sandbox ZZ-TEST-Spine-Analysis": ("revlabs", 0.0),
    "HomeEasy (Leasify test bed)": ("leasify", 0.0),  # usage billed to HomeEasy, outside this model
}


def leasify_client(n):
    """Per client per month, base case from 02-LEASIFY-FIT.md section 5 (plan share excluded)."""
    # 20k SMS segments (20 per lead, red team 07 correction of 02's 12), 6k emails, 2 numbers,
    # 6k AI replies, 100 Voice AI min. 02's $172.55 at 12 segments + 8,000 x $0.0115.
    usage = 172.55 + 8000 * 0.0115
    addons = 25.33          # A2P $10 campaign + $64 brand over 12 months + Workflow Pro $10
    integrations = 50 / n + 2   # shared Postgres/n8n/matching infra, $50/mo fixed + $2 per client [assumption]
    labour = 40.0 + 4.0     # 5 h at $8 platform ops + 0.5 h monthly compliance audit (07); service delivery excluded
    build = 200 / n         # 300 h build at $8 = $2,400, spread over 12 months
    return usage + addons + integrations + labour + build


def revlabs_costs():
    """Per client per month by product, base case from 03-REVLABS-FIT.md section 5 (plan share excluded)."""
    return {
        "track_b": 8.14,    # no sub-account: domain, payment fee, 0.75 h labour
        "growth": 22.19 + 4.0,  # 03 base + 0.5 h monthly compliance audit (07)
        "full": 45.22 + 4.0,    # 03 ongoing run cost after the one-off $999 build + audit
    }


REVLABS_PRICE = {"track_b": 29, "growth": 99, "full": 149}  # Full system care fee set at $149 in 00-VERDICT
TF_PRICE = 249
TF_COST_TO_SERVE = 12.85 + 2.00  # context cost to serve + first A2P campaign (04 section 5)
LEASIFY_PRICE = 499


def scenario(plan_name, plan, n):
    rl = REVLABS_MIX
    rl_counts = {k: n * v for k, v in rl.items()}
    rl_ghl_clients = rl_counts["growth"] + rl_counts["full"]

    # Sub-accounts by line (verdict architecture: see 00-VERDICT.md)
    subs = {
        "leasify": n + 1,                 # one per client + HomeEasy
        "revlabs": rl_ghl_clients + 3,    # Growth/Full clients + Illinois, Texas, sandbox
        "tf": 0,                          # TF: don't use GHL for now (00-VERDICT)
    }
    total_subs = sum(subs.values())
    feasible = plan["max_subaccounts"] is None or total_subs <= plan["max_subaccounts"]

    fee = plan["fee"]
    share = {line: fee * s / total_subs for line, s in subs.items()}
    internal = {"leasify": 0.0, "revlabs": 0.0, "tf": 0.0}
    for _, (line, cost) in INTERNAL.items():
        internal[line] += cost

    rc = revlabs_costs()
    lines = {
        "Leasify": {
            "clients": n,
            "revenue": n * LEASIFY_PRICE,
            "plan_share": share["leasify"],
            "other_cost": n * leasify_client(n) + internal["leasify"],
        },
        "RevLabs": {
            "clients": n,
            "revenue": sum(rl_counts[k] * REVLABS_PRICE[k] for k in rl_counts),
            "plan_share": share["revlabs"],
            "other_cost": sum(rl_counts[k] * rc[k] for k in rl_counts) + internal["revlabs"],
        },
        "TF": {
            "clients": n,
            "revenue": n * TF_PRICE,
            "plan_share": share["tf"],
            "other_cost": n * TF_COST_TO_SERVE + internal["tf"],
        },
    }
    rows = []
    for name, d in lines.items():
        total = d["plan_share"] + d["other_cost"]
        rows.append({
            "plan": plan_name, "clients_per_line": n, "line": name,
            "feasible": "yes" if feasible else f"no: needs {total_subs:.0f} sub-accounts",
            "sub_accounts_total": round(total_subs),
            "revenue_month": round(d["revenue"], 2),
            "ghl_plan_share": round(d["plan_share"], 2),
            "other_cost": round(d["other_cost"], 2),
            "total_cost": round(total, 2),
            "cost_per_client": round(total / d["clients"], 2),
            "margin": round(d["revenue"] - total, 2),
            "margin_pct": round(100 * (d["revenue"] - total) / d["revenue"], 1) if d["revenue"] else None,
        })
    return rows


def main():
    out = []
    for pname, plan in PLANS.items():
        for n in N_VALUES:
            out.extend(scenario(pname, plan, n))

    path = Path(__file__).with_name("05-cost-model.csv")
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)

    # Markdown: cost per client and margin %, per plan, per line
    for pname in PLANS:
        print(f"\n#### {pname}\n")
        print("| Line | " + " | ".join(f"N={n}" for n in N_VALUES) + " |")
        print("|---|" + "---|" * len(N_VALUES))
        for line in ["Leasify", "RevLabs", "TF"]:
            cells = []
            for n in N_VALUES:
                r = next(r for r in out if r["plan"] == pname and r["clients_per_line"] == n and r["line"] == line)
                if r["feasible"] != "yes":
                    cells.append("not possible")
                else:
                    cells.append(f"${r['cost_per_client']:,.2f} ({r['margin_pct']:.0f}%)")
            print(f"| {line} | " + " | ".join(cells) + " |")
        tot = []
        for n in N_VALUES:
            rs = [r for r in out if r["plan"] == pname and r["clients_per_line"] == n]
            if rs[0]["feasible"] != "yes":
                tot.append("not possible")
                continue
            rev = sum(r["revenue_month"] for r in rs)
            cost = sum(r["total_cost"] for r in rs)
            tot.append(f"${rev - cost:,.0f} ({100 * (rev - cost) / rev:.0f}%)")
        print("| **All three, margin/month** | " + " | ".join(tot) + " |")


if __name__ == "__main__":
    main()
