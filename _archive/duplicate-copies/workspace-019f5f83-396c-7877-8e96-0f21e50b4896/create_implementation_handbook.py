
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
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

def heading(text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
    return h

def add_tbl(headers, rows, col_widths=None):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = 'Light Grid Accent 1'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.bold = True
                run.font.size = Pt(9)
                run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        shading = OxmlElement('w:shd')
        shading.set(qn('w:fill'), '1F4E79')
        shading.set(qn('w:val'), 'clear')
        cell.paragraphs[0].paragraph_format.space_before = Pt(2)
        cell.paragraphs[0].paragraph_format.space_after = Pt(2)
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        tcPr.append(shading)
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

def bullet(text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    if bold_prefix:
        run = p.add_run(bold_prefix)
        run.bold = True
        run.font.size = Pt(10.5)
        p.add_run(text)
    else:
        p.add_run(text)

def callout(text, icon="💡"):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.3)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(f"{icon} {text}")
    run.font.size = Pt(10)
    run.font.italic = True
    run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)

def checklist(items):
    for item in items:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.3)
        run = p.add_run("☐  ")
        run.font.size = Pt(11)
        run.font.bold = True
        p.add_run(item)

def worksheet(title, fields):
    heading(title, 3)
    for field in fields:
        p = doc.add_paragraph()
        run = p.add_run(f"{field}: ")
        run.bold = True
        run.font.size = Pt(10)
        p.add_run("_" * 60)
        p.paragraph_format.space_after = Pt(4)

def divider():
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("─" * 80)
    run.font.color.rgb = RGBColor(0xCC, 0xCC, 0xCC)
    run.font.size = Pt(6)

# ═══════════════════════════════════════════════════════════════
# COVER
# ═══════════════════════════════════════════════════════════════
doc.add_paragraph()
doc.add_paragraph()
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("IMPLEMENTATION HANDBOOK")
run.font.size = Pt(14)
run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
run.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("India → US Local SMB Services\nStudy Guide & Next-Phase Execution Playbook")
run.font.size = Pt(24)
run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x79)
run.bold = True

doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("From Analysis → Action: A Working Document for\nStudy, Decision-Making & Implementation")
run.font.size = Pt(12)
run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
run.font.italic = True

doc.add_paragraph()
doc.add_paragraph()

meta = [
    ("Document Type", "Implementation Handbook & Study Guide"),
    ("Companion Files", "Handover Document (.docx) + Analysis Spreadsheet (.xlsx)"),
    ("Date", datetime.date.today().strftime("%B %d, %Y")),
    ("Intended Audience", "Founders, Ops Leads, Delivery Managers, Sales Leads"),
    ("Purpose", "Study the analysis → Make decisions → Execute Phase 1"),
]
table = doc.add_table(rows=len(meta), cols=2)
for i, (l, v) in enumerate(meta):
    table.rows[i].cells[0].text = l
    table.rows[i].cells[1].text = v
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
# HOW TO USE THIS DOCUMENT
# ═══════════════════════════════════════════════════════════════
heading("How to Use This Document", 1)

doc.add_paragraph(
    "This is NOT a read-once-and-file document. It's a working handbook designed to be used "
    "over 4-6 weeks as your team studies the market analysis and builds toward launch. "
    "It contains:"
)

add_tbl(
    ["Section", "Purpose", "When to Use"],
    [
        ["Part A: Study Guide", "Structured reading plan for the analysis data", "Week 1 — Read before any decisions"],
        ["Part B: Decision Worksheets", "Fill-in worksheets for vertical & service selection", "Week 1-2 — Fill out as a team"],
        ["Part C: Implementation Playbook", "Step-by-step build plan for Phase 1", "Week 2-6 — Execute sequentially"],
        ["Part D: Delivery Blueprint", "How to actually deliver the services", "Week 3-6 — Build alongside sales"],
        ["Part E: Sales & Client Acquisition", "How to find and close first clients", "Week 4-8 — Start early, iterate"],
        ["Part F: Operations & Tools", "Tech stack, team structure, SOPs", "Week 2-4 — Set up early"],
        ["Part G: KPIs & Tracking", "What to measure and how", "Week 4+ — Track from day 1"],
        ["Part H: 12-Week Sprint Calendar", "Day-by-day execution timeline", "Throughout — Reference weekly"],
    ],
    col_widths=[1.5, 2.5, 2.2]
)

doc.add_paragraph()
callout("Recommended approach: Assign Part A as reading for Week 1. Hold a team workshop at end of Week 1 to complete Part B worksheets. Then begin Part C execution in Week 2.", "📋")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# PART A: STUDY GUIDE
# ═══════════════════════════════════════════════════════════════
heading("PART A: STUDY GUIDE", 1)
doc.add_paragraph("Purpose: Structured reading plan to deeply understand the 161-service analysis before making any decisions.")

# ── A1 ──
heading("A1. Day 1-2: Understand the Scoring Framework", 2)
doc.add_paragraph("Before looking at specific services, understand HOW they were scored.")

heading("Reading Assignments:", 3)
bullet("Spreadsheet → Sheet 'Legend & Notes' — Read every parameter definition")
bullet("Spreadsheet → Sheet 'Summary Dashboard' — Understand tier distribution")
bullet("Handover Doc → Section 3 (Scope & Methodology) — How the Opportunity Score works")
bullet("Handover Doc → Section 4 (Tier Framework) — What each tier means strategically")

heading("Study Questions (answer after reading):", 3)
checklist([
    "What are the 5 scoring parameters and what does each measure?",
    "What is the scoring formula? (Automation % + Competition Modifier + Confidence Modifier)",
    "Why does competition have a bigger modifier (−25) than confidence (+10)?",
    "What score range maps to each tier? (Platinum ≥85, Gold 70-84, Silver 52-69, Bronze 38-51, Red <38)",
    "Why did we use a 0-120 scale instead of 0-100?",
    "What's the difference between 'Automation Potential' and 'Automation Confidence'?",
])

callout("Key Insight: Competition matters MORE than automation confidence. A service that's 90% automatable in a Very High competition market scores LOWER than a 70% automatable service in a Low competition market. This is deliberate — market positioning beats technical capability.")

