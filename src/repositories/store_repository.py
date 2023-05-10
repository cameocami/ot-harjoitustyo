import csv
from entities.store import Store
from config import STORE_REPOSITORY_PATH


class StoreRepository:
    def __init__(self):
        self._file_path = STORE_REPOSITORY_PATH
        self._stores = []
        self.pull_database()

    def pull_database(self):
        with open(self._file_path, mode='r', encoding='UTF-8') as store_file:
            for row in csv.reader(store_file, delimiter=';'):
                name = row[0]
                departments = []
                for department in row[1:]:
                    departments.append(department)
                self._stores.append(Store(name, departments))

    def get_store_repository(self):
        return self._stores

    def get_store(self, store_name: str):
        for store in self._stores:
            if store_name == store.name:
                return store
        return self._stores[0]
