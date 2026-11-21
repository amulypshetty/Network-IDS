"""
NETGUARD IDS - About Project View
Comprehensive academic dossier, DCN theoretical background, visual workflow pipeline, and future roadmap.
All UI elements use native Streamlit components and clean_html() to prevent Markdown code block leaks.
"""

import streamlit as st
from dashboard.styles import (
    render_top_header,
    render_section_header,
    clean_html
)
from dashboard.data_loader import load_cached_metrics


def render_about_project():
    """Renders the About Project view with methodology, architecture workflow, and project details."""
    metrics = load_cached_metrics()

    # Page Header (Strictly shows OFFLINE BENCHMARK)
    st.markdown(
        render_top_header(
            title="ABOUT NETGUARD IDS • DCN PROJECT",
            subtitle="Machine Learning Driven Flow-Level Network Security Monitoring",
            badge_text="ACADEMIC DOSSIER",
            badge_color="purple"
        ),
        unsafe_allow_html=True
    )

    # Visual Workflow Pipeline Section
    st.markdown(
        render_section_header("End-to-End System Workflow Pipeline", "ENGINEERING METHODOLOGY"),
        unsafe_allow_html=True
    )
    st.caption("The architectural lifecycle from raw network packet captures to automated threat classification in the SOC:")

    st.markdown(
        clean_html("""
        <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 10px;">
            <div style="display: flex; align-items: stretch; gap: 12px; background: rgba(8, 13, 24, 0.6); border: 1px solid rgba(0, 212, 255, 0.2); border-radius: 8px; padding: 12px 16px;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; font-weight: 800; color: #00D4FF; min-width: 36px; display: flex; align-items: center;">01</div>
                <div style="border-left: 2px solid rgba(0, 212, 255, 0.3); padding-left: 12px;">
                    <div style="font-weight: 700; color: #F1F5F9; font-size: 0.92rem;">Dataset Collection (CIC-IDS2017)</div>
                    <div style="font-size: 0.8rem; color: #94A3B8;">Ingested 8 real-world traffic PCAP sessions containing 2,830,743 flows covering diverse attack profiles and realistic benign backgrounds.</div>
                </div>
            </div>

            <div style="display: flex; align-items: stretch; gap: 12px; background: rgba(8, 13, 24, 0.6); border: 1px solid rgba(52, 120, 246, 0.2); border-radius: 8px; padding: 12px 16px;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; font-weight: 800; color: #3478F6; min-width: 36px; display: flex; align-items: center;">02</div>
                <div style="border-left: 2px solid rgba(52, 120, 246, 0.3); padding-left: 12px;">
                    <div style="font-weight: 700; color: #F1F5F9; font-size: 0.92rem;">Data Preprocessing & Sanitization</div>
                    <div style="font-size: 0.8rem; color: #94A3B8;">Trimmed whitespace, mapped multiclass labels into binary (BENIGN: 0, ATTACK: 1), removed infinity/NaN values, and pruned duplicate flows, yielding 2,520,798 valid records.</div>
                </div>
            </div>

            <div style="display: flex; align-items: stretch; gap: 12px; background: rgba(8, 13, 24, 0.6); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 8px; padding: 12px 16px;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; font-weight: 800; color: #8B5CF6; min-width: 36px; display: flex; align-items: center;">03</div>
                <div style="border-left: 2px solid rgba(139, 92, 246, 0.3); padding-left: 12px;">
                    <div style="font-weight: 700; color: #F1F5F9; font-size: 0.92rem;">Feature Selection & Dimensionality Reduction</div>
                    <div style="font-size: 0.8rem; color: #94A3B8;">Evaluated feature variances and eliminated 8 non-informative constant/zero-variance columns, leaving a refined 70-feature statistical representation.</div>
                </div>
            </div>

            <div style="display: flex; align-items: stretch; gap: 12px; background: rgba(8, 13, 24, 0.6); border: 1px solid rgba(245, 158, 11, 0.2); border-radius: 8px; padding: 12px 16px;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; font-weight: 800; color: #F59E0B; min-width: 36px; display: flex; align-items: center;">04</div>
                <div style="border-left: 2px solid rgba(245, 158, 11, 0.3); padding-left: 12px;">
                    <div style="font-weight: 700; color: #F1F5F9; font-size: 0.92rem;">Stratified Train-Test Splitting (80/20)</div>
                    <div style="font-size: 0.8rem; color: #94A3B8;">Partitioned dataset using stratified sampling to preserve class ratios: 2,016,638 flows for training and 504,160 flows for unseen empirical evaluation.</div>
                </div>
            </div>

            <div style="display: flex; align-items: stretch; gap: 12px; background: rgba(8, 13, 24, 0.6); border: 1px solid rgba(34, 197, 94, 0.2); border-radius: 8px; padding: 12px 16px;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; font-weight: 800; color: #22C55E; min-width: 36px; display: flex; align-items: center;">05</div>
                <div style="border-left: 2px solid rgba(34, 197, 94, 0.3); padding-left: 12px;">
                    <div style="font-weight: 700; color: #F1F5F9; font-size: 0.92rem;">Ensemble Random Forest Training</div>
                    <div style="font-size: 0.8rem; color: #94A3B8;">Trained an ensemble of 100 Decision Trees with balanced class weights using parallel multi-core execution to prevent overfitting and capture non-linear flow boundaries.</div>
                </div>
            </div>

            <div style="display: flex; align-items: stretch; gap: 12px; background: rgba(8, 13, 24, 0.6); border: 1px solid rgba(0, 212, 255, 0.2); border-radius: 8px; padding: 12px 16px;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; font-weight: 800; color: #00D4FF; min-width: 36px; display: flex; align-items: center;">06</div>
                <div style="border-left: 2px solid rgba(0, 212, 255, 0.3); padding-left: 12px;">
                    <div style="font-weight: 700; color: #F1F5F9; font-size: 0.92rem;">Model Evaluation & Benchmarking</div>
                    <div style="font-size: 0.8rem; color: #94A3B8;">Evaluated on 504,160 unseen flows achieving 99.89% accuracy, 99.56% precision, 99.80% recall, and 0.9998 ROC-AUC.</div>
                </div>
            </div>

            <div style="display: flex; align-items: stretch; gap: 12px; background: rgba(8, 13, 24, 0.6); border: 1px solid rgba(239, 68, 68, 0.2); border-radius: 8px; padding: 12px 16px;">
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; font-weight: 800; color: #EF4444; min-width: 36px; display: flex; align-items: center;">07</div>
                <div style="border-left: 2px solid rgba(239, 68, 68, 0.3); padding-left: 12px;">
                    <div style="font-weight: 700; color: #F1F5F9; font-size: 0.92rem;">SOC Platform Deployment & Batch Inference</div>
                    <div style="font-size: 0.8rem; color: #94A3B8;">Built this enterprise SOC dashboard enabling interactive CSV upload, 70-feature validation, threat confidence scoring, and incident triage.</div>
                </div>
            </div>
        </div>
        """),
        unsafe_allow_html=True
    )

    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

    # Academic Project Context Row: Abstract & Problem Statement
    row1_c1, row1_c2 = st.columns([1, 1])

    with row1_c1:
        st.markdown(
            render_section_header("Project Abstract", "OVERVIEW"),
            unsafe_allow_html=True
        )
        st.markdown(
            clean_html("""
            <div class="soc-card-subtle" style="font-size: 0.85rem; color: #CBD5E1; line-height: 1.6;">
                Network security forms the foundation of modern digital communications. Traditional perimeter defenses, such as static packet filters
                and signature-based firewalls, frequently fail against zero-day exploits, polymorphic malware, and distributed volumetric attacks.<br><br>
                This project develops an intelligent <b>Network Intrusion Detection System (Network IDS)</b> leveraging the Canadian Institute for Cybersecurity
                <b>CIC-IDS2017</b> benchmark. By training a high-performance <b>Random Forest Classifier</b> on 70 statistical network flow features,
                the system delivers automated, high-precision detection of malicious sessions with sub-millisecond inference and an outstanding <b>99.89% accuracy</b>.
            </div>
            """),
            unsafe_allow_html=True
        )

    with row1_c2:
        st.markdown(
            render_section_header("Problem Statement", "CHALLENGE"),
            unsafe_allow_html=True
        )
        st.markdown(
            clean_html("""
            <div class="soc-card-subtle" style="font-size: 0.85rem; color: #CBD5E1; line-height: 1.6;">
                Modern enterprise computer networks handle massive gigabit-per-second traffic throughput. Security analysts face two critical bottlenecks:<br><br>
                1. <b>Signature Ineffectiveness:</b> Threat actors regularly alter payload signatures, bypassing conventional rule-based Snort/Suricata engines.<br>
                2. <b>Alert Fatigue:</b> High false positive rates in heuristic systems overwhelm SOC personnel, causing critical intrusions to go unnoticed.<br><br>
                <b>The Solution:</b> A statistical flow-based machine learning IDS that examines behavioral flow metrics (packet lengths, inter-arrival times, window sizes)
                rather than brittle payload strings, providing robust generalized classification.
            </div>
            """),
            unsafe_allow_html=True
        )

    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

    # Objectives & Technologies
    row2_c1, row2_c2 = st.columns([1, 1])

    with row2_c1:
        st.markdown(
            render_section_header("Core Project Objectives", "GOALS"),
            unsafe_allow_html=True
        )
        st.markdown(
            clean_html("""
            <div class="soc-card-subtle">
                <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="display: flex; align-items: flex-start; gap: 8px; font-size: 0.82rem; color: #CBD5E1;">
                        <span style="color: #00D4FF; font-weight: bold;">✔</span>
                        <span>Ingest and preprocess 2.8+ million raw flow records from the CIC-IDS2017 dataset.</span>
                    </div>
                    <div style="display: flex; align-items: flex-start; gap: 8px; font-size: 0.82rem; color: #CBD5E1;">
                        <span style="color: #00D4FF; font-weight: bold;">✔</span>
                        <span>Engineer a refined 70-feature vector space eliminating non-informative constant attributes.</span>
                    </div>
                    <div style="display: flex; align-items: flex-start; gap: 8px; font-size: 0.82rem; color: #CBD5E1;">
                        <span style="color: #00D4FF; font-weight: bold;">✔</span>
                        <span>Train and serialize a 100-estimator Random Forest classifier with balanced class weighting.</span>
                    </div>
                    <div style="display: flex; align-items: flex-start; gap: 8px; font-size: 0.82rem; color: #CBD5E1;">
                        <span style="color: #00D4FF; font-weight: bold;">✔</span>
                        <span>Rigidly evaluate model performance across 504k test records using Accuracy, Precision, Recall, F1, and ROC-AUC.</span>
                    </div>
                    <div style="display: flex; align-items: flex-start; gap: 8px; font-size: 0.82rem; color: #CBD5E1;">
                        <span style="color: #00D4FF; font-weight: bold;">✔</span>
                        <span>Build an enterprise-grade cybersecurity SOC dashboard with interactive CSV upload, feature schema validation, and triage filtering.</span>
                    </div>
                </div>
            </div>
            """),
            unsafe_allow_html=True
        )

    with row2_c2:
        st.markdown(
            render_section_header("Technology Stack & Libraries", "TECH STACK"),
            unsafe_allow_html=True
        )
        st.markdown(
            clean_html("""
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                <div class="soc-card-subtle">
                    <div style="color: #00D4FF; font-weight: 700; font-size: 0.82rem;">Machine Learning Core</div>
                    <div style="font-size: 0.75rem; color: #94A3B8; margin-top: 4px;">Scikit-learn 1.9.1 • Joblib 1.6.0 • NumPy 2.5.5</div>
                </div>
                <div class="soc-card-subtle">
                    <div style="color: #3478F6; font-weight: 700; font-size: 0.82rem;">Data Processing</div>
                    <div style="font-size: 0.75rem; color: #94A3B8; margin-top: 4px;">Pandas 3.1.1 • Fast tabular parsing</div>
                </div>
                <div class="soc-card-subtle">
                    <div style="color: #8B5CF6; font-weight: 700; font-size: 0.82rem;">Visualization & UI</div>
                    <div style="font-size: 0.75rem; color: #94A3B8; margin-top: 4px;">Streamlit 1.67.0 • Altair 6.3.0 • Matplotlib 3.11</div>
                </div>
                <div class="soc-card-subtle">
                    <div style="color: #22C55E; font-weight: 700; font-size: 0.82rem;">Environment & Platform</div>
                    <div style="font-size: 0.75rem; color: #94A3B8; margin-top: 4px;">Python 3.13 Virtualenv • Windows 64-bit</div>
                </div>
            </div>
            """),
            unsafe_allow_html=True
        )

    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

    # Limitations and Future Work
    lim_c1, lim_c2 = st.columns([1, 1])

    with lim_c1:
        st.markdown(
            render_section_header("Current Limitations", "CONSTRAINTS"),
            unsafe_allow_html=True
        )
        st.markdown(
            clean_html("""
            <div class="soc-card-subtle" style="border-left: 3px solid #F59E0B; font-size: 0.82rem; color: #CBD5E1; line-height: 1.6;">
                • <b>Offline Preprocessed Ingest:</b> Classification relies on pre-extracted tabular flows rather than live socket sniffing.<br>
                • <b>Binary Classification Scope:</b> Classes are aggregated into BENIGN vs ATTACK; individual attack families (e.g. DoS Slowloris vs GoldenEye) are not separated in this phase.<br>
                • <b>Fixed 70-Feature Schema:</b> Uploaded CSVs must conform strictly to the CIC-IDS2017 naming convention.
            </div>
            """),
            unsafe_allow_html=True
        )

    with lim_c2:
        st.markdown(
            render_section_header("Future Enhancements", "ROADMAP"),
            unsafe_allow_html=True
        )
        st.markdown(
            clean_html("""
            <div class="soc-card-subtle" style="border-left: 3px solid #00D4FF; font-size: 0.82rem; color: #CBD5E1; line-height: 1.6;">
                • <b>Live Promiscuous Sniffing:</b> Integrate Python Scapy or eBPF kernel hooks with real-time streaming feature extraction.<br>
                • <b>Multi-Class Attack Taxonomy:</b> Extend classification to 14 granular cyber-attack profiles.<br>
                • <b>Automated Incident Response:</b> Webhook dispatches to SIEM platforms (Splunk, Elastic) and automated IP firewall blocking via iptables/Palo Alto API.
            </div>
            """),
            unsafe_allow_html=True
        )
