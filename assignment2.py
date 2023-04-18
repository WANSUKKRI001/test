
#การคำนวนหาค่า bmi 

w=float(input("Enter Your weight "))
h=float(input("Enter Your height "))/100  # เอา n มาหารกับ 100

BMI= round(w/(h**2),4) # น้ำหนัก หารด้วย ส่วนสงยกกำลัง2 
# กำหนด ทศนิยมใช้ Round(  ,จำนวนที่ต้องการ) 

if BMI >= 30.0 and BMI< 40:
    result="โรคอ้วนอันตราย"
elif BMI > 25.0:
    result="โรคอ้วน"
elif BMI > 23.0:
    result="น้ำหนักเกิน"
elif BMI > 18.5:
    result="น้ำหนักเกิน"
else:
    result="น้ำหนักต่ำกว่าเกณฑ์"

print("ค่า BMI = ",BMI,"ผลคือ= ",result) 