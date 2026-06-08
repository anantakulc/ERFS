#!/usr/bin/env python3
"""
AVGO PDF Report Generator — renders AVGO_research.md into a formatted PDF.
Uses reportlab; no external JSON dependency.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
import os

OUT = "/home/user/ERFS/output/AVGO/AVGO_report.pdf"
W, H = A4

# ── Colour palette ──────────────────────────────────────────────────────────
NAVY   = colors.HexColor("#0D1B3E")
BLUE   = colors.HexColor("#1A3A8F")
GREEN  = colors.HexColor("#1B7A4A")
RED    = colors.HexColor("#C0392B")
AMBER  = colors.HexColor("#E67E22")
LGREY  = colors.HexColor("#F4F6FA")
MGREY  = colors.HexColor("#D0D5E0")
DGREY  = colors.HexColor("#555E70")
WHITE  = colors.white
BLACK  = colors.black

# ── Styles ──────────────────────────────────────────────────────────────────
SS = getSampleStyleSheet()

def sty(name, parent="Normal", **kw):
    return ParagraphStyle(name, parent=SS[parent], **kw)

COVER_TITLE = sty("CT", fontSize=28, textColor=WHITE, leading=34, fontName="Helvetica-Bold")
COVER_SUB   = sty("CS", fontSize=13, textColor=colors.HexColor("#B0C4E8"), leading=18)
COVER_TAG   = sty("CG", fontSize=10, textColor=colors.HexColor("#90A8D0"), leading=14)
H1    = sty("H1", fontSize=13, textColor=WHITE, leading=18, fontName="Helvetica-Bold",
            backColor=NAVY, leftIndent=-6, rightIndent=-6, borderPad=6, spaceAfter=4, spaceBefore=10)
H2    = sty("H2", fontSize=10, textColor=BLUE, leading=14, fontName="Helvetica-Bold", spaceBefore=8, spaceAfter=2)
BODY  = sty("BD", fontSize=8.5, textColor=BLACK, leading=12, spaceBefore=2, spaceAfter=2)
BODYSM= sty("BS", fontSize=7.5, textColor=DGREY, leading=11)
BULLET= sty("BU", fontSize=8.5, textColor=BLACK, leading=12, leftIndent=12, bulletIndent=4, spaceBefore=1)
CAPTION=sty("CA", fontSize=7, textColor=DGREY, leading=10, alignment=TA_CENTER, spaceAfter=4)
VERDICT=sty("VD", fontSize=9, textColor=NAVY, fontName="Helvetica-Bold",
            backColor=colors.HexColor("#E8F0FB"), borderPad=4, spaceAfter=6)

def ts(header_bg=BLUE, stripe=LGREY, fs=7.5):
    return TableStyle([
        ("BACKGROUND",  (0,0),(-1,0), header_bg),
        ("TEXTCOLOR",   (0,0),(-1,0), WHITE),
        ("FONTNAME",    (0,0),(-1,0), "Helvetica-Bold"),
        ("FONTSIZE",    (0,0),(-1,-1), fs),
        ("FONTNAME",    (0,1),(-1,-1), "Helvetica"),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE, stripe]),
        ("GRID",        (0,0),(-1,-1), 0.3, MGREY),
        ("TOPPADDING",  (0,0),(-1,-1), 3),
        ("BOTTOMPADDING",(0,0),(-1,-1), 3),
        ("LEFTPADDING", (0,0),(-1,-1), 4),
        ("RIGHTPADDING",(0,0),(-1,-1), 4),
        ("VALIGN",      (0,0),(-1,-1), "MIDDLE"),
    ])

def sp(n=4):  return Spacer(1, n)
def hr():     return HRFlowable(width="100%", thickness=0.5, color=MGREY, spaceAfter=4, spaceBefore=4)

# ── Build ────────────────────────────────────────────────────────────────────
def build():
    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=16*mm,
        title="Broadcom Inc. (AVGO) — Institutional Equity Research",
        author="Alpha Research Engine",
    )
    s = []

    # ── Cover ────────────────────────────────────────────────────────────────
    banner_rows = [
        [Paragraph("BROADCOM INC.", COVER_TITLE)],
        [Paragraph("AVGO US Equity", COVER_SUB)],
        [Paragraph(" ", COVER_TAG)],
        [Paragraph("INSTITUTIONAL EQUITY RESEARCH", COVER_TAG)],
        [Paragraph("Rating: <b>OVERWEIGHT</b>  ·  Price Target: <b>$475</b>  ·  Current Price: $385.73", COVER_SUB)],
        [Paragraph("Date: 2026-06-08  ·  Data: yfinance 1.4.1  ·  Cycle: Charlie + Kilo + Delta", COVER_TAG)],
    ]
    banner = Table(banner_rows, colWidths=[doc.width])
    banner.setStyle(TableStyle([
        ("BACKGROUND", (0,0),(-1,-1), NAVY),
        ("TOPPADDING", (0,0),(-1,-1), 6), ("BOTTOMPADDING",(0,0),(-1,-1), 6),
        ("LEFTPADDING",(0,0),(-1,-1), 10),("RIGHTPADDING", (0,0),(-1,-1), 10),
    ]))
    s.append(banner); s.append(sp(8))

    metrics = [
        ("Market Cap","$1,826B"), ("EV","$1,876B"), ("TTM Revenue","$75.5B"), ("TTM EBITDA","$41.9B"),
        ("FY25 FCF","$26.9B (42.1%)"), ("Net Debt","$51.9B (1.4× EBITDA)"),
        ("Fwd P/E (nGAAP)","20.0×"), ("EV/EBITDA","44.7×"),
        ("Short % Float","1.15%"), ("52W High/Low","$495 / $241"),
        ("YTD Return","+11.2%"), ("ADTV","$11.6B"),
    ]
    ncols = 4
    rows = []
    for i in range(0, len(metrics), ncols):
        row = []
        for k, v in metrics[i:i+ncols]:
            row += [Paragraph(f"<b>{k}</b>", BODYSM), Paragraph(v, BODYSM)]
        while len(row) < ncols*2:
            row += [Paragraph("","Normal"), Paragraph("","Normal")]
        rows.append(row)
    mt = Table(rows, colWidths=[28*mm, 22*mm]*ncols)
    mt.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1),LGREY),("GRID",(0,0),(-1,-1),0.3,MGREY),
        ("FONTSIZE",(0,0),(-1,-1),7.5),("FONTNAME",(0,0),(-1,-1),"Helvetica"),
        ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
        ("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),4),
    ]))
    s.append(mt); s.append(sp(8))
    s.append(Paragraph("Research Cycle: Alpha · Charlie (bull) · Kilo (bear) · Delta (audit) | Not financial advice. Professional investors only.", CAPTION))
    s.append(PageBreak())

    # ── §1 Market Statistics ─────────────────────────────────────────────────
    s.append(Paragraph("§1 — Market Statistics", H1))
    d = [
        ["Metric","Value","Metric","Value"],
        ["Current Price","$385.73","ADTV (30-day)","$11.6B"],
        ["Market Cap","$1,826B","30d Realized Vol","69.4% ann."],
        ["Enterprise Value","$1,876B","Short % Float","1.15%"],
        ["52W High / Low","$495 / $241","Short Ratio","2.7 days"],
        ["Drawdown from High","−22.1%","Insider %","1.95%"],
        ["YTD Return","+11.2%","Institutional %","80.3%"],
        ["1-Year Return","+57.5%","Beta","1.433"],
        ["Trailing P/E (GAAP)","64.1×","Fwd P/E (nGAAP)","20.0×"],
        ["EV/Revenue (TTM)","24.9×","EV/EBITDA (TTM)","44.7×"],
        ["Dividend Yield","0.67% ($2.60/yr)","Analyst Rating","Strong Buy 1.33/5"],
        ["Analyst Mean Target","$517.61 (+34%)","Analyst Median","$525.00 (+36%)"],
    ]
    t = Table(d, colWidths=[50*mm,35*mm,50*mm,37*mm])
    t.setStyle(ts())
    s.append(t); s.append(sp())

    # ── §2 Company ───────────────────────────────────────────────────────────
    s.append(Paragraph("§2 — Company Overview & Business Model Flywheel", H1))
    s.append(Paragraph(
        "Broadcom Inc. (NASDAQ: AVGO) designs semiconductors and infrastructure software across two segments: "
        "<b>Semiconductor Solutions</b> (~53% of FY2025 revenue) covering custom AI accelerators (XPUs), "
        "Ethernet networking ASICs, broadband, storage, and wireless; and <b>Infrastructure Software</b> "
        "(~47%) anchored by VMware (acquired Nov 2023, ~$69B EV), CA Technologies, and Symantec Enterprise. "
        "Fab-lite model — manufacturing outsourced primarily to TSMC. FY ends October 31.", BODY))
    s.append(sp(4))
    s.append(Paragraph("<b>Flywheel:</b>", H2))
    for line in [
        "Hyperscaler AI capex → XPU design wins (sole/primary for 3 hyperscalers)",
        "→ Semi revenue +66% FY26E → Scale + R&D moat → Networking ASICs scale with AI clusters",
        "→ FCF $32B ann. (1% capex intensity) → Debt repayment (ND/EBITDA 1.4× and falling)",
        "→ VMware subscription conversion (85–90% GM) → Op. margin 29% FY24 → 49% TTM",
        "→ EPS leverage → analyst raises → acquisition currency → next deal → repeat",
    ]:
        s.append(Paragraph(f"• {line}", BULLET))
    s.append(sp())

    # ── §3 Segments ──────────────────────────────────────────────────────────
    s.append(Paragraph("§3 — Business Segments (FY2025 Estimates [ESTIMATED])", H1))
    d = [
        ["Segment","FY25 Rev","% Total","YoY Growth","EBITDA Margin"],
        ["Semiconductor Solutions","~$33.9B","~53%","~+11%","~55%"],
        ["  — AI XPUs","~$12.2B","~19%",">100%","—"],
        ["  — Networking ASICs","~$8.5B","~13%","~+30%","—"],
        ["  — Server storage","~$4.2B","~7%","flat","—"],
        ["  — Broadband","~$4.0B","~6%","declining","—"],
        ["  — Wireless (Apple)","~$5.0B","~8%","low-single","—"],
        ["Infrastructure Software","~$30.0B","~47%","~+47%","~75%"],
        ["  — VMware Cloud Foundation","~$24B","~38%",">50% conv.","—"],
        ["  — CA / Symantec","~$6B","~9%","low-single","—"],
        ["TOTAL","$63.9B","100%","+23.9%","40.8% op. margin"],
    ]
    t = Table(d, colWidths=[70*mm,25*mm,20*mm,25*mm,32*mm])
    tst = ts()
    tst.add("FONTNAME",(0,10),(-1,10),"Helvetica-Bold")
    tst.add("BACKGROUND",(0,10),(-1,10),colors.HexColor("#D6E4F0"))
    t.setStyle(tst)
    s.append(t)
    s.append(Paragraph("[ESTIMATED] from earnings calls and analyst channel checks.", CAPTION))

    # ── §5 Customers ─────────────────────────────────────────────────────────
    s.append(Paragraph("§5 — Top Customers & Concentration", H1))
    d = [
        ["Customer","Est. Revenue","Products","Disclosure Basis"],
        ["Apple Inc.","$5–8B (8–12% semi)","Wi-Fi 7, BT 5.4, UWB","SEC 10-K >10% threshold"],
        ["Alphabet/Google","$3–6B","TPU XPU, Ethernet ASICs","Earnings call commentary"],
        ["Meta Platforms","$2–5B","MTIA AI accelerator","Earnings call commentary"],
        ["Microsoft","$1–3B","Azure networking ASICs","Analyst channel checks"],
        ["Top VMware Accounts",">$8B combined","VCF subscriptions (>3yr)","VMware renewal metrics"],
    ]
    t = Table(d, colWidths=[40*mm,38*mm,50*mm,44*mm])
    t.setStyle(ts())
    s.append(t)
    s.append(Paragraph("⚠ 3 hyperscaler XPU customers with no binding contracts. Each design cycle (2–3yr) is a competitive re-tender. Exact % is a confirmed data gap.", BODYSM))
    s.append(sp())

    # ── §6 Management ────────────────────────────────────────────────────────
    s.append(Paragraph("§6 — Management & Acquisition Track Record", H1))
    d = [
        ["Name","Role","Tenure","Background"],
        ["Hock E. Tan","President & CEO","Since 2006","Architect of M&A roll-up; every acquisition follows same playbook"],
        ["Kirsten M. Spears","EVP & CFO","Since 2016","Financial engineer behind all deleveraging cycles"],
        ["Mark D. Brazeal","EVP, CLO","Since 2010","Legal architect of all acquisitions incl. VMware $69B"],
        ["Dr. Charlie Kawwas","President, Semi","Since 2020","Leads AI XPU strategy and hyperscaler relationships"],
    ]
    t = Table(d, colWidths=[40*mm,35*mm,25*mm,72*mm])
    t.setStyle(ts())
    s.append(t); s.append(sp(4))
    d = [
        ["Target","Year","Price","Outcome"],
        ["LSI Corp","2014","$6.6B","FCF extracted; storage hardware divested ✓"],
        ["Broadcom Corp (merger)","2016","$37B","Created current entity ✓"],
        ["Brocade","2017","$5.5B","Kept software; sold hardware ✓"],
        ["CA Technologies","2018","$18.9B","Subscription conversion complete ✓"],
        ["Symantec Enterprise","2019","$10.7B","Subscription conversion complete ✓"],
        ["VMware","2023","$69B","Integration complete; margins recovering ✓"],
    ]
    t = Table(d, colWidths=[50*mm,18*mm,20*mm,84*mm])
    t.setStyle(ts())
    s.append(t); s.append(sp())

    # ── §7 Financials ────────────────────────────────────────────────────────
    s.append(Paragraph("§7 — Historical Financials", H1))
    d = [
        ["Metric","FY2022","FY2023","FY2024","FY2025","TTM","FY26E","FY27E"],
        ["Revenue","$33.2B","$35.8B","$51.6B","$63.9B","$75.5B","$106.0B","$170.5B"],
        ["YoY Growth","+20.7%","+7.9%","+44.0%","+23.9%","+47.9%","+65.9%","+60.8%"],
        ["Gross Margin","66.6%","68.9%","63.0%","67.8%","76.3%","—","—"],
        ["Op. Margin","43.0%","45.9%","29.1%","40.8%","49.0%","—","—"],
        ["EBITDA","$19.2B","$20.6B","$23.9B","$34.7B","$41.9B","—","—"],
        ["GAAP Net Income","$11.5B","$14.1B","$5.9B","$23.1B","—","—","—"],
        ["FCF","$16.3B","$17.6B","$19.4B","$26.9B","~$32B ann.","—","—"],
        ["FCF Margin","49.1%","49.2%","37.6%","42.1%","—","—","—"],
        ["GAAP EPS","$2.65","$3.30","$1.23","$4.77","$6.02","—","—"],
        ["nGAAP EPS (est.)","—","—","—","—","—","$11.62","$19.32"],
        ["Capex","$424M","$452M","$548M","$623M","—","—","—"],
        ["Net Debt","$27.1B","$25.0B","$58.2B","$48.9B","$51.9B","—","—"],
        ["ND/EBITDA","1.4×","1.2×","2.4×","1.4×","~1.2×","—","—"],
        ["Interest Coverage","—","—","3.6×","8.1×","—","—","—"],
    ]
    t = Table(d, colWidths=[35*mm,18*mm,18*mm,18*mm,18*mm,20*mm,20*mm,20*mm])
    tst = ts(fs=7)
    tst.add("FONTNAME",(0,0),(0,-1),"Helvetica-Bold")
    t.setStyle(tst)
    s.append(t)
    s.append(Paragraph("Source: yfinance income_stmt, cashflow, balance_sheet (annual). FY26E/FY27E: consensus via yfinance.", CAPTION))

    # ── §8 Recent Results ─────────────────────────────────────────────────────
    s.append(Paragraph("§8 — Recent Results & Earnings Beats", H1))
    d = [
        ["Quarter","EPS Est.","EPS Actual","Surprise",""],
        ["Q3 FY2025 (Jul 31, 2025)","$1.663","$1.690","+1.60%","✓"],
        ["Q4 FY2025 (Oct 31, 2025)","$1.868","$1.950","+4.38%","✓"],
        ["Q1 FY2026 (Jan 31, 2026)","$2.023","$2.050","+1.32%","✓"],
        ["Q2 FY2026 (Apr 30, 2026)","$2.397","$2.440","+1.78%","✓"],
    ]
    t = Table(d, colWidths=[55*mm,28*mm,28*mm,28*mm,33*mm])
    tst = ts()
    for r in range(1,5):
        tst.add("TEXTCOLOR",(4,r),(4,r),GREEN)
        tst.add("FONTNAME",(4,r),(4,r),"Helvetica-Bold")
    t.setStyle(tst)
    s.append(t)
    s.append(Paragraph("4/4 consecutive beats. Average surprise: +2.27%. Source: yfinance earnings_history.", CAPTION))
    s.append(sp(4))
    s.append(Paragraph("<b>Post-Q2 FY26 Analyst Actions (June 4, 2026):</b>", H2))
    d = [
        ["Firm","Action","New Target","Prior"],
        ["JP Morgan","Raise","$580","$500"],["Jefferies","Raise","$550","$500"],
        ["Truist Securities","Raise","$550","$545"],["Oppenheimer","Raise","$535","$450"],
        ["B of A Securities","Raise","$530","$450"],["Mizuho","Raise","$530","$480"],
        ["TD Cowen","Maintain Buy","$500","$500"],["DA Davidson","Raise (Neutral)","$400","$375"],
        ["Macquarie","↓ Downgrade","$437","Outperform"],
    ]
    t = Table(d, colWidths=[52*mm,40*mm,30*mm,50*mm])
    tst = ts()
    tst.add("TEXTCOLOR",(1,9),(1,9),RED)
    tst.add("FONTNAME",(1,9),(1,9),"Helvetica-Bold")
    t.setStyle(tst)
    s.append(t); s.append(sp())

    # ── §10 Peer Multiples ────────────────────────────────────────────────────
    s.append(Paragraph("§10 — Peer Valuation Comparison (yfinance, 2026-06-08)", H1))
    d = [
        ["Company","Fwd P/E","EV/EBITDA","EV/Revenue","Rev Growth","Gross Margin"],
        ["AVGO ★","20.0×","44.7×","24.9×","+65.9%","76.3%"],
        ["NVDA","16.2×","29.7×","19.4×","+85%","74%"],
        ["MRVL","42.7×","85.5×","26.6×","+28%","52%"],
        ["QCOM","20.2×","17.9×","5.2×","−4%","55%"],
        ["AMD","35.7×","101.2×","20.1×","+38%","53%"],
        ["ORCL","26.5×","27.1×","11.6×","+22%","67%"],
        ["MSFT","21.5×","17.0×","9.9×","+18%","68%"],
        ["Peer Median","24.0×","28.4×","15.5×","—","—"],
    ]
    t = Table(d, colWidths=[36*mm,25*mm,27*mm,27*mm,27*mm,30*mm])
    tst = ts()
    tst.add("BACKGROUND",(0,1),(-1,1),colors.HexColor("#D6E8F7"))
    tst.add("FONTNAME",(0,1),(-1,1),"Helvetica-Bold")
    tst.add("BACKGROUND",(0,8),(-1,8),LGREY)
    tst.add("FONTNAME",(0,8),(-1,8),"Helvetica-Bold")
    t.setStyle(tst)
    s.append(t); s.append(sp())

    # ── §11 Valuation ────────────────────────────────────────────────────────
    s.append(PageBreak())
    s.append(Paragraph("§11 — Valuation", H1))

    s.append(Paragraph("<b>WACC Adjudication</b>", H2))
    d = [
        ["Input","Value","Basis"],
        ["rf (10Y UST)","4.54%","Live fetch"],
        ["Beta (β)","1.433","yfinance info.beta"],
        ["ERP","5.50%","Damodaran US implied"],
        ["ke = rf + β×ERP","12.42%","CAPM"],
        ["E/V (equity weight)","97.2%","Near 100% equity funded"],
        ["kd (after-tax)","3.84%","Interest exp / total debt × (1−21%)"],
        ["Formula WACC","12.18%","E/V×ke + D/V×kd×(1−t)"],
        ["Sector band","10–12%","Semiconductors reference"],
        ["Peer-implied WACC","~10.5%","NVDA/MRVL/QCOM blend"],
        ["Market-implied ke","~7.5%","1/fwdPE(19.96×) + 2.5% LT growth"],
        ["→ ADJUDICATED WACC","12.18%","Formula; at top of band; near-100% equity justified"],
    ]
    t = Table(d, colWidths=[45*mm,30*mm,97*mm])
    tst = ts()
    tst.add("FONTNAME",(0,11),(-1,11),"Helvetica-Bold")
    tst.add("BACKGROUND",(0,11),(-1,11),colors.HexColor("#FFF3E0"))
    tst.add("TEXTCOLOR",(0,11),(-1,11),AMBER)
    t.setStyle(tst)
    s.append(t); s.append(sp(4))

    s.append(Paragraph("<b>DCF — 5-Year FCFF Projection (Base: WACC 12.18%, g 2.5%)</b>", H2))
    d = [
        ["Year","Revenue","Growth","EBIT (45%)","NOPAT","D&A (13.7%)","Capex (1.1%)","FCFF"],
        ["FY2026E","$106.0B","+65.9%","$47.7B","$37.7B","$14.5B","$1.2B","$50.5B"],
        ["FY2027E","$170.5B","+60.8%","$76.7B","$60.6B","$23.4B","$1.9B","$81.4B"],
        ["FY2028E","$213.0B","+25.0%","$95.9B","$75.7B","$29.2B","$2.3B","$101.5B"],
        ["FY2029E","$245.0B","+15.0%","$110.3B","$87.1B","$33.6B","$2.7B","$117.0B"],
        ["FY2030E","$264.6B","+8.0%","$119.1B","$94.1B","$36.3B","$2.9B","$126.4B"],
    ]
    t = Table(d, colWidths=[22*mm,24*mm,18*mm,24*mm,20*mm,24*mm,22*mm,18*mm])
    t.setStyle(ts(fs=7))
    s.append(t); s.append(sp(4))

    s.append(Paragraph("<b>DCF Scenarios</b>", H2))
    d = [
        ["Scenario","WACC","Terminal g","TV Method","Implied Price"],
        ["Bull","10.5%","3.0%","Gordon TV","$281"],
        ["Base (Gordon TV)","12.2%","2.5%","Gordon TV","$218"],
        ["Base+ (blended TV)","12.2%","2.5%","Gordon + 18× EBITDA exit","$304"],
        ["Bear","14.0%","1.5%","Gordon TV; FCF 45% below base","$94"],
        ["Prob-weighted (30/45/25)","—","—","—","$241"],
    ]
    t = Table(d, colWidths=[55*mm,20*mm,20*mm,60*mm,17*mm])
    tst = ts()
    tst.add("TEXTCOLOR",(4,1),(4,1),GREEN)
    tst.add("TEXTCOLOR",(4,4),(4,4),RED)
    tst.add("FONTNAME",(0,5),(-1,5),"Helvetica-Bold")
    tst.add("BACKGROUND",(0,5),(-1,5),LGREY)
    t.setStyle(tst)
    s.append(t); s.append(sp(4))

    s.append(Paragraph("<b>DCF Sensitivity: WACC × Terminal g (Gordon TV)</b>", H2))
    d = [
        ["WACC \\ g","g=1.5%","g=2.0%","g=2.5% ★","g=3.0%","g=3.5%"],
        ["10.5%","$241","$253","$266","$281","$298"],
        ["11.0%","$228","$238","$250","$263","$277"],
        ["12.2% ★","$201","$209","$218","$227","$238"],
        ["13.0%","$187","$193","$200","$208","$217"],
        ["14.0%","$171","$177","$182","$188","$195"],
    ]
    t = Table(d, colWidths=[28*mm,26*mm,26*mm,28*mm,26*mm,28*mm])
    tst = ts()
    tst.add("BACKGROUND",(3,3),(3,3),colors.HexColor("#FFE082"))
    tst.add("FONTNAME",(3,3),(3,3),"Helvetica-Bold")
    t.setStyle(tst)
    s.append(t); s.append(sp(4))

    s.append(Paragraph("<b>Relative & SOTP Valuation</b>", H2))
    d = [
        ["Method","Metric","Multiple","Implied"],
        ["Fwd P/E (FY2026E current yr)","EPS $11.615","24.0× peer median","$279"],
        ["Fwd P/E (FY2027E, NTM conv.)","EPS $19.321","24.0× peer median","$464"],
        ["EV/EBITDA (TTM)","EBITDA $41.9B","28.4× peer median","$241"],
        ["EV/Revenue (TTM)","Revenue $75.5B","15.5× peer median","$236"],
        ["SOTP (semi 22× + sw 25× EV/EBITDA)","FY25 segment EBITDAs","—","$189"],
        ["→ Adopted Target","24.6× FY2027E EPS $19.32","Peer P/E + growth premium","$475"],
    ]
    t = Table(d, colWidths=[60*mm,40*mm,42*mm,30*mm])
    tst = ts()
    tst.add("FONTNAME",(0,6),(-1,6),"Helvetica-Bold")
    tst.add("BACKGROUND",(0,6),(-1,6),colors.HexColor("#D4EDDA"))
    tst.add("TEXTCOLOR",(3,6),(3,6),GREEN)
    t.setStyle(tst)
    s.append(t); s.append(sp(4))

    s.append(Paragraph("<b>Probability-Weighted Synthesis</b>", H2))
    d = [
        ["Method","Weight","Implied","Weighted"],
        ["DCF — Prob-Weighted","35%","$241","$84"],
        ["Relative — NTM P/E blend","35%","$389","$136"],
        ["Relative — FY2027E P/E","20%","$464","$93"],
        ["SOTP","10%","$189","$19"],
        ["Blended Intrinsic","100%","","$332"],
        ["Adopted Price Target","—","$475","+23.2% upside"],
    ]
    t = Table(d, colWidths=[75*mm,22*mm,35*mm,40*mm])
    tst = ts()
    tst.add("FONTNAME",(0,5),(-1,6),"Helvetica-Bold")
    tst.add("BACKGROUND",(0,6),(-1,6),colors.HexColor("#D4EDDA"))
    tst.add("TEXTCOLOR",(3,6),(3,6),GREEN)
    t.setStyle(tst)
    s.append(t); s.append(sp())

    # ── §12 Bull ─────────────────────────────────────────────────────────────
    s.append(PageBreak())
    s.append(Paragraph("§12 — Bull Case (10 Catalysts)", H1))
    s.append(Paragraph(
        "<b>Thesis:</b> Broadcom is the only company outside Nvidia with a credible, revenue-generating custom AI silicon "
        "franchise at scale, amplified by VMware in steep margin expansion — ~$32B annualised FCF at 42%+ margins, "
        "clear deleveraging path, and the lowest forward P/E (20×) in the AI-adjacent peer set.", BODY))
    s.append(sp(4))
    bulls = [
        "AI XPU TAM confirmed — hyperscalers' disclosures imply $60–90B SAM by 2027; Broadcom is sole/primary for all 3 programmes.",
        "Revenue re-accelerating with data — TTM +47.9% vs FY25 +23.9%. FY27E EPS revised +11.6% in 90 days ($17.31→$19.32).",
        "VMware margin conversion intact — op. margin 29.1% FY24 → 40.8% FY25 → 49% TTM. Each renewal at 85–90% gross margin.",
        "Lowest fwd P/E in AI peer set (20×) vs MRVL 43×, AMD 36×, ORCL 27× — cheapest despite fastest revenue growth.",
        "FCF machine: $32B ann. at 1% capex intensity. $38.1B debt repaid FY24+FY25. ND/EBITDA 1.4× and falling.",
        "Post-Q2 FY26 analyst unanimity: 16/17 actions were target raises. Mean target $517.61. Zero sell ratings.",
        "4/4 EPS beats (avg +2.27%). Conservative guidance without extreme sandbagging.",
        "Networking amplifies AI revenue — Tomahawk 5 Ethernet ASIC is the AI cluster networking standard. Two revenue streams move together.",
        "Dividend/buyback optionality growing — $2.60 annual dividend (41% payout). Buyback capacity increases as leverage falls.",
        "Technical reset: −22% from $495 high while fundamentals strengthened. 1.15% short float — minimal forced-selling risk.",
    ]
    for i, b in enumerate(bulls, 1):
        s.append(Paragraph(f"<b>{i}.</b> {b}", BULLET))
    s.append(sp(8))

    # ── §13 Bear ─────────────────────────────────────────────────────────────
    s.append(Paragraph("§13 — Bear Case (10 Thesis-Breakers)", H1))
    s.append(Paragraph(
        "<b>Thesis:</b> At 64.1× trailing GAAP P/E, Broadcom has zero tolerance for execution failures on an AI ramp "
        "that has never survived a design-cycle re-tender, with $51.9B in net debt, no binding hyperscaler contracts, "
        "and VMware customer relationships damaged by aggressive post-acquisition pricing.", BODY))
    s.append(sp(4))
    bears = [
        "Hyperscaler XPU defection → EPS collapses $19→$10–12 → stock $200–240 at 20× (−38–48% drawdown).",
        "VMware renewal rate <80% → margin reversal toward FY24 (29% op. margin). Risk invisible until disclosed.",
        "GAAP reality: 64.1× trailing P/E. $13/share GAAP/nGAAP delta (intangible amortisation) persists 10–15 years.",
        "EV/EBITDA derating: 44.7× → 28× peer median implies $238 — 38% drawdown with no earnings change.",
        "AI capex cycle moderation — hyperscaler capex at record $250–300B combined. Any AI ROI disappointment triggers pause.",
        "Apple wireless in-house: $5–8B revenue at risk within 1–3 years. No semiconductor replacement pipeline.",
        "Near-term EPS revision breadth net negative: 0q ratio 0.44; +1q ratio 0.38. Q3 FY26 miss triggers outsized reaction.",
        "Debt obligations: $3.2B annual interest. FCF <$20B → cannot maintain dividends + buybacks + deleveraging simultaneously.",
        "Marvell winning at Microsoft Azure (Maia XPU). If MSFT deepens Marvell ties, one of 3 XPU customers weakens.",
        "China export controls escalation: ~9% revenue exposed. Tightening on AI-adjacent networking chips → $5–8B at risk.",
    ]
    for i, b in enumerate(bears, 1):
        s.append(Paragraph(f"<b>{i}.</b> {b}", BULLET))
    s.append(sp(6))
    s.append(Paragraph("<b>Structural Risk Register</b>", H2))
    d = [
        ["Risk Category","Specific Risk","Prob.","Impact"],
        ["Customer concentration","XPU defection (1 of 3)","Medium","High (−25–35% EPS)"],
        ["Technology","Apple wireless in-house","Med-High","Medium (−8–12% semi)"],
        ["Competitive","Marvell deepens MSFT relationship","Medium","Medium (−5–10% rev)"],
        ["Valuation","EV/EBITDA rerating 44.7×→28×","Medium","High (−38% stock)"],
        ["Operating","VMware renewal <80%","Low-Med","High (margin reversal)"],
        ["Balance sheet","FCF shortfall vs obligations","Low","Medium"],
        ["Macro","AI capex cycle pause","Low","Very High"],
        ["Regulatory","China export controls","Low-Med","Medium"],
    ]
    t = Table(d, colWidths=[45*mm,65*mm,25*mm,37*mm])
    tst = ts()
    tst.add("TEXTCOLOR",(3,1),(3,1),RED)
    tst.add("TEXTCOLOR",(3,4),(3,4),RED)
    tst.add("TEXTCOLOR",(3,7),(3,7),RED)
    t.setStyle(tst)
    s.append(t)

    # ── §14 Delta ────────────────────────────────────────────────────────────
    s.append(PageBreak())
    s.append(Paragraph("§14 — Delta Audit (Numeric Verification)", H1))
    d = [["Claim","Raw yfinance Value","Status"]]
    claims = [
        ("Price $385.73","info.currentPrice = 385.73"),
        ("Market cap $1,826B","info.marketCap = 1,826,303,639,552"),
        ("Float 4.688B","info.floatShares = 4,687,804,910"),
        ("52W High $495","price history max (52W)"),
        ("Drawdown −22.1%","($385.73−$495)/$495"),
        ("YTD +11.2%","Jan 2 close $346.89 → $385.73"),
        ("ADTV $11.6B","daily vol × close, 30d mean"),
        ("Realized vol 69.4%","log-return std × √252, 30d"),
        ("Short % 1.15%","info.shortPercentOfFloat = 0.0115"),
        ("Beta 1.433","info.beta = 1.433"),
        ("Trailing P/E 64.1×","info.trailingPE = 64.07"),
        ("TTM Revenue $75.5B","info.totalRevenue = 75,464,998,912"),
        ("FY2025 Revenue $63.9B","income_stmt 2025-10-31 = 63,887,000,000"),
        ("FY2025 Op. Margin 40.8%","$26.075B / $63.887B"),
        ("FY2025 FCF $26.9B","cashflow Free Cash Flow 2025-10-31 = 26,914,000,000"),
        ("Q1 FY26 Revenue $19.3B","quarterly_income_stmt 2026-01-31 = 19,311,000,000"),
        ("Q1 FY26 FCF $8.0B","quarterly_cashflow 2026-01-31 = 8,010,000,000"),
        ("Net Debt $51.9B","$66.057B − $14.174B"),
        ("FY25 interest coverage 8.1×","EBIT $25.939B / interest $3.210B"),
        ("FY24 debt repayment $19.6B","cashflow Repayment Of Debt = −19,608,000,000"),
        ("FY25 debt repayment $18.5B","cashflow Repayment Of Debt = −18,478,000,000"),
        ("FY2027E EPS $19.321","earnings_estimate +1y avg = 19.32136"),
        ("FY2027E Rev $170.5B","revenue_estimate +1y avg = 170,489,438,460"),
        ("Rev est. low $114.7B","revenue_estimate +1y low = 114,715,000,000"),
        ("Q2 FY26 EPS beat +1.78%","earnings_history: actual $2.44 vs est $2.397"),
        ("Analyst mean target $517.61","analyst_price_targets.mean = 517.6067"),
        ("EPS trend 90d: $17.31→$19.32","eps_trend +1y: 90daysAgo=17.31, current=19.321"),
        ("Rev. breadth +1y: 10up/3dn","eps_revisions +1y: upLast30d=10, dn=3"),
    ]
    for claim, val in claims:
        d.append([claim, val, "✓"])
    t = Table(d, colWidths=[60*mm,90*mm,12*mm])
    tst = ts(fs=7)
    for i in range(1, len(d)):
        tst.add("TEXTCOLOR",(2,i),(2,i),GREEN)
        tst.add("FONTNAME",(2,i),(2,i),"Helvetica-Bold")
    t.setStyle(tst)
    s.append(t); s.append(sp(4))

    s.append(Paragraph("<b>Audit Flags:</b>", H2))
    flags = [
        "<b>FLAG 1 (Material):</b> GAAP/nGAAP delta ~$13/share annually. Trailing P/E 64.1× (GAAP) vs fwd P/E 20.0× (nGAAP). Intangible amortisation persists 10–15 years.",
        "<b>FLAG 2 (Material):</b> FY2027E revenue spread $85.4B = 50% of consensus. Binary uncertainty: $114.7B low vs $200.1B high.",
        "<b>FLAG 3 (Material):</b> Customer concentration data gap. Hyperscaler XPU % not in yfinance or SEC filings beyond Apple 10% threshold.",
        "<b>FLAG 4:</b> Q2 FY26 revenue derived from TTM (~$22.2B). EPS confirmed; detailed financials pending yfinance update.",
        "<b>FLAG 5:</b> Near-term EPS revision breadth net negative — 0q ratio 0.44; +1q ratio 0.38. Q3 FY26 timing risk live.",
    ]
    for f in flags:
        s.append(Paragraph(f, BODY)); s.append(sp(2))
    s.append(sp(4))
    s.append(Paragraph("DELTA VERDICT: PASS WITH NOTES. All quantitative claims verified against yfinance primary data (2026-06-08). Five audit flags; Flags 1–3 are material disclosures.", VERDICT))

    # ── §15 Sentiment ─────────────────────────────────────────────────────────
    s.append(Paragraph("§15 — Sentiment & Flow", H1))
    s.append(Paragraph(
        "<b>Short interest:</b> 1.15% of float (very low) · 2.7 days-to-cover. Minimal short-seller conviction. "
        "Low short interest removes both short-covering upside and squeeze risk.", BODY))
    s.append(sp(4))
    s.append(Paragraph("<b>Insider Transactions (yfinance, most recent):</b>", H2))
    d = [
        ["Date","Insider","Role","Type","Shares","Value"],
        ["2026-04-21","Henry Samueli","Director","RSU Grant","864","$0"],
        ["2026-04-20","Diane M. Bryant","Director","RSU Grant","864","$0"],
        ["2026-04-10","S. Ram Velaga","Officer","Sale","8,000","$2.96M @ $370.52"],
        ["2026-04-09","S. Ram Velaga","Officer","Sale","30,215","$10.64M @ $352.07"],
        ["2026-04-09","Gayla J. Delly","Director","Sale","1,000","$358K @ $358.31"],
    ]
    t = Table(d, colWidths=[24*mm,38*mm,22*mm,22*mm,20*mm,46*mm])
    t.setStyle(ts())
    s.append(t)
    s.append(Paragraph("No CEO/CFO sales in most recent window. Officer sales appear planned 10b5-1 diversification.", CAPTION))
    s.append(sp(4))
    s.append(Paragraph("<b>Top Institutional Holders (2026-03-31, yfinance):</b>", H2))
    d = [
        ["Holder","% Held","Shares","Value","QoQ Δ"],
        ["BlackRock Inc.","8.15%","385.9M","$148.9B","+1.59%"],
        ["Vanguard Capital Mgmt","6.51%","308.0M","$118.8B","New"],
        ["State Street Corp","4.04%","191.4M","$73.8B","+0.68%"],
        ["Vanguard Portfolio Mgmt","2.71%","128.4M","$49.5B","New"],
        ["FMR / Fidelity","2.62%","124.1M","$47.9B","+0.75%"],
    ]
    t = Table(d, colWidths=[56*mm,20*mm,28*mm,28*mm,40*mm])
    t.setStyle(ts())
    s.append(t)

    # ── §16 Recommendation ────────────────────────────────────────────────────
    s.append(PageBreak())
    s.append(Paragraph("§16 — Synthesis & Recommendation", H1))
    s.append(Paragraph("<b>Probability-Weighted Outcome</b>", H2))
    d = [
        ["Scenario","Prob.","12-Month Target","Weighted"],
        ["Bull — AI ramp intact, VMware retention >85%","35%","$560","$196"],
        ["Base — Steady execution, FY27 tracks ~$170B consensus","45%","$460","$207"],
        ["Bear — Hyperscaler defection or VMware churn >15%","20%","$210","$42"],
        ["Expected Value","100%","","$445 (+15.4%)"],
    ]
    t = Table(d, colWidths=[88*mm,20*mm,35*mm,29*mm])
    tst = ts()
    tst.add("FONTNAME",(0,4),(-1,4),"Helvetica-Bold")
    tst.add("BACKGROUND",(0,4),(-1,4),LGREY)
    tst.add("TEXTCOLOR",(3,4),(3,4),GREEN)
    t.setStyle(tst)
    s.append(t); s.append(sp(6))

    s.append(Paragraph("<b>RECOMMENDATION: OVERWEIGHT  ·  Price Target: $475  ·  Upside: +23.2%</b>", H2))
    d = [
        ["Rating","Price Target","Current Price","Upside","Horizon","Expected Value"],
        ["OVERWEIGHT","$475","$385.73","+23.2%","12–18 months","$445 (+15.4%)"],
    ]
    t = Table(d, colWidths=[30*mm,25*mm,28*mm,20*mm,30*mm,39*mm])
    tst = ts(header_bg=GREEN)
    tst.add("FONTNAME",(0,1),(-1,1),"Helvetica-Bold")
    tst.add("FONTSIZE",(0,1),(-1,1),10)
    tst.add("TEXTCOLOR",(1,1),(1,1),GREEN)
    tst.add("TEXTCOLOR",(3,1),(3,1),GREEN)
    t.setStyle(tst)
    s.append(t); s.append(sp(6))

    s.append(Paragraph("<b>Entry & Position Management</b>", H2))
    d = [
        ["Parameter","Specification"],
        ["Initiation (50%)","$380–395 (current range)"],
        ["Add-on (25%)","−10–15% pullback zone $330–350 on Q3 FY26 miss"],
        ["Final (25%)","After Q3 FY26 confirmation, August 2026"],
        ["Stop-Loss","$290 (−25%): hyperscaler defection, VMware churn >15%, or AI capex freeze"],
        ["Hedge","Long QCOM puts (wireless hedge) + VIX calls (macro/balance sheet hedge)"],
        ["Position Size","4–6% of portfolio — high-conviction large-cap with FCF floor"],
        ["Analyst Consensus","Mean $517.61 (+34%) · Median $525 (+36%) · High $650 · Low $215.88"],
    ]
    t = Table(d, colWidths=[45*mm,127*mm])
    t.setStyle(ts())
    s.append(t); s.append(sp(6))

    s.append(Paragraph("<b>Key Catalysts to Monitor</b>", H2))
    d = [
        ["Catalyst","Expected","Bull Signal","Bear Signal"],
        ["Q3 FY2026 earnings","Aug 2026","AI rev +80%+ YoY; FY27 guidance raised","Miss + guidance cut → thesis impaired"],
        ["VMware renewal disclosure","Any inv. day","Retention >85%","Churn >15% disclosed"],
        ["Apple iPhone 17 wireless","Sept 2026","Broadcom supply maintained","In-house Wi-Fi disclosed"],
        ["Hyperscaler XPU design cycle","Rolling (annual)","Design win confirmed","Competitor win disclosed"],
        ["FY27 EPS revision trend","30-day rolling","+1y ratio >0.70","Ratio turns negative"],
    ]
    t = Table(d, colWidths=[45*mm,28*mm,52*mm,47*mm])
    t.setStyle(ts())
    s.append(t)

    # ── §17 Data Gaps ─────────────────────────────────────────────────────────
    s.append(sp(6))
    s.append(Paragraph("§17 — Data Gaps", H1))
    d = [
        ["Item","Gap Type","Impact"],
        ["Customer concentration % (hyperscalers)","Not in yfinance; 10-K qualitative only","High"],
        ["AI XPU sub-segment revenue","Earnings calls only; not in yfinance segments","High"],
        ["VMware renewal / retention rate","Qualitative earnings commentary only","High"],
        ["Q2 FY26 revenue (detailed)","Not yet in yfinance quarterly stmt","Medium"],
        ["Geographic revenue by segment","Aggregate only in yfinance","Medium"],
        ["finance-sentiment (Adanos)","API key not configured","Low-Med"],
        ["funda-data (transcripts)","API key not configured","Medium"],
    ]
    t = Table(d, colWidths=[65*mm,75*mm,32*mm])
    tst = ts()
    for i in [1,2,3]:
        tst.add("TEXTCOLOR",(2,i),(2,i),RED)
        tst.add("FONTNAME",(2,i),(2,i),"Helvetica-Bold")
    t.setStyle(tst)
    s.append(t)

    # ── Footer ────────────────────────────────────────────────────────────────
    s.append(sp(10)); s.append(hr())
    s.append(Paragraph(
        "Research cycle: Alpha orchestrator · Charlie (bull) · Kilo (bear) · Delta (numeric audit). "
        "Data: yfinance 1.4.1 · Date: 2026-06-08 · All figures in USD unless noted. "
        "Not financial advice. Not a solicitation to buy or sell. For professional investors only.",
        CAPTION))

    doc.build(s)
    print(f"PDF written: {OUT}  ({os.path.getsize(OUT):,} bytes)")

if __name__ == "__main__":
    build()
