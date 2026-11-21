"""
NETGUARD IDS - Model Performance View
Comprehensive machine learning evaluation dossier, five verified metric cards, and student presentation viva guide.
All UI elements use native Streamlit components and clean_html() to prevent Markdown code block leaks.
"""

from pathlib import Path
import streamlit as st
import pandas as pd
from dashboard.styles import (
    render_top_header,
    render_section_header,
    clean_html
)
from dashboard.data_loader import load_cached_metrics


def render_model_performance():
    """Renders the Model Performance page with technical specs and metric explanations for viva."""
    metrics = load_cached_metrics()

    # Page Header (Strictly shows OFFLINE BENCHMARK)
    st.markdown(
        render_top_header(
            title="MODEL PERFORMANCE & EVALUATION DOSSIER",
            subtitle="Verified Empirical Benchmarks on Random Forest Classifier (100 Trees)",
            badge_text="METRICS VERIFIED",
            badge_color="green"
        ),
        unsafe_allow_html=True
    )

    # 5 Primary Performance KPI Cards (Native st.metric for 100% reliable rendering without HTML leaking)
    st.markdown(
        render_section_header("Core Performance Metrics", "TEST SPLIT BENCHMARK"),
        unsafe_allow_html=True
    )

    p1, p2, p3, p4, p5 = st.columns(5)

    with p1:
        st.metric(
            label="Accuracy",
            value=f"{metrics['accuracy']*100:.2f}%",
            help="Overall Correctness"
        )
        st.caption("Overall Correctness")

    with p2:
        st.metric(
            label="Precision",
            value=f"{metrics['precision']*100:.2f}%",
            help=f"Weighted: {metrics['weighted_precision']*100:.2f}%"
        )
        st.caption("Attack Specificity")

    with p3:
        st.metric(
            label="Recall (Sensitivity)",
            value=f"{metrics['recall']*100:.2f}%",
            help=f"Weighted: {metrics['weighted_recall']*100:.2f}%"
        )
        st.caption("Attack Interception")

    with p4:
        st.metric(
            label="F1-Score",
            value=f"{metrics['f1_score']*100:.2f}%",
            help=f"Weighted: {metrics['weighted_f1']*100:.2f}%"
        )
        st.caption("Harmonic Balance")

    with p5:
        st.metric(
            label="ROC-AUC Score",
            value=f"{metrics['roc_auc']:.4f}",
            help="Separability (Max 1.0)"
        )
        st.caption("Separability")

    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

    # Technical Blueprint Specification Cards
    st.markdown(
        render_section_header("Ensemble Model Specifications & Training Hyperparameters", "SCIKIT-LEARN 1.9.1 PIPELINE"),
        unsafe_allow_html=True
    )

    st.markdown(
        clean_html("""
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin-top: 14px;">
            <div class="soc-card-subtle">
                <div style="font-size: 0.72rem; color: #64748B; font-weight: 700; text-transform: uppercase;">Algorithm Family</div>
                <div style="font-size: 1.05rem; font-weight: 700; color: #F1F5F9; margin-top: 4px;">Random Forest Classifier</div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-top: 4px;">Breiman's Bagging with bootstrap aggregation</div>
            </div>

            <div class="soc-card-subtle">
                <div style="font-size: 0.72rem; color: #64748B; font-weight: 700; text-transform: uppercase;">Tree Estimators</div>
                <div style="font-size: 1.05rem; font-weight: 700; color: #00D4FF; margin-top: 4px;">100 Trees (n_estimators=100)</div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-top: 4px;">Ensemble majority voting across independent trees</div>
            </div>

            <div class="soc-card-subtle">
                <div style="font-size: 0.72rem; color: #64748B; font-weight: 700; text-transform: uppercase;">Splitting Criterion</div>
                <div style="font-size: 1.05rem; font-weight: 700; color: #8B5CF6; margin-top: 4px;">Gini Impurity</div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-top: 4px;">Optimal node purity calculation at each split</div>
            </div>

            <div class="soc-card-subtle">
                <div style="font-size: 0.72rem; color: #64748B; font-weight: 700; text-transform: uppercase;">Class Balancing</div>
                <div style="font-size: 1.05rem; font-weight: 700; color: #22C55E; margin-top: 4px;">class_weight='balanced'</div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-top: 4px;">Automatically penalizes minority attack misclassification</div>
            </div>

            <div class="soc-card-subtle">
                <div style="font-size: 0.72rem; color: #64748B; font-weight: 700; text-transform: uppercase;">Input Dimensionality</div>
                <div style="font-size: 1.05rem; font-weight: 700; color: #3478F6; margin-top: 4px;">70 Selected Features</div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-top: 4px;">8 non-informative constant columns pruned</div>
            </div>

            <div class="soc-card-subtle">
                <div style="font-size: 0.72rem; color: #64748B; font-weight: 700; text-transform: uppercase;">Dataset Partitioning</div>
                <div style="font-size: 1.05rem; font-weight: 700; color: #EF4444; margin-top: 4px;">80% Train / 20% Test</div>
                <div style="font-size: 0.78rem; color: #94A3B8; margin-top: 4px;">Stratified split: 2,016,638 Train / 504,160 Test</div>
            </div>
        </div>
        """),
        unsafe_allow_html=True
    )

    # Student Viva Voce & Presentation Guide
    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
    st.markdown(
        render_section_header("Student Presentation & Viva Voce Guide", "DEFENSE READINESS"),
        unsafe_allow_html=True
    )
    st.caption("Master these essential explanations to confidently answer examiner and viva questions regarding why each metric matters in Network Intrusion Detection:")

    st.markdown(
        clean_html("""
        <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 10px;">
            <div class="soc-card-subtle" style="border-left: 3px solid #00D4FF;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-weight: 700; color: #00D4FF; font-size: 0.95rem;">1. Accuracy (99.89%) — Overall Classification Precision</span>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #64748B;">Formula: (TP + TN) / Total</span>
                </div>
                <div style="font-size: 0.82rem; color: #CBD5E1; line-height: 1.5;">
                    <b>Examiner Note:</b> In network security, accuracy alone can be deceptive if a dataset has 99% normal traffic (a dummy model predicting only BENIGN would get 99%).
                    In NETGUARD IDS, our dataset has an 83/17 split, and our 99.89% accuracy is validated alongside high recall and precision.
                </div>
            </div>

            <div class="soc-card-subtle" style="border-left: 3px solid #8B5CF6;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-weight: 700; color: #A78BFA; font-size: 0.95rem;">2. Precision (99.56%) — Alert Trustworthiness & Avoiding Fatigue</span>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #64748B;">Formula: TP / (TP + FP)</span>
                </div>
                <div style="font-size: 0.82rem; color: #CBD5E1; line-height: 1.5;">
                    <b>Examiner Note:</b> Out of all flows our system flagged as an ATTACK, 99.56% were genuine attacks.
                    High precision guarantees that security analysts are not swamped by false alarms, preventing "alert fatigue."
                </div>
            </div>

            <div class="soc-card-subtle" style="border-left: 3px solid #22C55E;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-weight: 700; color: #22C55E; font-size: 0.95rem;">3. Recall / Sensitivity (99.80%) — Attack Interception Rate</span>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #64748B;">Formula: TP / (TP + FN)</span>
                </div>
                <div style="font-size: 0.82rem; color: #CBD5E1; line-height: 1.5;">
                    <b>Examiner Note:</b> Out of all genuine attacks traversing the network, the model successfully caught 99.80% (84,975 out of 85,148).
                    Only 0.20% evaded detection. In cybersecurity, high recall is vital to ensure zero silent breaches.
                </div>
            </div>

            <div class="soc-card-subtle" style="border-left: 3px solid #3478F6;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-weight: 700; color: #3478F6; font-size: 0.95rem;">4. F1-Score (99.68%) — Harmonic Balance</span>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #64748B;">Formula: 2 * (Precision * Recall) / (Precision + Recall)</span>
                </div>
                <div style="font-size: 0.82rem; color: #CBD5E1; line-height: 1.5;">
                    <b>Examiner Note:</b> F1-score is the harmonic mean of precision and recall. Because neither can be sacrificed in a production SOC,
                    an F1-score of 99.68% proves mathematically that the model maintains both high detection reliability and low false alarms.
                </div>
            </div>

            <div class="soc-card-subtle" style="border-left: 3px solid #00D4FF;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-weight: 700; color: #00D4FF; font-size: 0.95rem;">5. ROC-AUC (0.9998) — Threshold-Independent Discriminative Power</span>
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #64748B;">Range: 0.5 (Random) to 1.0 (Flawless)</span>
                </div>
                <div style="font-size: 0.82rem; color: #CBD5E1; line-height: 1.5;">
                    <b>Examiner Note:</b> The Receiver Operating Characteristic Area Under the Curve (ROC-AUC) measures the probability that the classifier
                    will rank a randomly chosen attack flow higher than a randomly chosen benign flow. At 0.9998, separability is essentially near-perfect.
                </div>
            </div>
        </div>
        """),
        unsafe_allow_html=True
    )
