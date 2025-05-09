import sys
from stats import count_words, count_characters, sort_character

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
        return file_content

def main():
    if len(sys.argv) == 2:  
        file_path = sys.argv[1]
        book_text = get_book_text(file_path)
        num_words = count_words(book_text)
        num_characters = count_characters(book_text)
        sorted_characters = sort_character(num_characters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for character in sorted_characters:
            if character["name"].isalpha():
                print(f"{character["name"]}: {character["num"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


if __name__ == "__main__":
    main()
