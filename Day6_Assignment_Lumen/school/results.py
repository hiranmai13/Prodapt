def calculate_grade(marks):
    if marks >= 90:
        return "A Grade"
    elif marks >= 75:
        return "B Grade"
    elif marks >= 50:
        return "C Grade"
    else:
        return "Fail"