divider()

# ── A2 ──
heading("A2. Day 3: Study the Platinum Tier (63 Services)", 2)
doc.add_paragraph("These are your immediate-launch opportunities. Understand them deeply.")

heading("Reading Assignments:", 3)
bullet("Spreadsheet → Filter by Tier = 'Platinum' (column I)")
bullet("Sort by Score (column J) descending — study the top 20")
bullet("Handover Doc → Section 6.1 (Platinum Tier Analysis)")
bullet("Handover Doc → Section 5.2 (The Sweet Spot)")

heading("Study Questions:", 3)
checklist([
    "Which 5 Platinum services have the highest scores? What do they have in common?",
    "What are the top 3 Platinum clusters? (Scheduling/Routing, Compliance, Customer Communication)",
    "Which verticals have the MOST Platinum services? List them.",
    "For each Platinum service, read the 'CAN' vs 'CANNOT' column. What tasks still need humans?",
    "What's the average ticket size for Platinum services? (Compare to Bronze/Red Flag)",
    "Which Platinum services use SaaS delivery vs. retainer vs. per-task? What does this mean for operations?",
])

callout("Pattern Recognition: Almost all Platinum services are 'boring back-office' work — scheduling, compliance, billing, reminders. The unsexy stuff that SMBs hate doing. This is your opportunity. Glamorous services (social media, branding, lead gen) score poorly.", "🔍")

divider()

# ── A3 ──
heading("A3. Day 4: Study the Gold Tier (46 Services) + Verticals", 2)
doc.add_paragraph("Gold tier services are strong but need more strategy. Understand the difference.")

heading("Reading Assignments:", 3)
bullet("Spreadsheet → Filter by Tier = 'Gold' — Study all 46")
bullet("Handover Doc → Section 6.2 (Gold Tier Analysis)")
bullet("Handover Doc → Section 7 (Top 10 Verticals)")
bullet("Handover Doc → Section 8 (Automation vs Competition Matrix)")

heading("Study Questions:", 3)
checklist([
    "What's the #1 reason a Gold service isn't Platinum? (Usually: higher competition)",
    "Which Gold services could become Platinum with niche positioning? Give 3 examples.",
    "For each top-10 vertical, list the Platinum + Gold services available",
    "Which vertical has the highest TOTAL opportunity (Platinum + Gold combined)?",
    "In the Automation vs Competition matrix, where do most services cluster?",
    "What's the 'Sweet Spot' quadrant and how many services are in it?",
])

divider()

# ── A4 ──
heading("A4. Day 5: Study the Risk Assessment + GTM Strategy", 2)

heading("Reading Assignments:", 3)
bullet("Handover Doc → Section 9 (Risk Assessment) — All 7 risks")
bullet("Handover Doc → Section 10 (Go-to-Market Recommendations) — 4 strategic plays")
bullet("Handover Doc → Section 11 (90-Day Plan)")
bullet("Handover Doc → Section 12 (Open Questions) — These are YOUR decisions to make")

heading("Study Questions:", 3)
checklist([
    "Which risk has the highest severity + highest likelihood? (AI Displacement)",
    "What are the 4 strategic plays? Which one fits your team's strengths?",
    "What does the 90-day plan look like in summary? (Discovery → Build → Pilot → Launch)",
    "List the 10 open questions. Which 3 are most critical to answer first?",
    "What's the recommended pricing philosophy? (40-60% of US rates, not 80% discount)",
    "What's the recommended sales channel for fastest revenue? (White-label partnerships)",
])

divider()

# ── A5 ──
heading("A5. Day 5: Deep-Dive Your Shortlisted Verticals", 2)
doc.add_paragraph(
    "By now you should have 2-3 verticals in mind. Spend Day 5 going DEEP on each one."
)

heading("For Each Shortlisted Vertical, Research:", 3)
checklist([
    "How many SMBs exist in this vertical in the US? (Google: '[vertical] businesses in US statistics')",
    "What's the average revenue of an SMB in this vertical?",
    "What software/tools do they currently use? (Check G2, Capterra reviews in this category)",
    "What are the top 3 pain points mentioned in online forums/reviews? (Reddit, Facebook groups)",
    "Who are the existing India-based service providers for this vertical? (Clutch, Upwork search)",
    "What's the regulatory/compliance environment? (HIPAA? FCRA? State licensing?)",
    "What's the seasonality pattern? (When are they busiest? When do they buy services?)",
    "What would a 'dream client' look like in this vertical? (Size, location, revenue, tech adoption)",
])

callout("Pro Tip: Join 2-3 Facebook groups or Reddit communities for your shortlisted verticals. lurk for a week. The complaints and questions you see = your service opportunities.", "🎯")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# PART B: DECISION WORKSHEETS
# ═══════════════════════════════════════════════════════════════
heading("PART B: DECISION WORKSHEETS", 1)
doc.add_paragraph("Purpose: Structured worksheets to make key decisions as a team. Complete these by end of Week 2.")

# ── B1: Vertical Selection ──
heading("B1. Vertical Selection Worksheet", 2)
doc.add_paragraph("Score each candidate vertical on these criteria. Total the scores to rank them.")

add_tbl(
    ["Criteria", "Weight", "Vertical 1: ___", "Vertical 2: ___", "Vertical 3: ___"],
    [
        ["# of Platinum services available", "×3", "__ /10 → __", "__ /10 → __", "__ /10 → __"],
        ["Market size (# of SMBs in US)", "×3", "__ /10 → __", "__ /10 → __", "__ /10 → __"],
        ["Average ticket size potential", "×2", "__ /10 → __", "__ /10 → __", "__ /10 → __"],
        ["Team's existing domain knowledge", "×2", "__ /10 → __", "__ /10 → __", "__ /10 → __"],
        ["Low competition from India providers", "×2", "__ /10 → __", "__ /10 → __", "__ /10 → __"],
        ["Recurring revenue potential", "×2", "__ /10 → __", "__ /10 → __", "__ /10 → __"],
        ["Ease of client acquisition", "×1", "__ /10 → __", "__ /10 → __", "__ /10 → __"],
        ["Regulatory barrier (lower = better)", "×1", "__ /10 → __", "__ /10 → __", "__ /10 → __"],
        ["", "TOTAL", "___", "___", "___"],
    ],
    col_widths=[2.0, 0.6, 1.3, 1.3, 1.3]
)

