from pathlib import Path

contents = '\nWhat is your name?'
contents += '\nEnter "n" when you are done: '

names = []
while True:
    name = input(contents)
    if name == 'n':
        break

    print(f"Name added: {name}")
    names.append(name)

contents = ''
for name in names:
    contents += f'{name}\n'

path = Path('guest_book.txt')
path.write_text(contents)