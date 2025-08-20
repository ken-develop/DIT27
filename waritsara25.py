# เวอร์ชันวนซ้ำ ทำหลายรอบได้
while True:
    text = input("\nพิมพ์ q เพื่อออก หรือกด Enter เพื่อคำนวณต่อ: ").strip().lower()
    if text == "q":
        break

    try:
        a = float(input("ใส่ตัวเลขตัวที่ 1: "))
        op = input("เลือกเครื่องหมาย (+ หรือ -): ").strip()
        b = float(input("ใส่ตัวเลขตัวที่ 2: "))

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        else:
            print("❌ เครื่องหมายไม่ถูกต้อง ต้องเป็น + หรือ -")
            continue

        print(f"✅ ผลลัพธ์: {a} {op} {b} = {result}")
    except ValueError:
        print("❌ ใส่ตัวเลขไม่ถูกต้อง ลองใหม่อีกครั้ง")
