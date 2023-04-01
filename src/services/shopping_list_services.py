
class Shopping_list_service:

    def __init__(self):
        self._shopping_list = {}

        self.set_shopping_list()

    def set_shopping_list(self):
        shopping_list = {}
        shopping_list["omena"] = [1, "kpl", "hevi"]
        shopping_list["kevytmaito"] = [2, "l", "maitotuotteet"]
        shopping_list["tomaatti"] = [200, "g", "hevi"]
        self._shopping_list = shopping_list

    def get_shopping_list(self):
        return self._shopping_list

shopping_list_service = Shopping_list_service()