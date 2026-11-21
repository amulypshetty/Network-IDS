"""
NETGUARD IDS - Live Monitor View
Enterprise SOC Telemetry Console with clear indicators of offline status and future real-time capture architecture.
All HTML elements are cleaned with clean_html() to prevent Markdown code block leaks.
"""

import streamlit as st
import pandas as pd
import altair as alt
from dashboard.styles import (
    render_top_header,
    render_warning_banner,
    render_section_header,
    clean_html
)
from dashboard.data_loader import load_cached_metrics, load_sample_dataset


def render_live_monitor():
    """Renders the Live Monitor page with explicit offline transparency and architecture roadmap."""
    metrics = load_cached_metrics()

    # Page Header (Strictly shows OFFLINE BENCHMARK)
    st.markdown(
        render_top_header(
            title="REAL-TIME TELEMETRY & LIVE MONITOR",
            subtitle="Network Flow Ingestion Pipeline & Sensor Node Telemetry",
            badge_text="SENSOR STATUS: STANDBY (OFFLINE)",
            badge_color="amber"
        ),
        unsafe_allow_html=True
    )

    # CRITICAL ACCURACY REQUIREMENT: Explicit Live Sniffing Disclaimer
    st.markdown(
        render_warning_banner(
            "<b>LIVE PACKET CAPTURE: NOT CONNECTED (OFFLINE BENCHMARK MODE)</b><br>"
            "Live raw socket packet sniffing via <code>libpcap</code> or <code>Scapy</code> is currently deactivated. "
            "NETGUARD IDS operates strictly in deterministic offline verification mode using the preprocessed CIC-IDS2017 flow dataset. "
            "Fabricated alerts and synthetic live packets are explicitly suppressed to maintain operational integrity.",
            title="OFFLINE PROTOCOL ACTIVE"
        ),
        unsafe_allow_html=True
    )

    # Sensor Node Status Cards
    st.markdown(
        render_section_header("SOC Sensor Node Grid", "HARDWARE TELEMETRY"),
        unsafe_allow_html=True
    )

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        st.markdown(
            clean_html("""
            <div class="soc-card-subtle" style="border-left: 3px solid #F59E0B;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 0.75rem; color: #94A3B8; font-weight: 700;">SENSOR-01: GATEWAY DMZ</span>
                    <span class="badge-soc badge-amber">STANDBY</span>
                </div>
                <div style="font-size: 1.1rem; font-weight: 700; color: #F1F5F9; margin-top: 6px;">eth0 (Promiscuous)</div>
                <div style="font-size: 0.72rem; color: #64748B; margin-top: 4px;">Packet Sniffer: Offline</div>
            </div>
            """),
            unsafe_allow_html=True
        )

    with s2:
        st.markdown(
            clean_html("""
            <div class="soc-card-subtle" style="border-left: 3px solid #00D4FF;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 0.75rem; color: #94A3B8; font-weight: 700;">SENSOR-02: BENCHMARK REPLAY</span>
                    <span class="badge-soc badge-cyan">READY</span>
                </div>
                <div style="font-size: 1.1rem; font-weight: 700; color: #F1F5F9; margin-top: 6px;">CICFlowMeter Ingest</div>
                <div style="font-size: 0.72rem; color: #64748B; margin-top: 4px;">Flow Replay: Available</div>
            </div>
            """),
            unsafe_allow_html=True
        )

    with s3:
        st.markdown(
            clean_html("""
            <div class="soc-card-subtle" style="border-left: 3px solid #EF4444;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 0.75rem; color: #94A3B8; font-weight: 700;">SENSOR-03: INTERNAL LAN</span>
                    <span class="badge-soc badge-red">DISCONNECTED</span>
                </div>
                <div style="font-size: 1.1rem; font-weight: 700; color: #F1F5F9; margin-top: 6px;">tap0 (Mirror Port)</div>
                <div style="font-size: 0.72rem; color: #64748B; margin-top: 4px;">Hardware TAP: Inactive</div>
            </div>
            """),
            unsafe_allow_html=True
        )

    with s4:
        st.markdown(
            clean_html("""
            <div class="soc-card-subtle" style="border-left: 3px solid #22C55E;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 0.75rem; color: #94A3B8; font-weight: 700;">INFERENCE ENGINE</span>
                    <span class="badge-soc badge-green">ARMED</span>
                </div>
                <div style="font-size: 1.1rem; font-weight: 700; color: #F1F5F9; margin-top: 6px;">Random Forest (100)</div>
                <div style="font-size: 0.72rem; color: #64748B; margin-top: 4px;">Model Memory: Loaded</div>
            </div>
            """),
            unsafe_allow_html=True
        )

    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

    # Historical Flow Characteristics Section
    st.markdown(
        render_section_header("Historical Benchmark Flow Telemetry", "VERIFIED DATASET SAMPLES"),
        unsafe_allow_html=True
    )
    st.caption("Inspection of traffic distributions, port allocations, and flow duration dynamics observed across the benchmark flows.")

    try:
        sample_df = load_sample_dataset()

        # Port Distribution Chart
        top_ports = sample_df["Destination Port"].value_counts().head(8).reset_index()
        top_ports.columns = ["Destination Port", "Flow Count"]
        
        # Friendly port labels
        port_names = {
            80: "HTTP (80)",
            443: "HTTPS (443)",
            53: "DNS (53)",
            21: "FTP (21)",
            22: "SSH (22)",
            25: "SMTP (25)",
            8080: "HTTP-Alt (8080)"
        }
        top_ports["Port Label"] = top_ports["Destination Port"].apply(lambda p: port_names.get(int(p), f"Port {int(p)}"))

        hist_col1, hist_col2 = st.columns([1, 1])

        with hist_col1:
            st.write("**Most Frequently Targeted Destination Ports**")
            port_chart = alt.Chart(top_ports).mark_bar(cornerRadiusTopRight=4, cornerRadiusBottomRight=4).encode(
                x=alt.X("Flow Count:Q", title="Observed Flow Count", axis=alt.Axis(labelColor="#CBD5E1", titleColor="#94A3B8", gridColor="rgba(255,255,255,0.06)")),
                y=alt.Y("Port Label:N", title="Port / Protocol", sort="-x", axis=alt.Axis(labelColor="#CBD5E1", titleColor="#94A3B8")),
                color=alt.value("#00D4FF"),
                tooltip=["Destination Port", "Port Label", "Flow Count"]
            ).properties(height=240).configure_view(strokeWidth=0)
            st.altair_chart(port_chart, use_container_width=True)

        with hist_col2:
            st.write("**Flow Duration Distribution (Microseconds)**")
            duration_df = sample_df[["Flow Duration"]].copy()
            duration_df["Duration (ms)"] = (duration_df["Flow Duration"] / 1000).clip(upper=5000)
            
            dur_chart = alt.Chart(duration_df).mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3).encode(
                x=alt.X("Duration (ms):Q", bin=alt.Bin(maxbins=20), title="Flow Duration (ms, clipped at 5s)", axis=alt.Axis(labelColor="#CBD5E1", titleColor="#94A3B8")),
                y=alt.Y("count()", title="Number of Flows", axis=alt.Axis(labelColor="#CBD5E1", titleColor="#94A3B8", gridColor="rgba(255,255,255,0.06)")),
                color=alt.value("#3478F6"),
                tooltip=["count()"]
            ).properties(height=240).configure_view(strokeWidth=0)
            st.altair_chart(dur_chart, use_container_width=True)

    except Exception as e:
        st.warning(f"Could not load historical sample telemetry: {e}")

    # Future Enhancement Architecture Blueprint
    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
    st.markdown(
        render_section_header("Real-Time Packet Capture Integration Roadmap", "FUTURE ARCHITECTURE"),
        unsafe_allow_html=True
    )
    st.caption("The proposed engineering blueprint to transition NETGUARD IDS from offline dataset ingestion into a real-time live network monitor.")

    st.markdown(
        clean_html("""
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-top: 14px;">
            <div class="soc-card-subtle" style="border-top: 3px solid #00D4FF;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #00D4FF; font-weight: 700;">PHASE 1</div>
                <div style="font-size: 0.95rem; font-weight: 700; color: #F1F5F9; margin-top: 4px;">Raw Packet Ingestion</div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-top: 6px;">
                    Promiscuous network interface sniffing using <code>libpcap</code> or Python <code>Scapy</code> with ring-buffer packet capture.
                </div>
            </div>

            <div class="soc-card-subtle" style="border-top: 3px solid #3478F6;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #3478F6; font-weight: 700;">PHASE 2</div>
                <div style="font-size: 0.95rem; font-weight: 700; color: #F1F5F9; margin-top: 4px;">Session Flow Assembly</div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-top: 6px;">
                    Real-time 5-tuple flow reassembly (Src IP, Dst IP, Src Port, Dst Port, Protocol) via <code>CICFlowMeter</code> or eBPF kernel hooks.
                </div>
            </div>

            <div class="soc-card-subtle" style="border-top: 3px solid #8B5CF6;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #8B5CF6; font-weight: 700;">PHASE 3</div>
                <div style="font-size: 0.95rem; font-weight: 700; color: #F1F5F9; margin-top: 4px;">70-Feature Vectorization</div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-top: 6px;">
                    Streaming calculation of flow duration, packet inter-arrival times (IAT), byte rates, and TCP flag metrics.
                </div>
            </div>

            <div class="soc-card-subtle" style="border-top: 3px solid #22C55E;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #22C55E; font-weight: 700;">PHASE 4</div>
                <div style="font-size: 0.95rem; font-weight: 700; color: #F1F5F9; margin-top: 4px;">Sub-Millisecond Inference</div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-top: 6px;">
                    Inference dispatch to the trained 100-tree Random Forest engine with immediate syslog alert triggers.
                </div>
            </div>
        </div>
        """),
        unsafe_allow_html=True
    )
