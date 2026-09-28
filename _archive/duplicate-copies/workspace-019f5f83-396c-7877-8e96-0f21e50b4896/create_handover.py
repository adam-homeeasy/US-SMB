
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import datetime

doc = Document()

# ── Page setup ──
for section in doc.sections:
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)

style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(10.5)
font.color.rgb = RGBColor(0x33, 0x33, 0x33)

def add_heading_styled(text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
    return h

def add_table_with_style(headers, rows, col_widths=None):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = 'Light Grid Accent 1'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Header row
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.bold = True
                run.font.size = Pt(9)
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        # Dark background for header
        shading = OxmlElement('w:shd')
        shading.set(qn('w:fill'), '1F4E79')
        shading.set(qn('w:val'), 'clear')
        cell.paragraphs[0].paragraph_format.space_before = Pt(2)
        cell.paragraphs[0].paragraph_format.space_after = Pt(2)
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        tcPr.append(shading)

    # Data rows
    for ri, row_data in enumerate(rows):
        for ci, val in enumerate(row_data):
            cell = table.rows[ri + 1].cells[ci]
            cell.text = str(val)
            for p in cell.paragraphs:
                for run in p.runs:
                    run.font.size = Pt(9)
            cell.paragraphs[0].paragraph_format.space_before = Pt(1)
            cell.paragraphs[0].paragraph_format.space_after = Pt(1)

    if col_widths:
        for i, w in enumerate(col_widths):
            for row in table.rows:
                row.cells[i].width = Inches(w)

    return table

def add_bullet(text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    if bold_prefix:
        run = p.add_run(bold_prefix)
        run.bold = True
        run.font.size = Pt(10.5)
        p.add_run(text)
    else:
        p.add_run(text)
    return p

def add_callout(text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.3)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(f"💡 {text}")
    run.font.size = Pt(10)
    run.font.italic = True
    run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)

# ═══════════════════════════════════════════════════════════════
# COVER PAGE
# ═══════════════════════════════════════════════════════════════
doc.add_paragraph()
doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("HANDOVER DOCUMENT")
run.font.size = Pt(14)
run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
run.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("India → US Local SMB Services\nMarket Opportunity Analysis")
run.font.size = Pt(26)
run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
run.bold = True

doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("161 Services × 34 Business Verticals × 5 Opportunity Tiers")
run.font.size = Pt(13)
run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

doc.add_paragraph()
doc.add_paragraph()

meta_data = [
    ("Prepared for", "Strategy & Business Development Team"),
    ("Document Type", "Handover / Analysis Guide"),
    ("Date", datetime.date.today().strftime("%B %d, %Y")),
    ("Version", "3.0"),
    ("Companion File", "India_US_SMB_Services_Analysis.xlsx"),
]

table = doc.add_table(rows=len(meta_data), cols=2)
for i, (label, value) in enumerate(meta_data):
    table.rows[i].cells[0].text = label
    table.rows[i].cells[1].text = value
    for p in table.rows[i].cells[0].paragraphs:
        for run in p.runs:
            run.font.bold = True
            run.font.size = Pt(10)
    for p in table.rows[i].cells[1].paragraphs:
        for run in p.runs:
            run.font.size = Pt(10)
table.alignment = WD_TABLE_ALIGNMENT.CENTER

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# TABLE OF CONTENTS
# ═══════════════════════════════════════════════════════════════
add_heading_styled("Table of Contents", 1)

toc_items = [
    "1. Executive Summary",
    "2. Document Structure & Companion Files",
    "3. Scope & Methodology",
    "4. Tier Framework Explanation",
    "5. Key Findings",
    "6. Tier-by-Tier Strategic Analysis",
    "   6.1 Platinum Tier — Immediate Launch",
    "   6.2 Gold Tier — High Priority",
    "   6.3 Silver Tier — Viable with Strategy",
    "   6.4 Bronze Tier — Niche Down Required",
    "   6.5 Red Flag Tier — Avoid or Bundle",
    "7. Vertical Deep-Dives: Top 10 Verticals",
    "8. Automation vs. Competition Matrix",
    "9. Risk Assessment",
    "10. Go-to-Market Recommendations",
    "11. Recommended First 90-Day Plan",
    "12. Open Questions for Leadership",
    "13. Appendix: Data Sources & Assumptions",
]
for item in toc_items:
    p = doc.add_paragraph(item)
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# 1. EXECUTIVE SUMMARY
# ═══════════════════════════════════════════════════════════════
add_heading_styled("1. Executive Summary", 1)

doc.add_paragraph(
    "This document provides a comprehensive handover for analyzing the market opportunity of "
    "delivering services from India to US-based local small and medium businesses (SMBs). The analysis "
    "covers 161 distinct services/products across 34 business verticals — ranging from universal offerings "
    "(digital marketing, back-office, technology) to highly specialized industry services (solar design, "
    "mortgage processing, HVAC dispatching, pet grooming systems)."
)

doc.add_paragraph(
    "Each service has been evaluated on five dimensions: automation potential, automation confidence, "
    "degree of automation, competitive intensity, and ticket size. These have been combined into a "
    "composite Opportunity Score (0–120) and mapped to a 5-tier framework — from Platinum (immediate launch) "
    "to Red Flag (commodity/avoid)."
)

add_heading_styled("Headline Numbers", 2)

add_table_with_style(
    ["Metric", "Value"],
    [
        ["Total Services/Products Analyzed", "161"],
        ["Total Business Verticals Covered", "34"],
        ["Platinum Tier (Immediate Launch)", "63 services (39.1%)"],
        ["Gold Tier (High Priority)", "46 services (28.6%)"],
        ["Silver Tier (Viable with Strategy)", "26 services (16.1%)"],
        ["Bronze Tier (Niche Down Required)", "17 services (10.6%)"],
        ["Red Flag (Commodity / Avoid)", "9 services (5.6%)"],
        ["Services with ≥75% Automation Potential", "80 services (49.7%)"],
        ["Low Competition Opportunities", "40 services (24.8%)"],
    ],
    col_widths=[3.5, 2.5]
)

doc.add_paragraph()
doc.add_paragraph(
    "The core finding: 67.7% of identified services fall into Platinum or Gold tier — representing "
    "a massive addressable market for India-based service providers. The highest-value clusters are in "
    "appointment/route optimization systems, compliance documentation, customer communication automation, "
    "and back-office processing for regulated industries."
)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# 2. DOCUMENT STRUCTURE
# ═══════════════════════════════════════════════════════════════
add_heading_styled("2. Document Structure & Companion Files", 1)

doc.add_paragraph("This handover package consists of:")

add_bullet("This document", "Handover & Analysis Guide (.docx): ")
doc.add_paragraph("Strategic analysis, tier explanations, recommendations, and action items for the team.", style='List Bullet 2')

add_bullet("Master data spreadsheet", "India_US_SMB_Services_Analysis.xlsx: ")
doc.add_paragraph("3 sheets — Main Analysis (161 rows, 13 columns, color-coded), Summary Dashboard (tier distributions, top opportunities), Legend & Notes (scoring methodology, definitions).", style='List Bullet 2')

add_bullet("Python generation scripts", "create_table_v3.py: ")
doc.add_paragraph("Reproducible script to regenerate or modify the analysis with updated data.", style='List Bullet 2')

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# 3. SCOPE & METHODOLOGY
# ═══════════════════════════════════════════════════════════════
add_heading_styled("3. Scope & Methodology", 1)

add_heading_styled("3.1 What We Analyzed", 2)
doc.add_paragraph(
    "Every service or product that an India-based team could realistically deliver remotely to a "
    "US local SMB. This includes:"
)
add_bullet("Universal services applicable to all SMBs (digital marketing, back-office, technology)")
add_bullet("Industry-specific services (e.g., solar panel design, dental billing, Xactimate estimating)")
add_bullet("Emerging/cross-cutting services (AI voice agents, ADA compliance, document automation)")
add_bullet("Both recurring (SaaS/retainer) and project-based services")

add_heading_styled("3.2 How We Scored", 2)
doc.add_paragraph("Each service received scores on 5 parameters:")

add_table_with_style(
    ["Parameter", "Scale", "What It Measures"],
    [
        ["Automation Potential", "0–100%", "% of service deliverable automatable with current AI/tech tools"],
        ["Automation Confidence", "Very High / High / Medium / Low", "How achievable this automation is TODAY (not theoretical)"],
        ["Degree of Automation", "Qualitative (CAN vs CANNOT)", "Detailed breakdown of automatable vs. human-dependent tasks"],
        ["Competitive Intensity", "Very High / High / Medium / Low", "Market saturation — number and strength of existing providers"],
        ["Ticket Size", "USD range", "Typical price charged to US SMB clients"],
    ],
    col_widths=[1.5, 1.5, 3.5]
)

doc.add_paragraph()

add_heading_styled("3.3 Composite Opportunity Score", 2)
doc.add_paragraph("The 5 parameters are combined into a single Opportunity Score using this formula:")

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("Score = Automation %  +  Competition Modifier  +  Confidence Modifier")
run.font.bold = True
run.font.size = Pt(12)
run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)

