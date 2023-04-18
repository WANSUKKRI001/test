"""
ชนิดของข้อมูล
1. string
2. float
3. integer
4. boolean

"""
x= 1
y= 3.25
z="20"

#การแปลงชนิดข้อมูล
result = x+int(z) #แปลง z เป็น int
result =str(x)+z # แปลง x  เป็น string
result = float(z)+y # แปลง y เป็น float
print(result)

#วิธีเช็คชนิดของข้อมูล
print(type(x))