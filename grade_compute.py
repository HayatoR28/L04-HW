## Converts a letter grade into its numerical equivalent on a 4.0 scale.

# IT can handle various letter grade formats (e.g., A+, B-, c, D+).

# Returns the numerical value or None if the input is invalid.

def gradeToNumber(letter_grade):

    """Converts a letter grade to a numerical value."""

    letter_grade = letter_grade.upper() # Ensure case-insensitivity

    if letter_grade == "A+":

        return 4.0

    elif letter_grade == "A":

        return 3.7

    elif letter_grade == "A-":

        return 3.3

    elif letter_grade == "B+":

        return 3.0

    elif letter_grade == "B":

        return 2.7

    elif letter_grade == "B-":

        return 2.3

    elif letter_grade == "C+":

        return 2.0

    elif letter_grade == "C":

        return 1.7

    elif letter_grade == "C-":

        return 1.3

    elif letter_grade == "D+":

        return 1.0

    elif letter_grade == "D":

        return 0.7

    elif letter_grade == "F":

        return 0.0

    else:

        return None

## Converts a numerical grade back into its letter grade equivalent.

# Handles the 4.0 scale and returns the corresponding letter grade.

# Returns None if the input number is outside the expected range.

def numberToGrade(number_grade):

    """Converts a numerical value back to a letter grade."""

    if number_grade >= 3.85:

        return "A+"

    elif number_grade >= 3.5:

        return "A"

    elif number_grade >= 3.15:

        return "A-"

    elif number_grade >= 2.85:

        return "B+"

    elif number_grade >= 2.5:

        return "B"

    elif number_grade >= 2.15:

        return "B-"

    elif number_grade >= 1.85:

        return "C+"

    elif number_grade >= 1.5:

        return "C"

    elif number_grade >= 1.15:

        return "C-"

    elif number_grade >= 0.85:

        return "D+"

    elif number_grade >= 0.5:

        return "D"

    elif number_grade >= 0.0:

        return "F"

    else:

        return None

## Processes a list of letter grades, validates them, converts them to numbers,

# and finds the lowest numerical grade.

# Returns a list of valid numerical grades and the lowest numerical grade,

# or (None, None) if any input grade is invalid.

def processLine(grades_input):

    """Processes a list of letter grades, validates, converts to numbers, and finds the lowest."""

    numerical_grades = []

    lowest_grade_num = 4.0

    for grade_str in grades_input:

        grade_str = grade_str.strip()

        if not grade_str:

            continue

        if not isValidGrade(grade_str):

            print(f"Error: '{grade_str}' is not a valid letter grade. Please use A+ through F.")

            return None, None # Indicate an error occurred

        num_grade = gradeToNumber(grade_str)

        if num_grade is None:

            return None, None

        numerical_grades.append(num_grade)

        if num_grade < lowest_grade_num:

            lowest_grade_num = num_grade

    if len(numerical_grades) != 4:

        return None, None

    return numerical_grades, lowest_grade_num

# Returns True if valid false otherwise

def isValidGrade(letter_grade):

    """Validates if a single letter grade input is within the acceptable range (A+ to F)."""

    letter_grade = letter_grade.upper() # Ensure case-insensitivity

    if (letter_grade == "A+" or letter_grade == "A" or letter_grade == "A-" or

        letter_grade == "B+" or letter_grade == "B" or letter_grade == "B-" or

        letter_grade == "C+" or letter_grade == "C" or letter_grade == "C-" or

        letter_grade == "D+" or letter_grade == "D" or letter_grade == "F"):

        return True

    else:

        return False