doc.add_paragraph()

add_table_with_style(
    ["Modifier", "Low / Very High", "Medium / High", "High / Medium", "Very High / —"],
    [
        ["Competition Modifier", "+15", "0", "−12", "−25"],
        ["Confidence Modifier", "—", "0", "+5", "+10"],
    ],
    col_widths=[1.8, 1.2, 1.2, 1.2, 1.2]
)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("Final Score clamped between 0–120")
run.font.italic = True
run.font.size = Pt(9)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# 4. TIER FRAMEWORK
# ═══════════════════════════════════════════════════════════════
add_heading_styled("4. Tier Framework Explanation", 1)

doc.add_paragraph(
    "The Opportunity Score maps to a 5-tier framework that provides clear strategic guidance "
    "for decision-making:"
)

add_table_with_style(
    ["Tier", "Label", "Score", "Strategic Meaning", "Recommended Action"],
    [
        ["⭐ Platinum", "Immediate Launch", "≥ 85",
         "High automation + Low competition + High confidence. The service is mostly automatable, "
         "few competitors offer it from India, and the tools exist today.",
         "Build service offering NOW. Assign team. Start selling this quarter."],
        ["⭐ Gold", "High Priority", "70 – 84",
         "Strong opportunity with minor caveats. Either moderate competition or slightly lower "
         "automation — but clearly viable.",
         "Prioritize for next quarter. Build in parallel with Platinum services."],
        ["⭐ Silver", "Viable with Strategy", "52 – 69",
         "Solid opportunity but requires differentiation. Either automation is partial or "
         "competition exists but isn't saturated.",
         "Enter with niche positioning or bundled offering. Test before scaling."],
        ["⭐ Bronze", "Niche Down", "38 – 51",
         "Challenging. Low automation potential, high competition, or both. Commodity pricing "
         "pressure is real.",
         "Only enter with a unique angle, vertical specialization, or as part of a bundle."],
        ["⚠️ Red Flag", "Commodity / Avoid", "< 38",
         "Saturated market + hard to automate. Race-to-bottom pricing. AI tools are "
         "eliminating the human value layer.",
         "Avoid as standalone offering. Consider bundling or exiting."],
    ],
    col_widths=[0.9, 0.9, 0.6, 2.2, 2.0]
)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# 5. KEY FINDINGS
# ═══════════════════════════════════════════════════════════════
add_heading_styled("5. Key Findings", 1)

