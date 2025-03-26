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

def sort_chars_by_count(char_dict):
    char_list = []

    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        char_list.append(char_info)

    def sort_on(dict):
        return dict["count"]

    char_list.sort(reverse=True, key=sort_on)
    
    return char_list   