import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage



def list_entries():
    """
    Returns a list of all names of entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def get_entry(title):
    """
    Retrieves an entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