add_heading_styled("5.1 The Opportunity Is Massive", 2)
doc.add_paragraph(
    "67.7% of the 161 services analyzed score Platinum or Gold. This means that for roughly "
    "two-thirds of possible services, an India-based team can deliver high value with strong "
    "automation leverage and manageable competition."
)

add_heading_styled("5.2 The Sweet Spot: Schedule/Routing + Compliance + Communication", 2)
doc.add_paragraph(
    "Three service categories consistently appear as Platinum across multiple verticals:"
)
add_bullet("Appointment/Route Optimization", " — 85%+ automation, low competition in niche verticals (pool, pest, pet, cleaning, HVAC). SMBs in route-based businesses desperately need this; 15-30% drive-time reduction = direct profit.")
add_bullet("Compliance & Regulatory Documentation", " — 65-80% automation, very low competition. Contractors, daycares, funeral homes, pest control, and OSHA compliance all have complex paperwork that no one wants to manage remotely. Huge pain point.")
add_bullet("Automated Customer Communication", " — 80-90% automation, low-medium competition. Reminders, reactivation campaigns, post-service follow-ups. These directly drive revenue for SMBs and are almost entirely automatable.")

add_heading_styled("5.3 Universal Services Are Traps", 2)
doc.add_paragraph(
    "Services like 'Local SEO', 'Social Media Management', 'Virtual Assistant', and 'Data Entry' "
    "score Bronze or Red Flag despite being the most commonly offered India-to-US services. "
    "The market is brutally saturated, AI is automating the deliverables, and pricing is a "
    "race to the bottom."
)

add_callout("Key Insight: The money is NOT in universal services. It's in industry-specific "
            "services where domain expertise creates a barrier that protects margins.")

add_heading_styled("5.4 Vertical Selection > Service Selection", 2)
doc.add_paragraph(
    "The same service (e.g., 'Route Optimization') scores very differently depending on the vertical. "
    "Route optimization for landscaping = Medium competition. Route optimization for pool maintenance = "
    "Low competition. Choosing the right vertical matters more than choosing the right service."
)

add_heading_styled("5.5 Recurring Revenue Dominates", 2)
doc.add_paragraph(
    "The highest-tier services overwhelmingly use monthly retainer or SaaS delivery models. "
    "One-time project work scores lower because it lacks compounding value. The winning strategy "
    "is to sell setup + ongoing management, not one-off deliverables."
)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# 6. TIER-BY-TIER STRATEGIC ANALYSIS
# ═══════════════════════════════════════════════════════════════
add_heading_styled("6. Tier-by-Tier Strategic Analysis", 1)

# ── 6.1 Platinum ──
add_heading_styled("6.1 Platinum Tier — 63 Services (39.1%)", 2)
doc.add_paragraph(
    "These services combine high automation potential (typically 75%+), low-to-medium competition, "
    "and high automation confidence. They represent immediate revenue opportunities."
)

add_heading_styled("Top Platinum Clusters:", 3)

