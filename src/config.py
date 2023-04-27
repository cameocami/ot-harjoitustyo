import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

PRODUCT_REPOSITORY = os.getenv("PRODUCT_REPOSITORY") or "products.csv"
PRODUCT_REPOSITORY_PATH = os.path.join(dirname, "..", "data", PRODUCT_REPOSITORY)

STORE_REPOSITORY = os.getenv("STORE_REPOSITORY") or "stores.csv"
STORE_REPOSITORY_PATH = os.path.join(dirname, "..", "data", STORE_REPOSITORY)
