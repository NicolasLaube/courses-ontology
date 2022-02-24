"""Information Technologies courses"""
from src.builder import ONTOLOGY
from src.construction.micro_learning.classes import Course
from src.instances.micro_learning.thematics import information_technologies

with ONTOLOGY:
    networks = Course("Networks")
    cryptography = Course("Cryptography")
    blockchain = Course("Blockchain")

    information_technologies_courses = [networks, cryptography, blockchain]

    information_technologies.has_as_course.extend(information_technologies_courses)
