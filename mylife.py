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
