
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "India→US SMB Services Analysis"

# ── Column headers ──
headers = [
    "S.No.",
    "Category / Vertical",
    "Service / Product",
    "Description",
    "Automation\nPotential (%)",
    "Automation\nConfidence",
    "Degree of Automation\n(What can/can't be automated)",
    "Competitive\nIntensity",
    "Opportunity\nTier",
    "Opportunity\nScore",
    "Ticket Size\n(USD)",
    "Delivery\nModel",
    "Key Notes",
]

# ── Styles ──
header_font = Font(bold=True, color="FFFFFF", size=11, name="Calibri")
header_fill = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)

thin_border = Border(
    left=Side(style="thin", color="B0B0B0"),
    right=Side(style="thin", color="B0B0B0"),
    top=Side(style="thin", color="B0B0B0"),
    bottom=Side(style="thin", color="B0B0B0"),
)

cell_font = Font(size=10, name="Calibri")
cell_align = Alignment(vertical="center", wrap_text=True)
center_align = Alignment(horizontal="center", vertical="center", wrap_text=True)

# Color fills for automation confidence
conf_fills = {
    "Very High": PatternFill(start_color="92D050", end_color="92D050", fill_type="solid"),
    "High":      PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid"),
    "Medium":    PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid"),
    "Low":       PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid"),
}

# Color fills for competitive intensity
comp_fills = {
    "Very High": PatternFill(start_color="FF4444", end_color="FF4444", fill_type="solid"),
    "High":      PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid"),
    "Medium":    PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid"),
    "Low":       PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid"),
}
comp_fonts = {
    "Very High": Font(size=10, name="Calibri", bold=True, color="FFFFFF"),
    "High":      Font(size=10, name="Calibri", bold=True, color="9C0006"),
    "Medium":    Font(size=10, name="Calibri", bold=True, color="9C6500"),
    "Low":       Font(size=10, name="Calibri", bold=True, color="006100"),
}

# Automation potential color bands
def auto_pot_fill(val):
    if val >= 75:
        return PatternFill(start_color="92D050", end_color="92D050", fill_type="solid")
    elif val >= 50:
        return PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
    elif val >= 30:
        return PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
    else:
        return PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")

# ── TIER CALCULATION ──
def calc_tier_and_score(auto_pct, conf, comp):
    """Calculate opportunity tier and score"""
    score = auto_pct  # base from automation potential (0-100)

    # Competition modifier (reward low competition, penalize high)
    comp_mod = {"Low": 15, "Medium": 0, "High": -12, "Very High": -25}
    score += comp_mod.get(comp, 0)

    # Confidence modifier (reward high confidence)
    conf_mod = {"Very High": 10, "High": 5, "Medium": 0, "Low": -10}
    score += conf_mod.get(conf, 0)

    # Clamp
    score = max(0, min(120, score))

    # Tier assignment
    if score >= 85:
        tier = "⭐⭐⭐⭐⭐ Platinum"
        label = "Immediate Launch"
    elif score >= 70:
        tier = "⭐⭐⭐⭐ Gold"
        label = "High Priority"
    elif score >= 52:
        tier = "⭐⭐⭐ Silver"
        label = "Viable with Strategy"
    elif score >= 38:
        tier = "⭐⭐ Bronze"
        label = "Challenging / Niche Down"
    else:
        tier = "⚠️ Red Flag"
        label = "Commodity / Avoid"

    return tier, label, score

# Tier visual styles
tier_fills = {
    "⭐⭐⭐⭐⭐ Platinum": PatternFill(start_color="E5C100", end_color="E5C100", fill_type="solid"),  # Gold
    "⭐⭐⭐⭐ Gold":       PatternFill(start_color="D6E4F0", end_color="D6E4F0", fill_type="solid"),  # Blue-silver
    "⭐⭐⭐ Silver":       PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid"),  # Silver
    "⭐⭐ Bronze":         PatternFill(start_color="FDE9D9", end_color="FDE9D9", fill_type="solid"),  # Bronze
    "⚠️ Red Flag":         PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid"),  # Red
}
tier_fonts = {
    "⭐⭐⭐⭐⭐ Platinum": Font(size=10, name="Calibri", bold=True, color="6B4C00"),
    "⭐⭐⭐⭐ Gold":       Font(size=10, name="Calibri", bold=True, color="1F4E79"),
    "⭐⭐⭐ Silver":       Font(size=10, name="Calibri", bold=True, color="404040"),
    "⭐⭐ Bronze":         Font(size=10, name="Calibri", bold=True, color="843C0C"),
    "⚠️ Red Flag":         Font(size=10, name="Calibri", bold=True, color="9C0006"),
}

