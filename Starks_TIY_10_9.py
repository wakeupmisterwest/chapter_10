from pathlib import Path

def read(path):
    try:
        contents = path.read_text().rstrip()
    except FileNotFoundError:
        pass
    else:
        lines = contents.splitlines()
        for line in lines:
            print(line)

filenames = ['dogs.txt', 'cats.txt']
for filename in filenames:
    path = Path(filename)
    read(path)