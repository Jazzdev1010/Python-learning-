import requests

def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    else:
        return "C"

def exam_eligibility(name, marks, attendance):
    # Check eligibility
    if marks >= 40 and attendance >= 75:
        print(f"Student Name: {name.upper()}")
        print("Status: Eligible for Exam")

        # Grade calculation
        grade = get_grade(marks)

    else:
        print("Status: Not Eligible for Exam")
        if marks < 40:
            print("Reason: Minimum 40 marks required")
        if attendance < 75:
            print("Reason: Minimum 75% attendance required")
            
if __name__ == "__main__":
    student_name = input("Enter Student's Name: ")
    student_mark = int(input("Enter Student's Mark: "))
    student_attendance = int(input("Enter Student's Attendance Percentage: "))

    exam_eligibility(student_name, student_mark, student_attendance)
