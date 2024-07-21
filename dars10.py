# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number
#         self.__balance = balance

#     def get_account_number(self):
#         return self.__account_number

#     def get_balance(self):
#         return self.__balance


# account = BankAccount("123456789", 1000)
# print(account.get_account_number())
# print(account.get_balance())

###############

### 2

# class Employee:
#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary

#     def get_name(self):
#         return self.__name

#     def get_salary(self):
#         return self.__salary

#     def set_name(self, name):
#         self.__name = name

#     def set_salary(self, salary):
#         if salary > 0:
#             self.__salary = salary
#         else:
#             print("Salary must be positive!")

# employee = Employee("Alice", 70000)
# print(employee.get_name())
# print(employee.get_salary())
# employee.set_name("Bob")
# employee.set_salary(80000)
# print(employee.get_name())
# print(employee.get_salary())


##################

### 3

# class Student:
#     def __init__(self, student_id, grades):
#         self.__student_id = student_id
#         self.__grades = grades

#     def get_student_id(self):
#         return self.__student_id

#     def get_grades(self):
#         return self.__grades

#     def set_student_id(self, student_id):
#         self.__student_id = student_id

#     def add_grade(self, grade):
#         if 0 <= grade <= 100:
#             self.__grades.append(grade)
#         else:
#             print("Invalid grade!")

# student = Student("S12345", [85, 90, 78])
# print(student.get_student_id())
# print(student.get_grades())
# student.set_student_id("S54321")
# student.add_grade(95)
# print(student.get_student_id())
# print(student.get_grades())


##########################################################

#LeetCode

# class Solution(object):
#     def maximumWealth(self, accounts):
#         a = 0
#         for i in accounts:
#             if sum(i) > a:
#                 a = sum(i)
            
#         return a

# s = Solution()
# accounts = [[1,2,3],[3,2,1]]
# print(s.maximumWealth(accounts))