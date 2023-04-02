class Store:
    def __init__(self, name: str, departments: list):
        self.name = name
        self.departments = departments

    def get_department_order_in_store(self):
        return [department for department in self.departments]

    def rearrange_departments(self):
        pass

    def __repr__(self):
        return f'{self.name}: {self.departments}'
    

    
    