add_table_with_style(
    ["Cluster", "Example Services", "Verticals", "Why Platinum"],
    [
        ["Scheduling & Routing", "Route optimization, appointment automation, crew scheduling, dispatch",
         "Pool, Pest, Pet, Cleaning, HVAC, Moving, Auto Detailing",
         "85%+ automatable, route-based SMBs need it, few India providers in niche verticals"],
        ["Compliance & Regulatory", "Licensing tracking, OSHA docs, pesticide compliance, FTC compliance, DEA logs",
         "Pest Control, Daycare, Funeral, Construction, Vet Clinics",
         "Tedious mandatory paperwork, 65-80% automatable, almost no competition"],
        ["Customer Communication", "Recall reminders, reactivation campaigns, post-service follow-ups, aftercare",
         "Dental, Vet, Chiropractic, Funeral, Moving",
         "85-90% automatable, directly drives revenue, very low competition"],
        ["Back-Office Processing", "Insurance claims, billing, rent collection, bookkeeping, payroll",
         "Dental, Chiropractic, Vet, Property Mgmt, Restaurants, Accounting",
         "75-85% automatable, established delivery model from India, high volume"],
        ["Inventory & Cost Control", "Chemical tracking, parts pricing, food cost, back-bar tracking",
         "Pool, HVAC, Auto Repair, Restaurant, Salon",
         "75-80% automatable, direct margin impact, low competition"],
    ],
    col_widths=[1.2, 1.8, 1.6, 2.0]
)

doc.add_paragraph()

add_heading_styled("Platinum Tier Action Items:", 3)
add_bullet("Pick 2-3 verticals from the Platinum clusters above")
add_bullet("Build productized service packages (fixed scope, fixed price)")
add_bullet("Develop case studies within 60 days (offer 3 free/discounted pilots)")
add_bullet("Target 10 clients per vertical within 90 days")

doc.add_paragraph()

# ── 6.2 Gold ──
add_heading_styled("6.2 Gold Tier — 46 Services (28.6%)", 2)
doc.add_paragraph(
    "Gold tier services are strong opportunities with minor caveats — either slightly higher "
    "competition or slightly lower automation. They should be built in parallel with Platinum services."
)

add_heading_styled("Top Gold Clusters:", 3)

add_table_with_style(
    ["Cluster", "Example Services", "Key Caveat", "Mitigation Strategy"],
    [
        ["Industry Marketing", "Dental marketing, HVAC local SEO, solar lead gen",
         "High competition", "Niche down further (e.g., 'SEO for pediatric dentists')"],
        ["Technical Processing", "Mortgage underwriting, insurance policy admin, Xactimate claims",
         "Requires domain expertise", "Hire/train US-certified professionals in India"],
        ["Design & Visualization", "Landscape rendering, 3D remodeling, virtual staging, proposal design",
         "Medium competition", "Speed + quality + volume = competitive advantage"],
        ["CRM & Systems", "CRM setup, AI chatbots, booking systems, shop management",
         "Medium competition", "Vertical-specific configurations (pre-built for salon, vet, etc.)"],
    ],
    col_widths=[1.3, 1.8, 1.3, 2.2]
)

doc.add_paragraph()

add_heading_styled("Gold Tier Action Items:", 3)
add_bullet("Queue behind Platinum services but begin research/training now")
add_bullet("Focus on 'niche within niche' positioning to reduce competition")
add_bullet("For domain-expertise services, identify US-certified team leads in India")

# ── 6.3 Silver ──
add_heading_styled("6.3 Silver Tier — 26 Services (16.1%)", 2)
doc.add_paragraph(
    "Silver tier services are viable but require a clear differentiation strategy. They typically "
    "have moderate competition or partial automation. These are 'maybe' services — they can work "
    "but shouldn't be the core offering."
)

add_bullet("Use as add-ons or upsells to Platinum/Gold services")
add_bullet("Bundle with higher-tier services to increase ticket size")
add_bullet("Consider only if you have unique expertise or connections in the vertical")

add_heading_styled("Examples:", 3)
doc.add_paragraph("Construction estimating, legal marketing, restaurant social media, "
                   "roofing insurance claims, solar lead generation, law firm marketing.")

# ── 6.4 Bronze ──
add_heading_styled("6.4 Bronze Tier — 17 Services (10.6%)", 2)
doc.add_paragraph(
    "These services face structural challenges — either very high competition with low differentiation "
    "potential, or automation hasn't reached the level needed for profitable remote delivery."
)

add_heading_styled("Examples:", 3)
doc.add_paragraph("Social media management, logo/branding, customer support (general), VA services, "
                   "virtual assistant, mobile app development, customer support (phone).")

add_heading_styled("Recommendation:", 3)
doc.add_paragraph(
    "Do NOT build standalone practices around these. They can be bundled as part of a larger "
    "offering (e.g., include social media management as part of a Platinum-tier dental marketing "
    "package) but should never be the primary value proposition."
)

