from entities.department import Department


class Product:
    def __init__(self, name: str, department: Department):
        self.name = name.lower()
        self.department = department

    def __repr__(self):
        text = f'{self.name[0].upper()}{self.name[1:]}'
        return text



