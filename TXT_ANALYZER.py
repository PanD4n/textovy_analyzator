'''
author =
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Daniel Proisl
email: dan.proisl@gmail.com
discord: Daniel P#9243
"""
import ...
'''
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

separator = "-" * 40
users = ("bob", "ann", "mike", "liz")
passwords = ("123", "pass123", "password123", "pass123")

registered_users = tuple(zip(users, passwords))

# print(registered_users)

username = input("Enter user name: ")
password = input("Enter password: ")

print(separator)

if (username, password) in registered_users:
    print(f"""Welcome to the app {username}
we have 3 texts to be analyzed
{separator}""")
    which_txt = (input("Enter a number btw. 1 and 3 to select: "))
    print(separator)

    if which_txt.isnumeric():

        if int(which_txt) in range(1, 4):
            chosen_txt = TEXTS[int(which_txt) - 1]
            txt_strip = chosen_txt.replace(",", "")
            txt_strip = txt_strip.replace(".", "")
            txt_split = txt_strip.split()

            word_count = len(txt_split)
            words_upper = int(0)
            words_lower = int(0)
            words_title = 0
            numbers = int(0)
            numbers_sum = int(0)

            print(f"There are {word_count} words in selected text")

            for word in txt_split:
                if word.isupper():
                    words_upper += 1
                elif word.islower():
                    words_lower += 1
                elif word.istitle():
                    words_title += 1
                elif word.isnumeric():
                    numbers += 1
                    numbers_sum = numbers_sum + int(word)

            print(f"There are {words_title} titlecase words")
            print(f"There are {words_upper} uppercase words")
            print(f"There are {words_lower} lowercase words")
            print(f"There are {numbers} numeric strings")
            print(f"The sum of all the numbers {numbers_sum}")

            wrds_l = {}
            for word in txt_split:
                if len(word) not in wrds_l.keys():   #wrods_len = {delka_slova : pocet_slov_dane_delky}
                    wrds_l[len(word)] = 1
                else:
                    wrds_l[len(word)] += 1

            words_len_sorted = sorted(list(wrds_l.keys()))
            mid_col_len = sorted(wrds_l.values())[-1] + 2

            print(separator)
            print(f"""{'LEN' :>2}|{'OCCURANCES'.center(mid_col_len)}|NR. """)
            print(separator)
            for length in words_len_sorted:
                print(f"""{length :>3}|{"*" * int(wrds_l[length]) :<{mid_col_len}}|{wrds_l[length]} """)

            # print(wrds_l)
            # print(words_len_sorted)
            # print(TEXTS[int(which_txt) -1])
    elif not which_txt.isnumeric():
        print("You have to enter a number between 1 nad 3")
    else:
        print("Wrong number")

else:
    print("Wrong username or password, terminating the program...")