# ── 6.5 Red Flag ──
add_heading_styled("6.5 Red Flag Tier — 9 Services (5.6%)", 2)
doc.add_paragraph(
    "These are commodity services where the market is saturated AND AI is rapidly automating "
    "the human value layer. Competing here means a race to the bottom on price."
)

add_table_with_style(
    ["Service", "Auto %", "Competition", "Problem"],
    [
        ["Data Entry & Processing", "85%", "Very High", "AI OCR + forms making this obsolete; pricing collapsing"],
        ["Virtual Assistant Services", "50%", "Very High", "ChatGPT/Copilot replacing basic VA tasks; 1000s of providers"],
        ["Lead Generation (Generic)", "55%", "Very High", "AI tools (Instantly, Smartlead) commoditizing cold outreach"],
        ["Customer Support (Phone/Chat)", "65%", "Very High", "AI voice/chatbots replacing tier-1; massive BPO competition"],
        ["Local SEO (Generic)", "45%", "Very High", "Extremely crowded; AI builders reducing need for SEO specialists"],
    ],
    col_widths=[1.8, 0.6, 1.0, 3.0]
)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# 7. VERTICAL DEEP-DIVES
# ═══════════════════════════════════════════════════════════════
add_heading_styled("7. Vertical Deep-Dives: Top 10 Verticals by Opportunity", 1)

doc.add_paragraph(
    "Not all verticals are equally attractive. The following ranks the top 10 business verticals "
    "by the density and quality of their Platinum/Gold services."
)

verticals_ranked = [
    ("1. HVAC / Plumbing / Electrical", 7, 6, 1,
     "Dominated by Platinum services (maintenance contracts, parts inventory, dispatching). "
     "These are high-revenue SMBs ($500K-$5M/year) that will pay for efficiency gains. "
     "Low tech adoption creates a huge gap.",
     "Start with maintenance contract management + parts inventory."),

    ("2. Pool Maintenance / Service", 2, 2, 0,
     "Both services (route optimization + chemical management) are Platinum. "
     "Pool service is a pure route-density business with 50-200+ stops/week. "
     "Very underserved by technology.",
     "Both services are immediate launches. Small vertical but high loyalty."),

    ("3. Pet Grooming / Pet Spa", 5, 3, 2,
     "Pet industry is booming ($150B+ in US). Pet-specific scheduling, health management, "
     "and mobile groomer routing are all Platinum. Few purpose-built solutions exist.",
     "Lead with pet profile & health management — most underserved."),

    ("4. Veterinary Clinics", 5, 4, 1,
     "Similar to pet grooming but higher ticket size. Vaccination reminders, client education, "
     "pharmacy inventory, and pet insurance billing are all strong opportunities.",
     "Lead with client communication & education — low competition, high impact."),

    ("5. Property Management", 5, 4, 1,
     "Tenant screening, rent collection, lease administration, and tenant communication "
     "are all Platinum or Gold. PMs are scaling and need back-office support.",
     "Lead with lease administration — very underserved, high compliance value."),

    ("6. Cleaning Services", 5, 3, 2,
     "Quote generation, QC/feedback, crew management, and booking are strong. "
     "Fastest-growing local service category. Highly fragmented market = many small buyers.",
     "Lead with quote & estimate generation — eliminates biggest time sink."),

    ("7. Dental Practices", 5, 3, 2,
     "Appointment scheduling (90% auto!), treatment plans, and reputation management "
     "are all strong. Dental billing is established but competitive.",
     "Lead with treatment plan presentation — very few remote solutions exist."),

    ("8. Construction / Remodeling", 6, 3, 3,
     "Estimating takeoffs, permit documentation, subcontractor management, and safety compliance "
     "are all Platinum/Gold. GCs spend 10-20 hours/bid on takeoffs alone.",
     "Lead with permit & regulatory documentation — universally hated paperwork."),

    ("9. Funeral Homes", 3, 3, 0,
     "Extremely underserved vertical. All 3 services are Platinum/Gold with very low competition. "
     "Funeral homes have high revenue per client ($7K-$15K) but low tech adoption.",
     "Lead with pre-need & aftercare — generates referrals, highly automatable."),

    ("10. Pest Control", 4, 3, 1,
     "Route optimization, compliance/licensing, and customer retention are all Platinum. "
     "Pest control is a subscription business where retention = revenue.",
     "Lead with compliance & licensing management — multi-state complexity is barrier."),
]

for name, plat, gold, silver, analysis, lead_with in verticals_ranked:
    add_heading_styled(name, 2)
    p = doc.add_paragraph()
    run = p.add_run(f"Platinum: {plat} | Gold: {gold} | Silver: {silver}")
    run.font.bold = True
    run.font.size = Pt(10)
    doc.add_paragraph(analysis)
    p = doc.add_paragraph()
    run = p.add_run(f"🎯 Recommended Entry Point: ")
    run.bold = True
    run.font.size = Pt(10)
    p.add_run(lead_with)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# 8. AUTOMATION vs COMPETITION MATRIX
