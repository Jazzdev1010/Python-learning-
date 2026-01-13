student_name = input("Enter Student's Name: ")
student_mark = int(input("Enter Student's Mark: "))
student_attendance = int(input("Enter Student's Attendance Percentage: "))

def exam_eligibility(name, marks, attendance):
    # Check eligibility
    if marks >= 40 and attendance >= 75:
        print(f"Student Name: {name.upper()}")
        print("Status: Eligible for Exam")

        # Grade calculation
        if marks >= 80:
            print("Grade: A")
        elif marks >= 60:
            print("Grade: B")
        else:
            print("Grade: C")
    else:
        print("Status: Not Eligible for Exam")
        if marks < 40:
            print("Reason: Minimum 40 marks required")
        if attendance < 75:
            print("Reason: Minimum 75% attendance required")

exam_eligibility(student_name, student_mark, student_attendance)
