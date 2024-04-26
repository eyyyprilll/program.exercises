def write_to_file(sentence, choice):
    # Open the file for appending
    with open("mylife.txt", "a") as file:
        # Ask for confirmation
        if choice.lower() == 'yes':
            file.write(sentence + "\n")
            print("Sentence has been written to mylife.txt.")
            return True
        elif choice.lower() == 'no':
            print("No changes have been made.")
            return False
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
            return False

def main():
    continue_writing = True
    while continue_writing:
        sentence = input("Enter a sentence to write to mylife.txt: ")
        choice = input("Do you want to continue writing to mylife.txt? (yes/no): ")
        continue_writing = write_to_file(sentence, choice)

if __name__ == "__main__":
    main()
