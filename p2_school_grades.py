https://replit.com/join/gwllzkuclh-maria-fernan901
#Link code replit

# Function to calculate statistics from a list of grades
def calculate_statistics(grades):
    num_students = len(grades)
    if num_students == 0:
        return None, None, None, 0, 0

    total_grades = sum(grades)
    average_grade = total_grades / num_students
    highest_grade = max(grades)
    lowest_grade = min(grades)

    passed_count = len([grade for grade in grades if grade >= 60])
    failed_count = num_students - passed_count

    return average_grade, highest_grade, lowest_grade, passed_count, failed_count

# Main program
def main():
    print("Welcome to the Student Grade Statistics Program!")
    
    try:
        num_students = int(input("Enter the number of students: "))
        grades = []
        for i in range(num_students):
            grade = float(input(f"Enter the grade for student {i + 1}: "))
            grades.append(grade)
        
        average_grade, highest_grade, lowest_grade, passed_count, failed_count = calculate_statistics(grades)
        
        if average_grade is not None:
            print(f"Average Grade: {average_grade:.2f}")
            print(f"Highest Grade: {highest_grade}")
            print(f"Lowest Grade: {lowest_grade}")
            print(f"Number of Students Passed: {passed_count}")
            print(f"Number of Students Failed: {failed_count}")
        else:
            print("No grades entered. Cannot calculate statistics.")
    except ValueError:
        print("Invalid input. Please enter valid numeric values for grades.")

if __name__ == "__main__":
    main()
