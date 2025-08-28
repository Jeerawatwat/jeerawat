""" เขียน function ชื่อ calculate_circle ที่มีคุณสมบัติดังนี้:

รับ parameter 1 ตัว คือ radius
return dictionary ที่มี area และ circumference
ใช้ค่า π = 3.14159
ปัดเศษทั้งสองค่าให้เหลือ 2 ตำแหน่งหลังจุดทศนิยม """
def calculate_circle(radius):
    pi = 3.14159
    area = round(pi * radius ** 2, 2)
    circumference = round(2 * pi * radius, 2)
    return {
        "area": area,
        "circumference": circumference
    }
result = calculate_circle(5)
print(result)
