def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    new_dict = {}
    for char in text:
        if char.lower() not in new_dict:
            new_dict[char.lower()] = 1
        else:
            new_dict[char.lower()] += 1

    return new_dict

def sort_on(items):
    return items["num"]

def create_new_dict(dictionary):
    list_characters = []
    for key, value in dictionary.items():
        if key.isalpha():
            characters = {"name": key, "num": value}
            list_characters.append(characters)

    list_characters.sort(reverse=True, key=sort_on)

    return list_characters