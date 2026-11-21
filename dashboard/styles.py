"""
NETGUARD IDS - Styling and UI Components Module
Provides modern SOC cybersecurity design tokens, custom CSS, and reusable HTML widgets.
All HTML helpers use clean_html() to ensure zero leading indentation, preventing Markdown
parsers from misinterpreting HTML as <pre><code> blocks.
"""

def clean_html(html: str) -> str:
    """
    Strips leading and trailing whitespace from every line of an HTML string.
    Crucial for Streamlit: prevents CommonMark from interpreting indented lines (4+ spaces)
    as preformatted code blocks (<pre><code>).
    """
    lines = [line.strip() for line in html.strip().splitlines() if line.strip()]
    return "\n".join(lines)


SOC_THEME_CSS = """
<style>
/* =====================================================================
   NETGUARD IDS - ENTERPRISE CYBERSECURITY SOC THEME
   Palette:
     - Main Background:    #080D18
     - Secondary Panels:   #0D1424
     - Card Background:    #121D30
     - Primary Cyan:       #00D4FF
     - Electric Blue:      #3478F6
     - Cyber Purple:       #8B5CF6
     - Benign Green:       #22C55E
     - Alert Red:          #EF4444
     - Warning Amber:      #F59E0B
     - Primary Text:       #F1F5F9
     - Muted Text:         #94A3B8
     - Subtle Border:      rgba(0, 212, 255, 0.15)
   ===================================================================== */

@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Global Reset & Base Styling */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #F1F5F9;
}

code, pre, .mono {
    font-family: 'JetBrains Mono', monospace !important;
}

/* Main Container Background */
.stApp {
    background: radial-gradient(circle at 15% 15%, #0B162C 0%, #080D18 45%, #050811 100%) !important;
    background-attachment: fixed !important;
    color: #F1F5F9 !important;
}

/* Sidebar Custom Styling */
[data-testid="stSidebar"] {
    background-color: #0D1424 !important;
    border-right: 1px solid rgba(0, 212, 255, 0.12) !important;
    box-shadow: 4px 0 24px rgba(0, 0, 0, 0.4) !important;
}

[data-testid="stSidebar"] > div:first-child {
    background-color: #0D1424 !important;
}

/* Block container padding */
.main .block-container {
    padding-top: 1.8rem !important;
    padding-bottom: 3rem !important;
    max-width: 1380px !important;
}

/* Header bar transparency */
header[data-testid="stHeader"] {
    background: rgba(8, 13, 24, 0.8) !important;
    backdrop-filter: blur(8px) !important;
    border-bottom: 1px solid rgba(0, 212, 255, 0.08) !important;
}

/* Navigation Radio Styling */
[data-testid="stSidebar"] .stRadio > label {
    display: none !important;
}

[data-testid="stSidebar"] .stRadio > div {
    gap: 6px !important;
}

[data-testid="stSidebar"] .stRadio > div > label {
    background: rgba(18, 29, 48, 0.4) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 8px !important;
    padding: 10px 14px !important;
    margin: 2px 0 !important;
    cursor: pointer !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    color: #94A3B8 !important;
    font-weight: 500 !important;
    font-size: 0.92rem !important;
}

[data-testid="stSidebar"] .stRadio > div > label:hover {
    background: rgba(0, 212, 255, 0.08) !important;
    border-color: rgba(0, 212, 255, 0.35) !important;
    color: #F1F5F9 !important;
    transform: translateX(3px);
}

[data-testid="stSidebar"] .stRadio > div > label[data-checked="true"],
[data-testid="stSidebar"] .stRadio > div > label:has(input:checked) {
    background: linear-gradient(90deg, rgba(0, 212, 255, 0.16) 0%, rgba(52, 120, 246, 0.12) 100%) !important;
    border-color: #00D4FF !important;
    box-shadow: 0 0 16px rgba(0, 212, 255, 0.15) !important;
    color: #00D4FF !important;
    font-weight: 600 !important;
}

/* Streamlit Native Metric Overrides - Premium Cybersecurity Card */
[data-testid="stMetric"] {
    background: #121D30 !important;
    border: 1px solid rgba(0, 212, 255, 0.18) !important;
    border-radius: 12px !important;
    padding: 18px 20px !important;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.35) !important;
    position: relative !important;
    overflow: hidden !important;
    transition: transform 0.2s ease, border-color 0.2s ease !important;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-2px) !important;
    border-color: rgba(0, 212, 255, 0.45) !important;
    box-shadow: 0 8px 24px rgba(0, 212, 255, 0.1) !important;
}

[data-testid="stMetricLabel"] {
    color: #94A3B8 !important;
    font-size: 0.78rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
}

[data-testid="stMetricValue"] {
    color: #F1F5F9 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700 !important;
    font-size: 1.85rem !important;
    letter-spacing: -0.02em !important;
}

/* Custom SOC Cards & Panels */
.soc-card {
    background: #121D30;
    border: 1px solid rgba(0, 212, 255, 0.14);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 6px 22px rgba(0, 0, 0, 0.35);
    transition: border-color 0.25s ease, box-shadow 0.25s ease;
}

.soc-card:hover {
    border-color: rgba(0, 212, 255, 0.35);
    box-shadow: 0 8px 28px rgba(0, 212, 255, 0.08);
}

.soc-card-subtle {
    background: rgba(18, 29, 48, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 10px;
    padding: 16px;
    margin-bottom: 14px;
}

/* Pulsing Status Badges */
.pulse-dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    margin-right: 6px;
    vertical-align: middle;
}

.pulse-dot.green {
    background-color: #22C55E;
    box-shadow: 0 0 10px #22C55E;
    animation: pulseGreen 2s infinite;
}

.pulse-dot.red {
    background-color: #EF4444;
    box-shadow: 0 0 10px #EF4444;
    animation: pulseRed 2s infinite;
}

.pulse-dot.amber {
    background-color: #F59E0B;
    box-shadow: 0 0 10px #F59E0B;
    animation: pulseAmber 2s infinite;
}

.pulse-dot.cyan {
    background-color: #00D4FF;
    box-shadow: 0 0 10px #00D4FF;
    animation: pulseCyan 2s infinite;
}

@keyframes pulseGreen {
    0% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }
    70% { box-shadow: 0 0 0 7px rgba(34, 197, 94, 0); }
    100% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
}

@keyframes pulseRed {
    0% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
    70% { box-shadow: 0 0 0 7px rgba(239, 68, 68, 0); }
    100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
}

@keyframes pulseAmber {
    0% { box-shadow: 0 0 0 0 rgba(245, 158, 11, 0.7); }
    70% { box-shadow: 0 0 0 7px rgba(245, 158, 11, 0); }
    100% { box-shadow: 0 0 0 0 rgba(245, 158, 11, 0); }
}

@keyframes pulseCyan {
    0% { box-shadow: 0 0 0 0 rgba(0, 212, 255, 0.7); }
    70% { box-shadow: 0 0 0 7px rgba(0, 212, 255, 0); }
    100% { box-shadow: 0 0 0 0 rgba(0, 212, 255, 0); }
}

/* Badges */
.badge-soc {
    display: inline-flex;
    align-items: center;
    padding: 3px 10px;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    font-family: 'JetBrains Mono', monospace;
}

.badge-green {
    background: rgba(34, 197, 94, 0.12);
    color: #22C55E;
    border: 1px solid rgba(34, 197, 94, 0.35);
}

.badge-red {
    background: rgba(239, 68, 68, 0.14);
    color: #EF4444;
    border: 1px solid rgba(239, 68, 68, 0.4);
}

.badge-cyan {
    background: rgba(0, 212, 255, 0.12);
    color: #00D4FF;
    border: 1px solid rgba(0, 212, 255, 0.35);
}

.badge-amber {
    background: rgba(245, 158, 11, 0.12);
    color: #F59E0B;
    border: 1px solid rgba(245, 158, 11, 0.35);
}

.badge-purple {
    background: rgba(139, 92, 246, 0.12);
    color: #A78BFA;
    border: 1px solid rgba(139, 92, 246, 0.35);
}

/* Warning & Banner Notice */
.soc-banner {
    background: linear-gradient(90deg, rgba(239, 68, 68, 0.1) 0%, rgba(18, 29, 48, 0.8) 100%);
    border-left: 4px solid #EF4444;
    border-top: 1px solid rgba(239, 68, 68, 0.2);
    border-right: 1px solid rgba(239, 68, 68, 0.2);
    border-bottom: 1px solid rgba(239, 68, 68, 0.2);
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 18px;
}

.soc-banner-info {
    background: linear-gradient(90deg, rgba(0, 212, 255, 0.08) 0%, rgba(18, 29, 48, 0.8) 100%);
    border-left: 4px solid #00D4FF;
    border-top: 1px solid rgba(0, 212, 255, 0.2);
    border-right: 1px solid rgba(0, 212, 255, 0.2);
    border-bottom: 1px solid rgba(0, 212, 255, 0.2);
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 18px;
}

.soc-banner-warning {
    background: linear-gradient(90deg, rgba(245, 158, 11, 0.1) 0%, rgba(18, 29, 48, 0.8) 100%);
    border-left: 4px solid #F59E0B;
    border-top: 1px solid rgba(245, 158, 11, 0.2);
    border-right: 1px solid rgba(245, 158, 11, 0.2);
    border-bottom: 1px solid rgba(245, 158, 11, 0.2);
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 18px;
}

/* Streamlit Button Overrides */
.stButton > button {
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.12) 0%, rgba(52, 120, 246, 0.2) 100%) !important;
    color: #F1F5F9 !important;
    border: 1px solid rgba(0, 212, 255, 0.4) !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    padding: 8px 18px !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 2px 10px rgba(0, 212, 255, 0.1) !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.24) 0%, rgba(52, 120, 246, 0.35) 100%) !important;
    border-color: #00D4FF !important;
    color: #FFFFFF !important;
    box-shadow: 0 0 18px rgba(0, 212, 255, 0.3) !important;
    transform: translateY(-1px);
}

.stDownloadButton > button {
    background: linear-gradient(135deg, rgba(34, 197, 94, 0.15) 0%, rgba(0, 212, 255, 0.15) 100%) !important;
    color: #F1F5F9 !important;
    border: 1px solid rgba(34, 197, 94, 0.45) !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    padding: 8px 18px !important;
    box-shadow: 0 2px 12px rgba(34, 197, 94, 0.15) !important;
}

.stDownloadButton > button:hover {
    border-color: #22C55E !important;
    box-shadow: 0 0 20px rgba(34, 197, 94, 0.35) !important;
    transform: translateY(-1px);
}

/* Dataframe & Table Styling */
[data-testid="stDataFrame"] {
    background: #121D30 !important;
    border: 1px solid rgba(0, 212, 255, 0.15) !important;
    border-radius: 10px !important;
    overflow: hidden !important;
}

/* File Uploader */
[data-testid="stFileUploader"] {
    background: #121D30 !important;
    border: 1px dashed rgba(0, 212, 255, 0.35) !important;
    border-radius: 12px !important;
    padding: 16px !important;
    transition: border-color 0.2s ease !important;
}

[data-testid="stFileUploader"]:hover {
    border-color: #00D4FF !important;
}

/* Section Header Bar */
.section-header {
    border-bottom: 1px solid rgba(0, 212, 255, 0.15);
    padding-bottom: 8px;
    margin-bottom: 18px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.section-title {
    font-size: 1.15rem;
    font-weight: 700;
    color: #F1F5F9;
    letter-spacing: -0.01em;
    display: flex;
    align-items: center;
    gap: 8px;
}

.section-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: #00D4FF;
    background: rgba(0, 212, 255, 0.1);
    border: 1px solid rgba(0, 212, 255, 0.25);
    padding: 2px 8px;
    border-radius: 4px;
}

/* Progress bar cyber styling */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #00D4FF 0%, #3478F6 50%, #22C55E 100%) !important;
    border-radius: 4px !important;
}

/* Scrollbar Styling */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}

::-webkit-scrollbar-track {
    background: #080D18;
}

::-webkit-scrollbar-thumb {
    background: #1E293B;
    border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
    background: #00D4FF;
}

/* Expanders */
.streamlit-expanderHeader {
    background: #121D30 !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 8px !important;
    color: #F1F5F9 !important;
}

.streamlit-expanderContent {
    background: rgba(18, 29, 48, 0.6) !important;
    border-left: 1px solid rgba(0, 212, 255, 0.15) !important;
    border-right: 1px solid rgba(0, 212, 255, 0.15) !important;
    border-bottom: 1px solid rgba(0, 212, 255, 0.15) !important;
    border-radius: 0 0 8px 8px !important;
}
</style>
"""

