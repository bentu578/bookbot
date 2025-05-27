def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def chars_dict_to_sorted_list(char_dict):
    sorted_list = []

    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]