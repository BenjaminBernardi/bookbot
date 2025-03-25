def get_number_of_words(text):
    words = text.split()
    counter = len(words)
    return counter

def get_number_of_characters(text):
    list = {}
    text_lower = text.lower()

    for character in text_lower:
        if character in list:
            list[character] += 1
        else:
            list[character] = 1
    
    return list