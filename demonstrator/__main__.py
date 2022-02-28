"""Main demonstrator file"""
# pylint: disable=C0413
import sys

import streamlit as st

sys.path.append(".")

from demonstrator.sidebar import sidebar_view
from demonstrator.tab_graph import tab_graph_view
from demonstrator.tab_requests import tab_requests_view

st.set_page_config(
    page_title="Microlearning ontology",
    page_icon="📒",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "Capsule is a micro-learning startup",
    },
)


sidebar_view()


def show_tab(tab_name: str = "requests"):
    """Shows tab depending on session value"""
    if tab_name == "Requests":
        tab_requests_view()
    elif tab_name == "Graphs":
        tab_graph_view()


tab = st.session_state.get("navigation", True)
show_tab(tab)
