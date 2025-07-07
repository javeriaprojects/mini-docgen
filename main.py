import ast

def extract_docstrings(file_path):
    with open(file_path, "r") as file:
        tree = ast.parse(file.read())

    docs = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
            name = getattr(node, "name", "Module")
            docstring = ast.get_docstring(node)
            if docstring:
                docs.append((name, docstring))

    return docs

def generate_markdown(doc_list):
    md = "# 📄 Extracted Documentation\n\n"
    for name, doc in doc_list:
        md += f"## {name}\n{doc}\n\n"
    return md

if __name__ == "__main__":
    file = "test_script.py"
    extracted = extract_docstrings(file)

    # Step 1: Print to terminal
    for name, doc in extracted:
        print(f"-- {name}\n{doc}\n")

    # Step 2: Format as markdown
    markdown = generate_markdown(extracted)

    # Step 3: Save to file
    with open("output/docs.md", "w") as f:
        f.write(markdown)

    print(" Documentation saved to output/docs.md")