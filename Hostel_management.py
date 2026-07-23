class Student:
    def __init__(self, student_name, student_id, course):
        self.student_name = student_name
        self.student_id = student_id
        self.course = course
        self.fee_paid = 0
        self.room_no = None

    def pay_fee(self, amount):
        self.fee_paid += amount
        print("Fee paid successfully.")

    def allocate_room(self, room_no):
        self.room_no = room_no
        print("Room allocation successful")

    def display(self):
        print("------ Student Details ------")
        print("StudentName:", self.student_name)
        print("StudentID:", self.student_id)
        print("Course:", self.course)
        print("FeePaid:", self.fee_paid)
        print("Room No:", self.room_no)
        print("------------------------")

class HostelManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        sid = int(input("Enter Student ID: "))
        course = input("Enter Course Name: ")
        student = Student(name, sid, course)
        self.students.append(student)
        print("Student Added Successfully.")

    def find_student(self, sid):
        for student in self.students:
            if student.student_id == sid:
                return student
        return None

    def allocate_room(self):
        sid = int(input("Enter Student ID: "))
        student = self.find_student(sid)

        if student:
            room = int(input("Enter Room No: "))
            student.allocate_room(room)

        else:
            print("Student Not Found")

    def pay_fee(self):
        sid = int(input("Enter Student ID: "))
        student = self.find_student(sid)

        if student:
            amount = float(input("Enter fee amount: "))
            student.pay_fee(amount)
        else:
            print("Student Not Found")

    def display_student(self):
        sid = int(input("Enter Student ID: "))
        student = self.find_student(sid)
        if student:
            student.display()
        else:
            print("Student Not Found")

    def displayAll(self):
        if not self.students:
            print("No Student Found")
        else:
            for student in self.students:
                student.display()

hms = HostelManagementSystem()

while True:
    print("------------- Hostel Management System ----------------")
    print("1. Add Student")
    print("2. Allocate Room")
    print("3. pay fee")
    print("4. display Student")
    print("5. Display All")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        hms.add_student()
    elif choice == 2:
        hms.allocate_room()
    elif choice == 3:
        hms.pay_fee()
    elif choice == 4:
        hms.display_student()
    elif choice == 5:
        hms.displayAll()
    elif choice == 6:
        print("System Closed!")
        break

    else:
        print("Invalid Choice!")

