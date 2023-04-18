# การนับจำนวนข้อความ

#string

# len  การนับจำนวน วิธีใช้ print(len(var))
# strip ลบช่องว่างซ้ายขว้า lstrip ลบซ้าย rstrip ลบขว้า วิธีใช้ name=name.strip/ print(name.strip())
# upper ทำให้เป็นตัวอักษรใหญ่ทั้งหมด วิธีใช้ print(name.upper()) 
# lower ทำให้เป็นตัวอักษรเล็กทั้งหมด วิธีใช้ print(name.lower())
# capitalize ทำให้ตัวด้านหน้าสุดเป็นตัวใหญ่ วิธีใช้ print(name.capitalize())
# replaceแทนที่เก่า วิธีใช้ print(name.replace("ข้อความเก่า" "ค่าใหม่"))
# in เช็คว่าอยู่ในตัวแปรหรือไหม วิธีใช้ x= "ข้าว" in name / print(x) 
# not in เช็คว่าอยู่ในตัวแปรหรือไหม วิธีใช้ x= "ข้าว"not in name / print(x) 
# format การจัดรูปแบบข้อความ 
# count การนับจำนวนประโยค print(name.count("ชื่อที่ต้องนับ"))
# startswith   เช็คคำขึ้นต้น print(name.startswith("คำขึ้นต้น"))
# endswith  เช็คคำลงท้าย print(name.endswith(เช่นเลขลงทายที่ต้องการ  0 ))


my_string = "Hello, World!"
print(my_string.find("World")) # Output: 7







'''
name="ไก่ เป็ด"
x= "ไข่" in name    /ถ้ามีไข้ในตัวแปร จะแสดง true ถ้าไม่มี false
print(x)

'''
# การต่อ string
'''
แบบที่ 1
fname= "n"
lname = "w" 
print(fname+lname)
'''
'''
แบบที่ 2
fullname = fname+ lname
'''
'''#การจัดรูปแบบการแสดงผล format {}
fname= "n"
lname = "w" 
text = "name:{}  lname: {}"
print(text.format(fname,lname))'''



#โครงสร้าง While

#สร้างตัวแปรเก็บค่า 
i=1
# เข้า loop while ตามด้วย เงื่อนไข้
while i<=5:
#แสดงผล
    print(i)
# เพิ่มค่าที่ละ1
    i+=1