# CS-5103-Course-Project-Software-Engineering-Practice
#### Small personal project to get some experience on all the software engineering practices.

In order to run this project pandas needs to be installed.

    To install pandas run
    
    pip install pandas
    
    In case you have more than one python version available run
    
    pip3 install pandas

This project requires the user to input a file path when running the code.
**Example:**
python3 main.py test_file.txt

If the user does not provides the file path in the terminal, the program will ask for the path until it is a valid path

When a proper file path is inputed the program will open and read the file.
Line by line will split the words that are separated by space, tab, and new line characters.

When done will print in terminal each unique word and the how many times it repeats.