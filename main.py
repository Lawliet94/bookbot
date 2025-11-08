from stats import count_words, count_characters, sort_characters

def get_book_text(book_path):
    with open(book_path, "r") as book:
        return book.read()
    
def report_results(text_path):
    with open(text_path, "r") as text:
        return text.read()

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    sorted_characters = sort_characters(character_count)

    report_path = "report.txt"
    report = report_results(report_path)
    print(report.format(book_path=book_path, word_count=word_count, sorted_characters=sorted_characters))

if __name__ == "__main__":
    main()