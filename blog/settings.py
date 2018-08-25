import os


def parent_dir(path):
    return os.path.abspath(os.path.join(path, os.pardir))


APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = parent_dir(APP_DIR)
# In order to deploy to Github pages, you must build the static files to the project root
FREEZER_DESTINATION = PROJECT_ROOT
# This is a repo page(not a GH user page). We need to set the BASE_URL to the correct url as per GH Pages' standards
# FREEZER_BASE_URL = "http://localhost/{0}".format("vasiuadriana.github.io/")
# IMPORTANT: If this is True, all app files will be deleted when you run the freezer
FREEZER_REMOVE_EXTRA_FILES = False
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'

DEBUG = True
