# Week 2 - Debugging and Troubleshooting Python
# Student Marks Management Program

def calculate_average(marks):
    total = 0

    for mark in marks:
        total = total + mark

    average = total / len(marks)
    return average


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def save_result(name, average, grade):
    file = open("results.txt", "w")
    file.write(name + "," + str(average) + "," + grade + "\n")
    file.close()


def main():
    print("Student Marks Management System")

    name = input("Enter student name: ")

    marks = []

    for i in range(1, 4):
        while True:
            try:
                mark = int(input("Enter mark " + str(i) + ": "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Mark must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    average = calculate_average(marks)  
    grade = get_grade(average)

    print("\nStudent:", name)
    print("Average:", average)
    print("Grade:", grade)

    save_result(name, average, grade)


main()