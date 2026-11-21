"""
NETGUARD IDS - Attack Analysis View
Detailed security analytics, verified confusion matrix evaluation, and SOC operational impact analysis.
All UI elements use native Streamlit components and clean_html() to prevent Markdown code block leaks.
"""

from pathlib import Path
import streamlit as st
import pandas as pd
import altair as alt
from dashboard.styles import (
    render_top_header,
    render_section_header,
    render_info_banner,
    clean_html
)
from dashboard.data_loader import load_cached_metrics


def render_attack_analysis():
    """Renders the Attack Analysis view with verified test metrics and SOC impact deep-dive."""
    metrics = load_cached_metrics()

    # Page Header (Strictly shows OFFLINE BENCHMARK)
    st.markdown(
        render_top_header(
            title="ATTACK DETECTION & CONFUSION MATRIX ANALYTICS",
            subtitle="Ground-Truth Security Benchmark on 504,160 Test Flows",
            badge_text="BINARY CLASSIFICATION",
            badge_color="red"
        ),
        unsafe_allow_html=True
    )

    # Note on Binary Classification
    st.markdown(
        render_info_banner(
            "<b>Binary Classification Standard:</b> NETGUARD IDS classifies flows strictly into <b>BENIGN</b> and <b>ATTACK</b> categories. "
            "In strict accordance with academic rigor, individual sub-attack type distributions are not fabricated, ensuring verified ground-truth reliability.",
            title="METHODOLOGY INTEGRITY"
        ),
        unsafe_allow_html=True
    )

    # Confusion Matrix 4 KPI Cards (Native st.metric for 100% reliable rendering without HTML leaking)
    st.markdown(
        render_section_header("Confusion Matrix Key Indicators", "TEST SPLIT (20% EVALUATION)"),
        unsafe_allow_html=True
    )

    tp = metrics["tp"]
    tn = metrics["tn"]
    fp = metrics["fp"]
    fn = metrics["fn"]

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            label="True Positives (TP)",
            value=f"{tp:,}",
            help="Attacks Correctly Intercepted"
        )
        st.caption("Attacks Correctly Intercepted")

    with c2:
        st.metric(
            label="True Negatives (TN)",
            value=f"{tn:,}",
            help="Benign Traffic Correctly Allowed"
        )
        st.caption("Benign Traffic Correctly Allowed")

    with c3:
        st.metric(
            label="False Positives (FP)",
            value=f"{fp:,}",
            help="Benign Mistakenly Flagged"
        )
        st.caption("False Alarm Rate: 0.09%")

    with c4:
        st.metric(
            label="False Negatives (FN)",
            value=f"{fn:,}",
            help="Attacks Missed / Evasion"
        )
        st.caption("Miss Rate: 0.20%")

    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

    # Visual Confusion Matrix + Detection Effectiveness
    m_col1, m_col2 = st.columns([1.2, 1])

    with m_col1:
        st.markdown(
            render_section_header("Visual Confusion Matrix Heatmap", "VERIFIED MATRIX"),
            unsafe_allow_html=True
        )

        dark_cm_path = Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "confusion_matrix_dark.png"
        reg_cm_path = Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "confusion_matrix.png"

        if dark_cm_path.exists():
            st.image(str(dark_cm_path), use_container_width=True)
        elif reg_cm_path.exists():
            st.image(str(reg_cm_path), use_container_width=True)
        else:
            cm_df = pd.DataFrame([
                {"Actual": "BENIGN", "Predicted": "BENIGN", "Count": tn, "Label": f"TN: {tn:,}"},
                {"Actual": "BENIGN", "Predicted": "ATTACK", "Count": fp, "Label": f"FP: {fp:,}"},
                {"Actual": "ATTACK", "Predicted": "BENIGN", "Count": fn, "Label": f"FN: {fn:,}"},
                {"Actual": "ATTACK", "Predicted": "ATTACK", "Count": tp, "Label": f"TP: {tp:,}"}
            ])
            heatmap = alt.Chart(cm_df).mark_rect().encode(
                x=alt.X("Predicted:N", title="Predicted Label"),
                y=alt.Y("Actual:N", title="Actual Label"),
                color=alt.Color("Count:Q", scale=alt.Scale(scheme="blues")),
                tooltip=["Actual", "Predicted", "Count"]
            ).properties(height=260)
            st.altair_chart(heatmap, use_container_width=True)

    with m_col2:
        st.markdown(
            render_section_header("Detection Effectiveness Ratios", "SOC TELEMETRY"),
            unsafe_allow_html=True
        )

        # Real visual progress indicators using native Streamlit
        st.write(f"**Detection Rate (Sensitivity / Recall):** `{metrics['recall']*100:.2f}%`")
        st.progress(float(metrics["recall"]), text=f"84,975 of 85,148 attacks intercepted")

        st.write(f"**Specificity (True Negative Rate):** `{metrics['specificity']*100:.2f}%`")
        st.progress(float(metrics["specificity"]), text=f"418,634 of 419,012 benign flows verified")

        st.write(f"**False Alarm Rate (Fall-out / FPR):** `{metrics['false_alarm_rate']*100:.2f}%`")
        st.progress(float(min(metrics["false_alarm_rate"] * 10, 1.0)), text=f"Only 378 false alarms across 419k flows")

        st.write(f"**Miss Rate (False Negative Rate / FNR):** `{metrics['miss_rate']*100:.2f}%`")
        st.progress(float(min(metrics["miss_rate"] * 10, 1.0)), text=f"Only 173 evasions across 85k attack sessions")

    # Detailed Conceptual and Operational Breakdown
    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
    st.markdown(
        render_section_header("SOC Triage: Detailed Error Analysis & Operational Meaning", "THEORETICAL & APPLIED VIVA GUIDE"),
        unsafe_allow_html=True
    )

    st.markdown(
        clean_html("""
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 14px;">
            <div class="soc-card-subtle" style="border-left: 3px solid #22C55E;">
                <div style="color: #22C55E; font-weight: 700; font-size: 0.92rem; margin-bottom: 6px;">True Positive (TP) — 84,975</div>
                <div style="font-size: 0.82rem; color: #E2E8F0; line-height: 1.5;">
                    <b>Definition:</b> An attack flow was correctly identified by the Random Forest classifier.<br>
                    <b>SOC Context:</b> These represent successful cyber defense actions where malicious intrusions (such as DoS, PortScan, or Brute Force) were intercepted before compromising host resources.
                </div>
            </div>

            <div class="soc-card-subtle" style="border-left: 3px solid #00D4FF;">
                <div style="color: #00D4FF; font-weight: 700; font-size: 0.92rem; margin-bottom: 6px;">True Negative (TN) — 418,634</div>
                <div style="font-size: 0.82rem; color: #E2E8F0; line-height: 1.5;">
                    <b>Definition:</b> Legitimate benign traffic was correctly classified as normal network flow.<br>
                    <b>SOC Context:</b> Legitimate user activities (HTTPS browsing, DNS lookups, file transfers) pass through uninterrupted without causing service disruptions.
                </div>
            </div>

            <div class="soc-card-subtle" style="border-left: 3px solid #F59E0B;">
                <div style="color: #F59E0B; font-weight: 700; font-size: 0.92rem; margin-bottom: 6px;">False Positive (FP) — 378 (0.09%)</div>
                <div style="font-size: 0.82rem; color: #E2E8F0; line-height: 1.5;">
                    <b>Definition:</b> Benign network traffic was incorrectly flagged as an attack.<br>
                    <b>SOC Impact:</b> Causes "Alert Fatigue" for SOC operators. At <b>0.09%</b>, NETGUARD IDS maintains an exceptionally low false alarm rate, drastically reducing operator overhead.
                </div>
            </div>

            <div class="soc-card-subtle" style="border-left: 3px solid #EF4444;">
                <div style="color: #EF4444; font-weight: 700; font-size: 0.92rem; margin-bottom: 6px;">False Negative (FN) — 173 (0.20%)</div>
                <div style="font-size: 0.82rem; color: #E2E8F0; line-height: 1.5;">
                    <b>Definition:</b> A malicious attack was misclassified as benign and slipped past the classifier.<br>
                    <b>SOC Impact:</b> Represents breach risk. With only 173 misses out of 85,148 attacks, our 100-tree ensemble delivers an extraordinary <b>99.80% interception rate</b>.
                </div>
            </div>
        </div>
        """),
        unsafe_allow_html=True
    )
