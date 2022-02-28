"""Tab graph"""

import os
import streamlit as st
from streamlit_agraph import Config, Edge, Node, agraph
from demonstrator.utils.json_loader import load_json
from src.requests.requests_micro_learning import get_all_courses

MIN_DEPENDENCIES_PATH = os.path.join("storage", "min_dependencies.json")

str_courses = None
all_dependencies = None


def get_str_courses():
    """Return all courses as strings"""
    global str_courses
    if str_courses is None:
        courses = get_all_courses()
        str_courses = [course.name for course in courses]
    return str_courses


def get_dependencies(course_str):
    """Return all min dependencies of a course"""
    global all_dependencies
    if all_dependencies is None:
        all_dependencies = load_json(MIN_DEPENDENCIES_PATH)
    return all_dependencies[course_str]


def tab_graph_view():
    """Tab graph view"""
    st.markdown("# Graph")

    st.selectbox(
        "Select the course:",
        get_str_courses(),
        index=0,
        disabled=False,
        key="request",
    )

    get_graph_view()


def get_graph_view():

    with st.spinner("Loading graph"):
        request = st.session_state.get("request", True)
        dependencies = get_dependencies(request)

    nodes = []
    edges = []
    for module in dependencies.keys():
        nodes.append(
            Node(
                id=module,
                label=module,
                color="grey",
            )
        )
    for target_module in dependencies.keys():
        for source_module in dependencies[target_module]:
            edges.append(
                Edge(
                    source=source_module,
                    target=target_module,
                    color="#F7A7A6",
                )
            )

    config = Config(
        width=1300,
        height=750,
        graphviz_layout="dot",
        graphviz_config={"rankdir": "TB", "ranksep": 0, "nodesep": 0},
        directed=True,
        nodeHighlightBehavior=True,
        collapsible=False,
        node={"labelProperty": "label"},
        link={"labelProperty": "label", "renderLabel": True},
        maxZoom=3,
        minZoom=0.4,
        staticGraphWithDragAndDrop=False,
        staticGraph=False,
        initialZoom=1.2,
    )
    agraph(nodes=nodes, edges=edges, config=config)
