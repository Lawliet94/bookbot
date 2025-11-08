def count_words(book_text):
    """Return the number of words in the book."""
    return len(book_text.split())

def count_characters(book_text):
    """Return how many times each character appears in the book, treating uppercase and lowercase as the same."""
    score = {}
    for c in book_text:
        if c.lower() not in score.keys():
            score.update({c.lower(): 1})
        else:
            score[c.lower()] += 1
    return score

def sort_characters(character_count):
    """Return a string of alphabetic characters and their counts, sorted in descending order."""
    sorted = []
    sorted_dict = {}

    for k, v in character_count.items():
        if k.isalpha():
            sorted.append({"char": k, "num": v})
        else:
            continue

    def sort_on(items):
        return items["num"]
    
    sorted.sort(reverse=True, key= sort_on)
    for d in sorted:
        sorted_dict.update({d["char"]: d["num"]})
    
    return "".join(f"{k}: {v}\n" for k, v in sorted_dict.items()) 