doc.add_paragraph()
doc.add_paragraph("Decision: Primary vertical = _______________  |  Secondary vertical = _______________")
doc.add_paragraph()

# ── B2: Service Selection ──
heading("B2. Service Selection Worksheet", 2)
doc.add_paragraph("For your chosen primary vertical, select 3-5 services to launch with.")

add_tbl(
    ["Service Name", "Tier", "Score", "Ticket Size", "Why This Service?", "Delivery Complexity"],
    [
        ["1. _______________", "____", "___", "$___/mo", "", "□ Low □ Med □ High"],
        ["2. _______________", "____", "___", "$___/mo", "", "□ Low □ Med □ High"],
        ["3. _______________", "____", "___", "$___/mo", "", "□ Low □ Med □ High"],
        ["4. _______________", "____", "___", "$___/mo", "", "□ Low □ Med □ High"],
        ["5. _______________", "____", "___", "$___/mo", "", "□ Low □ Med □ High"],
    ],
    col_widths=[1.5, 0.6, 0.5, 0.7, 2.0, 1.2]
)

doc.add_paragraph()
callout("Selection Rule: Pick at least 1 'anchor' service (highest score, easiest to deliver) and 1 'differentiator' service (unique, competitors don't offer it). The anchor gets clients in the door; the differentiator keeps them.")

# ── B3: Package Design ──
heading("B3. Service Package Design Worksheet", 2)
doc.add_paragraph("Design your 3-tier offering for each vertical.")

add_tbl(
    ["", "Starter", "Growth", "Enterprise"],
    [
        ["Package Name", "", "", ""],
        ["Services Included", "", "", ""],
        ["Monthly Price (USD)", "$___ – $___", "$___ – $___", "$___ – $___"],
        ["Setup Fee", "$___", "$___", "$___"],
        ["Target Client Profile", "Solo / 1 location", "2-5 locations", "5+ locations / franchise"],
        ["Key Deliverables", "", "", ""],
        ["SLA / Response Time", "", "", ""],
        ["Estimated Delivery Cost", "$___/client/mo", "$___/client/mo", "$___/client/mo"],
        ["Target Gross Margin", "___%", "___%", "___%"],
    ],
    col_widths=[1.5, 1.8, 1.8, 1.8]
)

# ── B4: Team Requirements ──
heading("B4. Team Requirements Worksheet", 2)

add_tbl(
    ["Role", "# Needed", "Skills Required", "Hire/Train/Outsource", "Monthly Cost"],
    [
        ["Vertical Domain Lead", "___", "", "□ Hire □ Train □ Outsource", "$___"],
        ["Delivery Specialist(s)", "___", "", "□ Hire □ Train □ Outsource", "$___"],
        ["Sales / BD (US-facing)", "___", "", "□ Hire □ Train □ Outsource", "$___"],
        ["Tech / Automation Engineer", "___", "", "□ Hire □ Train □ Outsource", "$___"],
        ["QA / Client Success", "___", "", "□ Hire □ Train □ Outsource", "$___"],
        ["Project Manager", "___", "", "□ Hire □ Train □ Outsource", "$___"],
        ["", "TOTAL", "", "", "$___/mo"],
    ],
    col_widths=[1.5, 0.7, 1.8, 1.5, 1.0]
)

# ── B5: Competitive Positioning ──
heading("B5. Competitive Positioning Worksheet", 2)
doc.add_paragraph("For each service, map the competitive landscape and define your angle.")

add_tbl(
    ["Service", "US Competitors\n(who offers this?)", "India Competitors\n(Clutch/Upwork)", "Their Price Range", "Your Differentiator"],
    [
        ["________", "", "", "$___ – $___", ""],
        ["________", "", "", "$___ – $___", ""],
        ["________", "", "", "$___ – $___", ""],
    ],
    col_widths=[1.0, 1.5, 1.5, 1.0, 1.8]
)

doc.add_paragraph()
callout("Positioning Framework: 'We help [VERTICAL] businesses in [GEOGRAPHY] achieve [OUTCOME] by [UNIQUE MECHANISM], unlike [COMPETITOR] who [THEIR WEAKNESS].'", "🎯")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# PART C: IMPLEMENTATION PLAYBOOK
# ═══════════════════════════════════════════════════════════════
heading("PART C: IMPLEMENTATION PLAYBOOK", 1)
doc.add_paragraph("Purpose: Step-by-step execution plan for Phase 1. Each step has owners, deliverables, and deadlines.")

# ── C1: Week 1 — Foundation ──
heading("C1. Week 1: Foundation & Decisions", 2)

add_tbl(
    ["Day", "Task", "Owner", "Deliverable", "Done?"],
    [
        ["Mon", "Team reads Part A of this handbook (Day 1-2 assignments)", "All", "Everyone completes study questions", "☐"],
        ["Tue", "Team reads Part A (Day 3-5 assignments)", "All", "Study questions answered", "☐"],
        ["Wed", "Deep-dive research on 3 shortlisted verticals (A5)", "BD Lead", "Vertical research briefs", "☐"],
        ["Thu", "Team workshop: Complete B1 (Vertical Selection) worksheet", "All", "Primary + Secondary vertical selected", "☐"],
        ["Thu", "Complete B2 (Service Selection) worksheet", "All", "3-5 launch services selected", "☐"],
        ["Fri", "Complete B3 (Package Design) worksheet", "Ops Lead", "3-tier pricing defined", "☐"],
        ["Fri", "Complete B4 (Team Requirements) worksheet", "Ops Lead", "Hiring plan drafted", "☐"],
        ["Fri", "Complete B5 (Competitive Positioning) worksheet", "BD Lead", "Positioning statements written", "☐"],
    ],
    col_widths=[0.4, 2.5, 0.8, 1.8, 0.5]
)

# ── C2: Week 2 — Build ──
heading("C2. Week 2: Build Service Delivery", 2)

