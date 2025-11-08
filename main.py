from stats import count_words, count_characters

def get_book_text(book_path):
    with open(book_path, "r") as book:
        return book.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {count_words(book_text)} total words")
    character_count = count_characters(book_text)
    print(character_count)

if __name__ == "__main__":
    main()