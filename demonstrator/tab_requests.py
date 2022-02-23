"""Tab graph"""
from inspect import signature

import streamlit as st

from src.requests.requests_micro_learning import get_all_thematics, get_course_modules


def tab_requests_view():
    """Tab requests view"""

    st.markdown("# Requests")

    st.selectbox(
        "Select the type of request:",
        ("Thematics", "Modules of course"),
        index=0,
        disabled=False,
        key="request",
    )

    get_request_view()

    st.button("Apply")


def get_request_view():
    """Returns the request view"""

    request = st.session_state.get("request", True)

    funct: callable = SPARQL_REQUESTS[request]

    sig = signature(funct)
    params = sig.parameters

    st.markdown(f"###### {funct.__doc__}")

    col1, col2 = st.columns(2)

    with col1:
        for param in params:
            st.text(f"Please select {param.capitalize()}: ")

    with col2:
        for param in params:
            st.text_input("course id")


SPARQL_REQUESTS = {
    "Thematics": get_all_thematics,
    "Modules of course": get_course_modules,
}
