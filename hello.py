# print("Hello Python")
# Base Class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks   # List of 5 subject marks


# Derived Class
class Result(Student):
    def __init__(self, name, marks):
        super().__init__(name, marks)
        self.total = 0
        self.percentage = 0
        self.grade = ""

    def calculate_result(self):
        self.total = sum(self.marks)
        self.percentage = self.total / len(self.marks)

        if self.percentage >= 90:
            self.grade = "A"
        elif self.percentage >= 75:
            self.grade = "B"
        elif self.percentage >= 60:
            self.grade = "C"
        elif self.percentage >= 40:
            self.grade = "D"
        else:
            self.grade = "F"

    def generate_marksheet(self):
        filename = f"{self.name}_Marksheet.txt"

        with open(filename, "w") as file:
            file.write("----------------------------------------\n")
            file.write("           STUDENT MARKSHEET\n")
            file.write("----------------------------------------\n")
            file.write(f"Name        : {self.name}\n")
            file.write("----------------------------------------\n")

            for i, mark in enumerate(self.marks):
                file.write(f"Subject {i+1}   : {mark}\n")

            file.write("----------------------------------------\n")
            file.write(f"Total       : {self.total}\n")
            file.write(f"Percentage  : {self.percentage:.2f}%\n")
            file.write(f"Grade       : {self.grade}\n")
            file.write("----------------------------------------\n")


# Main Program
def main():
    try:
        with open("students.txt", "r") as infile:
            lines = infile.readlines()

            for line in lines[:50]:   # Process first 50 students
                data = line.strip().split()

                name = data[0]
                marks = list(map(int, data[1:]))

                student = Result(name, marks)
                student.calculate_result()
                student.generate_marksheet()

        print("50 Marksheet files generated successfully!")

    except FileNotFoundError:
        print("Error: students.txt file not found!")


if __name__ == "__main__":
    main()