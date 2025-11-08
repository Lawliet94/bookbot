def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    score = {}

    for c in book_text:
        if c.lower() not in score.keys():
            score.update({c.lower(): 1})
        else:
            score[c.lower()] += 1
    return score