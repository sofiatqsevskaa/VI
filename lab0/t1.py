import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"


class Student:
    def __init__(self,fullname,index):
        self.fullname=fullname
        self.index=index
        self.courses={}
    
    def add_course(self,course,grade):
        self.courses[course]=grade
    
    def print_info(self):
        print(f"Student: {self.fullname}")
        for course, grade in self.courses.items():
            print(f"----{course}: {grade}")
        
        
def calculate_grade(score):
        if score <= 50:
            return 5
        elif score <= 60:
            return 6
        elif score <= 70:
            return 7
        elif score <= 80:
            return 8
        elif score <= 90:
            return 9
        else:
            return 10

def get_fullname(words):
    return words[0] + " " + words[1]

def calculate_total_points(words):
    return int(words[4]) + int(words[5]) + int(words[6])

def process_student_data(students):
    while True:
        user_input = input()
        if user_input == "end":
            break
        data = user_input.split(",")
        fullname = get_fullname(data)
        if int(data[2]) not in students:
            students[int(data[2])]=Student(fullname,data[2])
        points = calculate_total_points(data)
        grade = calculate_grade(points)
        students[int(data[2])].add_course(data[3],grade)

def print_student_info(students):
    for student in students.values():
        student.print_info()
        print()

if __name__ == "__main__":
    students = {}
    process_student_data(students)
    print_student_info(students)
  
        