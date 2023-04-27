class Store:
    """Class responsible for keeping track of the department order in a store.

    Attributes:
            name (str): store name
            departments (list): list of departments in the order which they appear in the store
    """

    def __init__(self, name: str, departments: list):
        """Class constructor.

        Args:
            name (str): store name
            departments (list): list of departments in the order which they appear in the store
        """
        self.name = name
        self.departments = departments

    def get_department_order_in_store(self):
        """Retrieves the list of departments in order, which is a hidden attribute.

        Returns:
            list: departments in the order which they appear in the store
        """
        return self.departments
