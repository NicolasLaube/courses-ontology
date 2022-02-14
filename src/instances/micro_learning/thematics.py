"""Thematics instances"""
from src import config
from src.construction.micro_learning.classes import Thematic

with config.ONTOLOGY as onto:

    biology = Thematic("Biology")
    history = Thematic("History")
    music = Thematic("Music")
    arts = Thematic("Arts")
    literature = Thematic("Literature")
    astronomy = Thematic("Astronomy")
