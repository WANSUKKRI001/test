


#กำหนด แม่เริ่มต้น และ แม่สุดท้าย
s=int(input("ป้อนแม่สูตรคูณเริ่มต้น "))
e=int(input("ป้อนแม่สูตรคูณสุดท้าย "))
for i in range(s,e+1):
    print("แม่", i)
    for x in range(1,13):
        print(i,"x",x," = ", (i*x))