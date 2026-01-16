try:
    # read file
    with open("data.txt", "r") as file:
        content = file.read()

    print("Original Content:\n")
    print(content)

    # replace word
    old_word = "Python"
    new_word = "Java"

    modified_content = content.replace(old_word, new_word)

    # Modified content 
    with open("data.txt", "w") as file:
        file.write(modified_content)

    print("\nModified Content Saved Successfully!")

except FileNotFoundError:
    print("Error: File not found. Please check file name.")

except PermissionError:
    print("Error: Permission denied while accessing the file.")

except Exception as e:
    print("Unexpected Error:", e)
