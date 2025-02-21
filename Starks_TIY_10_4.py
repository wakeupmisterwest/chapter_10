from pathlib import Path

contents = input()

path = Path('guest.txt')
path.write_text(contents)