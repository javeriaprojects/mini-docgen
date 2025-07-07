"""This module handles math operations."""

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

class Calculator:
    """A simple calculator class."""

    def multiply(self, x, y):
        """Multiplies two numbers."""
        return x * y
folder_path = "."  # or specify path like "my_scripts/"

docs_all = []

for filename in os.listdir(folder_path):
    if filename.endswith(".py") and filename != "main.py":
        file_path = os.path.join(folder_path, filename)
        extracted = extract_docstrings(file_path)
        docs_all.extend([(f"{filename} → {name}", doc) for name, doc in extracted])
folder_path = "."  # or specify path like "my_scripts/"

docs_all = []

for filename in os.listdir(folder_path):
    if filename.endswith(".py") and filename != "main.py":
        file_path = os.path.join(folder_path, filename)
        extracted = extract_docstrings(file_path)
        docs_all.extend([(f"{filename} → {name}", doc) for name, doc in extracted])