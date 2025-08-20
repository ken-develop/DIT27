# ฟังก์ชันสำหรับเครื่องคิดเลข
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "ไม่สามารถหารด้วยศูนย์ได้"

# แสดงเมนู
print("เลือกการคำนวณ:")
print("1. บวก")
print("2. ลบ")
print("3. คูณ")
print("4. หาร")

# รับค่าจากผู้ใช้
choice = input("กรุณาเลือกตัวเลข (1/2/3/4): ")

num1 = float(input("กรุณาใส่ตัวเลขตัวแรก: "))
num2 = float(input("กรุณาใส่ตัวเลขตัวที่สอง: "))

# คำนวณและแสดงผลลัพธ์
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("เลือกไม่ถูกต้อง")
