
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

cat_font = Font(bold=True, size=10.5, name="Calibri", color="1F4E79")
cat_fill = PatternFill(start_color="D6E4F0", end_color="D6E4F0", fill_type="solid")

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

# ── DATA ──
# (category, service, description, automation%, confidence, degree, competition, ticket_size, delivery, notes)
data = [
    # ═══════ UNIVERSAL – DIGITAL MARKETING ═══════
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

    # ═══════ UNIVERSAL – BACK OFFICE ═══════
    ("Universal – Back Office", "Bookkeeping & Accounting",
     "QuickBooks/Xero management, reconciliation, AP/AR, financial reporting, tax prep support",
     75, "High",
     "CAN: Automated bank feeds, receipt OCR, transaction categorization (AI), reconciliation, financial report generation, tax document preparation.\nCANNOT: Complex tax strategy, audit representation, advisory/forecasting judgment, nuanced GAAP decisions, client relationship management.",
     "High", "$300 – $1,500/mo", "Monthly Retainer",
     "Strong demand; established Indian players (Odesk, BPO firms). Differentiate via industry specialization."),

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

    # ═══════ UNIVERSAL – TECHNOLOGY ═══════
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

    # ═══════ LANDSCAPING ═══════
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

    # ═══════ LOCATOR / PI ═══════
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

    # ═══════ MORTGAGE BROKER ═══════
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
     "Regulatory complexity creates demand; expertise barrier is high, which limits competition."),

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

    # ═══════ SOLAR ═══════
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

    # ═══════ SALON / SPA ═══════
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

    # ═══════ PET GROOMING ═══════
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

    # ═══════ ADDITIONAL EMERGING / CROSS-CUTTING SERVICES ═══════
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
]

# ── Write headers ──
col_widths = [6, 24, 32, 42, 14, 16, 55, 16, 22, 18, 45]
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
for idx, (cat, svc, desc, auto_pct, conf, degree, comp, ticket, delivery, notes) in enumerate(data, 1):
    # Category separator row
    if cat != prev_cat:
        if prev_cat is not None:
            row_idx += 1  # blank spacer
        for ci in range(1, len(headers)+1):
            cell = ws.cell(row=row_idx, column=ci)
            cell.fill = PatternFill(start_color="2E75B6", end_color="2E75B6", fill_type="solid")
        ws.cell(row=row_idx, column=1, value="").font = Font(size=1)
        # Merge the category label across columns B-K
        ws.merge_cells(start_row=row_idx, start_column=2, end_row=row_idx, end_column=len(headers))
        cat_cell = ws.cell(row=row_idx, column=2, value=cat.upper())
        cat_cell.font = Font(bold=True, size=12, color="FFFFFF", name="Calibri")
        cat_cell.fill = PatternFill(start_color="2E75B6", end_color="2E75B6", fill_type="solid")
        cat_cell.alignment = Alignment(vertical="center")
        ws.row_dimensions[row_idx].height = 28
        row_idx += 1
        prev_cat = cat

    # Data row
    vals = [idx, cat.split("–")[-1].strip() if "–" in cat else cat, svc, desc,
            auto_pct, conf, degree, comp, ticket, delivery, notes]
    for ci, v in enumerate(vals, 1):
        cell = ws.cell(row=row_idx, column=ci, value=v)
        cell.font = cell_font
        cell.alignment = center_align if ci in (1, 5, 6, 8, 10) else cell_align
        cell.border = thin_border
        # Alternate row shading
        if idx % 2 == 0:
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

    ws.row_dimensions[row_idx].height = 80
    row_idx += 1

# ── Summary sheet ──
ws2 = wb.create_sheet("Summary Dashboard")

# Summary stats
summary_data = [
    ("TOTAL SERVICES ANALYZED", len(data)),
    ("", ""),
    ("AUTOMATION POTENTIAL BREAKDOWN", ""),
    ("Highly Automatable (≥75%)", sum(1 for d in data if d[3] >= 75)),
    ("Moderately Automatable (50-74%)", sum(1 for d in data if 50 <= d[3] < 75)),
    ("Low Automation Potential (<50%)", sum(1 for d in data if d[3] < 50)),
    ("", ""),
    ("COMPETITION BREAKDOWN", ""),
    ("Very High Competition", sum(1 for d in data if d[6] == "Very High")),
    ("High Competition", sum(1 for d in data if d[6] == "High")),
    ("Medium Competition", sum(1 for d in data if d[6] == "Medium")),
    ("Low Competition (Opportunity!)", sum(1 for d in data if d[6] == "Low")),
    ("", ""),
    ("TOP OPPORTUNITIES (High Auto + Low Competition)", ""),
]

