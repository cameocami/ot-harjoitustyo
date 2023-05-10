

class Product:
    """Class responsible for keeping track of the department of a product.

    Attributes:
            name (str): product name
            department (str): department in which product is found
    """

    def __init__(self, name: str, department: str):
        """Class constructor, that creates a new product 
        Args:
            name (str): product name
            department (str): department in which product is found
        """
        self.name = name.lower()
        self.department = department

    def __repr__(self):
        """ Forms a string formatted representation for the product.

        Returns:
            string : product name capitalized
        """
        text = f'{self.name.capitalize()}'
        return text
