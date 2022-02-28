"""Objects parsers"""
from typing import Any

from src.construction import Course, Knowledge, Learner, Module


def parse(obj: str, value: str) -> Any:
    """Parse object"""
    if obj == "course":
        return Course(value)
    if obj == "module":
        return Module(value)
    if obj == "learner":
        return Learner(value)
    if obj == "knwoledge":
        return Knowledge(value)
    return None
