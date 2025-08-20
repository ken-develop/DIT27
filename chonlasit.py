# เครื่องคิดเลขแบบง่ายใน Python

def calculator():
    print("=== เครื่องคิดเลข ===")
    print("เลือกการทำงาน: ")
    print("1. บวก (+)")
    print("2. ลบ (-)")
    print("3. คูณ (*)")
    print("4. หาร (/)")
    
    choice = input("กรอกเลขที่เลือก (1/2/3/4): ")
    
    num1 = float(input("กรอกตัวเลขตัวแรก: "))
    num2 = float(input("กรอกตัวเลขตัวที่สอง: "))

    if choice == '1':
        print(f"ผลลัพธ์: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"ผลลัพธ์: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"ผลลัพธ์: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"ผลลัพธ์: {num1} / {num2} = {num1 / num2}")
        else:
            print("⚠️ ไม่สามารถหารด้วยศูนย์ได้")
    else:
        print("❌ เลือกไม่ถูกต้อง")

# เรียกใช้งาน
calculator()
