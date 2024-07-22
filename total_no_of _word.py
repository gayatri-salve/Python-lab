#Write a function in Python to count and display the total number of words in a text file “ABC.txt”



def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()  # Read the entire content of the file
            words = content.split()  # Split the content into words
            total_words = len(words)  # Count the number of words
            print(f"Total number of words: {total_words}")
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# calling the function
count_words_in_file('XYZ.txt')


#Output

Total number of words: 22