# Find best opportunities
opportunities = sorted(data, key=lambda x: (-x[3], x[6]))
top_opps = [d for d in data if d[3] >= 70 and d[6] in ("Low", "Medium")]

row = 1
ws2.cell(row=row, column=1, value="INDIA → US SMB SERVICES: ANALYSIS SUMMARY").font = Font(bold=True, size=14, name="Calibri", color="1F4E79")
ws2.merge_cells("A1:D1")
row = 3

for label, val in summary_data:
    ws2.cell(row=row, column=1, value=label).font = Font(bold=True, size=10, name="Calibri", color="1F4E79" if label else "000000")
    ws2.cell(row=row, column=2, value=val).font = Font(size=10, name="Calibri", bold=True)
    row += 1

row += 1
# Top opportunities header
ws2.cell(row=row, column=1, value="Service").font = Font(bold=True, size=10, color="FFFFFF")
ws2.cell(row=row, column=2, value="Automation %").font = Font(bold=True, size=10, color="FFFFFF")
ws2.cell(row=row, column=3, value="Competition").font = Font(bold=True, size=10, color="FFFFFF")
ws2.cell(row=row, column=4, value="Ticket Size").font = Font(bold=True, size=10, color="FFFFFF")
for c in range(1, 5):
    ws2.cell(row=row, column=c).fill = header_fill
    ws2.cell(row=row, column=c).alignment = header_align
row += 1

for d in sorted(top_opps, key=lambda x: (-x[3])):
    ws2.cell(row=row, column=1, value=d[1]).font = Font(size=10, name="Calibri")
    ws2.cell(row=row, column=2, value=d[3]).font = Font(size=10, name="Calibri", bold=True)
    ws2.cell(row=row, column=2).fill = auto_pot_fill(d[3])
    ws2.cell(row=row, column=3, value=d[6]).font = comp_fonts.get(d[6], cell_font)
    ws2.cell(row=row, column=3).fill = comp_fills.get(d[6], PatternFill())
    ws2.cell(row=row, column=4, value=d[7]).font = Font(size=10, name="Calibri")
    for c in range(1, 5):
        ws2.cell(row=row, column=c).border = thin_border
    row += 1

ws2.column_dimensions['A'].width = 40
ws2.column_dimensions['B'].width = 18
ws2.column_dimensions['C'].width = 18
ws2.column_dimensions['D'].width = 28

# Freeze panes
ws.freeze_panes = "A2"
ws.auto_filter.ref = f"A1:K{row_idx-1}"

# ── Legend sheet ──
ws3 = wb.create_sheet("Legend & Notes")
legend = [
    ("PARAMETER", "DESCRIPTION"),
    ("Automation Potential (%)", "Estimated % of the total service deliverable that can be automated using current AI/technology tools"),
    ("Automation Confidence", "How confident we are that this automation level is achievable TODAY (not theoretical future capability)"),
    ("Degree of Automation", "Detailed breakdown of what CAN be automated vs what CANNOT (requires human judgment/expertise)"),
    ("Competitive Intensity", "How saturated the market is with service providers (both India-based and global) — Low = Opportunity"),
    ("Ticket Size (USD)", "Typical price range charged to US SMB clients for this service"),
    ("Delivery Model", "How the service is typically sold/billed (Project, Monthly Retainer, Per-unit, etc.)"),
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
ws3.column_dimensions['A'].width = 30
ws3.column_dimensions['B'].width = 90

output_path = "/home/user/India_US_SMB_Services_Analysis.xlsx"
wb.save(output_path)
print(f"Saved to {output_path}")
print(f"Total services: {len(data)}")
print(f"High automation (≥75%): {sum(1 for d in data if d[3]>=75)}")
print(f"Low competition: {sum(1 for d in data if d[6]=='Low')}")
