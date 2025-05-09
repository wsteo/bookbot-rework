def count_words(text_str):
    words_list = text_str.split()
    word_count = 0
    for word in words_list:
        word_count += 1
    
    return word_count

def count_characters(text_str):
    characters_count = {}

    for word in text_str.lower():
        if word not in characters_count:
            characters_count[word] = 1
        else:
            characters_count[word] += 1

    return characters_count

def sort_on(dict):
    return dict["num"]

def sort_character(character_count_dict):
    new_character_count = []
    for key, item in character_count_dict.items():
        new_character_count.append({"name":key, "num": item})

    new_character_count.sort(reverse=True, key=sort_on)
    return new_character_count
