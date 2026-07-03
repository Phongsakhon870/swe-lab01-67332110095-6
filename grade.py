def calculate_grade(scores):
    # 1. ตรวจสอบก่อนว่าลิสต์ว่างหรือไม่ เพื่อป้องกัน ZeroDivisionError
    if not scores:
        return "N/A", 0

    # 2. ใช้ฟังก์ชัน sum() เพื่อความรวดเร็วและอ่านง่าย
    try:
        total = sum(scores)
    except TypeError:
        return "Error: ข้อมูลในลิสต์ต้องเป็นตัวเลขเท่านั้น", 0

    average = total / len(scores)

    # การตัดเกรด
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return grade, average

# ทดสอบกรณีปกติ
scores = [85, 92, 78, 88, 95]
grade, avg = calculate_grade(scores)
print(f"Average: {avg}, Grade: {grade}")

# ทดสอบกรณีลิสต์ว่าง (เพื่อเช็คว่า Bug หายไปไหม)
empty_scores = []
print(f"Empty list test: {calculate_grade(empty_scores)}")
