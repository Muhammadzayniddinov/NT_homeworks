class Members:
  member_num = 0
  def __init__(self, username, email, age):
    self.name = username
    self.email = email
    self.age = age
  
  @classmethod
  def member_counter(cls):
    cls.member_num += 1
    return cls.member_num
  
  def display_info(self):
    return f"{Members.member_counter()}. Name: {self.name}, Age: {self.age}, Email: {self.email}"


class Student(Members):
  def __init__(self, username, email, age, student_id): 
      super().__init__(username, email, age)
      self.student_id = student_id
      self.courses = {}

  def enroll_in_course(self, course: str):
      self.courses[course] = None

  def set_grade(self, course: str, grade: float):
     self.courses[course] = grade

  @property
  def get_avarage_grade(self):
     grades = [v for v in self.courses.values()]
     return sum(grades) / len(grades)
  
  def display_info(self):
     courses_info = ", ".join(f"{course}: {grades}" for course, grades in self.courses.items())
     return f'Student \n {super().display_info()} Student id: {self.student_id} \n Courses: {courses_info} \n Average grade: {student1.get_avarage_grade}.'

class Teacher(Members):
  def __init__(self, username, email, age, teacher_id):
      super().__init__(username, email, age)
      self.teacher_id = teacher_id
      self.subjects = []

  def assign_subject(self, subject):
     self.subjects.append(subject)

  def display_info(self):
     return f'Teacher \n {super().display_info()} Teacher id: {self.teacher_id}  \n {self.subjects} dan dars beradi.'

class AdminStaff(Members):
  def __init__(self, username, email, age, staff_id, department):
      super().__init__(username, email, age)
      self.staff_id = staff_id
      self.department = department
  
  def display_info(self):
     return f'Admin \n {super().display_info()} Staff id : {self.staff_id} \n {self.department} bo\'limida ishlaydi.'




student1 = Student('M', 17, 'a@mail.com', 1)
teacher1 = Teacher('Professor', 'm@gmail.com' ,72 ,1)
staff1 = AdminStaff('S', 's@gmail.com', 22, 1, 'Olma')

student1.enroll_in_course('Math')
student1.set_grade('Math', 85)
student1.enroll_in_course('Physics')
student1.set_grade('Physics', 78)

teacher1.assign_subject("History")

print(student1.display_info())
print(teacher1.display_info())
print(staff1.display_info())