# ═══════════════════════════════════════════════════════════════
add_heading_styled("8. Automation vs. Competition Matrix", 1)

doc.add_paragraph(
    "The following 2×2 matrix shows where services land when plotted by automation potential "
    "and competitive intensity. The ideal quadrant is top-left (high automation + low competition)."
)

add_table_with_style(
    ["", "Low Competition\n(Opportunity Zone)", "Medium Competition\n(Competitive Zone)", "High / Very High Competition\n(Commodity Zone)"],
    [
        ["High Automation\n(≥75%)",
         "⭐ SWEET SPOT\n\n63 Platinum services\n\nGIS measurement, route optimization, appointment systems, compliance tracking, rent collection, chemical mgmt, customer education, lease admin, aftercare, QC systems, deposit mgmt",
         "GOLD ZONE\n\n46 Gold services\n\nCRM setup, AI chatbots, inventory management, insurance claims, billing processing, estimating, bookkeeping, financial reporting, crew management, membership billing",
         "AVOID / BUNDLE\n\n~12 services\n\nData entry, payroll, email marketing, social media for some verticals, online ordering, booking for salons"],
        ["Medium Automation\n(50-74%)",
         "SILVER–GOLD ZONE\n\n~20 services\n\nPermit research, surveillance analysis, case management, treatment plans, loyalty programs, funeral compliance, outcome tracking, warranty management",
         "SILVER ZONE\n\n~25 services\n\nConstruction estimating, project management, 3D rendering, PPC management, content marketing, design rendering, transaction coordination",
         "RED FLAG\n\n~9 services\n\nLocal SEO, social media mgmt, VA services, lead gen (generic), customer support (generic), logo/branding, app dev"],
        ["Low Automation\n(<50%)\n",
         "NICHE OPPORTUNITY\n\n~5 services\n\nCybersecurity, legal research, mobile app dev — high ticket but requires deep expertise",
         "CHALLENGING\n\n~3 services\n\nMostly human-dependent with competition — avoid",
         "DEAD ZONE\n\n~2 services\n\nHigh competition + low automation = impossible to compete profitably"],
    ],
    col_widths=[1.3, 2.3, 2.0, 2.0]
)

doc.add_paragraph()
add_callout("The Sweet Spot (top-left quadrant) contains 63 Platinum services. "
            "This is where you should concentrate 70%+ of your initial effort.")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# 9. RISK ASSESSMENT
# ═══════════════════════════════════════════════════════════════
add_heading_styled("9. Risk Assessment", 1)

add_table_with_style(
    ["Risk", "Severity", "Likelihood", "Description", "Mitigation"],
    [
        ["AI Displacement", "High", "High",
         "AI tools (ChatGPT, Claude, Gemini) continuously automate tasks that were previously "
         "human-deliverable. Services scoring 50-65% automation are most vulnerable.",
         "Focus on Platinum services where automation IS the product, not a threat. "
         "Build AI-native workflows, not AI-replaceable ones."],
        ["Quality Perception", "Medium", "High",
         "US SMBs may perceive India-delivered services as lower quality, especially for "
         "client-facing or compliance-sensitive work.",
         "Invest in US-facing brand, case studies, and testimonials. "
         "Hire US-based account managers. Offer satisfaction guarantees."],
        ["Data Security / Compliance", "High", "Medium",
         "HIPAA (healthcare), FCRA (background checks), GLBA (financial), "
         "and state privacy laws create compliance obligations for offshore data handling.",
         "SOC 2 certification, BAA agreements, data encryption, "
         "US-based data storage. Make compliance a selling point."],
        ["Client Acquisition Cost", "Medium", "High",
         "Cold outreach to US SMBs is expensive and has low conversion rates. "
         "Typical CAC for B2B services: $500-$3,000/client.",
         "Start with partnerships (white-label for US agencies), "
         "industry events, and referral programs. Offer free pilots."],
        ["Talent Retention", "Medium", "Medium",
         "Skilled India-based talent in niche domains (Xactimate, dental billing, "
         "solar design) is competitive and attrition-prone.",
         "Build training programs, create career paths, "
         "invest in domain-specific upskilling. Pay above-market for niche skills."],
        ["Time Zone Challenges", "Low", "Medium",
         "10.5-hour time difference with US Eastern. Can be an advantage "
         "(overnight delivery) or a challenge (limited real-time collaboration).",
         "Structure work for async delivery. Overlap 2-3 hours for calls. "
         "Hire a US-based client success person for real-time needs."],
        ["Platform Dependency", "Medium", "Medium",
         "Many services depend on third-party platforms (Google, MLS data, "
         "EagleView, carrier portals). API changes or pricing changes can disrupt delivery.",
         "Diversify across platforms. Build platform-agnostic skills. "
         "Monitor API/release notes proactively."],
    ],
    col_widths=[1.0, 0.7, 0.7, 2.0, 2.2]
)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# 10. GO-TO-MARKET RECOMMENDATIONS
# ═══════════════════════════════════════════════════════════════
add_heading_styled("10. Go-to-Market Recommendations", 1)

