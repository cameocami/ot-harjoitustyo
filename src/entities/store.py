class Store:
    def __init__(self, name="Default"):
        self.name = name
        self.departments = []

    def add_department(self, department: Department):
        self._departments.append(department)
    
    