def render_sidebar_header() -> str:
    """Renders the top branding card in the sidebar."""
    return clean_html("""
    <div style="padding: 10px 4px 18px 4px; border-bottom: 1px solid rgba(0, 212, 255, 0.15); margin-bottom: 16px;">
        <div style="display: flex; align-items: center; gap: 12px;">
            <div style="width: 44px; height: 44px; border-radius: 10px; background: linear-gradient(135deg, rgba(0, 212, 255, 0.2) 0%, rgba(52, 120, 246, 0.3) 100%); border: 1.5px solid #00D4FF; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 16px rgba(0, 212, 255, 0.25);">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2L3 7V12C3 17.52 6.84 22.74 12 24C17.16 22.74 21 17.52 21 12V7L12 2Z" fill="url(#shield-grad)" fill-opacity="0.3" stroke="#00D4FF" stroke-width="1.8" stroke-linejoin="round"/>
                    <path d="M12 7V17M12 12H8M12 12H16" stroke="#22C55E" stroke-width="2" stroke-linecap="round"/>
                    <defs>
                        <linearGradient id="shield-grad" x1="3" y1="2" x2="21" y2="24" gradientUnits="userSpaceOnUse">
                            <stop stop-color="#00D4FF"/>
                            <stop offset="1" stop-color="#8B5CF6"/>
                        </linearGradient>
                    </defs>
                </svg>
            </div>
            <div>
                <div style="font-size: 1.15rem; font-weight: 800; letter-spacing: 0.02em; color: #F1F5F9; line-height: 1.2;">NETGUARD <span style="color: #00D4FF;">IDS</span></div>
                <div style="font-size: 0.72rem; color: #94A3B8; font-weight: 500; letter-spacing: 0.06em; text-transform: uppercase;">Network Security Intelligence</div>
            </div>
        </div>
        <div style="margin-top: 14px; display: flex; align-items: center; justify-content: space-between; background: rgba(8, 13, 24, 0.6); padding: 6px 10px; border-radius: 6px; border: 1px solid rgba(255, 255, 255, 0.05);">
            <div style="display: flex; align-items: center;">
                <span class="pulse-dot amber"></span>
                <span style="font-size: 0.72rem; color: #94A3B8; font-weight: 600;">SOC ENGINE</span>
            </div>
            <span class="badge-soc badge-amber">ARMED (OFFLINE)</span>
        </div>
    </div>
    """)

