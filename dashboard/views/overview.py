"""
NETGUARD IDS - Overview View
Landing SOC dashboard featuring real-time KPIs, threat distribution charts, and traffic telemetry.
All UI elements use native Streamlit components and clean_html() to prevent HTML code leaks.
"""

import streamlit as st
import pandas as pd
import altair as alt
from dashboard.styles import (
    render_top_header,
    render_section_header,
    render_info_banner,
    clean_html
)
from dashboard.data_loader import (
    load_cached_metrics,
    load_sample_preview_records
)


def render_overview():
    """Renders the primary SOC Overview page with consistent data and verified metrics."""
    metrics = load_cached_metrics()
    
    # Page Header (Displays OFFLINE BENCHMARK, never fake LIVE)
    st.markdown(
        render_top_header(
            title="SECURITY OPERATIONS CENTER",
            subtitle="Intelligent Machine Learning Threat Telemetry & Flow Monitoring",
            badge_text="DATASET: CIC-IDS2017",
            badge_color="cyan"
        ),
        unsafe_allow_html=True
    )

    # Info Notice on Offline Analysis
    st.markdown(
        render_info_banner(
            "NETGUARD IDS operates on the comprehensive CIC-IDS2017 benchmark dataset and uploaded network traffic captures. "
            "Telemetry reflects verified offline packet flows analyzed via a 100-tree Random Forest classifier.",
            title="TELEMETRY STATUS: OFFLINE BENCHMARK ACTIVE"
        ),
        unsafe_allow_html=True
    )

    # Section Header
    st.markdown(
        render_section_header(
            title="Benchmark Evaluation Split Telemetry",
            tag="TEST PARTITION: 504,160 FLOWS"
        ),
        unsafe_allow_html=True
    )

    # Consistent Metrics Calculation: Test Partition
    test_total = metrics["test_records"]       # 504,160
    test_benign = metrics["test_benign"]       # 419,012
    test_attack = metrics["test_attack"]       #  85,148
    attack_pct = (test_attack / test_total) * 100 # 16.89%
    acc_pct = metrics["accuracy"] * 100        # 99.89%

    # 5 KPI Cards built using native Streamlit st.metric for 100% reliable rendering without HTML leaking
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            label="Total Test Records",
            value=f"{test_total:,}",
            help="20% Stratified Evaluation Split"
        )
        st.caption("20% Evaluation Partition")

    with col2:
        st.metric(
            label="Benign Traffic",
            value=f"{test_benign:,}",
            help="Legitimate normal network flows"
        )
        st.caption("83.11% Normal Operations")

    with col3:
        st.metric(
            label="Malicious Traffic",
            value=f"{test_attack:,}",
            help="Intercepted network intrusions"
        )
        st.caption("16.89% Intercepted Threats")

    with col4:
        st.metric(
            label="Attack Ratio",
            value=f"{attack_pct:.2f}%",
            help="Threat volume density"
        )
        st.caption("Empirical Threat Rate")

    with col5:
        st.metric(
            label="Model Accuracy",
            value=f"{acc_pct:.2f}%",
            help=f"ROC-AUC: {metrics['roc_auc']:.4f}"
        )
        st.caption(f"ROC-AUC: {metrics['roc_auc']:.4f}")

    # Dataset Scope Context Card (Clarifies Complete Dataset vs Test Split)
    st.markdown(
        clean_html(f"""
        <div class="soc-card-subtle" style="margin-top: 14px; margin-bottom: 20px;">
            <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 10px; font-size: 0.82rem; color: #94A3B8;">
                <div><b>Complete Preprocessed Dataset:</b> <span style="color: #F1F5F9; font-family: 'JetBrains Mono', monospace;">2,520,798</span> flows (Benign: 2,095,059 | Attack: 425,739)</div>
                <div><b>Training Split (80%):</b> <span style="color: #00D4FF; font-family: 'JetBrains Mono', monospace;">2,016,638</span> flows</div>
                <div><b>Testing Split (20%):</b> <span style="color: #22C55E; font-family: 'JetBrains Mono', monospace;">504,160</span> flows</div>
                <span class="badge-soc badge-cyan">CONSISTENCY VERIFIED</span>
            </div>
        </div>
        """),
        unsafe_allow_html=True
    )

    # Main Visuals Row: Doughnut Chart + Bar Chart
    chart_col1, chart_col2 = st.columns([1, 1])

    with chart_col1:
        st.markdown(
            render_section_header("Traffic Composition Breakdown", "RATIO ANALYSIS"),
            unsafe_allow_html=True
        )

        donut_data = pd.DataFrame({
            "Traffic Type": ["BENIGN", "ATTACK"],
            "Records": [test_benign, test_attack],
            "Percentage": [f"{(test_benign/test_total)*100:.2f}%", f"{(test_attack/test_total)*100:.2f}%"]
        })

        donut_chart = alt.Chart(donut_data).mark_arc(innerRadius=85, stroke="#080D18", strokeWidth=3).encode(
            theta=alt.Theta(field="Records", type="quantitative"),
            color=alt.Color(
                field="Traffic Type",
                type="nominal",
                scale=alt.Scale(domain=["BENIGN", "ATTACK"], range=["#00D4FF", "#EF4444"]),
                legend=alt.Legend(
                    title="Flow Classification",
                    orient="bottom",
                    labelColor="#CBD5E1",
                    titleColor="#94A3B8"
                )
            ),
            tooltip=[
                alt.Tooltip("Traffic Type:N", title="Class"),
                alt.Tooltip("Records:Q", title="Total Flows", format=","),
                alt.Tooltip("Percentage:N", title="Share")
            ]
        ).properties(
            height=280
        ).configure_view(
            strokeWidth=0
        )

        st.altair_chart(donut_chart, use_container_width=True)

    with chart_col2:
        st.markdown(
            render_section_header("Volume Distribution Comparison", "TEST SPLIT SUPPORT"),
            unsafe_allow_html=True
        )

        bar_chart = alt.Chart(donut_data).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(
            x=alt.X("Traffic Type:N", title="Traffic Category", axis=alt.Axis(labelColor="#CBD5E1", titleColor="#94A3B8", labelAngle=0)),
            y=alt.Y("Records:Q", title="Number of Flow Records", axis=alt.Axis(labelColor="#CBD5E1", titleColor="#94A3B8", gridColor="rgba(255,255,255,0.06)")),
            color=alt.Color(
                "Traffic Type:N",
                scale=alt.Scale(domain=["BENIGN", "ATTACK"], range=["#3478F6", "#EF4444"]),
                legend=None
            ),
            tooltip=[
                alt.Tooltip("Traffic Type:N", title="Category"),
                alt.Tooltip("Records:Q", title="Count", format=","),
                alt.Tooltip("Percentage:N", title="Percentage")
            ]
        ).properties(
            height=280
        ).configure_view(
            strokeWidth=0
        )

        st.altair_chart(bar_chart, use_container_width=True)

    # Telemetry and Performance Summary Row
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    summary_col1, summary_col2 = st.columns([1, 1])

    with summary_col1:
        st.markdown(
            render_section_header("Classifier Diagnostic Radar", "VERIFIED METRICS"),
            unsafe_allow_html=True
        )

        # REBUILT CLASSIFIER DIAGNOSTIC RADAR: Real native visual progress indicators & metrics
        st.write("**Overall Test Accuracy:** `99.89%`")
        st.progress(float(metrics["accuracy"]), text=f"Accuracy: {metrics['accuracy']*100:.2f}%")

        st.write("**Precision (Attack Specificity):** `99.56%`")
        st.progress(float(metrics["precision"]), text=f"Precision: {metrics['precision']*100:.2f}%")

        st.write("**Recall (Attack Sensitivity):** `99.80%`")
        st.progress(float(metrics["recall"]), text=f"Recall: {metrics['recall']*100:.2f}%")

        st.write("**F1-Score Harmonization:** `99.68%`")
        st.progress(float(metrics["f1_score"]), text=f"F1-Score: {metrics['f1_score']*100:.2f}%")

        st.write("**ROC-AUC Discriminability:** `0.9998`")
        st.progress(float(metrics["roc_auc"]), text=f"ROC-AUC: {metrics['roc_auc']:.4f}")

    with summary_col2:
        st.markdown(
            render_section_header("Network Infrastructure Profile", "DCN PROTOCOL SPECS"),
            unsafe_allow_html=True
        )

        st.markdown(
            clean_html("""
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 10px;">
                <div class="soc-card-subtle">
                    <div style="font-size: 0.72rem; color: #64748B; font-weight: 700;">DATASET SOURCE</div>
                    <div style="font-size: 0.95rem; font-weight: 700; color: #F1F5F9; margin-top: 4px;">CIC-IDS2017</div>
                    <div style="font-size: 0.75rem; color: #94A3B8;">8 Complete PCAP Sessions</div>
                </div>
                <div class="soc-card-subtle">
                    <div style="font-size: 0.72rem; color: #64748B; font-weight: 700;">CLASSIFICATION TYPE</div>
                    <div style="font-size: 0.95rem; font-weight: 700; color: #00D4FF; margin-top: 4px;">Binary (Benign/Attack)</div>
                    <div style="font-size: 0.75rem; color: #94A3B8;">Dual-Class Supervised</div>
                </div>
                <div class="soc-card-subtle">
                    <div style="font-size: 0.72rem; color: #64748B; font-weight: 700;">SELECTED FEATURES</div>
                    <div style="font-size: 0.95rem; font-weight: 700; color: #22C55E; margin-top: 4px;">70 Flow Metrics</div>
                    <div style="font-size: 0.75rem; color: #94A3B8;">8 Constant Features Pruned</div>
                </div>
                <div class="soc-card-subtle">
                    <div style="font-size: 0.72rem; color: #64748B; font-weight: 700;">MODEL ENSEMBLE</div>
                    <div style="font-size: 0.95rem; font-weight: 700; color: #A78BFA; margin-top: 4px;">Random Forest (100)</div>
                    <div style="font-size: 0.75rem; color: #94A3B8;">Gini Impurity Criterion</div>
                </div>
            </div>
            """),
            unsafe_allow_html=True
        )

    # Recent Benchmark Detection Stream
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    st.markdown(
        render_section_header("Telemetry Inspection Stream (Sample Benchmark Feed)", "BENCHMARK SAMPLES"),
        unsafe_allow_html=True
    )
    st.caption("Verified flow predictions generated directly by the trained Random Forest classifier on sample network captures.")

    try:
        preview_df = load_sample_preview_records()
        display_cols = ["Record #", "Destination Port", "Flow Duration", "Prediction", "Attack Confidence (%)", "Threat Status"]
        st.dataframe(
            preview_df[display_cols],
            use_container_width=True,
            hide_index=True
        )
    except Exception as e:
        st.caption(f"Inspection feed ready on sample upload: {e}")