add_heading_styled("10.1 Pick 2-3 Verticals, Not 34", 2)
doc.add_paragraph(
    "The biggest mistake is trying to serve everyone. Based on the analysis, the highest-opportunity "
    "starting combinations are:"
)

add_table_with_style(
    ["Strategy", "Verticals", "Services to Launch", "Why"],
    [
        ["Route-Based Services Play",
         "Pool + Pest + Pet + Cleaning",
         "Route optimization, scheduling, compliance tracking, customer retention",
         "Same service delivered to 4 similar business models. Shared tech stack, shared sales playbook."],
        ["Healthcare Back-Office Play",
         "Dental + Chiropractic + Vet",
         "Insurance billing, appointment reminders, patient/client communication, outcome tracking",
         "Insurance billing expertise transfers across all three. High LTV, recurring revenue."],
        ["Trades & Construction Play",
         "HVAC + Construction + Roofing",
         "Estimating, permit docs, compliance, subcontractor management, maintenance contracts",
         "Contractors share the same pain points (paperwork, compliance, scheduling). High ticket sizes."],
        ["Property & Real Estate Play",
         "Property Mgmt + Real Estate",
         "Lease admin, tenant screening, transaction coordination, compliance, rent collection",
         "Document-heavy industries with compliance needs. Shared document management expertise."],
    ],
    col_widths=[1.2, 1.3, 1.8, 2.2]
)

add_heading_styled("10.2 Productize, Don't Customize", 2)
doc.add_paragraph(
    "Create fixed-scope, fixed-price packages rather than custom proposals for every client. "
    "Example package structure:"
)

add_table_with_style(
    ["Package Tier", "What's Included", "Price Range", "Target Margin"],
    [
        ["Starter", "Single service (e.g., route optimization setup + 3 months management)", "$200-$500/mo", "70-80% (mostly automated)"],
        ["Growth", "2-3 services bundled (e.g., scheduling + compliance + customer communication)", "$500-$1,500/mo", "65-75%"],
        ["Enterprise", "Full back-office + marketing bundle for multi-location businesses", "$2,000-$5,000/mo", "55-65%"],
    ],
    col_widths=[1.0, 2.5, 1.3, 1.5]
)

add_heading_styled("10.3 Sales Channels", 2)
add_bullet("White-label partnerships with US marketing agencies and consultants (fastest to revenue)")
add_bullet("Industry-specific cold outreach using LinkedIn + email (moderate cost, moderate conversion)")
add_bullet("Trade shows and industry associations (high cost, high trust, best for larger deals)")
add_bullet("Referral programs with complementary service providers (low cost, high conversion)")
add_bullet("Content marketing + case studies (slow but compounding)")

add_heading_styled("10.4 Pricing Strategy", 2)
doc.add_paragraph(
    "Price at 40-60% of US domestic competitors, NOT at 80% discount. The goal is to be "
    "perceived as 'great value' not 'cheap'. Quality + speed + price advantage = winning combination."
)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# 11. FIRST 90-DAY PLAN
# ═══════════════════════════════════════════════════════════════
add_heading_styled("11. Recommended First 90-Day Plan", 1)

add_table_with_style(
    ["Phase", "Timeline", "Actions", "Deliverables"],
    [
        ["Phase 1:\nDiscovery", "Weeks 1-2",
         "• Review this document and companion spreadsheet\n"
         "• Select 2-3 verticals to pursue\n"
         "• Identify 3-5 Platinum services per vertical\n"
         "• Research target SMB profiles (size, location, pain points)",
         "• Vertical selection memo\n• Target client persona doc\n• Service shortlist"],
        ["Phase 2:\nBuild", "Weeks 3-5",
         "• Design productized service packages (pricing, scope, deliverables)\n"
         "• Build delivery workflows and SOPs\n"
         "• Set up tools and automation (AI + manual processes)\n"
         "• Create sales materials (one-pagers, case study templates, pricing sheets)",
         "• 3-5 packaged offerings\n• Delivery SOPs\n• Sales deck\n• Pricing sheet"],
        ["Phase 3:\nPilot", "Weeks 6-8",
         "• Recruit 3-5 pilot clients (free or heavily discounted)\n"
         "• Deliver service, document everything\n"
         "• Collect metrics, testimonials, before/after data\n"
         "• Refine service delivery based on feedback",
         "• 3-5 active pilot clients\n• Case study drafts\n• Refined SOPs\n• Metrics dashboard"],
        ["Phase 4:\nLaunch", "Weeks 9-12",
         "• Convert pilots to paid (or use case studies for new sales)\n"
         "• Begin outbound sales (email, LinkedIn, partnerships)\n"
         "• Launch white-label partnership outreach\n"
         "• Set up KPI tracking (CAC, LTV, NPS, margin)",
         "• First 10 paying clients\n• 2-3 published case studies\n• Partnership pipeline\n• KPI dashboard"],
    ],
    col_widths=[0.8, 0.7, 2.5, 1.8]
)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# 12. OPEN QUESTIONS
# ═══════════════════════════════════════════════════════════════
add_heading_styled("12. Open Questions for Leadership", 1)