def render_sidebar_footer() -> str:
    """Renders the system specification footer in the sidebar."""
    return clean_html("""
    <div style="padding-top: 16px; border-top: 1px solid rgba(0, 212, 255, 0.12); margin-top: 24px;">
        <div style="background: rgba(18, 29, 48, 0.7); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 8px; padding: 12px; margin-bottom: 12px;">
            <div style="font-size: 0.7rem; color: #64748B; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 6px;">Engine Architecture</div>
            <div style="display: flex; justify-content: space-between; font-size: 0.78rem; margin-bottom: 4px;">
                <span style="color: #94A3B8;">Algorithm</span>
                <span style="color: #00D4FF; font-family: 'JetBrains Mono', monospace; font-weight: 600;">Random Forest</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.78rem; margin-bottom: 4px;">
                <span style="color: #94A3B8;">Estimators</span>
                <span style="color: #F1F5F9; font-family: 'JetBrains Mono', monospace;">100 Trees</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.78rem; margin-bottom: 4px;">
                <span style="color: #94A3B8;">Dimensionality</span>
                <span style="color: #F1F5F9; font-family: 'JetBrains Mono', monospace;">70 Features</span>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.78rem;">
                <span style="color: #94A3B8;">Benchmark Set</span>
                <span style="color: #A78BFA; font-family: 'JetBrains Mono', monospace;">CIC-IDS2017</span>
            </div>
        </div>
        <div style="text-align: center; font-size: 0.68rem; color: #64748B; font-family: 'JetBrains Mono', monospace;">
            STATUS: OFFLINE BENCHMARK • DCN PROJECT
        </div>
    </div>
    """)