add_tbl(
    ["Day", "Task", "Owner", "Deliverable", "Done?"],
    [
        ["Mon", "Set up delivery tools & accounts (see Part F)", "Tech Lead", "All tools provisioned", "☐"],
        ["Mon", "Build automation workflows for Service #1", "Tech Lead", "Workflow documented & tested", "☐"],
        ["Tue", "Build automation workflows for Service #2", "Tech Lead", "Workflow documented & tested", "☐"],
        ["Tue", "Write Delivery SOP for Service #1 (see Part D template)", "Ops Lead", "SOP document v1", "☐"],
        ["Wed", "Write Delivery SOP for Service #2", "Ops Lead", "SOP document v1", "☐"],
        ["Wed", "Create client onboarding template & process", "Ops Lead", "Onboarding checklist + welcome email", "☐"],
        ["Thu", "Internal training: team delivers mock service for pilot client", "Domain Lead", "Training completed", "☐"],
        ["Thu", "Create sales materials: one-pager, pricing sheet, capabilities deck", "BD Lead", "Sales kit v1", "☐"],
        ["Fri", "Identify & reach out to 10 potential pilot clients", "BD Lead", "Outreach sent, 10 prospects contacted", "☐"],
        ["Fri", "Build CRM/pipeline for tracking prospects", "BD Lead", "CRM set up with 10 leads", "☐"],
    ],
    col_widths=[0.4, 2.8, 0.8, 1.8, 0.5]
)

# ── C3: Week 3-4 — Pilot ──
heading("C3. Weeks 3-4: Pilot Delivery", 2)

add_tbl(
    ["Week", "Task", "Owner", "Deliverable", "Done?"],
    [
        ["3", "Close 3-5 pilot clients (free or 80% discount for case study rights)", "BD Lead", "3-5 signed pilot agreements", "☐"],
        ["3", "Onboard pilot clients: collect access, data, preferences", "Ops Lead", "All pilots onboarded", "☐"],
        ["3", "Begin delivering Service #1 to pilots", "Delivery Team", "First deliverables sent", "☐"],
        ["3", "Daily standup: what's working, what's broken", "Ops Lead", "Issues log updated daily", "☐"],
        ["4", "Continue delivery + begin Service #2 for pilots", "Delivery Team", "Both services active", "☐"],
        ["4", "Collect metrics: time spent, client satisfaction, results achieved", "Ops Lead", "Metrics dashboard v1", "☐"],
        ["4", "Collect testimonials + before/after data from pilots", "BD Lead", "2-3 testimonials drafted", "☐"],
        ["4", "Refine SOPs based on pilot learnings", "Ops Lead", "SOPs v2 (updated)", "☐"],
        ["4", "Convert pilots to paid (or extend with case study agreement)", "BD Lead", "Pilot → Paid conversion plan", "☐"],
    ],
    col_widths=[0.4, 2.8, 0.8, 1.8, 0.5]
)

# ── C4: Week 5-8 — Launch & Scale ──
heading("C4. Weeks 5-8: Launch & Scale", 2)

add_tbl(
    ["Week", "Task", "Owner", "Deliverable", "Done?"],
    [
        ["5", "Publish 2-3 case studies from pilots", "Marketing", "Published case studies", "☐"],
        ["5", "Begin outbound sales campaign (email + LinkedIn)", "BD Lead", "50 prospects contacted", "☐"],
        ["5", "Launch white-label partnership outreach (5 US agencies)", "BD Lead", "5 partnership proposals sent", "☐"],
        ["6", "Continue outbound + follow up on partnerships", "BD Team", "Pipeline: 20+ active prospects", "☐"],
        ["6", "Build remaining services (Service #3, #4, #5)", "Tech Lead", "All services operational", "☐"],
        ["6", "Attend 1 industry event / join 2 online communities", "BD Lead", "Network connections made", "☐"],
        ["7", "Close first 5-10 paying clients", "BD Team", "5-10 signed contracts", "☐"],
        ["7", "Onboard paying clients using refined process", "Ops Lead", "All new clients onboarded", "☐"],
        ["7", "Review KPIs: CAC, margin, NPS, delivery quality", "Ops Lead", "KPI report #1", "☐"],
        ["8", "Team retrospective: what worked, what didn't", "All", "Retrospective doc", "☐"],
        ["8", "Plan Phase 2: additional services, second vertical", "Leadership", "Phase 2 brief", "☐"],
    ],
    col_widths=[0.4, 2.8, 0.8, 1.8, 0.5]
)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# PART D: DELIVERY BLUEPRINT
# ═══════════════════════════════════════════════════════════════
heading("PART D: DELIVERY BLUEPRINT", 1)
doc.add_paragraph("Purpose: Templates and frameworks for actually delivering services to clients.")

# ── D1: SOP Template ──
heading("D1. Service Delivery SOP Template", 2)
doc.add_paragraph("Copy this template for each service you deliver. Fill in the blanks.")

sop_template = [
    ("Service Name", ""),
    ("Service Tier", "□ Starter  □ Growth  □ Enterprise"),
    ("Vertical", ""),
    ("Client's Weekly Time Commitment", "___ minutes/week"),
    ("Our Weekly Time Commitment", "___ hours/week"),
    ("", ""),
    ("DELIVERY PROCESS", ""),
    ("Step 1: Client Onboarding", ""),
    ("  Tools to set up", ""),
    ("  Access/credentials needed", ""),
    ("  Information to collect", ""),
    ("  Timeline", ""),
    ("Step 2: Weekly/Monthly Delivery", ""),
    ("  What we deliver", ""),
    ("  What's automated vs. manual", ""),
    ("  Quality checkpoints", ""),
    ("  Client approval needed?", ""),
    ("Step 3: Reporting & Communication", ""),
    ("  What reports we send", ""),
    ("  Frequency", ""),
    ("  Communication channels", ""),
    ("Step 4: Escalation & Issue Handling", ""),
    ("  Common issues & resolution", ""),
    ("  Escalation path", ""),
    ("  SLA commitments", ""),
    ("", ""),
    ("AUTOMATION MAP", ""),
    ("Task 1: ____ → □ Fully Auto □ Semi-Auto □ Manual", ""),
    ("Task 2: ____ → □ Fully Auto □ Semi-Auto □ Manual", ""),
    ("Task 3: ____ → □ Fully Auto □ Semi-Auto □ Manual", ""),
    ("Task 4: ____ → □ Fully Auto □ Semi-Auto □ Manual", ""),
    ("Task 5: ____ → □ Fully Auto □ Semi-Auto □ Manual", ""),
    ("", ""),
    ("QUALITY METRICS", ""),
    ("Accuracy target", "___%"),
    ("Turnaround time target", "___ hours/days"),
    ("Client satisfaction target", "___/10 NPS"),
]

