'''
#เกมทายเลข
import random

m= random.randrange(1,10)  #การกำหนดช่วงในการสุ่มในช่วงใด
print(m)
k=1
correct=False
while True:
    number=int(input("ป้อนคำตอบ = "))
    correct=(number==m)  #true / false
    
    if not correct :
        if number>m:
            print("น้อยกว่า")
        if number<m:
            print("มากกว่า")

        
    if correct:
        print("ต้องถูก555555555")
        break
    if number<0 or k==3 :
        break
    k+=1
print(" ")
if  not correct:
    print("เสียใจ")
print("เฉลย",m)
    
'''
#  เกมทายตัวเลข
import random #นำเข้า funtion random มาทำงาน

m=random.randrange(1,9) # เริม 1  สิ้นสุด 9
k=0  # จำนวนloop 
print(m)
while True:  #loop เรื่อยๆ จนกว่าจะเป็นจริง
    n= int(input("ป้อนตัวเลข =  "))
    c=n==m    #cคิอตัวแปร ถูก    n=ตัวแปรตัวเลขที่ป้อน  m=เฉลย random
    if not c:  # ถ้าc ไม่เท่ากับ !c=n==m  ให้แสดงข้อความ
        if n>m:
            print("น้อยกว่า")
        if n<m:
            print("มากกว่า")
    if c:        #ถ้าc=n==m ให้แสดง ถูก ถ้าไม่ ผิด
        print("ถูก")
        break  #ถ้าตอบถูกจะหยุดการทำงาน
    k+=1
    if k==3:   # ถ้า k==3 จะหยุดการทำงาน 
        print("ครบกำหนดแล้ว")
        break
print(" ")
if not c:  #ถ้า c ไม่เท่ากับ n==m ให้แสดงข้อความ
    print("เสียใจด้วย")
    print("เฉลย= ",m)

       