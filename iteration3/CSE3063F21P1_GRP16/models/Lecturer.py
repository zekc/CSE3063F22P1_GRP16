
from models.Staff import Staff


class Lecturer(Staff):
    def __init__(self):
        self._lecturer_degree = ""