add_tbl(
    ["Field", "Value"],
    sop_template,
    col_widths=[2.5, 4.0]
)

divider()

# ── D2: Client Onboarding Checklist ──
heading("D2. Client Onboarding Checklist", 2)
doc.add_paragraph("Standard onboarding process for every new client.")

onboarding = [
    "Pre-Onboarding (Before Kickoff Call)",
    "  ☐  Signed contract / MSA received",
    "  ☐  Setup fee invoice sent and paid",
    "  ☐  Welcome email sent with onboarding questionnaire",
    "  ☐  Internal kickoff brief prepared (client info, goals, contacts)",
    "  ☐  Delivery team assigned and briefed",
    "  ☐  Tool accounts created (if client needs access to our platforms)",
    "",
    "Kickoff Call (30-60 min)",
    "  ☐  Introductions: our team + their team",
    "  ☐  Review scope of services (what's included, what's not)",
    "  ☐  Collect access: logins, data exports, brand assets, etc.",
    "  ☐  Set expectations: timelines, communication cadence, reporting",
    "  ☐  Define success metrics: what does 'winning' look like?",
    "  ☐  Schedule recurring check-in calls (weekly/biweekly)",
    "  ☐  Identify their preferred communication channel (email/Slack/WhatsApp)",
    "",
    "Setup Phase (Week 1)",
    "  ☐  All access credentials received and tested",
    "  ☐  Audit/assessment completed (current state analysis)",
    "  ☐  Automation workflows configured and tested",
    "  ☐  First deliverable sent for client review",
    "  ☐  Feedback collected and incorporated",
    "  ☐  Client confirmed: 'This looks right, proceed with regular delivery'",
    "",
    "Steady State (Week 2+)",
    "  ☐  Regular delivery cadence established",
    "  ☐  First monthly report sent",
    "  ☐  First check-in call completed",
    "  ☐  NPS / satisfaction survey sent (after 30 days)",
    "  ☐  Upsell/cross-sell opportunity identified (if applicable)",
]
for item in onboarding:
    if item.startswith("  ☐"):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.5)
        p.add_run(item.strip())
    elif item == "":
        doc.add_paragraph()
    else:
        p = doc.add_paragraph()
        run = p.add_run(item)
        run.bold = True
        run.font.size = Pt(10)

divider()

# ── D3: Automation Stack ──
heading("D3. Automation Stack by Service Category", 2)
doc.add_paragraph("Recommended tools and platforms for automating each service category.")

add_tbl(
    ["Service Category", "Primary Automation Tools", "Backup / Alternatives", "Monthly Cost"],
    [
        ["Scheduling & Routing",
         "Route4Me, Google Maps API, Calendly",
         "OptimoRoute, Workiz, Jobber",
         "$50-$200/mo"],
        ["Customer Communication",
         "GoHighLevel (GHL), Twilio, Mailchimp",
         "ActiveCampaign, Klaviyo, SimplePractice",
         "$100-$400/mo"],
        ["Compliance & Documentation",
         "Airtable, Notion, Google Workspace",
         "Monday.com, Smartsheet, DocuWare",
         "$50-$200/mo"],
        ["Billing & Accounting",
         "QuickBooks Online, Stripe, Bill.com",
         "Xero, FreshBooks, Wave",
         "$50-$150/mo"],
        ["CRM & Pipeline",
         "GoHighLevel, HubSpot, Zoho CRM",
         "Pipedrive, Salesforce (for enterprise)",
         "$100-$500/mo"],
        ["AI & Content",
         "ChatGPT/Claude API, Canva, CapCut",
         "Jasper, Copy.ai, Descript, Midjourney",
         "$50-$300/mo"],
        ["Document Processing",
         "Zapier, Make.com, Google Apps Script",
         "n8n, Power Automate, custom Python",
         "$20-$200/mo"],
        ["Reporting & Dashboards",
         "Google Looker Studio, Airtable",
         "Tableau, Power BI, custom dashboards",
         "$0-$100/mo"],
    ],
    col_widths=[1.5, 2.0, 1.8, 1.0]
)

doc.add_paragraph()
callout("Cost-Saving Tip: GoHighLevel ($97-$297/mo) covers CRM + email + SMS + booking + landing pages + reviews + pipelines in ONE platform. For most verticals, this single tool replaces 4-5 separate subscriptions.", "💰")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# PART E: SALES & CLIENT ACQUISITION
# ═══════════════════════════════════════════════════════════════
heading("PART E: SALES & CLIENT ACQUISITION PLAYBOOK", 1)
doc.add_paragraph("Purpose: How to find and close your first 10 clients.")

# ── E1: Channels ──
heading("E1. Acquisition Channel Strategy", 2)

