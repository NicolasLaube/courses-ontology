"""Sidebar"""


import streamlit as st


def sidebar_view():
    """Sidebar view"""

    st.sidebar.markdown("## Navigation")

    st.sidebar.radio(
        "Pick tab", ("Requests", "Graphs", "Add user", "Add course"), key="navigation"
    )

    st.sidebar.markdown("### About")

    st.sidebar.caption("Capsule is a micro learning startup.", unsafe_allow_html=False)
