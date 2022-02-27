"""Tab graph"""

import streamlit as st
from streamlit_agraph import Config, Edge, Node, agraph
from src.requests import get_all_courses
from src.reasoner import get_min_dependencies_in_course

str_courses = None

all_dependencies = None


def get_str_courses():
    global str_courses
    if str_courses is None:
        courses = get_all_courses()
        str_courses = [course[0].name for course in courses]
    return str_courses


def get_dependencies(course_str):
    global all_dependencies
    if all_dependencies is None:
        courses = get_all_courses()
        courses = [course[0] for course in courses]
        all_dependencies = {}
        for course in courses:
            all_dependencies[course.name] = get_min_dependencies_in_course(course)
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
                id=module.name,
                label=module.name,
                color="grey",
            )
        )
    for target_module in dependencies.keys():
        for source_module in dependencies[target_module]:
            edges.append(
                Edge(
                    source=source_module.name,
                    target=target_module.name,
                    color="#F7A7A6",
                )
            )

    layout = st.sidebar.selectbox("layout", ["dot", "neato", "circo", "fdp", "sfdp"])

    rankdir = st.sidebar.selectbox("rankdir", ["TB", "BT", "LR", "RL"])
    ranksep = st.sidebar.slider("ranksep", min_value=0, max_value=10)
    nodesep = st.sidebar.slider("nodesep", min_value=0, max_value=10)

    config = Config(
        width=1300,
        height=750,
        graphviz_layout=layout,
        graphviz_config={"rankdir": rankdir, "ranksep": ranksep, "nodesep": nodesep},
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
