class Student:
    def __init__(self, first_name, last_name, gender, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.grade = grade
 
    def __repr__(self):
        return self.first_name
        
if __name__ == '__main__':
    student1 = Student('joe','boe','male',1)
    print(student1)