add_tbl(
    ["Channel", "Effort", "Cost", "Speed to Revenue", "Best For", "How to Execute"],
    [
        ["White-Label Partnerships", "Medium", "Low", "Fast (2-4 wks)",
         "Quickest path. Partner with US marketing agencies, business consultants, or industry SaaS companies who need delivery partners.",
         "Identify 20 agencies serving your vertical. Send personalized pitch. Offer free pilot project."],
        ["Cold Email Outreach", "High", "Low", "Medium (4-8 wks)",
         "Direct to SMB owners. Works best for verticals where you can clearly articulate pain + solution in 3 sentences.",
         "Build list of 500 prospects. 3-email sequence. Follow up by phone. Offer free audit/assessment."],
        ["LinkedIn Outreach", "Medium", "Low", "Medium (4-8 wks)",
         "Best for B2B verticals (property management, construction, accounting). Decision-makers are active on LinkedIn.",
         "Optimize profile. Connect with 50/week. Share valuable content. DM after connection with specific insight."],
        ["Industry Events / Trade Shows", "High", "High", "Slow (8-12 wks)",
         "Best for high-ticket services. Face-to-face trust building. Ideal for construction, legal, healthcare verticals.",
         "Attend 1-2 events per quarter. Pre-schedule 10 meetings. Follow up within 48 hours."],
        ["Referral Program", "Low", "Low", "Medium (4-8 wks)",
         "After first 5 clients. Ask for referrals. Offer $200-$500 referral fee or 1 month free.",
         "Formal referral program. Ask after NPS score of 8+. Make it easy (warm intro > cold referral)."],
        ["Content Marketing / SEO", "High", "Low", "Slow (3-6 mo)",
         "Long-term play. Write for your vertical's publications. Guest posts. YouTube tutorials. Build authority.",
         "Publish 2 articles/week. Target long-tail keywords for your vertical. Guest post on industry blogs."],
    ],
    col_widths=[1.0, 0.5, 0.5, 0.8, 1.8, 2.0]
)

divider()

# ── E2: Cold Email Templates ──
heading("E2. Cold Email Templates", 2)

heading("Template 1: Pain-Agitation-Solution", 3)
doc.add_paragraph(
    "Subject: [Specific pain point they likely have]\n\n"
    "Hi [First Name],\n\n"
    "I noticed [specific observation about their business — e.g., 'your Google listing shows 47 reviews but your competitor has 200+']. "
    "Most [vertical] businesses in [area] struggle with [pain point].\n\n"
    "We help [vertical] businesses [achieve outcome] by [unique mechanism]. "
    "[Social proof: 'Recently helped a [similar business] achieve [specific result] in [timeframe].']\n\n"
    "Would it make sense to have a quick 15-min call this week to see if this could help [their business name]?\n\n"
    "[Your name]"
)

heading("Template 2: Free Value First", 3)
doc.add_paragraph(
    "Subject: I made this for [their business name]\n\n"
    "Hi [First Name],\n\n"
    "I took the liberty of putting together a [free audit/analysis/report] for [their business name]. "
    "[Brief description of what you analyzed — e.g., 'I ran your website through our accessibility checker and found 12 WCAG violations that could expose you to ADA lawsuits.']\n\n"
    "Happy to send the full report over — no strings attached. Just thought it might be helpful.\n\n"
    "[Your name]\n"
    "[Title] | [Company]"
)

heading("Template 3: Referral / Social Proof", 3)
doc.add_paragraph(
    "Subject: [Mutual connection] suggested I reach out\n\n"
    "Hi [First Name],\n\n"
    "[Mutual connection] mentioned you might be dealing with [pain point]. "
    "We've been working with [vertical] businesses like [named client] to [outcome].\n\n"
    "[One specific result: 'They reduced no-shows by 35% in the first month.']\n\n"
    "Would you be open to a quick chat about whether we could do something similar for [their business]?\n\n"
    "[Your name]"
)

divider()

# ── E3: Partnership Outreach ──
heading("E3. White-Label Partnership Pitch", 2)
doc.add_paragraph("Template for approaching US agencies/consultants who could resell your services.")

doc.add_paragraph(
    "Subject: Delivery partner for your [vertical] clients?\n\n"
    "Hi [Name],\n\n"
    "I run a [service] team specializing in [vertical]. We work as a white-label delivery partner "
    "for US-based [agency type / consultants] who need reliable backend support for their clients.\n\n"
    "Here's what we handle:\n"
    "• [Service 1] — we deliver [output] within [turnaround]\n"
    "• [Service 2] — we deliver [output] within [turnaround]\n"
    "• [Service 3] — we deliver [output] within [turnaround]\n\n"
    "Your clients get the work done. You keep the relationship and the margin. "
    "We stay invisible.\n\n"
    "We currently work with [X] agencies and maintain a [X]% client retention rate. "
    "Happy to do a trial project for one of your clients at no cost so you can evaluate our quality.\n\n"
    "Worth a 15-min call?\n\n"
    "[Your name]"
)

divider()

# ── E4: Pricing Psychology ──
heading("E4. Pricing Guidelines", 2)

add_tbl(
    ["Principle", "Do", "Don't"],
    [
        ["Anchor high", "Show a premium tier first ($2,000/mo) so Growth tier ($800/mo) feels reasonable",
         "Lead with your cheapest option — it anchors low"],
        ["Show ROI", "'Our route optimization saves 3 hrs/day × $40/hr tech = $2,400/mo value. You pay $400.'",
         "Just list features without connecting to revenue/savings"],
        ["Offer pilot", "'Try us for 30 days at 50% off. If you don't see results, full refund.'",
         "Demand 12-month contracts from new clients with no trust built"],
        ["Bundle services", "'Scheduling + Compliance + Communication = $800/mo (vs $1,200 separately)'",
         "Price each service separately and let client pick — they'll pick only the cheapest"],
        ["Name the competitor", "'[Competitor] charges $3,000/mo for this. We deliver the same at $1,200.'",
         "Never mention competitors — clients will comparison shop without context"],
        ["Use 'investment'", "'Your monthly investment is $800' not 'it costs $800'",
         "Use the word 'cost' or 'expense' — frame as investment with returns"],
    ],
    col_widths=[1.2, 2.8, 2.5]
)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# PART F: OPERATIONS & TOOLS
# ═══════════════════════════════════════════════════════════════
heading("PART F: OPERATIONS SETUP", 1)

heading("F1. Recommended Team Structure (Starting Lean)", 2)

add_tbl(
    ["Role", "Count", "Responsibilities", "Key Skill", "India Market Rate"],
    [
        ["Delivery Lead / Vertical SME", "1", "Owns service quality, client escalation, SOPs, team training",
         "Domain expertise in chosen vertical + project management", "₹60K-1.2L/mo"],
        ["Automation / Tech Engineer", "1", "Builds workflows, integrations, manages tools, monitors systems",
         "Zapier/Make + Python + API integrations + GoHighLevel", "₹50K-90K/mo"],
        ["Delivery Specialist(s)", "2-3", "Day-to-day service delivery, client communication, reporting",
         "English fluency + attention to detail + vertical knowledge", "₹25K-45K/mo each"],
        ["Sales / BD (India-based)", "1", "Outbound prospecting, partnership outreach, pipeline management",
         "English fluency + LinkedIn/email outreach + CRM management", "₹35K-60K/mo + commission"],
        ["QA / Client Success", "1 (shared)", "Quality audits, client satisfaction surveys, issue resolution",
         "Analytical mindset + client empathy + process improvement", "₹30K-50K/mo"],
    ],
    col_widths=[1.3, 0.4, 1.8, 1.6, 1.2]
)