def render_top_header(title: str, subtitle: str, badge_text: str = "BENCHMARK: CIC-IDS2017", badge_color: str = "cyan") -> str:
    """Renders an enterprise SOC page header with live date and accurate offline telemetry badge."""
    import datetime
    today_str = datetime.date.today().strftime("%d %b %Y").upper()
    return clean_html(f"""
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid rgba(0, 212, 255, 0.14);">
        <div>
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 4px;">
                <h1 style="font-size: 1.85rem; font-weight: 800; color: #F1F5F9; margin: 0; letter-spacing: -0.02em;">{title}</h1>
                <span class="badge-soc badge-{badge_color}">{badge_text}</span>
            </div>
            <div style="font-size: 0.88rem; color: #94A3B8; font-weight: 400;">{subtitle}</div>
        </div>
        <div style="display: flex; align-items: center; gap: 12px; background: #121D30; border: 1px solid rgba(0, 212, 255, 0.15); padding: 8px 14px; border-radius: 8px;">
            <div style="text-align: right;">
                <div style="font-size: 0.68rem; color: #64748B; font-weight: 700; text-transform: uppercase;">System Date</div>
                <div style="font-size: 0.82rem; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #00D4FF;">{today_str}</div>
            </div>
            <div style="width: 1px; height: 24px; background: rgba(255, 255, 255, 0.1);"></div>
            <div style="display: flex; align-items: center; gap: 6px;">
                <span class="pulse-dot amber"></span>
                <span style="font-size: 0.72rem; color: #F59E0B; font-weight: 700; font-family: 'JetBrains Mono', monospace;">OFFLINE BENCHMARK</span>
            </div>
        </div>
    </div>
    """)

