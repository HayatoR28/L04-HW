from grade_compute import processLine, numberToGrade

## Has a main function to run the letter grade averaging program.

# Prompts the user for input, processes the grades, and displays the results in the terminal

# in an ASCII box. Handles quitting the program.

def main():

    """Main function to run the letter grade averaging program."""

    print("Welcome to the Letter Grade Averager!")

    print("Enter 4 letter grades separated by dollar signs (e.g., A$B+$c$d).")

    print("Type 'Q' to quit.")

    while True:

        user_input = input("Enter grades: ").strip()

        if user_input.upper() == 'Q':

            print("Exiting program. Goodbye!")

            break

        grades_list = user_input.split('$')

        if len(grades_list) != 4:

            print("Error: Please enter exactly 4 grades separated by dollar signs.")

            continue

        original_grades = [grade.strip().upper() for grade in grades_list]

        numerical_grades, lowest_grade_num = processLine(grades_list)

        if numerical_grades is None:

            continue

        numerical_grades.sort()

        grades_to_average = numerical_grades[1:]

        average_grade_num = sum(grades_to_average) / len(grades_to_average)

        if average_grade_num < 2.3:

            average_grade_num += 0.25

        lowest_letter = numberToGrade(lowest_grade_num)

        average_letter = numberToGrade(average_grade_num)

        box_width = 40

        content_width = box_width - 2

        top_border = "+" + "-" * content_width + "+"

        bottom_border = "+" + "-" * content_width + "+"

        print(top_border)

        print(f"| {'GRADE REPORT SUMMARY':^{content_width}} |")

        print(f"| {'-' * content_width} |") # Separator line

        grades_entered = 'Grades Entered: ' + ', '.join(original_grades)

        lowest_dropped = 'Lowest Grade Dropped: ' + lowest_letter

        calc_average = 'Calculated Average: ' + f'{average_grade_num:.2f}'

        final_grade = 'Final Letter Grade: ' + average_letter

        grades_entered = (grades_entered[:content_width] if len(grades_entered) > content_width else grades_entered).ljust(content_width)

        lowest_dropped = (lowest_dropped[:content_width] if len(lowest_dropped) > content_width else lowest_dropped).ljust(content_width)

        calc_average = (calc_average[:content_width] if len(calc_average) > content_width else calc_average).ljust(content_width)

        final_grade = (final_grade[:content_width] if len(final_grade) > content_width else final_grade).ljust(content_width)

        print(f"| {grades_entered} |")

        print(f"| {lowest_dropped} |")

        print(f"| {calc_average} |")

        print(f"| {final_grade} |")

        print(bottom_border)

        print("\n" + "=" * box_width + "\n") # Separator for next input

if __name__ == "__main__":

    main()