doc.add_paragraph()
callout("Starting budget: ₹3-5 Lakhs/month (~$3,600-$6,000/month) for a 6-person team delivering to 5-15 clients. Break-even at ~$4,000/month in client revenue with 60%+ gross margins.", "💰")

heading("F2. Internal Tool Stack", 2)

add_tbl(
    ["Function", "Recommended Tool", "Cost", "Why This Tool"],
    [
        ["Project Management", "ClickUp or Notion", "Free-$10/user/mo", "Flexible, handles SOPs + tasks + docs in one place"],
        ["Communication (Internal)", "Slack or Microsoft Teams", "Free-$8/user/mo", "Channel-based comms, integrations with everything"],
        ["CRM (for our sales)", "HubSpot Free or GoHighLevel", "Free-$97/mo", "Track prospects, pipeline, partnerships"],
        ["Client Communication", "Slack Connect or email", "Free (included)", "Real-time client comms without giving them your PM tool"],
        ["Automation", "Make.com + Zapier", "$29+$20/mo", "Make.com for complex workflows, Zapier for simple ones"],
        ["AI / LLM", "ChatGPT Plus + Claude Pro", "$20+$20/mo", "Content generation, data analysis, document drafting"],
        ["Time Tracking", "Toggl or Clockify", "Free-$10/user/mo", "Track delivery hours per client for margin analysis"],
        ["File Storage", "Google Workspace", "$7/user/mo", "Shared drives, docs, sheets — client deliverables"],
        ["Video Calls", "Google Meet or Zoom", "Free-$15/mo", "Client calls, team standups, screen sharing"],
        ["Invoicing", "Stripe + Wave or Zoho Invoice", "Free-$15/mo", "Professional invoicing, recurring billing, payments"],
    ],
    col_widths=[1.2, 1.5, 1.0, 2.5]
)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# PART G: KPIs & TRACKING
# ═══════════════════════════════════════════════════════════════
heading("PART G: KPIs & TRACKING DASHBOARD", 1)
doc.add_paragraph("What to measure from Day 1. Build this dashboard in Google Sheets or Airtable.")

heading("G1. North Star Metrics", 2)

add_tbl(
    ["Metric", "Formula", "Target (90 Days)", "Why It Matters"],
    [
        ["Monthly Recurring Revenue (MRR)", "Sum of all active monthly contracts", "$5,000-$10,000",
         "Revenue stability — this is your business value"],
        ["Active Clients", "# of clients paying monthly", "5-15",
         "Proof of product-market fit"],
        ["Gross Margin", "(Revenue − Delivery Cost) / Revenue", "≥ 60%",
         "Sustainability — below 50% means you're underpricing or overdelivering"],
        ["Client Retention Rate", "Clients retained / Total clients (monthly)", "≥ 90%/month",
         "Retention > acquisition. Losing clients = leaking revenue."],
    ],
    col_widths=[1.5, 1.8, 1.2, 2.0]
)

heading("G2. Sales Metrics", 2)

add_tbl(
    ["Metric", "Formula", "Target", "Frequency"],
    [
        ["Outreach Volume", "# of cold emails/DMs/.calls sent", "100+/week", "Weekly"],
        ["Response Rate", "Replies / Outreach sent", "≥ 5%", "Weekly"],
        ["Meeting Booked Rate", "Meetings / Replies", "≥ 30%", "Weekly"],
        ["Close Rate", "Closed deals / Meetings held", "≥ 20%", "Monthly"],
        ["Customer Acquisition Cost (CAC)", "Total sales cost / New clients", "< $500", "Monthly"],
        ["Pipeline Value", "Sum of all active deal values", "3× monthly revenue target", "Weekly"],
    ],
    col_widths=[1.5, 2.0, 1.5, 1.2]
)

heading("G3. Delivery Metrics", 2)

add_tbl(
    ["Metric", "Formula", "Target", "Frequency"],
    [
        ["On-Time Delivery Rate", "Deliverables on time / Total deliverables", "≥ 95%", "Weekly"],
        ["Error / Rework Rate", "Reworks / Total deliverables", "≤ 5%", "Weekly"],
        ["Hours per Client per Month", "Total delivery hours / Active clients", "Track trend", "Monthly"],
        ["Automation Rate", "Automated tasks / Total tasks", "≥ 60% (and growing)", "Monthly"],
        ["NPS (Client Satisfaction)", "Survey score (0-10)", "≥ 8", "Monthly (after 30 days)"],
        ["Revenue per Team Member", "MRR / Team size", "≥ $1,000", "Monthly"],
    ],
    col_widths=[1.5, 2.0, 1.5, 1.2]
)

heading("G4. Weekly Reporting Template", 2)
doc.add_paragraph("Every Monday, the Ops Lead fills this out and shares with the team:")

add_tbl(
    ["Category", "This Week", "Last Week", "Trend", "Notes"],
    [
        ["MRR", "$___", "$___", "↑↓→", ""],
        ["Active Clients", "___", "___", "↑↓→", ""],
        ["New Leads in Pipeline", "___", "___", "↑↓→", ""],
        ["Meetings Booked", "___", "___", "↑↓→", ""],
        ["Proposals Sent", "___", "___", "↑↓→", ""],
        ["Deals Closed", "___", "___", "↑↓→", ""],
        ["On-Time Delivery %", "___%", "___%", "↑↓→", ""],
        ["Client Issues Open", "___", "___", "↑↓→", ""],
        ["Team Utilization %", "___%", "___%", "↑↓→", ""],
        ["Biggest Win", "", "", "", ""],
        ["Biggest Challenge", "", "", "", ""],
        ["Next Week Priority", "", "", "", ""],
    ],
    col_widths=[1.3, 1.0, 1.0, 0.5, 2.5]
)

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# PART H: 12-WEEK SPRINT CALENDAR
# ═══════════════════════════════════════════════════════════════
heading("PART H: 12-WEEK SPRINT CALENDAR", 1)
doc.add_paragraph("Full quarter at a glance. Print this and pin it on the wall.")

