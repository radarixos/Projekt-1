"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Radek Svejda

email: ok1vbr@gmail.com

discord: radarixos
"""
# ver 1.0 alfa
# tnxai!

import sys
import string

# Users list
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Texts from external source
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright
         red, purple, yellow and gray beds of the Wasatch
         Formation. Eroded portions of these horizontal
         beds slope gradually upward from the valley floor
         and steepen abruptly. Overlying them and extending
         to the top of the butte are the much steeper
         buff-to-white beds of the Green River Formation,
         which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects
         a portion of the largest deposit of freshwater fish
         fossils in the world. The richest fossil fish deposits
         are found in multiple limestone layers, which lie some
         100 feet below the top of the butte. The fossils
         represent several varieties of perch, as well as
         other freshwater genera and herring similar to those
         in modern oceans. Other fish such as paddlefish,
         garpike and stingray are also present.'''
         ]


def authenticate(username, password):
    return users.get(username) == password


def get_text_choice():
    try:
        choice = int(input("Enter a number between 1 and 3 to select: "))
        if choice not in [1, 2, 3]:
            print("Invalid choice, terminating the program...")
            sys.exit()
        return TEXTS[choice - 1]
    except ValueError:
        print("Invalid input, terminating the program...")
        sys.exit()


def clean_word(word):
    return word.strip(string.punctuation)


def is_lowercase(word):
    return word.islower() or (any(char.isdigit() for char in word) and any(char.isupper() for char in word))

# US a 30N issue
"""
def is_titlecase(word):
    if len(word) > 1:
        return word[0].isupper() or word[1].isupper()
    elif len(word) == 1:
        return word[0].isupper()
    return False
    """
def is_titlecase(word):
    return len(word) > 0 and word[0].isupper() or (len(word) > 1 and word[1].isupper())


def analyze_text(text):
    words = text.split()
    cleaned_words = [clean_word(word) for word in words]

    num_words = len(cleaned_words)
    titlecase_words = [word for word in cleaned_words if is_titlecase(word)]
    uppercase_words = [word for word in cleaned_words if word.isupper() and word.isalpha()]
    lowercase_words = [word for word in cleaned_words if is_lowercase(word)]
    numeric_strings = [word for word in cleaned_words if word.isdigit()]
    sum_of_numbers = sum(int(word) for word in cleaned_words if word.isdigit())

    print(f"There are {num_words} words in the selected text.")
    print(f"There are {len(titlecase_words)} titlecase words.")
    print(f"There are {len(uppercase_words)} uppercase words.")
    print(f"There are {len(lowercase_words)} lowercase words.")
    print(f"There are {len(numeric_strings)} numeric strings.")
    print(f"The sum of all the numbers is {sum_of_numbers}")
    print("----------------------------------------")

    word_lengths = {}
    for word in cleaned_words:
        word_length = len(word)
        if word_length in word_lengths:
            word_lengths[word_length] += 1
        else:
            word_lengths[word_length] = 1

    maxstars = 15

    print(f"{'LEN':<3}| {'OCCURRENCES':<{maxstars}} |NR.")
    print("----------------------------------------")
    for length in sorted(word_lengths):
        occurrences = word_lengths[length]
        if occurrences > maxstars:
            stars = '*' * (maxstars - 1) + '+'
        else:
            stars = '*' * occurrences
        print(f"{length:<3}| {stars:<{maxstars}} |{word_lengths[length]}")


def main():
    username = input("username: ")
    password = input("password: ")

    if authenticate(username, password):
        print("----------------------------------------")
        print(f"Welcome to the app, {username}")
        print("We have 3 texts to be analyzed.")
        print("----------------------------------------")
        text = get_text_choice()
        print("----------------------------------------")
        analyze_text(text)
    else:
        print("unregistered user, terminating the program..")


if __name__ == "__main__":
    main()
