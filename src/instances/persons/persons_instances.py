"""Persons instances"""
from src.builder import ONTOLOGY
from src.construction import Person

with ONTOLOGY:

    antoine = Person("Antoine")
    romain = Person("Romain")
    nicolas = Person("Nicolas")

    lola = Person("Lola")
    paola = Person("Paola")
    mathilde = Person("Mathilde")
    lucy = Person("Lucy")
    lea = Person("Lea")
    beatrice = Person("Beatrice")

    theo = Person("Theo")
    leo = Person("Leo")
    george = Person("George")
