from datetime import datetime

def calculate_age(birthdate_str):
    # แปลง string เป็น datetime (รูปแบบ วัน/เดือน/ปี)
    birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
    today = datetime.today()

    age = today.year - birthdate.year

    # ถ้าวันเดือนปีนี้ยังไม่ถึงวันเกิด ให้ลบอายุ 1 ปี
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age

# รับวันเกิดจากผู้ใช้
birthdate_input = input("กรุณากรอกวันเกิดของคุณ (วัน/เดือน/ปี เช่น 13/08/2000): ")
age = calculate_age(birthdate_input)
print(f"คุณมีอายุ {age} ปี")