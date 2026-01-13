from exam_eligibility import exam_eligibility

student_name = input("Enter Student's Name: ")
student_mark = int(input("Enter Student's Mark: "))
student_attendance = int(input("Enter Student's Attendance Percentage: "))

exam_eligibility(student_name, student_mark, student_attendance)