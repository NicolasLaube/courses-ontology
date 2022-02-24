"""Tab graph"""
from inspect import signature
from typing import Any, Callable

import pandas as pd
import streamlit as st

from demonstrator.utils.parser import parse
from src.requests.requests_dict import SPARQL_REQUESTS


def tab_requests_view():
    """Tab requests view"""

    st.markdown("# Requests")

    st.selectbox(
        "Select the type of request:",
        SPARQL_REQUESTS.keys(),
        index=0,
        disabled=False,
        key="request",
    )

    get_request_view()

    st.dataframe(st.session_state.get("df"))


def get_request_view():
    """Returns the request view"""

    request = st.session_state.get("request", True)

    funct: Callable[[Any], Any] = SPARQL_REQUESTS[request]

    sig = signature(funct)
    params = sig.parameters

    with st.form(f"{funct.__doc__}"):

        st.markdown(f"###### {funct.__doc__}")

        for param in params:
            st.text_input(
                f"Please enter {param.capitalize()}: ", value="", key=str(param)
            )

        st.form_submit_button(
            "Apply",
            on_click=show_results,
            args=[funct, *params],
        )


def show_results(funct: Callable[[Any], Any], *args):
    """Shows results"""
    params_values = [parse(param, st.session_state.get(str(param))) for param in args]

    results = funct(*params_values)

    st.session_state["df"] = pd.DataFrame(
        [str(ele[0]) for ele in results],
    )