# ── DATA ──
# (category, service, description, automation%, confidence, degree, competition, ticket_size, delivery, notes)
data = [
    # ═══════════════════════════════════════════════════════════════
    # UNIVERSAL – DIGITAL MARKETING
    # ═══════════════════════════════════════════════════════════════
    ("Universal – Digital Marketing", "Website Design & Development",
     "Custom websites, landing pages, WordPress/Shopify builds",
     55, "Medium",
     "CAN: Template generation, asset resizing, CMS population, code scaffolding, image optimization via AI.\nCANNOT: Custom UX strategy, complex interactive features, client-facing revisions, accessibility compliance auditing.",
     "Very High", "$2,000 – $10,000", "Project + Retainer",
     "AI builders (Wix, Framer) squeezing low end; differentiation needs vertical specialization."),

    ("Universal – Digital Marketing", "Local SEO",
     "Google Business Profile optimization, local citations, keyword ranking, on-page SEO",
     45, "Medium",
     "CAN: Citation building, schema markup, meta tag generation, rank tracking, audit reports via tools.\nCANNOT: Hyperlocal relationship strategies, Google reinstatement appeals, nuanced content localization, competitive market strategy.",
     "Very High", "$500 – $2,000/mo", "Monthly Retainer",
     "Extremely crowded market; low barrier to entry. Need to niche down (e.g., SEO for solar or salons)."),

    ("Universal – Digital Marketing", "Social Media Management",
     "Content creation, posting, engagement, community management across platforms",
     55, "Medium",
     "CAN: AI caption/copy generation, hashtag research, scheduling, basic graphic templates, sentiment analysis.\nCANNOT: Authentic brand voice, real-time crisis response, influencer negotiations, trending content creation, video production quality.",
     "Very High", "$500 – $3,000/mo", "Monthly Retainer",
     "Saturated at low end; premium differentiation via video/reels expertise."),

    ("Universal – Digital Marketing", "PPC / Paid Ads Management",
     "Google Ads, Facebook/Meta Ads, campaign setup, optimization, A/B testing",
     65, "High",
     "CAN: Automated bid management, audience segmentation, ad copy variants, performance reporting, budget allocation via AI tools.\nCANNOT: Creative strategy, brand positioning, cross-channel attribution nuance, client reporting/communication.",
     "High", "$500 – $3,000/mo + ad spend", "Monthly Retainer",
     "Google Performance Max & Meta Advantage+ increasing automation; human value shifting to strategy."),

    ("Universal – Digital Marketing", "Email & SMS Marketing",
     "Campaign design, drip sequences, newsletters, automated workflows",
     80, "Very High",
     "CAN: AI copywriting, template design, send-time optimization, segmentation, A/B testing, analytics, trigger-based automation.\nCANNOT: Brand tone calibration for unique businesses, complex lifecycle journey design, legal compliance review (CAN-SPAM, TCPA).",
     "High", "$300 – $1,500/mo", "Monthly Retainer",
     "Klaviyo, Mailchimp, GoHighLevel already automate heavily; value-add in strategy & integration."),

    ("Universal – Digital Marketing", "Review & Reputation Management",
     "Review monitoring, response drafting, review generation campaigns, rating improvement",
     70, "High",
     "CAN: Automated review solicitation (SMS/email), sentiment monitoring, AI-drafted responses, alert systems, competitor comparison.\nCANNOT: Handling fake/negative review disputes with platforms, in-person service recovery advice, complex complaint resolution.",
     "Medium", "$200 – $800/mo", "Monthly Retainer",
     "Growing demand; tools like Podium, Birdeye exist but white-label opportunity for personalized service."),

    ("Universal – Digital Marketing", "Content Creation (Blog, Video, Graphics)",
     "Blog posts, video editing, infographics, social media graphics, photo editing",
     60, "High",
     "CAN: AI blog drafts, social graphics (Canva/Templated), video clipping, thumbnail generation, transcription, basic photo editing.\nCANNOT: Original investigative journalism, brand-specific video production, high-end motion graphics, nuanced editorial judgment.",
     "Very High", "$300 – $2,500/mo", "Monthly Retainer / Per-piece",
     "AI content flooding market; quality differentiation critical. Video editing commands premium rates."),

    ("Universal – Digital Marketing", "Logo & Branding",
     "Brand identity, logo design, brand guidelines, style guides",
     50, "Medium",
     "CAN: AI logo concept generation (Midjourney, DALL-E), color palette suggestions, font pairing, mood boards.\nCANNOT: Unique brand strategy, trademark viability assessment, deep market research, client presentation/persuasion, final design refinement.",
     "High", "$500 – $5,000", "Project",
     "AI tools enabling commodity pricing; human designers needed for premium/strategic branding."),

    # ═══════════════════════════════════════════════════════════════
    # UNIVERSAL – BACK OFFICE
    # ═══════════════════════════════════════════════════════════════
    ("Universal – Back Office", "Bookkeeping & Accounting",
     "QuickBooks/Xero management, reconciliation, AP/AR, financial reporting, tax prep support",
     75, "High",
     "CAN: Automated bank feeds, receipt OCR, transaction categorization (AI), reconciliation, financial report generation, tax document preparation.\nCANNOT: Complex tax strategy, audit representation, advisory/forecasting judgment, nuanced GAAP decisions, client relationship management.",
     "High", "$300 – $1,500/mo", "Monthly Retainer",
     "Strong demand; established Indian players. Differentiate via industry specialization."),

    ("Universal – Back Office", "Payroll Processing Support",
     "Payroll data processing, compliance tracking, benefits administration support",
     80, "Very High",
     "CAN: Data entry, timesheet compilation, tax calculation, compliance checking, report generation, garnishment processing.\nCANNOT: Employment law interpretation, complex benefit plan design, state-specific compliance judgment, client advisory.",
     "Medium", "$200 – $800/mo", "Monthly Retainer",
     "ADP, Gusto, Rippling automating core; support/processing role shrinking but still needed for complex cases."),

    ("Universal – Back Office", "Virtual Assistant Services",
     "Scheduling, email management, data entry, research, travel booking, admin tasks",
     50, "Medium",
     "CAN: Calendar management, email triage, data entry, basic research, booking/travel, document formatting.\nCANNOT: Judgment calls, complex problem-solving, in-person tasks, relationship management, confidential decision-making.",
     "Very High", "$4 – $15/hr ($600 – $2,400/mo)", "Hourly / Monthly",
     "Largest and most competitive segment; AI assistants (ChatGPT, Copilot) eroding low-end VA tasks."),

    ("Universal – Back Office", "Customer Support (Phone/Email/Chat)",
     "Inbound/outbound customer service, helpdesk, ticket management, FAQ handling",
     65, "High",
     "CAN: AI chatbots (tier-1), email response drafting, ticket routing, FAQ automation, sentiment detection, call transcription & summarization.\nCANNOT: Complex complaint resolution, empathetic handling of sensitive issues, upselling judgment, escalation management, multi-language real-time calls.",
     "Very High", "$800 – $3,000/mo", "Monthly Retainer / Per-agent",
     "Massive Indian BPO industry; AI chatbots replacing tier-1 but human agents still needed for complex cases."),

    ("Universal – Back Office", "CRM Setup & Management",
     "HubSpot, Salesforce, Zoho configuration, pipeline management, data hygiene",
     60, "High",
     "CAN: Data import/cleanup, pipeline automation setup, report/dashboards, email sequence configuration, lead scoring rules.\nCANNOT: Sales strategy design, custom complex integrations, change management, user adoption training, business process reengineering.",
     "Medium", "$1,000 – $5,000 setup + $500–$1,500/mo", "Project + Retainer",
     "Specialized skill; high value-add for SMBs struggling with CRM adoption."),

    ("Universal – Back Office", "Lead Generation & Qualification",
     "Outbound prospecting, list building, cold email/calls, lead scoring, appointment setting",
     55, "Medium",
     "CAN: List building (Apollo, ZoomInfo), cold email sequences, AI-powered lead scoring, data enrichment, basic qualification scripts.\nCANNOT: Complex B2B relationship building, nuanced objection handling, industry-specific qualification judgment, closing strategy.",
     "Very High", "$500 – $3,000/mo", "Monthly Retainer + Commission",
     "Very crowded; AI tools (Instantly, Smartlead) enabling everyone to do cold outreach. Need niche expertise."),

    # ═══════════════════════════════════════════════════════════════
    # UNIVERSAL – TECHNOLOGY
    # ═══════════════════════════════════════════════════════════════
    ("Universal – Technology", "Custom SaaS / Web Application",
     "Booking systems, field service apps, customer portals, custom software",
     50, "Medium",
     "CAN: AI code generation (Copilot, Cursor), boilerplate scaffolding, standard CRUD apps, database design, API integrations.\nCANNOT: Complex business logic design, security architecture, scalable system design, client requirements gathering, UX strategy, QA testing for edge cases.",
     "High", "$5,000 – $50,000+", "Project",
     "Indian dev shops dominate globally; race to bottom on commodity apps. Need domain expertise for premium."),

    ("Universal – Technology", "Mobile App Development",
     "iOS/Android customer-facing apps, technician apps, internal tools",
     50, "Medium",
     "CAN: UI scaffolding, standard CRUD features, push notifications, basic API integration, cross-platform development (Flutter/React Native).\nCANNOT: Native performance optimization, complex UX, App Store compliance, real-time features, hardware integration, security architecture.",
     "High", "$10,000 – $50,000+", "Project",
     "Very competitive; low-code tools reducing simple app demand. Premium in complex, industry-specific apps."),

    ("Universal – Technology", "AI Chatbot & Automation",
     "Customer FAQ bots, lead capture bots, appointment booking bots, workflow automation",
     75, "High",
     "CAN: AI chatbot building (Botpress, Voiceflow, custom GPT), Zapier/Make workflows, document processing, data extraction, auto-responses.\nCANNOT: Complex multi-step business process automation, edge case handling, physical workflow integration, brand voice training without human oversight.",
     "Medium", "$1,000 – $10,000 + $200–$500/mo", "Project + Maintenance",
     "Hot market; AI making this more accessible but implementation expertise still valuable."),

    ("Universal – Technology", "Cloud Infrastructure & DevOps",
     "AWS/GCP hosting, CI/CD, security, backups, monitoring",
     60, "High",
     "CAN: IaC (Terraform/Pulumi), automated deployments, monitoring setup, backup configuration, security scanning, cost optimization.\nCANNOT: Complex architecture decisions, incident response judgment, compliance strategy, disaster recovery planning, vendor negotiation.",
     "Medium", "$1,000 – $5,000/mo", "Monthly Retainer",
     "Skilled talent needed; AI-assisted DevOps growing but human oversight critical for production systems."),

    ("Universal – Technology", "Data Entry & Processing",
     "Manual data entry, document digitization, form processing, data migration",
     85, "Very High",
     "CAN: OCR, AI data extraction, automated form processing, structured data migration, spreadsheet automation, API-based data transfer.\nCANNOT: Handwritten document interpretation, ambiguous data judgment calls, physical document handling, quality verification of complex data.",
     "Very High", "$3 – $10/hr ($400 – $1,600/mo)", "Hourly / Per-task",
     "Rapidly being automated by AI; shrinking market. Transition to 'data quality' or 'data management' for longevity."),

    # ═══════════════════════════════════════════════════════════════
    # LANDSCAPING / LAWN CARE
    # ═══════════════════════════════════════════════════════════════
    ("Landscaping / Lawn Care", "GIS & Satellite Property Measurement",
     "Property boundary mapping, lawn area calculation, hardscape measurement using aerial imagery",
     85, "Very High",
     "CAN: Fully automated via satellite imagery APIs (Google Earth, Nearmap), AI lot segmentation, area calculation, PDF report generation.\nCANNOT: On-site verification, micro-terrain assessment, tree/obstacle identification for mowing complexity, client-specific measurement requests.",
     "Low", "$5 – $25/property", "Per-report / API",
     "Highly automatable; companies like GIS Pros already doing this. Low competition from India specifically but high tech barrier."),

    ("Landscaping / Lawn Care", "Landscape Design Rendering (2D/3D)",
     "Visual design mockups, 3D renderings, before/after concepts for client proposals",
     55, "Medium",
     "CAN: AI image generation for concepts, plant library integration, basic 2D layouts, photo overlays.\nCANNOT: Site-specific design judgment, plant compatibility knowledge, local climate/soil considerations, detailed construction drawings, client presentation.",
     "Medium", "$100 – $500/design", "Per-design",
     "AI tools (Midjourney, VizTerra) enabling faster production; skilled designers add value for complex projects."),

    ("Landscaping / Lawn Care", "Job Estimating & Quoting",
     "Material cost calculation, labor estimation, proposal document generation",
     60, "High",
     "CAN: Material cost calculators, labor hour estimation from area data, proposal PDF generation, pricing templates, supplier price lookup.\nCANNOT: Site condition assessment, access difficulty judgment, client budget negotiation, custom design costing, local market pricing knowledge.",
     "Medium", "$50 – $200/estimate", "Per-estimate / Retainer",
     "Needs integration with estimating software (Jobber, LMN); value in speed and accuracy."),

    ("Landscaping / Lawn Care", "Route Optimization for Crews",
     "Minimize drive time between jobs, fuel cost optimization, schedule optimization",
     80, "Very High",
     "CAN: Algorithmic route optimization (Google Maps API, Route4Me), schedule optimization, fuel cost calculation, real-time traffic integration, automated re-routing.\nCANNOT: Crew preference management, on-site delay handling, equipment allocation, emergency rescheduling judgment.",
     "Medium", "$200 – $500/mo", "Monthly SaaS / Retainer",
     "Existing tools (Route4Me, OptimoRoute) available; white-label/managed service opportunity."),

    ("Landscaping / Lawn Care", "Seasonal Marketing Campaigns",
     "Spring cleanup promos, fall leaf removal campaigns, email/SMS blasts for seasonal services",
     65, "High",
     "CAN: AI copywriting, email/SMS automation, graphic templates, social media scheduling, campaign analytics, A/B testing.\nCANNOT: Local market timing intuition, competitive response strategy, client relationship management, creative campaign concepts.",
     "High", "$300 – $1,000/mo", "Monthly Retainer",
     "Part of broader digital marketing; industry knowledge is the differentiator."),

    ("Landscaping / Lawn Care", "Permit & Regulation Research",
     "County/city permit requirements, HOA compliance, zoning research for landscape projects",
     65, "High",
     "CAN: Online permit database research, zoning code lookup, document preparation, checklist generation, deadline tracking.\nCANNOT: In-person permit submission, official communication with authorities, site-specific variance requests, legal interpretation of ambiguous codes.",
     "Low", "$50 – $150/permit", "Per-task",
     "Niche service; very few players. Good opportunity for specialization."),

    # ═══════════════════════════════════════════════════════════════
    # LOCATOR / PRIVATE INVESTIGATION
    # ═══════════════════════════════════════════════════════════════
    ("Locator / Private Investigation", "Skip Tracing Research",
     "Locating hard-to-find individuals through database searches, public records, social media",
     75, "High",
     "CAN: Automated database queries (TLO, IRB), public records search, social media OSINT, address history compilation, phone number verification.\nCANNOT: Field investigation, surveillance, interview/deception detection, legal process serving, court testimony.",
     "Medium", "$10 – $75/report", "Per-report / Volume",
     "Moderate competition; established skip tracing tools exist but research/analysis still needs human touch for hard cases."),

    ("Locator / Private Investigation", "Background Check Report Compilation",
     "Report writing, court records retrieval, criminal history compilation, verification",
     70, "High",
     "CAN: Court record retrieval (PACER, county portals), report formatting, data aggregation, identity verification, automated report generation.\nCANNOT: Legal interpretation of records, FCRA compliance decisions, investigative judgment, client advisory on risk assessment.",
     "Medium", "$15 – $50/report", "Per-report / Volume",
     "Regulated industry (FCRA); compliance knowledge is barrier and differentiator."),

    ("Locator / Private Investigation", "Surveillance Report Analysis",
     "Review and catalog field footage, timeline creation, evidence organization",
     60, "High",
     "CAN: Video transcription, timestamp extraction, AI-powered object/person detection, timeline compilation, report formatting.\nCANNOT: Field surveillance, legal evidence chain of custody, courtroom testimony, investigative strategy.",
     "Low", "$25 – $100/report", "Per-report",
     "Low competition from India; niche opportunity with video AI capabilities."),

    ("Locator / Private Investigation", "Case Management System",
     "Custom CRM for PI firms, case tracking, evidence management, client reporting",
     55, "Medium",
     "CAN: Database design, custom web app development, document management, automated workflows, client portal.\nCANNOT: Legal compliance design, evidence handling protocol, investigator training, complex integration with law enforcement systems.",
     "Low", "$5,000 – $20,000", "Project",
     "Very niche; few custom solutions for PI firms specifically. High-value opportunity."),

    # ═══════════════════════════════════════════════════════════════
    # MORTGAGE BROKER
    # ═══════════════════════════════════════════════════════════════
    ("Mortgage Broker", "Loan Processing / File Preparation",
     "Loan file setup, document collection, verification, conditions clearing",
     65, "High",
     "CAN: Document collection/verification (AI OCR), income/asset calculation, AUS review, condition tracking, file status updates, disclosure preparation.\nCANNOT: Borrower relationship management, complex file scenario judgment, fraud detection nuance, investor guideline interpretation, closing coordination.",
     "High", "$100 – $500/loan file", "Per-loan",
     "Established Indian mortgage processing industry; competitive but growing US market creates volume demand."),

    ("Mortgage Broker", "Underwriting Support & Analysis",
     "Income/asset analysis, credit analysis, condition review, AU findings review",
     55, "Medium",
     "CAN: Automated income calculation, credit report analysis, guideline matching, condition checklist generation, ratio calculations.\nCANNOT: Complex scenario underwriting judgment, exception approval strategy, investor overlay interpretation, regulatory compliance decisions.",
     "High", "$150 – $600/loan", "Per-loan",
     "Requires deep US mortgage knowledge; experienced underwriters command premium. AI tools augmenting but not replacing."),

    ("Mortgage Broker", "Compliance & QC Review",
     "TRID compliance, post-closing audit, file review, regulatory compliance checking",
     60, "High",
     "CAN: Automated TRID timeline checking, document completeness verification, regulatory checklist, audit report generation, discrepancy flagging.\nCANNOT: Legal compliance judgment, regulatory interpretation, remediation strategy, state-specific regulation knowledge, auditor communication.",
     "Medium", "$100 – $400/loan", "Per-loan / Monthly",
     "Regulatory complexity creates demand; expertise barrier is high, which limits competition somewhat."),

    ("Mortgage Broker", "Appraisal Review & Comp Research",
     "Appraisal report analysis, comparable sales research, value opinion support",
     65, "High",
     "CAN: MLS data retrieval, comparable sales analysis, automated valuation models (AVM), report formatting, market trend analysis.\nCANNOT: Licensed appraisal opinions, property condition judgment, local market expertise, appraisal dispute strategy.",
     "Medium", "$50 – $150/review", "Per-review",
     "Needs access to US MLS data (cost barrier); established players exist but volume demand is consistent."),

    ("Mortgage Broker", "Borrower Communication & Updates",
     "Loan status updates, document request follow-ups, appointment scheduling, FAQ handling",
     70, "High",
     "CAN: Automated status emails/SMS, document request workflows, FAQ chatbot, appointment scheduling, NPS surveys.\nCANNOT: Complex borrower counseling, sensitive financial discussion, complaint resolution, loan officer relationship management.",
     "High", "$300 – $1,000/mo per broker", "Monthly Retainer",
     "High volume opportunity; borrower experience is key differentiator for brokers."),

    ("Mortgage Broker", "Digital Marketing for Mortgage",
     "Realtor outreach, referral network management, digital ads, content marketing",
     50, "Medium",
     "CAN: Email campaign automation, social media content, ad campaign management, CRM-based outreach, newsletter creation.\nCANNOT: Realtor relationship building, referral trust development, compliance in marketing (RESPA, NMLS), local market positioning.",
     "High", "$1,000 – $5,000/mo", "Monthly Retainer",
     "Niche mortgage marketing requires RESPA compliance knowledge; regulatory barrier limits competition somewhat."),

    # ═══════════════════════════════════════════════════════════════
    # SOLAR
    # ═══════════════════════════════════════════════════════════════
    ("Solar", "System Design & Engineering (Aurora/Helioscope)",
     "Panel layout design, string sizing, shading analysis, production estimates",
     70, "High",
     "CAN: Automated panel layouts, production modeling (Helioscope, Aurora), shading analysis, string sizing, single-line diagrams, permit-ready drawings.\nCANNOT: Site-specific structural assessment, local code interpretation, utility-specific requirements, custom engineering for complex roofs.",
     "High", "$50 – $200/design", "Per-design",
     "Established Indian solar design firms; competitive. Quality + speed differentiators needed."),

    ("Solar", "Proposal Generation",
     "Custom sales proposals with savings projections, financing options, visual presentations",
     65, "High",
     "CAN: Automated proposal generation from design data, savings calculation, financing option modeling, ROI projections, visual rendering.\nCANNOT: Sales strategy customization, client-specific objection handling, competitive positioning, brand-aligned creative design.",
     "High", "$30 – $100/proposal", "Per-proposal / Retainer",
     "Volume play; solar companies generate hundreds of proposals monthly. Quality + speed = competitive edge."),

    ("Solar", "Utility Rate & Incentive Research",
     "Rate analysis, net metering policy research, federal/state/local incentive research",
     75, "High",
     "CAN: Automated utility rate database lookups, incentive research, tax credit calculation, SREC market analysis, policy tracking.\nCANNOT: Real-time policy change interpretation, utility-specific negotiation strategy, complex commercial rate analysis, regulatory filing.",
     "Medium", "$25 – $75/research", "Per-research / Retainer",
     "Niche expertise; high value-add for solar companies. Database maintenance creates recurring need."),

    ("Solar", "Permit & Interconnection Documentation",
     "AHJ-specific permit sets, utility interconnection applications, engineering stamps coordination",
     55, "Medium",
     "CAN: Permit document preparation, standard drawing sets, application form filling, checklist generation, submission tracking.\nCANNOT: AHJ-specific relationship management, plan reviewer negotiation, structural engineering stamps, field inspection support.",
     "Medium", "$50 – $200/permit set", "Per-permit",
     "Jurisdiction-specific knowledge is barrier; scale advantage if you cover many AHJs."),

    ("Solar", "Lead Generation & Appointment Setting",
     "Door-to-door canvassing lists, digital lead gen, phone appointment setting, lead qualification",
     50, "Medium",
     "CAN: Canvassing route optimization, digital ad campaigns, AI-powered lead scoring, automated outreach, CRM management.\nCANNOT: In-person sales, complex objection handling, door-to-door canvassing execution, closing, customer relationship management.",
     "Very High", "$500 – $3,000/mo + commission", "Retainer + Commission",
     "Extremely competitive; solar lead gen is a $1B+ market. Differentiate with data quality and qualification rigor."),

    ("Solar", "Post-Installation Monitoring & Support",
     "System performance monitoring, warranty claims, troubleshooting, customer service",
     70, "High",
     "CAN: Automated performance monitoring, anomaly detection, warranty claim processing, ticket management, customer FAQ, reporting.\nCANNOT: Physical system inspection, inverter troubleshooting judgment, roof leak assessment, utility negotiation, system redesign.",
     "Medium", "$200 – $800/mo per installer", "Monthly Retainer",
     "Growing market as solar installations age; monitoring + support is high-value recurring service."),

    ("Solar", "Commercial Solar Feasibility Analysis",
     "Financial modeling, energy audit support, PPA/lease analysis, commercial proposal development",
     60, "High",
     "CAN: Financial modeling (NPV, IRR), utility bill analysis, incentive stacking, load profile analysis, report generation.\nCANNOT: On-site energy audit, structural roof assessment, utility negotiation, complex commercial deal structuring.",
     "Low", "$500 – $2,000/analysis", "Per-analysis",
     "Niche within solar; higher ticket size, lower competition. Requires financial modeling + energy knowledge."),

    # ═══════════════════════════════════════════════════════════════
    # SALON / SPA / BARBERSHOP
    # ═══════════════════════════════════════════════════════════════
    ("Salon / Spa / Barbershop", "Booking System & Online Scheduling",
     "Custom appointment booking, automated reminders, no-show reduction, calendar management",
     85, "Very High",
     "CAN: Automated booking engine, SMS/email reminders, waitlist management, deposit collection, calendar syncing, no-show analytics.\nCANNOT: In-person customer service, walk-in management, stylist preference matching, complex rescheduling negotiation.",
     "High", "$200 – $500/mo", "Monthly SaaS",
     "Vagaro, Square, Fresha dominate; custom builds only for chains or unique needs."),

    ("Salon / Spa / Barbershop", "Social Media Content & Growth",
     "Instagram/TikTok reels, before/after posts, trending content, influencer coordination",
     55, "Medium",
     "CAN: AI video editing, caption writing, hashtag research, scheduling, template design, analytics reporting.\nCANNOT: On-site video production, authentic stylist content, trending sound selection, in-person influencer events, real-time engagement.",
     "High", "$300 – $1,500/mo", "Monthly Retainer",
     "Visual platforms critical for salons; video content commands premium. On-site production limits remote delivery."),

    ("Salon / Spa / Barbershop", "Email & SMS Campaigns",
     "Re-activation campaigns, birthday offers, holiday promos, new service announcements",
     80, "Very High",
     "CAN: Automated birthday/anniversary emails, re-activation sequences, promo campaigns, segmentation, A/B testing, analytics.\nCANNOT: Personalized stylist-client relationship messages, event planning, complex loyalty program design.",
     "High", "$200 – $800/mo", "Monthly Retainer",
     "Highly automatable; value in integration with booking system and personalized messaging."),

    ("Salon / Spa / Barbershop", "Loyalty & Membership Program Design",
     "Points systems, monthly memberships, referral programs, package deals",
     60, "High",
     "CAN: Program structure design, automated tracking, reward fulfillment, analytics, promotional campaigns.\nCANNOT: Pricing strategy for local market, member experience design, staff incentive alignment, competitive positioning.",
     "Low", "$1,000 – $5,000 setup + $200–$500/mo", "Project + Retainer",
     "Underserved niche; salons want recurring revenue but lack program design expertise."),

    ("Salon / Spa / Barbershop", "Inventory & Product Management",
     "Back-bar tracking, retail product orders, reorder alerts, vendor management",
     75, "High",
     "CAN: Automated reorder alerts, usage tracking, vendor price comparison, inventory analytics, purchase order generation.\nCANNOT: Physical inventory counts, product quality assessment, vendor negotiation, theft/shrinkage investigation.",
     "Low", "$200 – $500/mo", "Monthly Retainer",
     "Niche but valuable; salons lose significant money on product waste and stockouts."),

    # ═══════════════════════════════════════════════════════════════
    # PET GROOMING / PET SPA
    # ═══════════════════════════════════════════════════════════════
    ("Pet Grooming / Pet Spa", "Appointment & Reminder System",
     "Automated booking, SMS reminders, vaccination tracking, breed-specific scheduling",
     85, "Very High",
     "CAN: Automated booking, multi-channel reminders (SMS/email), vaccination due alerts, breed-specific time allocation, no-show reduction, calendar optimization.\nCANNOT: Pet temperament assessment, in-person check-in, emergency rescheduling for distressed pets, client relationship management.",
     "Medium", "$150 – $400/mo", "Monthly SaaS",
     "Pet-specific scheduling is niche; general booking tools don't handle breed-specific grooming times well."),

    ("Pet Grooming / Pet Spa", "Pet Profile & Health Management",
     "Breed-specific service recommendations, vaccination tracking, health notes, grooming history",
     80, "Very High",
     "CAN: Automated breed-based recommendations, health record tracking, vaccination schedule alerts, grooming history, allergy/condition flags.\nCANNOT: Veterinary assessment, in-person health observation, emergency medical judgment, breed-specific grooming technique guidance.",
     "Low", "$100 – $300/mo", "Monthly SaaS / Retainer",
     "Very niche; few purpose-built solutions. High-value for pet spas managing 100+ regular clients."),

    ("Pet Grooming / Pet Spa", "Social Media & Pet Content Marketing",
     "Cute pet photos/videos for engagement, grooming transformations, local marketing",
     55, "Medium",
     "CAN: Photo/video editing, social scheduling, caption writing, hashtag research, before/after collages, review response.\nCANNOT: On-site pet photography (pets need handling), authentic pet content, video production, in-person events.",
     "High", "$200 – $1,000/mo", "Monthly Retainer",
     "Pet content is inherently viral; high engagement but needs authentic on-site content capture."),

    ("Pet Grooming / Pet Spa", "Mobile Groomer Route Optimization",
     "Route planning for mobile groomers, scheduling optimization, territory management",
     85, "Very High",
     "CAN: Route optimization algorithms, appointment clustering, drive-time minimization, fuel cost tracking, territory mapping, automated scheduling.\nCANNOT: On-site service delivery, pet handling decisions, emergency route changes, client scheduling preferences.",
     "Low", "$150 – $400/mo", "Monthly SaaS",
     "Growing mobile pet grooming market; route optimization directly impacts profitability."),

    ("Pet Grooming / Pet Spa", "Pet Product E-commerce Setup",
     "Online store for pet products, grooming supplies, branded merchandise",
     65, "High",
     "CAN: E-commerce setup (Shopify/WooCommerce), product listing, payment integration, inventory management, email marketing, SEO.\nCANNOT: Product sourcing decisions, physical fulfillment, product quality testing, vendor negotiation, custom product development.",
     "Medium", "$1,000 – $5,000 setup + $300–$800/mo", "Project + Retainer",
     "Pet industry e-commerce booming; opportunity for recurring product revenue for pet spas."),

    # ═══════════════════════════════════════════════════════════════
    # HVAC / PLUMBING / ELECTRICAL
    # ═══════════════════════════════════════════════════════════════
    ("HVAC / Plumbing / Electrical", "Estimating & Quoting Software",
     "Job cost estimation, material takeoffs, labor calculation, proposal generation",
     70, "High",
     "CAN: Automated material takeoffs, cost calculator engines, proposal PDF generation, labor hour estimation from job type, pricing database management.\nCANNOT: On-site job assessment, hidden problem anticipation, code compliance judgment, client negotiation, custom scope changes.",
     "Medium", "$50 – $300/estimate or $300–$1,000/mo", "Per-estimate / SaaS",
     "ServiceTitan, Housecall Pro have built-in; custom solutions for smaller shops underserved."),

    ("HVAC / Plumbing / Electrical", "Dispatching & Scheduling Optimization",
     "Technician scheduling, emergency dispatch logic, route optimization, workload balancing",
     80, "Very High",
     "CAN: Algorithmic scheduling, real-time dispatch, route optimization, skill-matching algorithms, automated ETAs, workload balancing.\nCANNOT: Technician preference management, emergency judgment calls, on-site scope changes, customer relationship nuance, field troubleshooting.",
     "Medium", "$300 – $1,000/mo", "Monthly SaaS / Retainer",
     "Critical for profitability; 15-30% drive-time reduction is typical. Existing tools exist but managed service opportunity."),

    ("HVAC / Plumbing / Electrical", "Permit & Code Compliance Research",
     "Local building code research, permit application preparation, inspection checklists",
     65, "High",
     "CAN: Building code database lookup, permit application form filling, inspection checklist generation, deadline tracking, document preparation.\nCANNOT: Licensed professional sign-off, jurisdiction relationship management, on-site code interpretation, variance request strategy.",
     "Low", "$75 – $250/permit", "Per-task",
     "Very underserved; contractors hate paperwork. Huge pain point with few dedicated solutions."),

    ("HVAC / Plumbing / Electrical", "Parts & Inventory Management",
     "Stock tracking, auto-reorder, supplier price comparison, van inventory optimization",
     80, "Very High",
     "CAN: Automated reorder triggers, supplier price comparison, inventory analytics, barcode scanning integration, usage pattern analysis, purchase order generation.\nCANNOT: Physical inventory counting, part quality inspection, supplier relationship management, emergency parts sourcing.",
     "Low", "$200 – $800/mo", "Monthly Retainer / SaaS",
     "Contractors lose thousands in overstock/stockouts; very few purpose-built solutions for trade SMBs."),

    ("HVAC / Plumbing / Electrical", "Local SEO & Lead Generation",
     "Google LSA management, HomeAdvisor/Angi lead response, local search ranking, emergency service marketing",
     55, "Medium",
     "CAN: Google LSA optimization, review management, SEO content, paid search campaigns, lead response automation, competitor tracking.\nCANNOT: Emergency call handling, relationship with lead platforms, market-specific pricing strategy, brand differentiation in commoditized market.",
     "Very High", "$1,000 – $5,000/mo", "Monthly Retainer",
     "Extremely competitive; HVAC/Plumbing are top-spending local SEO categories. Seasonal demand fluctuations."),

    ("HVAC / Plumbing / Electrical", "Maintenance Contract Management",
     "Seasonal maintenance reminders, contract renewals, automated scheduling, customer communication",
     85, "Very High",
     "CAN: Automated renewal reminders, seasonal campaign scheduling, contract tracking, customer communication, payment processing, analytics.\nCANNOT: On-site service delivery, equipment assessment, pricing negotiation, customer relationship management.",
     "Low", "$200 – $600/mo", "Monthly SaaS / Retainer",
     "Maintenance contracts are the #1 profit driver for HVAC; very few automated management tools exist."),

    ("HVAC / Plumbing / Electrical", "Invoice & Payment Processing",
     "Field-to-office invoice flow, payment collection, A/R aging, financing application support",
     75, "High",
     "CAN: Automated invoice generation from job data, payment reminders, online payment links, A/R aging reports, financing application processing.\nCANNOT: Dispute resolution, payment plan negotiation, lien filing, legal collection actions, complex accounting decisions.",
     "Medium", "$200 – $500/mo", "Monthly Retainer",
     "Cash flow is #1 challenge for trade SMBs; faster invoicing = faster payment."),

    # ═══════════════════════════════════════════════════════════════
    # AUTO REPAIR / MECHANIC SHOPS
    # ═══════════════════════════════════════════════════════════════
    ("Auto Repair / Mechanic", "Estimating & Digital Inspections",
     "Digital vehicle inspection reports, repair estimates, photo documentation, customer approval workflows",
     70, "High",
     "CAN: Digital inspection templates, automated estimate generation, photo/video documentation, customer approval via SMS, DTC code lookup, parts pricing.\nCANNOT: Physical inspection, diagnostic judgment, technician skill assessment, complex drivetrain diagnostics, warranty adjudication.",
     "Medium", "$200 – $600/mo", "Monthly SaaS",
     "Digital vehicle inspections (DVIs) dramatically increase repair approval rates; high ROI for shops."),

    ("Auto Repair / Mechanic", "Parts Sourcing & Pricing",
     "Supplier comparison, parts lookup, pricing optimization, availability checking",
     75, "High",
     "CAN: Multi-supplier price comparison, automated parts lookup (VIN-based), availability checking, price history tracking, auto-order workflows.\nCANNOT: Physical parts inspection, supplier relationship negotiation, warranty claims, core charge management, emergency sourcing.",
     "Medium", "$150 – $500/mo", "Monthly SaaS",
     "Parts margin is 30-40% of shop revenue; even small pricing improvements = significant profit."),

    ("Auto Repair / Mechanic", "Customer Communication & Reminders",
     "Service reminders, repair status updates, review requests, follow-up campaigns",
     85, "Very High",
     "CAN: Automated service reminders (oil change, tire rotation), repair status SMS, review requests, recall notifications, seasonal campaigns.\nCANNOT: In-person customer service, complaint resolution, upselling judgment, estimate explanation, pickup/delivery logistics.",
     "Medium", "$150 – $400/mo", "Monthly SaaS",
     "Service reminders alone can increase shop revenue 20-30%; very high ROI for customers."),

    ("Auto Repair / Mechanic", "Shop Management System (SMM)",
     "Work order management, technician scheduling, inventory, invoicing, vendor management",
     60, "High",
     "CAN: Work order workflows, technician assignment, time tracking, invoicing automation, inventory alerts, reporting dashboards.\nCANNOT: Shop layout optimization, technician training, customer relationship management, regulatory compliance (EPA, OSHA), purchasing strategy.",
     "High", "$300 – $1,000/mo", "Monthly SaaS",
     "Shop-Link, Mitchell1, tekmetric exist; custom solutions only for multi-shop operations or unique workflows."),

    ("Auto Repair / Mechanic", "Warranty & Recall Management",
     "Manufacturer warranty claim processing, recall notification, campaign tracking",
     70, "High",
     "CAN: Recall database monitoring, automated customer notification, warranty claim form preparation, deadline tracking, reimbursement tracking.\nCANNOT: Manufacturer negotiation, warranty denial appeals, technical warranty interpretation, physical repair verification.",
     "Low", "$100 – $400/mo", "Monthly Retainer",
     "Very underserved niche; shops lose thousands in unclaimed warranty/reimbursements annually."),

    # ═══════════════════════════════════════════════════════════════
    # REAL ESTATE
    # ═══════════════════════════════════════════════════════════════
    ("Real Estate", "Listing Marketing & Content",
     "Property descriptions, virtual staging, photo editing, video tours, social media content",
     60, "High",
     "CAN: AI property descriptions, virtual staging (AI furniture placement), photo enhancement, video tour editing, social media content creation.\nCANNOT: On-site photography, property assessment, client relationship management, market pricing strategy, negotiation support.",
     "High", "$100 – $500/listing", "Per-listing / Retainer",
     "Virtual staging is 90%+ automatable with AI; massive demand from agents. Photo editing is commodity."),

    ("Real Estate", "Transaction Coordination",
     "Contract tracking, deadline management, document preparation, closing coordination",
     75, "High",
     "CAN: Automated deadline tracking, document preparation, milestone checklists, party communication, compliance checking, e-signature management.\nCANNOT: Legal review, title issue resolution, inspection negotiation support, lender coordination, client advisory.",
     "High", "$300 – $700/transaction", "Per-transaction",
     "Huge volume opportunity; transaction coordinators are in short supply. 80% of TC work is document/deadline management."),

    ("Real Estate", "Lead Generation & CRM Management",
     "Zillow/Realtor.com lead follow-up, ISA services, CRM setup, drip campaigns, database management",
     60, "High",
     "CAN: Automated lead follow-up sequences, AI-powered lead scoring, CRM management, drip campaigns, market report generation, social media lead capture.\nCANNOT: Buyer/seller consultation, showing coordination, negotiation, market expertise, relationship building.",
     "Very High", "$500 – $3,000/mo", "Monthly Retainer",
     "Inside Sales Agent (ISA) services are booming; AI tools improving conversion but human follow-up still critical."),

    ("Real Estate", "CMA & Market Analysis Reports",
     "Comparative market analysis, market trend reports, neighborhood data, investment analysis",
     75, "High",
     "CAN: MLS data extraction, automated CMA generation, market trend analysis, neighborhood demographic reports, investment ROI calculations.\nCANNOT: Property condition assessment, local market intuition, client presentation, pricing strategy, unique property valuation.",
     "Medium", "$50 – $200/report", "Per-report / Monthly",
     "Data-heavy work perfect for remote delivery; agents spend 3-5 hours/week on CMAs."),

    ("Real Estate", "Listing Website & Single Property Sites",
     "Custom property landing pages, virtual tour integration, lead capture forms",
     80, "Very High",
     "CAN: Automated website templates, photo gallery setup, virtual tour embedding, lead capture forms, automated copy from MLS data.\nCANNOT: Custom design for luxury properties, unique branding, interactive feature development, IDX integration for brokerages.",
     "Medium", "$100 – $500/site", "Per-site",
     "Highly templatable; 10-15 min per site with automation. Luxury market commands premium for custom work."),

    ("Real Estate", "Compliance & File Management",
     "Transaction file compliance, document organization, audit preparation, record retention",
     80, "Very High",
     "CAN: Document checklist automation, file organization, compliance verification, e-signature tracking, audit-ready file assembly, deadline monitoring.\nCANNOT: Legal compliance interpretation, dispute resolution, regulatory filing, brokerage policy development, error resolution.",
     "Medium", "$200 – $500/mo", "Monthly Retainer",
     "Compliance is a major pain point for brokerages; fines for non-compliance are $1,000-$10,000+."),

    # ═══════════════════════════════════════════════════════════════
    # DENTAL PRACTICES
    # ═══════════════════════════════════════════════════════════════
    ("Dental Practices", "Appointment Scheduling & Reminders",
     "Automated booking, recall reminders, no-show reduction, waitlist management",
     90, "Very High",
     "CAN: Automated recall reminders, multi-channel confirmations, waitlist fill automation, new patient scheduling, cancellation backfill, holiday hour management.\nCANNOT: Emergency scheduling judgment, insurance pre-authorization, treatment plan discussion, clinical triage.",
     "Medium", "$200 – $600/mo", "Monthly SaaS",
     "Dental recall automation alone can recover 15-25% of unscheduled patients; massive ROI."),

    ("Dental Practices", "Insurance Verification & Claims Processing",
     "Benefits verification, claim submission, EOB processing, denial management, patient responsibility calculation",
     75, "High",
     "CAN: Automated benefits verification, claim scrubbing, EOB posting, denial tracking, patient balance calculation, appeal letter generation.\nCANNOT: Complex claim appeals, payer negotiation, regulatory compliance (HIPAA), patient financial counseling, audit defense.",
     "High", "$500 – $2,000/mo", "Monthly Retainer",
     "Dental billing is specialized; practices lose 5-15% revenue to claim errors. Indian dental billing is established."),

    ("Dental Practices", "Treatment Plan Presentation",
     "Visual treatment plans, cost breakdown, financing options, before/after simulations",
     60, "High",
     "CAN: Automated treatment plan documents, cost calculators, financing option comparison, before/after image simulation, comparison charts.\nCANNOT: Clinical treatment recommendation, patient education, chair-side presentation, insurance coverage optimization, clinical photography.",
     "Low", "$200 – $500/mo", "Monthly SaaS",
     "Visual treatment plans increase case acceptance 20-40%; very few remote solutions for this."),

    ("Dental Practices", "Patient Review & Reputation Management",
     "Review solicitation, Google Business optimization, review response, online reputation monitoring",
     75, "High",
     "CAN: Automated review requests (post-visit), AI-drafted responses, reputation monitoring, competitor comparison, Google Business optimization, review analytics.\nCANNOT: Handling negative review disputes, patient complaint resolution, HIPAA-compliant response drafting, legal review situations.",
     "Medium", "$200 – $600/mo", "Monthly Retainer",
     "Dental practices highly dependent on Google reviews; 4.5+ rating significantly impacts new patient flow."),

    ("Dental Practices", "Digital Marketing for Dental",
     "Local SEO, paid ads, new patient acquisition campaigns, content marketing",
     55, "Medium",
     "CAN: SEO content, paid search campaigns, social media management, patient educational content, email campaigns.\nCANNOT: Patient relationship building, community engagement, referral network development, brand positioning, local market intuition.",
     "Very High", "$1,000 – $5,000/mo", "Monthly Retainer",
     "Dental marketing is a $2B+ market; very competitive but high lifetime value per patient ($10K+)."),

    # ═══════════════════════════════════════════════════════════════
    # CHIROPRACTIC / PT / WELLNESS
    # ═══════════════════════════════════════════════════════════════
    ("Chiropractic / PT / Wellness", "Patient Scheduling & Communication",
     "Automated booking, appointment reminders, reactivation campaigns, exercise program delivery",
     85, "Very High",
     "CAN: Automated booking, multi-channel reminders, reactivation campaigns, exercise video delivery, progress tracking, patient education content.\nCANNOT: Clinical assessment, treatment planning, manual therapy, patient education in-person, insurance pre-auth.",
     "Medium", "$200 – $500/mo", "Monthly SaaS",
     "Patient reactivation is #1 revenue driver; automated reminders can recover 20%+ of inactive patients."),

    ("Chiropractic / PT / Wellness", "Insurance Billing & Claims",
     "Insurance verification, claim submission, EOB processing, denial management, patient billing",
     75, "High",
     "CAN: Automated eligibility verification, claim scrubbing/submission, EOB posting, denial tracking, appeal letter drafting, patient balance notices.\nCANNOT: Complex appeals, payer negotiation, clinical documentation improvement, audit defense, regulatory compliance.",
     "High", "$500 – $2,000/mo", "Monthly Retainer",
     "Insurance billing complexity drives practices to outsource; established Indian providers but room for specialization."),

    ("Chiropractic / PT / Wellness", "Content Marketing & Patient Education",
     "Blog posts, social media, patient education materials, video content, wellness newsletters",
     65, "High",
     "CAN: AI health content drafts, social media graphics, video editing, email newsletters, patient education handouts, SEO blog posts.\nCANNOT: Clinical accuracy review, provider personal branding, patient testimonials (need consent), local community content.",
     "Medium", "$300 – $1,500/mo", "Monthly Retainer",
     "Patient education content drives organic search traffic; needs clinical review but production is highly automatable."),

    ("Chiropractic / PT / Wellness", "Outcome Tracking & Reporting",
     "Patient outcome measurement, progress reports, satisfaction surveys, data analytics",
     80, "Very High",
     "CAN: Automated survey distribution, outcome score calculation, progress report generation, satisfaction analytics, trend dashboards, payer reporting.\nCANNOT: Clinical interpretation, treatment modification, research methodology, patient interview, clinical judgment.",
     "Low", "$200 – $600/mo", "Monthly SaaS / Retainer",
     "Outcome data increasingly required by payers and for marketing; very few automated solutions for small practices."),

    # ═══════════════════════════════════════════════════════════════
    # RESTAURANTS / FOOD SERVICE
    # ═══════════════════════════════════════════════════════════════
    ("Restaurants / Food Service", "Online Ordering & Menu Management",
     "Website/app ordering, menu updates, online presence across platforms, order routing",
     80, "Very High",
     "CAN: Online ordering system setup, menu sync across platforms (DoorDash, UberEats, Grubhub), automated menu updates, order routing, inventory integration.\nCANNOT: Food quality control, kitchen workflow, delivery logistics, customer complaint resolution, chef relationship management.",
     "High", "$200 – $800/mo", "Monthly SaaS",
     "Toast, Square, ChowNow dominate; custom solutions for multi-location restaurants or ghost kitchens."),

    ("Restaurants / Food Service", "Social Media & Food Photography Editing",
     "Food photo editing, Instagram/TikTok content, influencer coordination, user-generated content curation",
     55, "Medium",
     "CAN: Photo enhancement, social media scheduling, caption writing, hashtag research, review response, content calendar management.\nCANNOT: On-site food photography, video production, influencer relationship management, real-time content creation, brand aesthetic development.",
     "High", "$300 – $1,500/mo", "Monthly Retainer",
     "Visual content is everything for restaurants; needs authentic on-site photography but editing/posting is remote-able."),

    ("Restaurants / Food Service", "Inventory & Cost Control",
     "Food cost tracking, inventory management, waste monitoring, vendor price comparison, recipe costing",
     75, "High",
     "CAN: Automated inventory tracking, recipe cost calculation, waste analytics, vendor price comparison, order suggestion algorithms, food cost reporting.\nCANNOT: Physical inventory counts, food quality assessment, supplier negotiation, menu engineering decisions, kitchen process optimization.",
     "Medium", "$200 – $800/mo", "Monthly Retainer / SaaS",
     "Food cost is 28-35% of revenue; even 1-2% improvement = significant profit. MarketMan/Restaurant365 exist but managed service gap."),

    ("Restaurants / Food Service", "Reservation & Table Management",
     "Online reservations, waitlist management, table turnover optimization, customer preference tracking",
     85, "Very High",
     "CAN: Automated reservations, waitlist management, table turnover optimization, customer preference tracking, no-show prediction, SMS confirmations.\nCANNOT: Host stand management, walk-in judgment, VIP treatment decisions, overbooking strategy, service recovery.",
     "Medium", "$150 – $500/mo", "Monthly SaaS",
     "OpenTable, Resy dominate; custom solutions for unique concepts or multi-unit operators."),

    ("Restaurants / Food Service", "Review Management & Local Marketing",
     "Google/Yelp/TripAdvisor review management, local SEO, promotional campaigns, event marketing",
     70, "High",
     "CAN: Automated review solicitation, response drafting, review monitoring, local SEO optimization, promotional email/SMS, event announcement.\nCANNOT: Handling food safety complaints, health department response, local PR crisis, community relationship building, influencer events.",
     "Medium", "$300 – $1,000/mo", "Monthly Retainer",
     "Restaurants live/die by reviews; automated response + review generation is high-value service."),

    ("Restaurants / Food Service", "Bookkeeping & Financial Reporting",
     "POS reconciliation, sales tax, vendor payments, P&L reporting, labor cost analysis",
     80, "Very High",
     "CAN: POS data extraction, automated reconciliation, sales tax calculation, vendor bill processing, P&L generation, labor cost analysis, prime cost reporting.\nCANNOT: Restaurant-specific tax strategy, cash flow advisory, equipment financing decisions, expansion planning, investor relations.",
     "Medium", "$300 – $1,200/mo", "Monthly Retainer",
     "Restaurants have complex bookkeeping (daily sales, tips, vendor terms); specialized knowledge commands premium."),

    # ═══════════════════════════════════════════════════════════════
    # GYMS / FITNESS / YOGA
    # ═══════════════════════════════════════════════════════════════
    ("Gyms / Fitness / Yoga", "Member Management & Billing",
     "Membership billing, auto-renewals, dunning management, member portal, freeze/cancel processing",
     90, "Very High",
     "CAN: Automated billing, auto-renewals, failed payment retry (dunning), member portal, freeze/cancel processing, proration calculation, revenue analytics.\nCANNOT: Member retention strategy, complaint handling, membership negotiation, community building, facility management.",
     "Medium", "$200 – $600/mo", "Monthly SaaS",
     "Mindbody, Zen Planner, PushPress dominate; custom solutions for boutique studios or franchise groups."),

    ("Gyms / Fitness / Yoga", "Lead Capture & Conversion",
     "Website lead forms, trial class scheduling, follow-up automation, membership sales support",
     75, "High",
     "CAN: Lead capture forms, automated trial booking, follow-up email/SMS sequences, lead scoring, CRM management, conversion tracking.\nCANNOT: Facility tours, sales conversations, membership negotiation, relationship building, community event planning.",
     "Medium", "$300 – $1,000/mo", "Monthly Retainer",
     "Gym membership sales follow predictable patterns; automated follow-up can increase conversion 30-50%."),

    ("Gyms / Fitness / Yoga", "Class Scheduling & Program Management",
     "Class timetable, instructor scheduling, waitlist management, capacity optimization",
     85, "Very High",
     "CAN: Automated scheduling, waitlist fill, instructor assignment, capacity optimization, class reminder automation, attendance tracking.\nCANNOT: Instructor relationship management, class quality assessment, member preference matching, emergency coverage, program design.",
     "Medium", "$150 – $500/mo", "Monthly SaaS",
     "Highly automatable; class optimization alone can increase revenue per square foot 15-25%."),

    ("Gyms / Fitness / Yoga", "Social Media & Content Marketing",
     "Workout content, transformation photos, challenges, community engagement, influencer partnerships",
     55, "Medium",
     "CAN: Content templates, caption writing, scheduling, hashtag research, challenge campaign setup, analytics.\nCANNOT: On-site content production, authentic trainer content, real-time engagement, trending workout creation, in-person events.",
     "High", "$300 – $1,500/mo", "Monthly Retainer",
     "Fitness content is inherently visual; needs on-site capture but editing and management is remote-able."),

    ("Gyms / Fitness / Yoga", "Member Retention & Reactivation",
     "Churn prediction, win-back campaigns, engagement scoring, personalized outreach, milestone celebrations",
     80, "Very High",
     "CAN: Churn prediction algorithms, automated win-back campaigns, engagement scoring, attendance tracking, birthday/milestone automation, personalized offers.\nCANNOT: Personal trainer relationship, community building, complaint resolution, membership negotiation, exit interview insights.",
     "Low", "$200 – $600/mo", "Monthly SaaS / Retainer",
     "Gym churn is 40-60% annually; reactivating even 10% of lapsed members = significant revenue. Very underserved."),

    # ═══════════════════════════════════════════════════════════════
    # CLEANING SERVICES
    # ═══════════════════════════════════════════════════════════════
    ("Cleaning Services", "Booking & Scheduling System",
     "Online booking, automated scheduling, crew assignment, recurring appointment management",
     85, "Very High",
     "CAN: Online booking engine, crew scheduling algorithms, recurring appointment automation, route optimization, time tracking, automated confirmations.\nCANNOT: Quality inspection, in-person client management, supply management, complaint handling, staff training.",
     "Medium", "$200 – $600/mo", "Monthly SaaS",
     "Cleaning businesses run on schedules; automated booking can reduce admin time 50%+."),

    ("Cleaning Services", "Quote & Estimate Generation",
     "Automated quotes based on sqft/rooms, pricing calculator, proposal documents",
     80, "Very High",
     "CAN: Automated quote calculators (sqft, rooms, frequency), pricing engine, proposal generation, upsell suggestions, competitive pricing analysis.\nCANNOT: On-site assessment, condition-based pricing, client negotiation, special request evaluation, move-in/deep clean scoping.",
     "Low", "$50 – $200/mo or per-quote", "Per-quote / SaaS",
     "Cleaning companies spend 30+ min per quote; automation frees up massive time for selling."),

    ("Cleaning Services", "Quality Control & Client Feedback",
     "Post-clean surveys, quality scoring, complaint tracking, re-clean management",
     75, "High",
     "CAN: Automated post-service surveys, quality scoring, complaint tracking, re-clean scheduling, review solicitation, trend analytics.\nCANNOT: On-site quality inspection, staff coaching, client relationship repair, service technique assessment, supply quality evaluation.",
     "Low", "$150 – $400/mo", "Monthly SaaS / Retainer",
     "Very few QC automation tools for cleaning companies; quality consistency is #1 growth challenge."),

    ("Cleaning Services", "Crew Management & Payroll",
     "Crew scheduling, time tracking, payroll calculation, performance metrics, supply ordering",
     80, "Very High",
     "CAN: Crew scheduling, GPS time tracking, automated payroll calculation, performance dashboards, supply reorder automation, training tracking.\nCANNOT: In-person supervision, hiring decisions, conflict resolution, performance coaching, background check judgment.",
     "Medium", "$200 – $600/mo", "Monthly Retainer",
     "High turnover industry (100-200% annually); efficient crew management directly impacts profitability."),

    ("Cleaning Services", "Local Marketing & Lead Generation",
     "Google Local Services, Facebook ads, referral programs, local SEO, nextdoor marketing",
     60, "High",
     "CAN: Google LSA management, Facebook ad campaigns, referral program automation, SEO content, review management, lead tracking.\nCANNOT: In-home estimates, community relationship building, referral networking, brand differentiation, competitive pricing strategy.",
     "High", "$500 – $2,000/mo", "Monthly Retainer",
     "Cleaning is one of the fastest-growing local service categories; marketing demand is high but competitive."),

    # ═══════════════════════════════════════════════════════════════
    # CONSTRUCTION / REMODELING
    # ═══════════════════════════════════════════════════════════════
    ("Construction / Remodeling", "Estimating & Takeoff Services",
     "Material takeoffs, cost estimation, bid preparation, subcontractor pricing",
     65, "High",
     "CAN: Automated plan reading (AI), material takeoff calculations, cost database lookup, bid document preparation, subcontractor bid comparison, proposal generation.\nCANNOT: Site condition assessment, labor productivity judgment, risk assessment, client relationship, construction means & methods decisions.",
     "Medium", "$200 – $1,000/bid", "Per-bid / Retainer",
     "Estimating takeoffs are 80% remote-able; GCs spend 10-20 hours/bid on takeoffs. Indian estimating services exist but quality varies."),

    ("Construction / Remodeling", "Project Management & Scheduling",
     "Gantt charts, subcontractor scheduling, milestone tracking, daily logs, RFI management",
     60, "High",
     "CAN: Schedule creation (MS Project/Primavera), automated milestone tracking, daily report compilation, RFI/submittal tracking, photo documentation management, change order processing.\nCANNOT: On-site supervision, subcontractor coordination, weather/force majeure judgment, quality control, safety management.",
     "Medium", "$500 – $2,000/mo", "Monthly Retainer",
     "Construction management is relationship-heavy; back-office PM support is the remote opportunity."),

    ("Construction / Remodeling", "Permit & Regulatory Documentation",
     "Building permit applications, plan review submissions, inspection scheduling, code compliance research",
     65, "High",
     "CAN: Permit application preparation, document compilation, code research, inspection scheduling, deadline tracking, form filling, fee calculation.\nCANNOT: In-person permit counter submission, plan reviewer negotiation, on-site code interpretation, variance request strategy, contractor license compliance.",
     "Low", "$100 – $500/permit", "Per-task",
     "Contractors hate permit paperwork; highly fragmented by jurisdiction, creating complexity that's valuable to manage."),

    ("Construction / Remodeling", "3D Rendering & Design Visualization",
     "3D room renders, before/after visualizations, material selection overlays, client presentation materials",
     60, "High",
     "CAN: AI-powered 3D rendering, material swap visualizations, before/after overlays, floor plan visualization, presentation PDF creation.\nCANNOT: Architectural design, structural engineering, client design consultation, building code compliance, site-specific design.",
     "Medium", "$100 – $500/rendering", "Per-rendering / Project",
     "Remodeling companies using 3D renders close 30-50% more projects; high perceived value."),

    ("Construction / Remodeling", "Subcontractor & Vendor Management",
     "Bid solicitation, subcontractor tracking, vendor payment processing, lien waiver management",
     70, "High",
     "CAN: Bid solicitation emails, subcontractor qualification tracking, vendor payment processing, lien waiver collection, compliance tracking, insurance certificate monitoring.\nCANNOT: Subcontractor relationship management, performance evaluation, negotiation, dispute resolution, on-site coordination.",
     "Low", "$300 – $1,000/mo", "Monthly Retainer",
     "Subcontractor management is a major pain point for GCs; compliance tracking (insurance, licenses) is automatable."),

    ("Construction / Remodeling", "Safety & Compliance Documentation",
     "OSHA documentation, safety plans, incident reports, toolbox talk tracking, certifications management",
     70, "High",
     "CAN: Safety plan template generation, OSHA form preparation, incident report documentation, certification tracking, toolbox talk library, compliance checklists.\nCANNOT: On-site safety inspection, safety training delivery, incident investigation, OSHA audit response, safety culture development.",
     "Low", "$300 – $800/mo", "Monthly Retainer",
     "OSHA compliance is mandatory but universally neglected by small contractors; huge liability if non-compliant."),

    # ═══════════════════════════════════════════════════════════════
    # ROOFING COMPANIES
    # ═══════════════════════════════════════════════════════════════
    ("Roofing Companies", "Satellite Roof Measurement & Estimating",
     "Roof area measurement from satellite/aerial imagery, material calculation, waste factor, cost estimation",
     90, "Very High",
     "CAN: Satellite measurement (EagleView, Roofr), automated material calculation, waste factor, cost estimation, report generation, pitch analysis.\nCANNOT: On-site inspection, deck condition assessment, flashing detail verification, interior damage assessment, insurance supplement.",
     "Medium", "$10 – $50/report", "Per-report",
     "Extremely automatable; EagleView/Satellite already used but report processing & estimate prep is remote-able."),

    ("Roofing Companies", "Insurance Claim Documentation",
     "Storm damage documentation, claim filing support, supplement preparation, Xactimate estimating",
     60, "High",
     "CAN: Xactimate estimate preparation, claim documentation, photo organization, scope comparison, supplement writing, deadline tracking.\nCANNOT: On-site damage inspection, adjuster negotiation, carrier relationship management, physical measurement verification, claim strategy.",
     "Medium", "$100 – $500/claim", "Per-claim / Retainer",
     "Insurance restoration is massive (>$30B market); Xactimate skills are valuable and remote-able."),

    ("Roofing Companies", "Lead Generation & Storm Chasing Support",
     "Storm tracking, canvassing lists, door-to-door support, digital ads, appointment setting",
     50, "Medium",
     "CAN: Storm tracking alerts, canvassing route optimization, digital ad campaigns, lead qualification, CRM management, appointment setting.\nCANNOT: Door-to-door canvassing, in-home sales, insurance inspection attendance, client relationship management.",
     "Very High", "$1,000 – $5,000/mo", "Retainer + Commission",
     "Storm response requires speed; pre-built storm databases and quick campaign deployment = competitive advantage."),

    ("Roofing Companies", "Project Management & Production Tracking",
     "Installation scheduling, crew tracking, material ordering, production reporting, warranty registration",
     65, "High",
     "CAN: Automated scheduling, crew assignment, material ordering triggers, production reporting, photo documentation, warranty registration processing.\nCANNOT: On-site quality control, crew supervision, weather management, client communication, subcontractor coordination.",
     "Low", "$300 – $800/mo", "Monthly Retainer",
     "Roofing companies run 3-5 crews simultaneously; coordination support prevents costly scheduling errors."),

    # ═══════════════════════════════════════════════════════════════
    # PEST CONTROL
    # ═══════════════════════════════════════════════════════════════
    ("Pest Control", "Route Optimization & Scheduling",
     "Technician routing, recurring service scheduling, territory management, seasonal planning",
     85, "Very High",
     "CAN: Route optimization, recurring schedule automation, territory assignment, seasonal planning alerts, drive-time minimization, fuel tracking.\nCANNOT: On-site pest identification, treatment decisions, customer education, equipment management, emergency call handling.",
     "Medium", "$200 – $500/mo", "Monthly SaaS",
     "Pest control is route-density business; optimization directly impacts revenue per technician per day."),

    ("Pest Control", "Compliance & Licensing Management",
     "Pesticide license tracking, continuing education monitoring, EPA documentation, state regulatory compliance",
     80, "Very High",
     "CAN: License expiration tracking, CE requirement monitoring, EPA documentation, state regulation tracking, application deadline alerts, renewal processing.\nCANNOT: In-person inspections, regulatory filing, legal compliance interpretation, state board communication, incident investigation.",
     "Low", "$200 – $500/mo", "Monthly Retainer",
     "Multi-state pest companies face complex compliance; very few tools exist for this specific niche."),

    ("Pest Control", "Customer Communication & Retention",
     "Service reminders, post-treatment follow-ups, seasonal campaigns, re-activation, review requests",
     85, "Very High",
     "CAN: Automated service reminders, post-treatment care instructions, seasonal campaign emails, re-activation outreach, review solicitation, referral program.\nCANNOT: On-site customer service, complaint resolution, treatment guarantee management, pest callback handling, in-person sales.",
     "Medium", "$150 – $400/mo", "Monthly SaaS",
     "Pest control is a subscription business; customer retention = recurring revenue. Annual churn costs companies 20-30% revenue."),

    ("Pest Control", "Digital Marketing & Lead Generation",
     "Local SEO, Google LSA, seasonal ad campaigns, lead follow-up, competitor monitoring",
     55, "Medium",
     "CAN: Google LSA management, local SEO, seasonal ad campaigns, lead follow-up automation, competitor tracking, review management.\nCANNOT: In-home inspection/sales, termite inspection, community networking, brand differentiation, pricing strategy.",
     "High", "$500 – $2,500/mo", "Monthly Retainer",
     "Pest control is highly seasonal (spring/summer peaks); marketing needs to match demand cycles."),

    # ═══════════════════════════════════════════════════════════════
    # INSURANCE AGENCIES
    # ═══════════════════════════════════════════════════════════════
    ("Insurance Agencies", "Policy Administration & Processing",
     "Policy data entry, renewal processing, certificate of insurance, endorsement processing",
     80, "Very High",
     "CAN: Policy data entry, renewal processing, COI generation, endorsement documentation, premium comparison, carrier portal management.\nCANNOT: Coverage recommendation, risk assessment, claims advocacy, client advisory, carrier relationship management, compliance decisions.",
     "High", "$500 – $2,000/mo", "Monthly Retainer",
     "Insurance agencies are drowning in paperwork; policy processing is highly remote-able. Established Indian providers exist."),

    ("Insurance Agencies", "Claims Support & Documentation",
     "First notice of loss, claim documentation, follow-up tracking, status updates, carrier communication",
     70, "High",
     "CAN: FNOL processing, claim documentation, status tracking, carrier follow-up, status update communication, claim analytics.\nCANNOT: Claims investigation, coverage determination, settlement negotiation, claimant interaction, litigation support.",
     "Medium", "$400 – $1,500/mo", "Monthly Retainer",
     "Claims support frees up agents to sell; high value but needs insurance-specific training."),

    ("Insurance Agencies", "Marketing & Lead Generation",
     "Insurance-specific digital marketing, quote request follow-up, cross-sell campaigns, referral programs",
     55, "Medium",
     "CAN: Digital ad campaigns, quote request follow-up automation, cross-sell/upsell campaigns, referral program management, content marketing, email nurturing.\nCANNOT: Client consultation, coverage needs analysis, relationship building, community networking, carrier appointment strategy.",
     "High", "$1,000 – $4,000/mo", "Monthly Retainer",
     "Insurance marketing is competitive but high LTV per client ($3,000-$10,000+); ROI justifies investment."),

    ("Insurance Agencies", "Compliance & E&O Management",
     "E&O documentation, compliance tracking, licensing management, continuing education monitoring",
     75, "High",
     "CAN: E&O file documentation, compliance checklist automation, license tracking, CE monitoring, audit preparation, regulatory calendar management.\nCANNOT: Legal compliance interpretation, E&O claim defense, state DOI correspondence, regulatory strategy, carrier compliance negotiation.",
     "Medium", "$300 – $1,000/mo", "Monthly Retainer",
     "E&O claims average $50K+; proactive documentation is cheap insurance for agencies."),

    # ═══════════════════════════════════════════════════════════════
    # LAW FIRMS (SMALL)
    # ═══════════════════════════════════════════════════════════════
    ("Law Firms (Small)", "Legal Research & Document Drafting",
     "Case law research, motion drafting, contract review, legal memo preparation",
     55, "Medium",
     "CAN: AI legal research (Casetext, Harvey), document drafting templates, contract review/redlining, citation checking, legal memo outlines, court filing research.\nCANNOT: Legal strategy, client counseling, courtroom representation, negotiation, legal judgment, bar-advised practice.",
     "Medium", "$25 – $75/hr or per-task", "Hourly / Per-task",
     "Paralegal work from India is established; AI legal tools are transforming but attorney review always required."),

    ("Law Firms (Small)", "Client Intake & CRM",
     "Lead qualification, intake form processing, conflict checks, consultation scheduling",
     75, "High",
     "CAN: Automated intake forms, lead qualification scoring, conflict check processing, consultation scheduling, follow-up sequences, CRM management.\nCANNOT: Attorney-client privileged communication, case evaluation, retainer negotiation, client counseling, conflict resolution.",
     "Medium", "$300 – $1,000/mo", "Monthly Retainer",
     "Law firms lose 30-50% of leads from slow response; automated intake + fast follow-up = more retained cases."),

    ("Law Firms (Small)", "Document Management & eDiscovery",
     "Document organization, Bates stamping, privilege review, eDiscovery processing, case file management",
     70, "High",
     "CAN: AI document review, Bates stamping, privilege log generation, document organization, eDiscovery processing, metadata extraction.\nCANNOT: Legal judgment on privilege, work product determination, case strategy, client communication, court filing.",
     "Medium", "$500 – $3,000/mo", "Monthly Retainer / Per-case",
     "eDiscovery is a $12B+ market; AI dramatically reducing costs but human review still required for privilege."),

    ("Law Firms (Small)", "Billing & Trust Accounting",
     "Time entry, billing, trust account reconciliation, IOLTA compliance, financial reporting",
     75, "High",
     "CAN: Time entry processing, bill generation, trust account reconciliation, IOLTA compliance checking, financial reporting, collections follow-up.\nCANNOT: Billing judgment, fee dispute resolution, trust account legal compliance, audit response, financial strategy.",
     "Medium", "$300 – $1,000/mo", "Monthly Retainer",
     "Law firm billing is complex (LEDES, trust accounting, IOLTA); errors can result in bar discipline."),

    ("Law Firms (Small)", "Legal Marketing & SEO",
     "Attorney website SEO, content marketing, directory management, review generation, PPC management",
     50, "Medium",
     "CAN: Legal SEO content, directory submissions, review management, PPC campaigns, social media management, blog content.\nCANNOT: Attorney branding strategy, community positioning, Martindale/AV rating strategy, referral network development, bar association marketing rules.",
     "High", "$1,000 – $5,000/mo", "Monthly Retainer",
     "Legal marketing is extremely competitive (personal injury $1,000+/click); niche practice areas are less competitive."),

    # ═══════════════════════════════════════════════════════════════
    # VETERINARY CLINICS
    # ═══════════════════════════════════════════════════════════════
    ("Veterinary Clinics", "Appointment Scheduling & Reminders",
     "Automated booking, vaccination reminders, follow-up scheduling, surgical prep instructions",
     85, "Very High",
     "CAN: Automated booking, vaccination reminder sequences, post-surgery follow-up scheduling, pre-appointment instructions, recall campaigns, SMS confirmations.\nCANNOT: Emergency triage, clinical assessment, surgical scheduling priority, client communication for serious diagnoses.",
     "Medium", "$200 – $500/mo", "Monthly SaaS",
     "Vaccination reminders are #1 revenue driver; automated recall can increase visits 20-30%."),

    ("Veterinary Clinics", "Insurance & Billing Processing",
     "Pet insurance claims, estimate preparation, payment plans, client billing, collections",
     75, "High",
     "CAN: Pet insurance claim submission, estimate generation, payment plan processing, client billing, collections automation, EOB posting.\nCANNOT: Clinical justification for claims, insurance denial appeals, client financial counseling, payment negotiation.",
     "Medium", "$300 – $800/mo", "Monthly Retainer",
     "Pet insurance claims growing rapidly (25%+ annually); claims processing complexity is increasing."),

    ("Veterinary Clinics", "Client Communication & Education",
     "Post-visit care instructions, medication reminders, educational content, seasonal wellness campaigns",
     85, "Very High",
     "CAN: Automated post-visit instructions, medication reminders, educational email sequences, seasonal campaigns, dental month promotions, nutrition guides.\nCANNOT: Clinical advice, treatment recommendation, emergency guidance, in-person client education.",
     "Low", "$150 – $400/mo", "Monthly SaaS / Retainer",
     "Client education improves compliance and outcomes; very few vet-specific automated education tools."),

    ("Veterinary Clinics", "Pharmacy & Inventory Management",
     "Medication tracking, auto-reorder, controlled substance logs, supplier management, expiration tracking",
     80, "Very High",
     "CAN: Automated inventory tracking, reorder triggers, controlled substance logging, expiration alerts, supplier price comparison, usage analytics.\nCANNOT: Physical inventory counts, medication quality assessment, DEA compliance decisions, supplier negotiation, veterinary pharmaceutical purchasing.",
     "Low", "$200 – $600/mo", "Monthly Retainer / SaaS",
     "Controlled substance logging is legally required and tedious; automation reduces compliance risk."),

    ("Veterinary Clinics", "Review Management & Local Marketing",
     "Google reviews, social media, new client acquisition, community marketing",
     65, "High",
     "CAN: Review solicitation automation, response drafting, social media scheduling, new client campaigns, Google Business optimization, referral programs.\nCANNOT: On-site photography, community event planning, brand positioning, competitor differentiation, client relationship management.",
     "Medium", "$300 – $1,200/mo", "Monthly Retainer",
     "Vet practices depend on local reputation; review count/rating directly impacts new client acquisition."),

    # ═══════════════════════════════════════════════════════════════
    # PROPERTY MANAGEMENT
    # ═══════════════════════════════════════════════════════════════
    ("Property Management", "Tenant Screening & Application Processing",
     "Application processing, background checks, credit reports, employment verification, lease preparation",
     80, "Very High",
     "CAN: Application data extraction, background check ordering, credit report review, employment verification, lease document generation, denial/adverse action notices.\nCANNOT: Fair housing compliance decisions, applicant judgment, landlord-tenant negotiation, lease term negotiation, eviction decisions.",
     "High", "$50 – $150/application", "Per-application",
     "High volume, highly processable; FCRA/Fair Housing compliance knowledge is critical differentiator."),

    ("Property Management", "Maintenance Request & Work Order Management",
     "Tenant request intake, vendor dispatch, work order tracking, follow-up, cost tracking",
     75, "High",
     "CAN: Automated request intake, vendor dispatch, work order tracking, tenant communication, cost tracking, preventative maintenance scheduling, analytics.\nCANNOT: On-site inspection, vendor quality assessment, emergency maintenance judgment, capital improvement planning, tenant relationship.",
     "Medium", "$300 – $1,000/mo", "Monthly Retainer",
     "Maintenance coordination is the #1 time sink for property managers; automation directly scales portfolio size."),

    ("Property Management", "Rent Collection & Financial Reporting",
     "Rent collection, late fee processing, owner distributions, financial reporting, CAM reconciliation",
     85, "Very High",
     "CAN: Automated rent collection, late fee calculation, owner distribution processing, financial reporting, CAM reconciliation, delinquency tracking, bank reconciliation.\nCANNOT: Eviction processing, legal compliance, tenant negotiation, owner relationship management, audit response, tax strategy.",
     "Medium", "$300 – $1,500/mo", "Monthly Retainer",
     "Property management accounting is complex (trust accounts, CAM, owner statements); high demand for specialized bookkeeping."),

    ("Property Management", "Lease Administration & Compliance",
     "Lease abstraction, critical date tracking, compliance monitoring, renewal processing, document management",
     80, "Very High",
     "CAN: Lease data abstraction, critical date alerts, compliance monitoring, renewal processing, document organization, regulatory tracking.\nCANNOT: Legal interpretation, lease negotiation, tenant relationship, compliance judgment, eviction proceedings.",
     "Low", "$200 – $800/mo", "Monthly Retainer",
     "Commercial lease administration is particularly complex; missed dates cost thousands. Very underserved niche."),

    ("Property Management", "Tenant Communication & Portal Management",
     "Tenant portal setup, announcements, community updates, document distribution, feedback collection",
     85, "Very High",
     "CAN: Tenant portal management, automated announcements, document distribution, feedback surveys, maintenance status updates, community newsletter.\nCANNOT: In-person tenant relations, complaint resolution, lease negotiation, community event planning, emergency communication.",
     "Medium", "$150 – $500/mo", "Monthly SaaS",
     "Tenant communication platforms (AppFolio, Buildium) exist; managed service for smaller PMs is underserved."),

    # ═══════════════════════════════════════════════════════════════
    # DAYCARE / CHILDCARE
    # ═══════════════════════════════════════════════════════════════
    ("Daycare / Childcare", "Enrollment & Parent Communication",
     "Enrollment processing, parent updates, daily reports, photo sharing, billing",
     80, "Very High",
     "CAN: Enrollment form processing, automated parent updates, daily report templates, photo sharing platforms, billing automation, attendance tracking, waitlist management.\nCANNOT: Child supervision, parent meeting/conference, licensing compliance judgment, curriculum planning, staff supervision.",
     "Medium", "$150 – $500/mo", "Monthly SaaS",
     "Brightwheel/Procare dominate; managed service for independent centers is underserved."),

    ("Daycare / Childcare", "Licensing & Regulatory Compliance",
     "State licensing documentation, staff certification tracking, health inspections prep, ratio compliance",
     75, "High",
     "CAN: Licensing documentation preparation, staff certification tracking, health inspection checklists, ratio monitoring, policy template generation, renewal deadline tracking.\nCANNOT: In-person licensing inspections, staff training delivery, emergency protocol development, state licensing communication.",
     "Low", "$200 – $600/mo", "Monthly Retainer",
     "Childcare licensing compliance is complex and state-specific; violations can shut down centers. Very few remote compliance services."),

    ("Daycare / Childcare", "Billing & Tuition Management",
     "Tuition collection, subsidy billing, late fee processing, financial assistance tracking, tax credit documentation",
     85, "Very High",
     "CAN: Automated tuition billing, subsidy invoice processing, late fee calculation, payment plan management, tax credit documentation, financial reporting.\nCANNOT: Financial aid decisions, parent payment negotiation, subsidy program compliance, state audit response.",
     "Medium", "$200 – $500/mo", "Monthly SaaS / Retainer",
     "Childcare billing is complex (subsidies, sliding scales, siblings); errors create parent trust issues."),

    ("Daycare / Childcare", "Marketing & Enrollment Management",
     "Website, enrollment inquiry follow-up, tour scheduling, social media, community marketing",
     65, "High",
     "CAN: Website management, enrollment inquiry follow-up, tour scheduling automation, social media content, community event promotion, review management.\nCANNOT: Facility tours, parent relationship building, community networking, brand positioning, enrollment conversion.",
     "Medium", "$300 – $1,000/mo", "Monthly Retainer",
     "Full enrollment = full revenue; most daycares lose $5K-$15K/month per empty slot. Fast inquiry response = more enrollments."),

    # ═══════════════════════════════════════════════════════════════
    # MOVING COMPANIES
    # ═══════════════════════════════════════════════════════════════
    ("Moving Companies", "Estimating & Survey Management",
     "Virtual surveys, estimate generation, inventory lists, pricing calculation",
     75, "High",
     "CAN: Virtual survey via video/photo, automated inventory lists, cubic feet calculation, pricing engine, estimate document generation, comparison tools.\nCANNOT: On-site survey, access difficulty assessment, specialty item handling, client negotiation, packing material estimation.",
     "Medium", "$50 – $200/estimate", "Per-estimate / Retainer",
     "Virtual surveys are growing post-pandemic; 60%+ of estimates can now be done remotely."),

    ("Moving Companies", "Crew Scheduling & Dispatch",
     "Crew assignment, truck scheduling, route optimization, job sequencing",
     80, "Very High",
     "CAN: Automated crew scheduling, truck assignment, route optimization, job sequencing, real-time dispatch, fuel cost calculation.\nCANNOT: On-site crew management, loading judgment, customer service, equipment maintenance scheduling, emergency handling.",
     "Medium", "$200 – $600/mo", "Monthly SaaS",
     "Moving companies run thin margins; crew utilization directly impacts profitability."),

    ("Moving Companies", "Customer Communication & Tracking",
     "Move confirmation, status updates, tracking, delivery scheduling, post-move follow-up",
     85, "Very High",
     "CAN: Automated move confirmations, GPS tracking updates, delivery window notifications, post-move surveys, review requests, referral program.\nCANNOT: In-person move coordination, damage claim handling, delivery rescheduling, customer complaint resolution.",
     "Low", "$150 – $400/mo", "Monthly SaaS",
     "Moving is stress-heavy; proactive communication dramatically reduces complaint calls and improves reviews."),

    ("Moving Companies", "Claim & Damage Documentation",
     "Damage claim processing, photo documentation, valuation calculation, claims communication",
     70, "High",
     "CAN: Claim form processing, photo documentation management, valuation calculation, claims communication templates, settlement tracking, analytics.\nCANNOT: Damage assessment judgment, settlement negotiation, customer complaint resolution, insurance carrier negotiation.",
     "Low", "$100 – $400/mo or per-claim", "Per-claim / Retainer",
     "Moving claims are complex and time-consuming; dedicated claims support reduces resolution time significantly."),

    # ═══════════════════════════════════════════════════════════════
    # ACCOUNTING / TAX PREP FIRMS
    # ═══════════════════════════════════════════════════════════════
    ("Accounting / Tax Prep", "Tax Return Preparation",
     "Individual & business tax return preparation, data entry, form filling, review support",
     70, "High",
     "CAN: Tax data extraction, form preparation (1040, 1120, 1065), schedule preparation, deduction analysis, prior-year comparison, filing processing.\nCANNOT: Tax strategy/planning, complex transaction judgment, audit representation, client advisory, state-specific tax planning.",
     "High", "$50 – $300/return", "Per-return (seasonal)",
     "Established Indian tax prep industry; competitive during tax season. Quality + speed differentiators."),

    ("Accounting / Tax Prep", "Bookkeeping Clean-Up",
     "Catch-up bookkeeping, messy file cleanup, reconciliation, chart of accounts optimization",
     75, "High",
     "CAN: Bank feed reconciliation, transaction categorization, expense review, chart of accounts cleanup, prior-period adjustment, financial statement preparation.\nCANNOT: Tax strategy implications, audit defense, business advisory, complex transaction judgment, client advisory.",
     "Medium", "$500 – $3,000/project", "Per-project",
     "Tax firms need clean books before filing; seasonal demand spike creates opportunity for cleanup services."),

    ("Accounting / Tax Prep", "Audit Support & Workpaper Preparation",
     "Audit workpaper compilation, PBC list management, document preparation, auditor communication support",
     70, "High",
     "CAN: Workpaper preparation, PBC list tracking, document compilation, schedule preparation, trial balance reconciliation, engagement letter processing.\nCANNOT: Audit judgment, materiality decisions, client advisory on findings, GAAP interpretation, auditor negotiation.",
     "Medium", "$500 – $2,000/engagement", "Per-engagement",
     "CPA firms are understaffed; audit prep support is high-value seasonal work."),

    ("Accounting / Tax Prep", "CFO/Advisory Report Preparation",
     "Financial dashboards, KPI reports, cash flow forecasting, budget vs. actual analysis",
     75, "High",
     "CAN: Dashboard creation, KPI calculation, cash flow projections, budget vs. actual reports, management report generation, trend analysis.\nCANNOT: Strategic advisory, business interpretation, board presentation, industry benchmarking judgment, business forecasting strategy.",
     "Low", "$500 – $2,000/mo", "Monthly Retainer",
     "Fractional CFO services growing; report prep can be offshored while advisory stays local."),

    # ═══════════════════════════════════════════════════════════════
    # FLORISTS
    # ═══════════════════════════════════════════════════════════════
    ("Florists", "Online Ordering & E-commerce",
     "Online flower shop, order management, delivery scheduling, occasion-based marketing",
     80, "Very High",
     "CAN: E-commerce setup, order management system, delivery route optimization, occasion-based campaigns (Valentine's, Mother's Day), inventory alerts.\nCANNOT: Floral design, arrangement creation, flower quality assessment, delivery execution, customer consultation.",
     "Medium", "$200 – $800/mo", "Monthly SaaS + Setup",
     "Florists lose massive holiday revenue without strong online presence; 60%+ of orders are now online."),

    ("Florists", "Seasonal Marketing & Occasion Campaigns",
     "Holiday campaigns, wedding inquiry management, event marketing, subscription programs",
     70, "High",
     "CAN: Holiday campaign automation, wedding inquiry follow-up, subscription flower program management, email sequences, social media, event promotion.\nCANNOT: Floral design consultation, wedding venue networking, event styling, in-person sales, brand aesthetics.",
     "Low", "$200 – $800/mo", "Monthly Retainer",
     "Florists are terrible at marketing; occasion-based campaigns are highly predictable and automatable."),

    # ═══════════════════════════════════════════════════════════════
    # TUTORING / EDUCATION
    # ═══════════════════════════════════════════════════════════════
    ("Tutoring / Education", "Student Enrollment & Scheduling",
     "Enrollment processing, tutor-student matching, session scheduling, calendar management",
     85, "Very High",
     "CAN: Enrollment automation, tutor-student matching algorithms, session scheduling, calendar sync, automated reminders, waitlist management.\nCANNOT: Academic assessment, tutor quality evaluation, parent meeting, curriculum decisions, learning disability accommodation.",
     "Medium", "$150 – $400/mo", "Monthly SaaS",
     "Tutoring logistics (matching, scheduling) is the #1 admin burden; automation frees time for instruction."),

    ("Tutoring / Education", "Progress Tracking & Parent Communication",
     "Student progress reports, assessment tracking, parent updates, goal setting",
     80, "Very High",
     "CAN: Automated progress reports, assessment tracking, parent update emails, goal milestone tracking, attendance reporting, performance analytics.\nCANNOT: Academic instruction, learning plan development, parent conference, student motivation, educational strategy.",
     "Low", "$150 – $400/mo", "Monthly SaaS / Retainer",
     "Parent communication is #1 retention driver for tutoring centers; automated reporting keeps parents engaged."),

    ("Tutoring / Education", "Digital Marketing & Enrollment",
     "Local SEO, parent testimonials, open house marketing, enrollment campaigns, school partnership outreach",
     60, "High",
     "CAN: Local SEO, testimonial video editing, enrollment campaign management, email nurturing, social media, school outreach templates.\nCANNOT: In-person tours, parent consultation, school relationship building, community networking, educational positioning.",
     "Medium", "$300 – $1,500/mo", "Monthly Retainer",
     "Education marketing requires trust-building; parent testimonials and results are the most powerful content."),

    # ═══════════════════════════════════════════════════════════════
    # FUNERAL HOMES
    # ═══════════════════════════════════════════════════════════════
    ("Funeral Homes", "Obituary & Memorial Content",
     "Obituary writing, memorial page creation, photo collages, tribute video production",
     70, "High",
     "CAN: Obituary drafting from questionnaire, memorial web pages, photo collage creation, tribute video editing, social media memorial posts, guestbook management.\nCANNOT: Family consultation, service planning, grief counseling, cultural/religious ceremony knowledge, legal death certificate processing.",
     "Low", "$50 – $200/obituary or $200–$500/mo", "Per-service / Retainer",
     "Funeral homes are underserved by tech; obituary content creation is highly remote-able and meaningful."),

    ("Funeral Homes", "Pre-Need & Aftercare Communication",
     "Pre-need plan documentation, aftercare follow-up, anniversary remembrance, grief resources",
     80, "Very High",
     "CAN: Pre-need documentation processing, aftercare email sequences, anniversary/reminder automation, grief resource distribution, follow-up scheduling, CRM management.\nCANNOT: Family consultation, pre-need sales, grief counseling, community relationship, service arrangement.",
     "Low", "$200 – $500/mo", "Monthly Retainer",
     "Aftercare programs generate pre-need referrals; automated follow-up is high-value with minimal effort."),

    ("Funeral Homes", "Regulatory Compliance & Documentation",
     "Death certificate processing, regulatory filing, FTC compliance, embalming documentation",
     75, "High",
     "CAN: Death certificate data processing, regulatory form preparation, FTC compliance checklist, document management, filing deadline tracking, record retention.\nCANNOT: Legal compliance interpretation, regulatory filing, state board communication, death investigation coordination, funeral director advisory.",
     "Low", "$300 – $800/mo", "Monthly Retainer",
     "Funeral homes face complex federal (FTC) and state regulations; compliance documentation is critical but tedious."),

    # ═══════════════════════════════════════════════════════════════
    # AUTO DETAILING / CAR WASH
    # ═══════════════════════════════════════════════════════════════
    ("Auto Detailing / Car Wash", "Booking & Membership Management",
     "Online booking, unlimited wash memberships, recurring billing, appointment scheduling",
     85, "Very High",
     "CAN: Online booking, membership signup/renewal, automated billing, appointment reminders, waitlist management, loyalty tracking.\nCANNOT: On-site service, vehicle assessment, membership sales, upselling, customer complaint handling.",
     "Medium", "$150 – $500/mo", "Monthly SaaS",
     "Unlimited wash memberships are the business model for car washes; membership management = recurring revenue."),

    ("Auto Detailing / Car Wash", "Before/After Content Marketing",
     "Transformation photos/videos, social media, local marketing, review generation",
     55, "Medium",
     "CAN: Photo/video editing, before/after collages, social scheduling, caption writing, review solicitation, ad campaign management.\nCANNOT: On-site photography, video production, detailing consultation, community event marketing, customer relationship.",
     "High", "$200 – $800/mo", "Monthly Retainer",
     "Detailing is inherently visual; before/after content drives enormous engagement and new customer acquisition."),

    # ═══════════════════════════════════════════════════════════════
    # TATTOO / PIERCING STUDIOS
    # ═══════════════════════════════════════════════════════════════
    ("Tattoo / Piercing Studios", "Booking & Deposit Management",
     "Appointment booking, deposit collection, cancellation policy enforcement, waitlist management",
     85, "Very High",
     "CAN: Online booking, deposit collection, cancellation fee processing, waitlist management, consultation scheduling, automated reminders, consent form processing.\nCANNOT: Artist consultation, design discussion, in-person scheduling, no-show judgment, walk-in management.",
     "Low", "$100 – $300/mo", "Monthly SaaS",
     "Tattoo studios lose thousands in no-shows; deposit management and cancellation enforcement are critical."),

    ("Tattoo / Piercing Studios", "Artist Portfolio & Social Media",
     "Portfolio websites, Instagram content, flash design promotion, event marketing",
     55, "Medium",
     "CAN: Portfolio website management, photo editing, social scheduling, flash design promotion, event announcement, review management.\nCANNOT: On-site photography, artist brand development, convention promotion, in-person consultation, design creation.",
     "Medium", "$150 – $600/mo", "Monthly Retainer",
     "Tattoo artists need strong visual portfolios; Instagram is the primary client acquisition channel."),

    # ═══════════════════════════════════════════════════════════════
    # POOL MAINTENANCE / SERVICE
    # ═══════════════════════════════════════════════════════════════
    ("Pool Maintenance / Service", "Route Optimization & Scheduling",
     "Technician routing, recurring service scheduling, chemical tracking, seasonal opening/closing",
     85, "Very High",
     "CAN: Route optimization, recurring schedule management, chemical tracking, seasonal campaign scheduling, automated reminders, service reports.\nCANNOT: On-site service, water testing, equipment repair, customer relationship, emergency service.",
     "Low", "$150 – $400/mo", "Monthly SaaS",
     "Pool service is pure route density; optimization can add 20-30% more pools per route per day."),

    ("Pool Maintenance / Service", "Chemical & Inventory Management",
     "Chemical usage tracking, auto-reorder, dosing calculation, compliance documentation",
     80, "Very High",
     "CAN: Chemical usage tracking, dosing calculation, auto-reorder triggers, compliance documentation, water test recording, seasonal chemical planning.\nCANNOT: Physical chemical testing, water quality judgment, equipment assessment, chemical supplier negotiation, emergency treatment.",
     "Low", "$100 – $300/mo", "Monthly SaaS / Retainer",
     "Chemical costs are 30-40% of pool service revenue; optimization directly impacts profitability."),

    # ═══════════════════════════════════════════════════════════════
    # EMERGING / CROSS-CUTTING
    # ═══════════════════════════════════════════════════════════════
    ("Emerging / Cross-Cutting", "AI Voice Agent / Phone Receptionist",
     "AI-powered phone answering, appointment booking, FAQ handling, call routing for SMBs",
     75, "High",
     "CAN: AI voice agents (Bland.ai, Vapi, Retell), appointment booking, FAQ handling, call routing, after-hours answering, multi-language support.\nCANNOT: Complex complaint handling, empathetic conversations, sales calls requiring nuance, emergency situation handling, brand voice authenticity.",
     "Medium", "$200 – $1,000/mo per line", "Monthly SaaS",
     "Explosive growth area; AI voice quality now good enough for SMB phone handling."),

    ("Emerging / Cross-Cutting", "AI-Powered Reporting & Analytics",
     "Business dashboards, KPI tracking, automated reporting, data visualization",
     80, "Very High",
     "CAN: Automated data collection, dashboard creation, report generation, trend analysis, anomaly detection, alert systems.\nCANNOT: Business interpretation & strategy, data quality judgment, stakeholder presentation, complex data modeling decisions.",
     "Medium", "$500 – $2,000 setup + $200–$500/mo", "Project + Retainer",
     "SMBs lack data visibility; high value but low awareness of opportunity."),

    ("Emerging / Cross-Cutting", "Video Editing & Short-Form Content",
     "Reels/TikToks, YouTube shorts, promotional videos, testimonial videos",
     55, "Medium",
     "CAN: AI video editing (CapCut, Descript), auto-captioning, clip extraction, thumbnail generation, basic motion graphics.\nCANNOT: On-site video production, complex editing/artistic vision, talent direction, sound design, brand storytelling.",
     "High", "$300 – $2,000/mo", "Monthly Retainer",
     "High demand from all verticals; short-form video is the #1 marketing channel for local SMBs."),

    ("Emerging / Cross-Cutting", "Document Automation & Template Systems",
     "Proposal templates, contract generation, intake forms, automated document workflows",
     80, "Very High",
     "CAN: Template creation, automated document generation, e-signature integration, form building, workflow automation, data extraction.\nCANNOT: Legal document drafting/review, complex contract negotiation, regulatory compliance judgment, custom clause development.",
     "Medium", "$500 – $3,000 setup + $100–$300/mo", "Project + Retainer",
     "High-value efficiency play; every SMB drowns in paperwork. Industry-specific templates = differentiator."),

    ("Emerging / Cross-Cutting", "Cybersecurity & Data Protection",
     "Security audits, employee training, compliance (PCI, HIPAA), incident response planning",
     55, "Medium",
     "CAN: Automated vulnerability scanning, security policy templates, employee training content, compliance checklists, monitoring setup.\nCANNOT: Incident response judgment, penetration testing, complex security architecture, regulatory legal interpretation, breach management.",
     "Low", "$1,000 – $5,000 setup + $500–$2,000/mo", "Project + Retainer",
     "Growing regulatory pressure on SMBs; low awareness but increasing demand. High-ticket opportunity."),

    ("Emerging / Cross-Cutting", "Multi-Language Translation & Localization",
     "Website translation, marketing material localization, multilingual customer support",
     70, "High",
     "CAN: AI translation (DeepL, GPT), website localization, document translation, multilingual chatbot setup, cultural adaptation review.\nCANNOT: Legal document translation certification, cultural nuance judgment, in-person interpretation, brand voice localization strategy.",
     "Medium", "$200 – $1,000/project", "Per-project / Monthly",
     "Growing US Hispanic market + multilingual communities create demand. AI reducing cost but quality review still needed."),

    ("Emerging / Cross-Cutting", "Accessibility Compliance (ADA/Digital)",
     "Website accessibility (WCAG), ADA compliance audits, remediation, ongoing monitoring",
     70, "High",
     "CAN: Automated accessibility scanning (WAVE, axe), WCAG remediation, alt text generation, color contrast fixing, keyboard navigation fixes, compliance reports.\nCANNOT: Legal compliance interpretation, physical ADA compliance, user testing with disabled users, litigation defense, policy development.",
     "Low", "$500 – $5,000/project + $100–$300/mo", "Project + Monitoring",
     "ADA website lawsuits growing 300%+ since 2018; every SMB website is at risk. Very underserved market."),
]

