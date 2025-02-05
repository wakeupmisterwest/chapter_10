from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
py_string = ''
for line in lines:
    py_string += line.lstrip()

print(py_string.replace('python','java'))