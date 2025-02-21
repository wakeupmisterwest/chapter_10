from pathlib import Path

def common_words(filename, word):
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, file {path} not found")
    else:
        words = contents.lower().count(word)
        message = f"{word} appears {words} times in {filename}"
        print(message)

common_words('metamorphosis.txt','gregor')