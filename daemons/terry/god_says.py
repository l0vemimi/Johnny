import random

animals = ["cats", "dogs", "frogs", "elephants", "bears", "monkeys"]
actions = ["jumping", "coding", "blazing", "flying", "spinning", "bouncing"]
objects = ["cars", "computers", "chairs", "neon lights", "phones", "windows"]
nature = ["trees", "mountains", "rivers", "clouds", "volcanoes", "oceans"]
random_words = ["quantum", "time", "shifting", "eternal", "sacred", "infinite", "holy", "bizarre"]

def god_says():
    all_words = animals + actions + objects + nature + random_words
    random.shuffle(all_words)  
    sentence = "God says: " + " ".join(all_words[:random.randint(5, 12)]) + "!"  
    return sentence