add_tbl(
    ["Week", "Theme", "Key Milestones", "Decision Gates"],
    [
        ["1", "📚 Study & Decide",
         "• Complete Part A study guide\n• Fill all Part B worksheets\n• Select vertical(s) + services\n• Positioning defined",
         "☐ Vertical selected?\n☐ Services selected?\n☐ Packages priced?\n☐ Team plan approved?"],
        ["2", "🔧 Build",
         "• Tools provisioned\n• Service #1 & #2 workflows built\n• SOPs written\n• Sales materials created\n• 10 pilot prospects contacted",
         "☐ Workflows tested?\n☐ SOPs reviewed?\n☐ Sales kit ready?"],
        ["3", "🧪 Pilot",
         "• 3-5 pilot clients signed\n• Onboarding completed\n• Service #1 delivery begins\n• Daily standups started\n• Issues logged",
         "☐ Pilots onboarded?\n☐ Delivery started?\n☐ Feedback loop active?"],
        ["4", "🧪 Pilot + Refine",
         "• Service #2 delivery begins\n• Metrics collected\n• Testimonials drafted\n• SOPs updated (v2)\n• Pilot → Paid conversion plan",
         "☐ Results measured?\n☐ SOPs improved?\n☐ Conversion offers sent?"],
        ["5", "🚀 Launch",
         "• Case studies published\n• Outbound campaign begins (50 prospects)\n• Partnership outreach (5 agencies)\n• Content plan started",
         "☐ Case studies live?\n☐ Outbound running?\n☐ Partnership proposals sent?"],
        ["6", "🚀 Launch + Build",
         "• Continue outbound (50 more)\n• Services #3-5 built\n• 1 industry event attended\n• Pipeline: 20+ active prospects",
         "☐ All services ready?\n☐ Pipeline healthy?\n☐ First non-pilot lead?"],
        ["7", "📈 Scale",
         "• First 5-10 paying clients closed\n• New client onboarding\n• Delivery team at capacity?\n• KPI report #1",
         "☐ Paying clients signed?\n☐ Delivery quality maintained?\n☐ Need more hires?"],
        ["8", "📈 Scale + Optimize",
         "• Continue closing\n• Automate more tasks (reduce delivery hours)\n• Referral program launched\n• Retrospective meeting",
         "☐ 10 clients hit?\n☐ Margins ≥ 60%?\n☐ NPS ≥ 8?"],
        ["9", "🔁 Optimize",
         "• Upsell existing clients to Growth/Enterprise\n• Expand to secondary vertical\n• Hire if needed\n• SOPs v3",
         "☐ Upsell revenue?\n☐ 2nd vertical started?\n☐ Team scaled right?"],
        ["10", "🔁 Optimize",
         "• Continue outbound at higher volume\n• Partnership(s) activated\n• Content marketing accelerating\n• KPI report #3",
         "☐ Partnerships generating?\n☐ Content traffic growing?\n☐ MRR target on track?"],
        ["11", "📊 Review",
         "• Full quarter metrics review\n• Client interviews (top 3 + bottom 3)\n• Competitive landscape update\n• Phase 2 planning begins",
         "☐ All KPIs reviewed?\n☐ Client feedback collected?\n☐ Phase 2 direction clear?"],
        ["12", "🗺️ Plan Phase 2",
         "• Phase 2 brief written\n• Next vertical selected\n• New services identified\n• Team growth plan\n• Budget for next quarter",
         "☐ Phase 2 approved?\n☐ Budget allocated?\n☐ Hires planned?"],
    ],
    col_widths=[0.4, 1.0, 2.5, 1.8]
)

doc.add_paragraph()
callout("Decision Gate: At the end of each week, the team reviews the decision gates. If a gate isn't cleared, STOP and fix it before moving forward. Don't accumulate unresolved issues.", "🚦")

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════
# QUICK REFERENCE
# ═══════════════════════════════════════════════════════════════
heading("Quick Reference: Key Numbers", 1)

add_tbl(
    ["Metric", "Value"],
    [
        ["Total services analyzed", "161"],
        ["Total verticals covered", "34"],
        ["Platinum services (launch now)", "63 (39.1%)"],
        ["Gold services (high priority)", "46 (28.6%)"],
        ["Sweet spot (High Auto + Low Comp)", "63 services"],
        ["Services ≥75% automatable", "80 (49.7%)"],
        ["Low competition opportunities", "40 (24.8%)"],
        ["Top vertical: HVAC/Plumbing/Electrical", "7 services, 6 Platinum"],
        ["Top vertical: Pool Maintenance", "2 services, 2 Platinum"],
        ["Top vertical: Pet Grooming", "5 services, 3 Platinum"],
        ["Starting team size", "5-6 people"],
        ["Starting monthly budget", "₹3-5 Lakhs ($3,600-$6,000)"],
        ["Break-even target", "$4,000/month revenue"],
        ["90-day MRR target", "$5,000-$10,000"],
        ["90-day client target", "5-15 active clients"],
        ["Target gross margin", "≥ 60%"],
        ["Target client retention", "≥ 90% monthly"],
    ],
    col_widths=[3.0, 3.0]
)

doc.add_paragraph()
doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("— End of Implementation Handbook —")
run.font.italic = True
run.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run(
    "Companion files: Handover Document (.docx) + Analysis Spreadsheet (.xlsx)\n"
    "Use the study guide (Part A) first. Then fill the worksheets (Part B). Then execute (Part C-H)."
)
run.font.italic = True
run.font.size = Pt(9)
run.font.color.rgb = RGBColor(0x99, 0x99, 0x99)

# ── Save ──
output = "/home/user/India_US_SMB_Implementation_Handbook.docx"
doc.save(output)
print(f"Saved to {output}")
