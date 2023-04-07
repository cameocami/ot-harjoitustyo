import csv
from entities.department import Department
from entities.store import Store


class StoreRepository:
    def __init__(self):
        self._stores = []

        self.pull_database()

    def get_store_repository(self):
        return self._stores

    def pull_database(self):
        with open('stores.cvs',mode='r', encoding='UTF-8') as store_file:
            for row in csv.reader(store_file, delimiter=';'):
                name = row[0]
                departments = []
                for department_name in row[1:]:
                    departments.append(Department(department_name))
                self._stores.append(Store(name, departments))

    def save_to_database(self):
        with open('stores.cvs',mode='w', encoding='UTF-8') as store_file:
            for store in self._stores:
                store_file.write(f'{store.name}')
                for department in store.departments:
                    store_file.write(f';{department}')
                store_file.write('\n')

    def get_store(self, store_name: str):
        for store in self._stores:
            if store_name == store.name:
                return store
        return self._stores[0]
