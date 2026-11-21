"""
NETGUARD IDS - Traffic Detection View
Enterprise CSV upload, 70-feature validation pipeline, high-precision batch inference, and threat filtering.
All UI elements use native Streamlit components and clean_html() to prevent Markdown code block leaks.
"""

import streamlit as st
import pandas as pd
import altair as alt
from dashboard.styles import (
    render_top_header,
    render_section_header,
    render_warning_banner,
    render_info_banner,
    clean_html
)
from dashboard.data_loader import (
    load_rf_model,
    load_sample_dataset,
    validate_and_predict,
    get_expected_features
)


def render_traffic_detection():
    """Renders the Traffic Detection view with CSV upload, feature checking, and prediction explorer."""
    st.markdown(
        render_top_header(
            title="TRAFFIC DETECTION & CLASSIFICATION",
            subtitle="Batch Ingestion, 70-Feature Schema Verification & ML Inference",
            badge_text="ENGINE: RANDOM FOREST",
            badge_color="cyan"
        ),
        unsafe_allow_html=True
    )

    model = load_rf_model()
    expected_features = get_expected_features(model)

    # Ingestion Section Header
    st.markdown(
        render_section_header("Network Flow Data Ingestion", "SCHEMA: 70 FEATURES REQUIRED"),
        unsafe_allow_html=True
    )
    st.caption("Upload a structured CSV network capture file. The preprocessor will validate all 70 required statistical flow features and execute deterministic classification via the Random Forest model.")

    upload_col1, upload_col2 = st.columns([3, 1.2])

    with upload_col1:
        uploaded_file = st.file_uploader(
            "Upload Network Traffic CSV",
            type=["csv"],
            help="Select a CSV containing CIC-IDS2017 compliant flow metrics (70 numeric features)."
        )

    with upload_col2:
        st.write("**Quick Demo Benchmark**")
        use_sample = st.button("⚡ Load Sample CSV (100 Flows)", use_container_width=True)
        
        # Sample file download option
        sample_df = load_sample_dataset()
        csv_sample_bytes = sample_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇ Download Sample Template",
            data=csv_sample_bytes,
            file_name="netguard_sample_template.csv",
            mime="text/csv",
            use_container_width=True
        )

    # Determine data source
    input_df = None
    source_name = None

    if uploaded_file is not None:
        try:
            input_df = pd.read_csv(uploaded_file)
            source_name = uploaded_file.name
        except Exception as e:
            st.error(f"Error reading uploaded CSV file: {e}")
    elif use_sample:
        input_df = sample_df.copy()
        source_name = "sample_upload.csv (Pre-validated Benchmark)"

    # If no data loaded yet, show guidance & schema specifications
    if input_df is None:
        st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
        st.markdown(
            render_section_header("Required Feature Schema Specifications", "70 NETWORK METRICS"),
            unsafe_allow_html=True
        )
        st.caption("The trained Random Forest model requires exact compliance with 70 flow telemetry features extracted from network sessions.")

        st.markdown(
            clean_html("""
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; margin-top: 10px;">
                <div class="soc-card-subtle">
                    <div style="color: #00D4FF; font-weight: 700; font-size: 0.85rem; margin-bottom: 4px;">Session Dynamics & Duration</div>
                    <div style="font-size: 0.78rem; color: #94A3B8;">Destination Port, Flow Duration, Total Fwd/Bwd Packets, Flow Bytes/s, Flow Packets/s.</div>
                </div>
                <div class="soc-card-subtle">
                    <div style="color: #3478F6; font-weight: 700; font-size: 0.85rem; margin-bottom: 4px;">Packet Length Metrics</div>
                    <div style="font-size: 0.78rem; color: #94A3B8;">Fwd/Bwd Packet Length Max, Min, Mean, Std, Average Packet Size, Segment Sizes.</div>
                </div>
                <div class="soc-card-subtle">
                    <div style="color: #8B5CF6; font-weight: 700; font-size: 0.85rem; margin-bottom: 4px;">Inter-Arrival Times (IAT)</div>
                    <div style="font-size: 0.78rem; color: #94A3B8;">Flow IAT Mean/Std/Max/Min, Fwd IAT Total/Mean/Max, Bwd IAT Total/Mean/Max.</div>
                </div>
                <div class="soc-card-subtle">
                    <div style="color: #22C55E; font-weight: 700; font-size: 0.85rem; margin-bottom: 4px;">TCP Flags & Window Stats</div>
                    <div style="font-size: 0.78rem; color: #94A3B8;">FIN, SYN, RST, PSH, ACK, URG Flag Counts, Header Lengths, Init_Win_bytes.</div>
                </div>
            </div>
            """),
            unsafe_allow_html=True
        )
        return

    # Process and Predict
    st.markdown(
        clean_html(f"""
        <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 14px; margin-bottom: 16px;">
            <div style="font-size: 0.95rem; font-weight: 700; color: #F1F5F9;">
                Active Ingestion File: <span style="color: #00D4FF; font-family: 'JetBrains Mono', monospace;">{source_name}</span>
            </div>
            <span class="badge-soc badge-cyan">{len(input_df):,} RECORDS INGESTED</span>
        </div>
        """),
        unsafe_allow_html=True
    )

    with st.spinner("Executing Random Forest feature validation and threat inference..."):
        results_df, summary, err = validate_and_predict(input_df, model)

    if err:
        st.markdown(render_warning_banner(err, title="INGESTION SCHEMA ERROR"), unsafe_allow_html=True)
        return

    # Post-Prediction KPI Summary: Using native st.metric for 100% reliable rendering without HTML leaking
    k1, k2, k3, k4, k5 = st.columns(5)
    with k1:
        st.metric(
            label="Processed Records",
            value=f"{summary['total']:,}"
        )
        st.caption("100% Ingestion Complete")
    with k2:
        st.metric(
            label="Benign Flows",
            value=f"{summary['benign']:,}"
        )
        st.caption(f"{(summary['benign']/summary['total'])*100:.1f}% Verified Safe")
    with k3:
        st.metric(
            label="Attack Flows",
            value=f"{summary['attack']:,}"
        )
        st.caption(f"{summary['attack_pct']:.1f}% Threat Infiltration")
    with k4:
        st.metric(
            label="Threat Ratio",
            value=f"{summary['attack_pct']:.2f}%"
        )
        st.caption("Attack Volume Density")
    with k5:
        st.metric(
            label="Avg Attack Confidence",
            value=f"{summary['avg_confidence']:.1f}%"
        )
        st.caption("Ensemble Probability")

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

    # Threat Summary Banner
    if summary["attack"] > 0:
        st.markdown(
            render_warning_banner(
                f"<b>SECURITY ALERT:</b> Detected {summary['attack']} malicious network flow(s) in this capture session. "
                f"Immediate quarantine or IP firewall blocking recommended for high-confidence flows.",
                title=f"THREATS DETECTED ({summary['attack']})"
            ),
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            render_info_banner(
                "All analyzed network flows matched verified benign baselines. No intrusive traffic or anomalies detected in this batch.",
                title="ALL FLOWS BENIGN"
            ),
            unsafe_allow_html=True
        )

    # Interactive Filter and Search Controls
    st.markdown(
        render_section_header("Detection Results Explorer", "INTERACTIVE TRIAGE"),
        unsafe_allow_html=True
    )

    ctrl1, ctrl2, ctrl3 = st.columns([1.5, 2, 1.5])

    with ctrl1:
        filter_option = st.selectbox(
            "Filter Classification",
            ["All Records", "Attacks Only (ATTACK)", "Benign Only (BENIGN)", "High-Confidence Threats (>80%)"]
        )

    with ctrl2:
        search_query = st.text_input(
            "Search Records",
            placeholder="Search by Destination Port (e.g. 80, 443, 21)..."
        )

    with ctrl3:
        suspicious_only = st.checkbox("Show Only Suspicious (Confidence > 50%)", value=False)

    # Apply filters
    filtered_df = results_df.copy()

    if filter_option == "Attacks Only (ATTACK)":
        filtered_df = filtered_df[filtered_df["Prediction"] == "ATTACK"]
    elif filter_option == "Benign Only (BENIGN)":
        filtered_df = filtered_df[filtered_df["Prediction"] == "BENIGN"]
    elif filter_option == "High-Confidence Threats (>80%)":
        filtered_df = filtered_df[(filtered_df["Prediction"] == "ATTACK") & (filtered_df["Attack Confidence (%)"] >= 80)]

    if suspicious_only:
        filtered_df = filtered_df[filtered_df["Attack Confidence (%)"] > 50]

    if search_query.strip():
        q = search_query.strip()
        if "Destination Port" in filtered_df.columns:
            filtered_df = filtered_df[
                filtered_df["Destination Port"].astype(str).str.contains(q, case=False, na=False) |
                filtered_df["Record #"].astype(str).str.contains(q, case=False, na=False)
            ]

    # Display primary columns in table
    primary_display_cols = [
        "Record #",
        "Destination Port",
        "Flow Duration",
        "Prediction",
        "Attack Confidence (%)",
        "Threat Status"
    ]
    
    available_cols = [c for c in primary_display_cols if c in filtered_df.columns]

    st.write(f"Showing **{len(filtered_df):,}** of **{len(results_df):,}** total records")
    
    # Streamlit dataframe with custom column config for progress bars
    st.dataframe(
        filtered_df[available_cols],
        use_container_width=True,
        hide_index=True,
        column_config={
            "Prediction": st.column_config.TextColumn(
                "Classification",
                help="Random Forest predicted traffic category"
            ),
            "Attack Confidence (%)": st.column_config.ProgressColumn(
                "Attack Confidence (%)",
                help="Model attack probability estimate",
                format="%.1f%%",
                min_value=0,
                max_value=100
            ),
            "Threat Status": st.column_config.TextColumn(
                "Threat Assessment",
                help="Categorized SOC risk level"
            )
        }
    )

    # Download Button for Results
    csv_out = results_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇ Download Enriched Detection Results (CSV)",
        data=csv_out,
        file_name="netguard_ids_detection_results.csv",
        mime="text/csv",
        use_container_width=False
    )

    # Batch Analytics Visuals
    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
    vis_col1, vis_col2 = st.columns([1, 1])

    with vis_col1:
        st.markdown(
            render_section_header("Batch Threat Breakdown", "COUNT"),
            unsafe_allow_html=True
        )
        batch_summary_df = pd.DataFrame({
            "Traffic Type": ["BENIGN", "ATTACK"],
            "Records": [summary["benign"], summary["attack"]]
        })

        b_chart = alt.Chart(batch_summary_df).mark_bar(cornerRadiusTopLeft=5, cornerRadiusTopRight=5).encode(
            x=alt.X("Traffic Type:N", title="Predicted Class", axis=alt.Axis(labelColor="#CBD5E1", titleColor="#94A3B8", labelAngle=0)),
            y=alt.Y("Records:Q", title="Flow Count", axis=alt.Axis(labelColor="#CBD5E1", titleColor="#94A3B8", gridColor="rgba(255,255,255,0.06)")),
            color=alt.Color(
                "Traffic Type:N",
                scale=alt.Scale(domain=["BENIGN", "ATTACK"], range=["#22C55E", "#EF4444"]),
                legend=None
            ),
            tooltip=["Traffic Type", "Records"]
        ).properties(height=220).configure_view(strokeWidth=0)

        st.altair_chart(b_chart, use_container_width=True)

    with vis_col2:
        st.markdown(
            render_section_header("Attack Confidence Distribution", "PROBABILITY SPREAD"),
            unsafe_allow_html=True
        )

        conf_hist = alt.Chart(results_df).mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3).encode(
            x=alt.X("Attack Confidence (%):Q", bin=alt.Bin(maxbins=15), title="Threat Confidence (%)", axis=alt.Axis(labelColor="#CBD5E1", titleColor="#94A3B8")),
            y=alt.Y("count()", title="Flow Records", axis=alt.Axis(labelColor="#CBD5E1", titleColor="#94A3B8", gridColor="rgba(255,255,255,0.06)")),
            color=alt.value("#8B5CF6"),
            tooltip=["count()"]
        ).properties(height=220).configure_view(strokeWidth=0)

        st.altair_chart(conf_hist, use_container_width=True)
