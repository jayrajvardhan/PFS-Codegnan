class person:
    university = "codegnan"
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

class student(person):
    student_count = 0
    def __init__(self, name, age, stu_id, dept, Course):
        super().__init__(name, age, dept)
        self.stu_id = stu_id
        self.dept = dept
        self.Course = Course
        student.student_count+=1
    def display_info(self):
        print(f"Name: {self.name}\n age:{self.age}\n stu_id:{self.stu_id}\n dept:{self.dept}\n Course:{self.Course}")

class faculty(person):
    faculty_count = 0
    def __init__(self, name, age, face_id, dept):
        super().__init__(name, age,dept)
        self.face_id = face_id
        self.dept = dept
        faculty.faculty_count += 1
    def display_info(self):
        print(f"Name: {self.name}\n age:{self.age}\n face_id:{self.face_id}\n dept:{self.dept}")

class Driver(person):
    Driver_count = 0
    def __init__(self, name, age, Experience,dept, licence_no):
        super().__init__(name, age, dept)
        self.Experience = Experience
        self.licence_no = licence_no
        Driver.Driver_count += 1
    def display_info(self):
        print(f"Name: {self.name}\n age:{self.age}\n Experience:{self.Experience}\n licence_no:{self.licence_no}")

class Cleaner(person):
    Cleaner_count = 0
    def __init__(self,name, age, Experience,dept):
        super().__init__(name, age, dept)
        self.Experience = Experience
        Cleaner.Cleaner_count += 1
    def display_info(self):
        print(f"Name: {self.name}\n age:{self.age}\n Experience:{self.Experience}\n dept:{self.dept}")


stu = student("Jayraj",21,"5H3", "CSE", "Python full stack")
stu.display_info()
faculty = faculty("Rajesh",45,996,"CSE")
faculty.display_info()
Dri = Driver("Ramarao", 48, 2, 4775, "AP305572")
Dri.display_info()
Clean = Cleaner("Subhash", 51, 3, "Buildings")
Clean.display_info()