def render_section_header(title: str, tag: str = "") -> str:
    """Renders a styled SOC section header."""
    tag_html = f'<span class="section-tag">{tag}</span>' if tag else ""
    return clean_html(f"""
    <div class="section-header">
        <span class="section-title">{title}</span>
        {tag_html}
    </div>
    """)

def render_warning_banner(message: str, title: str = "NOTICE") -> str:
    """Renders a cybersecurity alert banner."""
    return clean_html(f"""
    <div class="soc-banner">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
            <span class="pulse-dot red"></span>
            <span style="font-size: 0.82rem; font-weight: 800; color: #EF4444; letter-spacing: 0.05em; text-transform: uppercase;">{title}</span>
        </div>
        <div style="font-size: 0.85rem; color: #E2E8F0; line-height: 1.4;">{message}</div>
    </div>
    """)

def render_info_banner(message: str, title: str = "SYSTEM STATUS") -> str:
    """Renders a cybersecurity info banner."""
    return clean_html(f"""
    <div class="soc-banner-info">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
            <span class="pulse-dot cyan"></span>
            <span style="font-size: 0.82rem; font-weight: 800; color: #00D4FF; letter-spacing: 0.05em; text-transform: uppercase;">{title}</span>
        </div>
        <div style="font-size: 0.85rem; color: #CBD5E1; line-height: 1.4;">{message}</div>
    </div>
    """)
