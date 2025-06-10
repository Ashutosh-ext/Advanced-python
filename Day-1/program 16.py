#report card generator
def report(name,marks,subject="python"):
    average = sum(marks)/len(marks)
    grade = "A" if average > 70 else "B" if average > 50 else "C"
    print(f"{name}'s {subject} Report\nMarks:{marks}\nGrade:{grade}")
report("Ashutosh",[84,78,81])