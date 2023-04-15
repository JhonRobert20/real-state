import os

from real_state.settings import *  # noqa

MONGO_DB_DATABASE = os.environ.get("MONGO_DB_DATABASE", "test")
