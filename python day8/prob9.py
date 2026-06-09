class Student:
    def placement_status(self):
        print("Placement Eligibility: Assessment Score Above 60")

class AdvancedStudent(Student):
    def placement_status(self):
        print("Placement Eligibility: Assessment Score Above 80")

student = AdvancedStudent()
student.placement_status()