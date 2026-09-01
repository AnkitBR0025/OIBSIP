# Random Password Generator (CLI)

A simple command-line tool made in Python.
It generates random passwords based on what the user picks.

## Why I made this

I wanted to practice loops, functions, and input validation in Python.
So I built something small but useful — a password generator.

## Features

- Minimum length of 8 characters. Anything less is rejected.
- Choose which character types to include: uppercase, lowercase, numbers, symbols.
- At least 2 character types must be selected.
- Every selected type is guaranteed to appear in the password.
- Handles wrong input like letters, blank input, or too-short length.
- Keeps running until the user says no. No need to restart the script.

## Project Structure

- `get_length()` — asks for password length and checks it's valid.
- `get_choices()` — asks which character types to use.
- `make_password()` — builds the password and shuffles it.
- `main()` — runs everything and handles the "generate again" loop.

## How to Run

1. Download the script file.
2. Open terminal in that folder.
3. Run this command:

```bash
python password_generator.py
```

4. Enter the password length when asked.
5. Answer y or n for each character type.
6. Your password will be printed on screen.
7. Type y to generate another, or n to exit.

## Example

```
Enter password length (min 8): 10
Uppercase letters? (y/n): y
Lowercase letters? (y/n): y
Numbers? (y/n): y
Symbols? (y/n): n

Generated Password: aB3fT9mZk2

Generate another password? (y/n): n
Goodbye!
```

## How the password is built

First, one character from each selected type is added.
This makes sure every chosen type actually shows up.
Then the rest of the password is filled randomly from the full pool.
At the end, everything is shuffled so the order isn't predictable.

## Future Improvements

- Add a GUI version using tkinter.
- Copy password directly to clipboard.
- Show password strength (weak/medium/strong).
- Use the `secrets` module instead of `random` for real security use cases.

## Tech Used

- Python
- `random` module
- `string` module

No extra installation needed. Just Python.