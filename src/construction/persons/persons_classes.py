"""Person classes"""
import owlready2 as owl  # type: ignore

from src.builder import ONTOLOGY

with ONTOLOGY:

    class Person(owl.Thing):
        """
        Person class
        ---
        """

    class Learner(Person):
        """
        Learner class
        ---
        For example 'Theo' who is following a course is a Learner
        """

    class Creator(Person):
        """
        Creator class
        ---
        For example 'Lola' who created a course about Quantum physics is a Creator
        """

    class Reviewer(Person):
        """
        Reviewer class
        ---
        For example 'Mathilde' who reviewed and modified some parts is a Reviewer
        """

    class Follower(Person):
        """
        Follower class
        ---
        For example 'Lee' who follows Lola's publications is a Follower
        """
