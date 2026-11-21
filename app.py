"""
========================================================================================
NETGUARD IDS — Enterprise Network Intrusion Detection System
Security Operations Center (SOC) Dashboard

Dataset: CIC-IDS2017 (Canadian Institute for Cybersecurity)
Model: Random Forest Classifier (100 Estimators, Balanced Class Weights)
Dimensionality: 70 Selected Flow Features
Author / Project: College DCN (Data Communications and Networks) Capstone
========================================================================================
"""

import sys
import os
from pathlib import Path

# Ensure workspace root is in sys.path for robust modular imports on Windows
WORKSPACE_ROOT = Path(__file__).resolve().parent
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

import streamlit as st

# Page Configuration - Enterprise SOC Dashboard Layout
st.set_page_config(
    page_title="NETGUARD IDS • Cybersecurity SOC Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import Custom Styling & SOC Components
from dashboard.styles import (
    SOC_THEME_CSS,
    render_sidebar_header,
    render_sidebar_footer
)

# Import Modular Views
from dashboard.views.overview import render_overview
from dashboard.views.live_monitor import render_live_monitor
from dashboard.views.traffic_detection import render_traffic_detection
from dashboard.views.attack_analysis import render_attack_analysis
from dashboard.views.model_performance import render_model_performance
from dashboard.views.about_project import render_about_project

# Inject Global Dark SOC Theme
st.markdown(SOC_THEME_CSS, unsafe_allow_html=True)

# ======================================================================================
# SIDEBAR NAVIGATION
# ======================================================================================

with st.sidebar:
    st.markdown(render_sidebar_header(), unsafe_allow_html=True)
    
    st.markdown(
        "<div style='font-size: 0.72rem; color: #64748B; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin: 10px 0 6px 4px;'>Navigation</div>",
        unsafe_allow_html=True
    )
    
    # Navigation options mapped to SOC workflows
    nav_pages = [
        "Overview",
        "Live Monitor",
        "Traffic Detection",
        "Attack Analysis",
        "Model Performance",
        "About Project"
    ]
    
    selected_page = st.radio(
        "Navigation Menu",
        nav_pages,
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown(render_sidebar_footer(), unsafe_allow_html=True)

# ======================================================================================
# VIEW DISPATCHER
# ======================================================================================

try:
    if selected_page == "Overview":
        render_overview()
    elif selected_page == "Live Monitor":
        render_live_monitor()
    elif selected_page == "Traffic Detection":
        render_traffic_detection()
    elif selected_page == "Attack Analysis":
        render_attack_analysis()
    elif selected_page == "Model Performance":
        render_model_performance()
    elif selected_page == "About Project":
        render_about_project()
except Exception as e:
    st.error(f"Application Error during view execution: {e}")
    st.exception(e)
