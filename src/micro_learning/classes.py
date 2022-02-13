"""
Base ontologies
Classes in ontologies are abstract groups, sets or collections of objects.
"""
import owlready2 as owl

from src import config

with config.ONTOLOGY as onto:

    class Thematic(owl.Thing):
        """
        Thematics class
        ---
        For exemple 'Music' is a thematic
        """

        ontology = onto

    class Course(Thematic):
        """
        Courses class
        ---
        For example 'The pop' is a course
        """

        ontology = onto

    class Module(Course):
        """
        Module class
        ---
        For example 'The pop in the 80s' is a module
        """

        ontology = onto

    class Knowledge(Module):
        """
        Knowledge class
        ---
        For example 'Micheal Jackson was king of the pop' is a knwoledge
        """

        ontology = onto

    class Fragment(Knowledge):
        """
        Knowledge class
        ---
        A fragment is a Complement, Example or Anecdot
        """

        ontology = onto
