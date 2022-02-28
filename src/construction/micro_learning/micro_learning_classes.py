"""
Base ontologies
Classes in ontologies are abstract groups, sets or collections of objects.
"""
import owlready2 as owl  # type: ignore

from src.builder import ONTOLOGY

with ONTOLOGY:

    class Thematic(owl.Thing):
        """
        Thematics class
        ---
        For exemple 'Music' is a thematic
        """

    # The creation of this class adds two RDF triplets
    # The first one indicates that Thematic is a OWL class
    # The second one indicates Thematic herits from Thing

    class Course(owl.Thing):
        """
        Courses class
        ---
        For example 'The pop' is a course
        """

    class Module(owl.Thing):
        """
        Module class
        ---
        For example 'The pop in the 80s' is a module
        """

    class Knowledge(owl.Thing):
        """
        Knowledge class
        ---
        For example 'Micheal Jackson was king of the pop' is a knwoledge
        """

    class Fragment(owl.Thing):
        """
        Fragment class
        ---
        A fragment is a Complement, Example or Anecdote
        """

    class Complement(Fragment):
        """
        Complement class
        ---
        A Complement complete information given in a knowledge
        """

    class Example(Fragment):
        """
        Example class
        ---
        An Exemple gives an example about a knowledge
        """

    class Anecdote(Fragment):
        """
        Anecdote class
        ---
        An Anecdote gives an anecdote about a knowledge
        """

    owl.AllDisjoint([Thematic, Module, Course, Fragment, Knowledge])
    owl.AllDisjoint([Complement, Example, Anecdote])
