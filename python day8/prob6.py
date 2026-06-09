class Course:
    def course_fee(self):
        print("Course Fee: ₹5000")

class AdvancedCourse(Course):
    def course_fee(self):
        print("Course Fee: ₹12000")

course_type = input().strip()

if course_type == "Advanced Course":
    course = AdvancedCourse()
else:
    course = Course()

course.course_fee()