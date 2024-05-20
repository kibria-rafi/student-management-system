import csv

class StudentManagementSystem:
    def __init__(self, filename='students.csv'):
        self.filename = filename
        self.fields = ['id', 'name', 'age', 'grade']

    def add_student(self, student_id, name, age, grade):
        student = {
            'id': student_id,
            'name': name,
            'age': age,
            'grade': grade
        }
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fields)
            writer.writerow(student)
        print(f"Student {name} added successfully.")

    def view_students(self):
        try:
            with open(self.filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                students = list(reader)
                if not students:
                    print("No students found.")
                    return
                for student in students:
                    print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
        except FileNotFoundError:
            print("No students found.")

    def delete_student(self, student_id):
        students = []
        student_found = False
        try:
            with open(self.filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                students = list(reader)
            with open(self.filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fields)
                writer.writeheader()
                for student in students:
                    if student['id'] != student_id:
                        writer.writerow(student)
                    else:
                        student_found = True
                if student_found:
                    print(f"Student ID {student_id} deleted successfully.")
                else:
                    print(f"Student ID {student_id} not found.")
        except FileNotFoundError:
            print(f"Student ID {student_id} not found.")

    def search_student(self, student_id):
        try:
            with open(self.filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for student in reader:
                    if student['id'] == student_id:
                        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
                        return
            print(f"Student ID {student_id} not found.")
        except FileNotFoundError:
            print(f"Student ID {student_id} not found.")

def main():
    sms = StudentManagementSystem()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = input("Enter Student Age: ")
            grade = input("Enter Student Grade: ")
            sms.add_student(student_id, name, age, grade)
        elif choice == '2':
            sms.view_students()
        elif choice == '3':
            student_id = input("Enter Student ID to delete: ")
            sms.delete_student(student_id)
        elif choice == '4':
            student_id = input("Enter Student ID to search: ")
            sms.search_student(student_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
