import random
import time

names = ["Denis", "Georgi", "Maria", "Vladimir", "NotMyName", "Elizabeth", "Vasil", "Siyana", "Steven"]
places = ["New York", "Palm Beach", "Sofia", "Vienna", "London", "Beijing", "Rome", "Milano", "Varna", "Lisbon"]
verbs = ["eats", "plays", "is reading", "is running", "brings"]
nouns = ["tablet", "laptop", "apple", "cake", "stones", "mouse", "picture", "book", "phone"]
adverbs = ["warmly", "sadly", "diligently", "rapidly"]
details = ["at home", "at the bar", "in the park", "at the bus station", "on the street"]

my_name = input("Твоето име.")
names.append(my_name)

def get_random_word(words):
    return random.choice(words)


while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)



    print(f"{random_name}, from {random_place}, {random_verb}, {random_noun}, {random_adverb}, {random_detail}")
    if random_place == "Sofia":
        print("Best City tho ;)")
    input("Click [Enter] to generate a new one.")