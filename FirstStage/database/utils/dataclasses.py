from dataclasses import dataclass

@dataclass
class Group:
    id: int
    title: str
    faculty: int
    specialty: int
    