# ── COMPUTE TIERS ──
computed = []
for d in data:
    cat, svc, desc, auto_pct, conf, degree, comp, ticket, delivery, notes = d
    tier, label, score = calc_tier_and_score(auto_pct, conf, comp)
    computed.append((cat, svc, desc, auto_pct, conf, degree, comp, tier, label, score, ticket, delivery, notes))

# ── Write headers ──
col_widths = [6, 26, 34, 44, 14, 16, 56, 16, 22, 12, 26, 20, 48]
for ci, h in enumerate(headers, 1):
    cell = ws.cell(row=1, column=ci, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align
    cell.border = thin_border
    ws.column_dimensions[get_column_letter(ci)].width = col_widths[ci-1]

ws.row_dimensions[1].height = 38

# ── Write data ──
row_idx = 2
prev_cat = None
for idx, (cat, svc, desc, auto_pct, conf, degree, comp, tier, label, score, ticket, delivery, notes) in enumerate(computed, 1):
    # Category separator row
    if cat != prev_cat:
        if prev_cat is not None:
            row_idx += 1  # blank spacer
        for ci in range(1, len(headers)+1):
            cell = ws.cell(row=row_idx, column=ci)
            cell.fill = PatternFill(start_color="2E75B6", end_color="2E75B6", fill_type="solid")
        ws.merge_cells(start_row=row_idx, start_column=2, end_row=row_idx, end_column=len(headers))
        cat_cell = ws.cell(row=row_idx, column=2, value=cat.upper())
        cat_cell.font = Font(bold=True, size=12, color="FFFFFF", name="Calibri")
        cat_cell.fill = PatternFill(start_color="2E75B6", end_color="2E75B6", fill_type="solid")
        cat_cell.alignment = Alignment(vertical="center")
        ws.row_dimensions[row_idx].height = 28
        row_idx += 1
        prev_cat = cat

    # Data row
    vals = [idx, cat, svc, desc, auto_pct, conf, degree, comp, tier, score, ticket, delivery, notes]
    for ci, v in enumerate(vals, 1):
        cell = ws.cell(row=row_idx, column=ci, value=v)
        cell.font = cell_font
        cell.alignment = center_align if ci in (1, 5, 6, 8, 9, 10, 12) else cell_align
        cell.border = thin_border
        if idx % 2 == 0:
            if ci != 9:  # don't override tier color with alternating fill
                cell.fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")

    # Color the automation % cell
    ws.cell(row=row_idx, column=5).fill = auto_pot_fill(auto_pct)
    ws.cell(row=row_idx, column=5).font = Font(size=10, name="Calibri", bold=True)

    # Color the confidence cell
    conf_cell = ws.cell(row=row_idx, column=6)
    conf_cell.fill = conf_fills.get(conf, PatternFill())
    conf_cell.font = Font(size=10, name="Calibri", bold=True)

    # Color the competition cell
    comp_cell = ws.cell(row=row_idx, column=8)
    comp_cell.fill = comp_fills.get(comp, PatternFill())
    comp_cell.font = comp_fonts.get(comp, cell_font)

    # Color the tier cell
    tier_cell = ws.cell(row=row_idx, column=9)
    tier_cell.fill = tier_fills.get(tier, PatternFill())
    tier_cell.font = tier_fonts.get(tier, cell_font)

    # Color the score cell based on score value
    score_cell = ws.cell(row=row_idx, column=10)
    score_cell.fill = auto_pot_fill(score)
    score_cell.font = Font(size=11, name="Calibri", bold=True)

    ws.row_dimensions[row_idx].height = 80
    row_idx += 1

# ── Summary Dashboard ──
ws2 = wb.create_sheet("Summary Dashboard")

row = 1
ws2.cell(row=row, column=1, value="INDIA → US SMB SERVICES: 5-TIER OPPORTUNITY FRAMEWORK").font = Font(bold=True, size=14, name="Calibri", color="1F4E79")
ws2.merge_cells("A1:G1")
row = 3

# ── Tier definitions ──
ws2.cell(row=row, column=1, value="TIER DEFINITIONS").font = Font(bold=True, size=12, name="Calibri", color="1F4E79")
row += 1

tier_defs = [
    ("⭐⭐⭐⭐⭐ Platinum", "Immediate Launch", "Score ≥ 85", "High automation + Low competition + High confidence. Start selling now.", tier_fills["⭐⭐⭐⭐⭐ Platinum"], tier_fonts["⭐⭐⭐⭐⭐ Platinum"]),
    ("⭐⭐⭐⭐ Gold", "High Priority", "Score 70–84", "Strong opportunity with minor caveats. Prioritize for next quarter.", tier_fills["⭐⭐⭐⭐ Gold"], tier_fonts["⭐⭐⭐⭐ Gold"]),
    ("⭐⭐⭐ Silver", "Viable with Strategy", "Score 52–69", "Solid but needs differentiation or niche positioning.", tier_fills["⭐⭐⭐ Silver"], tier_fonts["⭐⭐⭐ Silver"]),
    ("⭐⭐ Bronze", "Challenging / Niche Down", "Score 38–51", "Either low automation or high competition. Must find a unique angle.", tier_fills["⭐⭐ Bronze"], tier_fonts["⭐⭐ Bronze"]),
    ("⚠️ Red Flag", "Commodity / Avoid", "Score < 38", "Saturated market and/or hard to automate. Consider pivoting or bundling.", tier_fills["⚠️ Red Flag"], tier_fonts["⚠️ Red Flag"]),
]

tier_headers = ["Tier", "Action Label", "Score Range", "Guidance"]
for ci, h in enumerate(tier_headers, 1):
    cell = ws2.cell(row=row, column=ci, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align
    cell.border = thin_border
row += 1

for tier_name, label, score_range, guidance, fill, font in tier_defs:
    ws2.cell(row=row, column=1, value=tier_name).font = font
    ws2.cell(row=row, column=1).fill = fill
    ws2.cell(row=row, column=2, value=label).font = Font(size=10, name="Calibri", bold=True)
    ws2.cell(row=row, column=3, value=score_range).font = Font(size=10, name="Calibri")
    ws2.cell(row=row, column=4, value=guidance).font = Font(size=10, name="Calibri")
    for ci in range(1, 5):
        ws2.cell(row=row, column=ci).border = thin_border
        ws2.cell(row=row, column=ci).alignment = Alignment(vertical="center", wrap_text=True)
    ws2.row_dimensions[row].height = 30
    row += 1

row += 1

# ── Tier distribution ──
ws2.cell(row=row, column=1, value="TIER DISTRIBUTION").font = Font(bold=True, size=12, name="Calibri", color="1F4E79")
row += 1

tier_counts = {}
tier_services = {}
for c in computed:
    t = c[7]  # tier
    tier_counts[t] = tier_counts.get(t, 0) + 1
    if t not in tier_services:
        tier_services[t] = []
    tier_services[t].append((c[1], c[0], c[9], c[3], c[4], c[6], c[10]))  # svc, cat, score, auto_pct, conf, comp, ticket

dist_headers = ["Tier", "Count", "% of Total", "Avg Score"]
for ci, h in enumerate(dist_headers, 1):
    cell = ws2.cell(row=row, column=ci, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align
    cell.border = thin_border
row += 1

tier_order = ["⭐⭐⭐⭐⭐ Platinum", "⭐⭐⭐⭐ Gold", "⭐⭐⭐ Silver", "⭐⭐ Bronze", "⚠️ Red Flag"]
total = len(computed)
for t in tier_order:
    count = tier_counts.get(t, 0)
    avg_score = sum(c[9] for c in computed if c[7] == t) / max(count, 1)
    ws2.cell(row=row, column=1, value=t).font = tier_fonts.get(t, cell_font)
    ws2.cell(row=row, column=1).fill = tier_fills.get(t, PatternFill())
    ws2.cell(row=row, column=2, value=count).font = Font(size=10, name="Calibri", bold=True)
    ws2.cell(row=row, column=3, value=f"{count/total*100:.0f}%").font = Font(size=10, name="Calibri")
    ws2.cell(row=row, column=4, value=f"{avg_score:.0f}").font = Font(size=10, name="Calibri")
    for ci in range(1, 5):
        ws2.cell(row=row, column=ci).border = thin_border
        ws2.cell(row=row, column=ci).alignment = center_align
    row += 1

# Total row
ws2.cell(row=row, column=1, value="TOTAL").font = Font(size=10, name="Calibri", bold=True)
ws2.cell(row=row, column=2, value=total).font = Font(size=10, name="Calibri", bold=True)
ws2.cell(row=row, column=3, value="100%").font = Font(size=10, name="Calibri", bold=True)
for ci in range(1, 5):
    ws2.cell(row=row, column=ci).border = thin_border
row += 2

# ── Scoring methodology ──
ws2.cell(row=row, column=1, value="SCORING METHODOLOGY").font = Font(bold=True, size=12, name="Calibri", color="1F4E79")
row += 1
methodology = [
    "Base Score = Automation Potential % (0–100 points)",
    "Competition Modifier: Low = +15, Medium = 0, High = −12, Very High = −25",
    "Confidence Modifier: Very High = +10, High = +5, Medium = 0, Low = −10",
    "Final Score = Base + Competition Modifier + Confidence Modifier (clamped 0–120)",
    "",
    "Tier Thresholds: Platinum ≥ 85 | Gold 70–84 | Silver 52–69 | Bronze 38–51 | Red Flag < 38",
]
for m in methodology:
    ws2.cell(row=row, column=1, value=m).font = Font(size=10, name="Calibri")
    row += 1

row += 2

# ── Platinum services detail ──
ws2.cell(row=row, column=1, value="⭐⭐⭐⭐⭐ PLATINUM SERVICES — IMMEDIATE LAUNCH").font = Font(bold=True, size=12, name="Calibri", color="6B4C00")
ws2.merge_cells(f"A{row}:G{row}")
row += 1

plat_headers = ["Service", "Vertical", "Score", "Auto %", "Confidence", "Competition", "Ticket Size"]
for ci, h in enumerate(plat_headers, 1):
    cell = ws2.cell(row=row, column=ci, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align
    cell.border = thin_border
row += 1

plat_services = sorted([s for s in tier_services.get("⭐⭐⭐⭐⭐ Platinum", [])], key=lambda x: -x[2])
for svc, cat, score, auto_pct, conf, comp, ticket in plat_services:
    ws2.cell(row=row, column=1, value=svc).font = Font(size=10, name="Calibri")
    ws2.cell(row=row, column=2, value=cat).font = Font(size=10, name="Calibri")
    ws2.cell(row=row, column=3, value=score).font = Font(size=10, name="Calibri", bold=True)
    ws2.cell(row=row, column=3).fill = auto_pot_fill(score)
    ws2.cell(row=row, column=4, value=auto_pct).font = Font(size=10, name="Calibri", bold=True)
    ws2.cell(row=row, column=4).fill = auto_pot_fill(auto_pct)
    ws2.cell(row=row, column=5, value=conf).font = Font(size=10, name="Calibri", bold=True)
    ws2.cell(row=row, column=5).fill = conf_fills.get(conf, PatternFill())
    ws2.cell(row=row, column=6, value=comp).font = comp_fonts.get(comp, cell_font)
    ws2.cell(row=row, column=6).fill = comp_fills.get(comp, PatternFill())
    ws2.cell(row=row, column=7, value=ticket).font = Font(size=10, name="Calibri")
    for ci in range(1, 8):
        ws2.cell(row=row, column=ci).border = thin_border
    row += 1

row += 2

# ── Gold services detail ──
ws2.cell(row=row, column=1, value="⭐⭐⭐⭐ GOLD SERVICES — HIGH PRIORITY").font = Font(bold=True, size=12, name="Calibri", color="1F4E79")
ws2.merge_cells(f"A{row}:G{row}")
row += 1

for ci, h in enumerate(plat_headers, 1):
    cell = ws2.cell(row=row, column=ci, value=h)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_align
    cell.border = thin_border
row += 1

gold_services = sorted([s for s in tier_services.get("⭐⭐⭐⭐ Gold", [])], key=lambda x: -x[2])
for svc, cat, score, auto_pct, conf, comp, ticket in gold_services:
    ws2.cell(row=row, column=1, value=svc).font = Font(size=10, name="Calibri")
    ws2.cell(row=row, column=2, value=cat).font = Font(size=10, name="Calibri")
    ws2.cell(row=row, column=3, value=score).font = Font(size=10, name="Calibri", bold=True)
    ws2.cell(row=row, column=3).fill = auto_pot_fill(score)
    ws2.cell(row=row, column=4, value=auto_pct).font = Font(size=10, name="Calibri", bold=True)
    ws2.cell(row=row, column=4).fill = auto_pot_fill(auto_pct)
    ws2.cell(row=row, column=5, value=conf).font = Font(size=10, name="Calibri", bold=True)
    ws2.cell(row=row, column=5).fill = conf_fills.get(conf, PatternFill())
    ws2.cell(row=row, column=6, value=comp).font = comp_fonts.get(comp, cell_font)
    ws2.cell(row=row, column=6).fill = comp_fills.get(comp, PatternFill())
    ws2.cell(row=row, column=7, value=ticket).font = Font(size=10, name="Calibri")
    for ci in range(1, 8):
        ws2.cell(row=row, column=ci).border = thin_border
    row += 1

# Column widths for summary
ws2.column_dimensions['A'].width = 36
ws2.column_dimensions['B'].width = 30
ws2.column_dimensions['C'].width = 12
ws2.column_dimensions['D'].width = 12
ws2.column_dimensions['E'].width = 16
ws2.column_dimensions['F'].width = 16
ws2.column_dimensions['G'].width = 30

# ── Legend sheet ──
ws3 = wb.create_sheet("Legend & Notes")
legend = [
    ("PARAMETER", "DESCRIPTION"),
    ("Automation Potential (%)", "Estimated % of the total service deliverable that can be automated using current AI/technology tools"),
    ("Automation Confidence", "How confident we are that this automation level is achievable TODAY (not theoretical future capability)"),
    ("Degree of Automation", "Detailed breakdown of what CAN be automated vs what CANNOT (requires human judgment/expertise)"),
    ("Competitive Intensity", "How saturated the market is with service providers (both India-based and global) — Low = Opportunity"),
    ("Opportunity Tier", "5-tier composite score combining automation potential, confidence, and competitive intensity"),
    ("Opportunity Score", "Numerical score (0–120) computed from automation % + competition modifier + confidence modifier"),
    ("Ticket Size (USD)", "Typical price range charged to US SMB clients for this service"),
    ("Delivery Model", "How the service is typically sold/billed (Project, Monthly Retainer, Per-unit, etc.)"),
    ("", ""),
    ("TIER DEFINITIONS", ""),
    ("⭐⭐⭐⭐⭐ Platinum (Score ≥ 85)", "Immediate launch opportunity. High automation, low competition, high confidence. Start selling now."),
    ("⭐⭐⭐⭐ Gold (Score 70–84)", "High priority. Strong opportunity with minor caveats. Prioritize for next quarter."),
    ("⭐⭐⭐ Silver (Score 52–69)", "Viable with strategy. Solid but needs differentiation or niche positioning to win."),
    ("⭐⭐ Bronze (Score 38–51)", "Challenging. Either low automation or high competition. Must find a unique angle or bundle."),
    ("⚠️ Red Flag (Score < 38)", "Commodity / Avoid. Saturated market and/or hard to automate. Consider pivoting or bundling with other services."),
    ("", ""),
    ("SCORING FORMULA", ""),
    ("Base Score", "= Automation Potential % (0–100)"),
    ("+ Competition Modifier", "Low = +15 | Medium = 0 | High = −12 | Very High = −25"),
    ("+ Confidence Modifier", "Very High = +10 | High = +5 | Medium = 0 | Low = −10"),
    ("= Final Score", "Clamped between 0–120, then mapped to tier"),
    ("", ""),
    ("COLOR CODING", ""),
    ("Green (Automation %)", "≥75% — Majority of work can be automated"),
    ("Light Green (Automation %)", "50-74% — Significant automation possible"),
    ("Yellow (Automation %)", "30-49% — Moderate automation opportunity"),
    ("Red (Automation %)", "<30% — Mostly human-dependent"),
    ("", ""),
    ("Green (Competition)", "Low — Market opportunity, few players"),
    ("Yellow (Competition)", "Medium — Competitive but room for differentiation"),
    ("Red (Competition)", "High — Saturated, need strong differentiation"),
    ("Dark Red (Competition)", "Very High — Extremely crowded, commodity pricing pressure"),
]
for ri, (a, b) in enumerate(legend, 1):
    ws3.cell(row=ri, column=1, value=a).font = Font(bold=True, size=10, name="Calibri")
    ws3.cell(row=ri, column=2, value=b).font = Font(size=10, name="Calibri")
ws3.column_dimensions['A'].width = 38
ws3.column_dimensions['B'].width = 100

# Freeze panes & auto-filter
ws.freeze_panes = "A2"
ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{row_idx-1}"

output_path = "/home/user/India_US_SMB_Services_Analysis.xlsx"
wb.save(output_path)
print(f"Saved to {output_path}")
print(f"Total services: {len(computed)}")
print()
print("═══ TIER DISTRIBUTION ═══")
for t in tier_order:
    count = tier_counts.get(t, 0)
    pct = count / total * 100
    print(f"  {t:25s}  {count:3d}  ({pct:4.1f}%)")
print(f"  {'TOTAL':25s}  {total:3d}")
