# Statistical Calculator (Mean, Median, Mode) in Python

## Project Description
Statistical Calculator is a simple Python-based program that allows users to calculate the **mean**, **median**, and **modus** of a set of numerical data. The program is designed with an interactive terminal interface, where the user can select the desired operation through a menu. The current version only supports single data, not grouped data.

This project was created to practice Python programming logic and understand basic statistical concepts, including the difference between theoretical calculations (position-based 1) and implementation in code (index-based 0).

## Features
- Calculates **Mean**: The average of all values.
- Calculates **Median**: The middle value after the data has been sorted.
- Calculates **Modus**: The most frequently occurring value (supports multiple modes if applicable).
- User input with error validation (only accepts comma separated numbers).
- Interactive menu with exit option.

## How to use
1. **Prerequisites**:
   - Make sure you have Python 3.x installed on your computer.

2. **Download and Run**:
   - Clone this repository:
     ``bash
    https://github.com/addictive378/statistical-calculator-v1.0.git
3. **Go to the project directory**:
   - cd [name-repo]
4. **Run the command**:
   - python [file-name]

## This program will display the menu 
=== Statistical Calculator Mean | Median | Modus ===
The version only supports single data, not group data.
Select the operation you want to perform:
1. Calculate Mean (Average)
2. Calculate Median
3. Calculate Modus
4. Exit

Enter numbers 1-4 to select the operation.
Type numeric data (separated by commas, e.g. 1, 2, 3, 4) when prompted.
Results will be displayed according to your selection.

Enter options 1 - 4: 1
Enter data in the form of numbers to be calculated (separate with ,) : 1, 2, 1, 3
Mean: 1.75

## Code Structure

    get_input_users(): Retrieves input from users and validates the data.
    calculate_mean(): Calculates the average using frequency.
    calculate_median(): Calculates the middle value of the sorted data.
    calculate_modus(): Finds the value with the highest frequency.
    show_menu(): Displays options to the user.
    main(): Sets up the program flow with an interactive loop.

## Note

    This program does not support grouped data or advanced statistical features such as quartiles.
    If all values appear with the same frequency, the mode will return all values as a list.

## Contributions

Suggestions and contributions are very welcome! Please fork this repository and create a pull request if you want to add features or improve the code.

## License
This project is free to use and modify for learning or personal purposes.
