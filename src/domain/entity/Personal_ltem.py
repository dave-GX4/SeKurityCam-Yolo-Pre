from dataclasses import dataclass

@dataclass
class PersonalItem(abs):
    id: int
    id_person: int
    class_name: str
    type_item: str
