import sys

from stats import get_num_words, get_num_characters, create_new_dict


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    characters = get_num_characters(text)
    sorted_characters = create_new_dict(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for characters in sorted_characters:
        print(f"{characters["name"]}: {characters["num"]}")
    print("============= END ===============")


main()