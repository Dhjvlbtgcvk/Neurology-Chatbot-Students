import os
from pathlib import Path

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/data_loader.py",
    "src/vector_store.py",
    "src/qa_chain.py",
    "research/trials.ipynb",
    "research/test.py",
    ".env",
    "requirements.txt",
    "app.py",
    "setup.py",
]

for file in list_of_files:
    path = Path(file)
    dir_name, file_name = os.path.split(path)

    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path, 'w') as f:
            pass
    else:
        print(f"'{file}' already exists.")
