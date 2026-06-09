class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name


class Assessment:
    def __init__(self, attendance, assessment_score):
        self.attendance = attendance
        self.assessment_score = assessment_score


class PlacementManager:
    def __init__(self):
        self.students = []

    def add_student(self, student, assessment):
        self.students.append((student, assessment))

    def check_eligibility(self, assessment):
        return assessment.attendance >= 75 and assessment.assessment_score >= 60

    def generate_report(self):
        for student, assessment in self.students:
            status = "ELIGIBLE" if self.check_eligibility(assessment) else "NOT ELIGIBLE"

            print("=" * 50)
            print("          PLACEMENT ELIGIBILITY REPORT")
            print("=" * 50)
            print()
            print(f"Student ID       : {student.student_id}")
            print(f"Student Name     : {student.student_name}")
            print()
            print(f"Attendance       : {assessment.attendance}%")
            print(f"Assessment Score : {assessment.assessment_score}")
            print()
            print(f"Placement Status : {status}")
            print()
            print("=" * 50)


# Test Case
student = Student("S101", "Ava")
assessment = Assessment(85, 78)

manager = PlacementManager()
manager.add_student(student, assessment)
manager.generate_report()