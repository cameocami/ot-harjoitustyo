class Department:
    def __init__(self, name: str):
        self.name = name.lower()
        self._position = None

    def set_position(self, position: int):
        self._position = position
    
    def get_position(self):
        return self._position
    
    def __repr__(self):
        text = f'{self.name.capitalize()}'
        return text