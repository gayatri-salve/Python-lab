#Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.


def read_file_line_by_line(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line, end='')  # end='' avoids adding extra newline
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# calling function
read_file_line_by_line('XYZ.txt')


#Output

Python is used for data analytics and it is very easy to learn.