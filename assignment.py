

# การแลกเงินและหาจำนวนแบงค์

n= int(input("Enter your Number "))
if n >= 1000:
    print("1000",n//1000,"ใบ") # หารปัดเศษ n=จำนวนที่ป้อน เ
    n%=1000 # เอาเศษเพื่อใช้งานต่อกับเงื่อนไข้ถัดไป
if n>=500:
    print("500",n//500,"ใบ")
    n%=500
if n>=100:
    print("100",n//100,"ใบ")
    n%=100
if n>=50:
    print("50",n//50,"ใบ")
    n%=50
if n>=20:
    print("20",n//20,"ใบ")