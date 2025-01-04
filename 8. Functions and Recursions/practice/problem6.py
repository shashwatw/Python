# Func to remove a word from the list and strip at the same time

list = ["Shashwat", "Rohan", "Shubham", "an"]


def remove_word(list, word):
    for item in list:
        list.remove(word)
        return list

def rem(list, word):
    n = []
    for item in list:
        if not(item == word):
            n.append(item.strip(word))
    return n


print(rem(list, "an"));