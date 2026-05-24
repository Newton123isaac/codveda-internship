def count_words(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            #splits the words into list so it can be counted 
            words = content.split()
            words_count = len(words)
            char_count  = len(content)
            line_count = len(content.splitlines())

            print("========= FILE ANALYSIS ========")
            print(f"total words :  {words_count}")
            print(f"total characters:  {char_count}")
            print(f"total lines: {line_count}")

    except FileNotFoundError:
        print("Error: file not found ")
    except PermissionError:
        print("error: permission denied")
    except Exception as e: 
        print(f"Unexpected error {e}")

def main():
    print("==== WORD COUNTER PROGRAM ====")

    file_name = input("Enter file name: ").strip()
    if not file_name:
        print("Error : file cannot be empty")
        return
    count_words(file_name)

if __name__ == "__main__":
    main()