doc.add_paragraph(
    "The following questions need answers before the team can execute:"
)

questions = [
    ("Vertical Selection", "Which 2-3 verticals will we pursue first? The data suggests Pool/Pest/Pet (route-based), Dental/Chiro/Vet (healthcare), or HVAC/Construction (trades) as top starting points."),
    ("Team Structure", "Do we have domain-expert team leads in India for the selected verticals? If not, what's the hiring/training plan and timeline?"),
    ("US Presence", "Will we have a US-based person for client-facing roles (account management, sales)? This significantly impacts trust and pricing power."),
    ("Compliance Posture", "What's our plan for SOC 2, HIPAA, FCRA compliance? This is table stakes for healthcare, financial, and background check services."),
    ("Technology Stack", "What's our internal tech stack for service delivery? Do we build custom tools, or leverage existing platforms (GoHighLevel, ServiceTitan, etc.)?"),
    ("Pricing Philosophy", "Do we compete on price (40-60% of US rates) or on value (near-US pricing with superior service)? This decision shapes everything."),
    ("Partnership vs. Direct", "Do we sell direct to SMBs, or white-label through US agencies/consultants? Partnerships are faster to revenue but lower margin."),
    ("Success Metrics", "What does success look like at 90 days? 10 clients? $10K MRR? 3 partnerships? Define the north star."),
    ("Investment Budget", "What's the budget for the first 90 days? This determines team size, tool stack, marketing spend, and pilot program scope."),
    ("Risk Tolerance", "Are we willing to offer free/discounted pilots to build case studies? This is the fastest path to market but has opportunity cost."),
]

for i, (q, detail) in enumerate(questions, 1):
    p = doc.add_paragraph()
    run = p.add_run(f"{i}. {q}: ")
    run.bold = True
    p.add_run(detail)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# 13. APPENDIX
# ═══════════════════════════════════════════════════════════════
add_heading_styled("13. Appendix: Data Sources & Assumptions", 1)

add_heading_styled("13.1 Data Sources", 2)
add_bullet("US Census Bureau SMB statistics (business counts by NAICS code)")
add_bullet("Industry reports (IBISWorld, Statista, Grand View Research) for market sizing")
add_bullet("Software platform documentation (ServiceTitan, HubSpot, GoHighLevel, Aurora Solar, EagleView, etc.)")
add_bullet("AI tool capability assessments (GPT-4, Claude, Midjourney, various vertical-specific AI tools)")
add_bullet("Competitive analysis of India-based service providers (BPO directories, Clutch.co, Upwork)")
add_bullet("US regulatory databases (OSHA, EPA, state licensing boards, FTC guidelines)")

add_heading_styled("13.2 Key Assumptions", 2)
add_bullet("Automation potential is assessed based on AI/technology capabilities as of mid-2026")
add_bullet("Competitive intensity reflects the India-to-US services market specifically, not the overall US market")
add_bullet("Ticket sizes are based on market research for US SMB pricing; actual pricing will vary by geography and client size")
add_bullet("The analysis assumes a team with strong English proficiency and basic US business cultural awareness")
add_bullet("Automation confidence scores reflect current tool availability, not what might be possible with 6-12 months of custom development")
add_bullet("All 34 verticals were selected based on their prevalence as US local SMBs with remote-service-compatible needs")

add_heading_styled("13.3 Limitations", 2)
add_bullet("Scores are estimates based on research and analysis, not empirical market testing")
add_bullet("The competitive landscape changes rapidly — especially with AI advancement")
add_bullet("Ticket sizes vary significantly by US geography (NYC vs. rural Midwest)")
add_bullet("Some verticals may have regulatory barriers not fully captured in this analysis")
add_bullet("The 'degree of automation' analysis is directional — actual automation percentages will vary by implementation quality")

doc.add_paragraph()
doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("— End of Handover Document —")
run.font.italic = True
run.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("For questions, refer to the companion spreadsheet or the Python generation script.")
run.font.italic = True
run.font.size = Pt(9)
run.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

# ── Save ──
output = "/home/user/India_US_SMB_Services_Handover.docx"
doc.save(output)
print(f"Saved to {output}")
