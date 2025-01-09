def main():
    file_path = "books/frankenstein.txt"
    file_text = get_book_text(file_path)
    print(f"--- Begin report for file {file_path} ---")
    print(f"\nThis file has {count_words(file_text)} words.")
    print(f"\nCharacters found in file:")
    #### alpha sort by key
    # for char, count in sorted(count_characters(file_text).items()):
    #     print(F"\t{char}: {count}")
    ###sort by value in dictionary
    for char, count in sorted(count_characters(file_text).items(), key=lambda x: x[1], reverse=True):
        print(F"\t{char}: {count}")
    print(f"\n--- End report for file {file_path} ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    character_dict = {}
    for char in text.lower():
        if char.isalpha():
            character_dict[char] = character_dict.get(char,0) + 1
    return character_dict

if __name__ == "__main__":
    main()