import csv
from pathlib import Path

from entities.store import Store
from config import STORE_REPOSITORY_PATH


class StoreRepository:
    def __init__(self):
        self._file_path = STORE_REPOSITORY_PATH
        self._stores = []
        self.pull_database()

    def pull_database(self):
        self._ensure_file_exists()
        with open(self._file_path, mode='r', encoding='UTF-8') as store_file:
            for row in csv.reader(store_file, delimiter=';'):
                name = row[0]
                departments = []
                for department in row[1:]:
                    departments.append(department)
                self._stores.append(Store(name, departments))

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def get_store_repository(self):
        return self._stores

    def get_store(self, store_name: str):
        for store in self._stores:
            if store_name == store.name:
                return store
        return self._stores[0]

    def delete_all(self):
        self._stores = []
        with open(self._file_path, mode='w', encoding='UTF-8') as product_file:
            pass
