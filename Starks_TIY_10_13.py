from pathlib import Path
import json

def get_stored_user(path):
    """Get stored user if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None

def get_new_user(path):
    """Prompt for a new user."""
    username = input("What is your name? ")
    age = input("What is your age? ")
    color = input("What is your favorite color? ")

    user = {
        'username': username,
        'age': age,
        'color': color,
    }

    contents = json.dumps(user)
    path.write_text(contents)
    return user

def greet_user():
    """Greet the user by name."""
    path = Path('user.json')
    user = get_stored_user(path)
    if user:
        print(f"Welcome back, {user['username']}. You are {user['age']} years "
              f"old. Your favorite color is {user['color']}.")
    else:
        user = get_new_user(path)
        print(f"We'll remember you when you come back, {user['username']}!")

greet_user()