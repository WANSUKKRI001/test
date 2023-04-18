

#ทำตาราง 8*8
n= 8

for row in range(n):
    for column in range(n):
        if row==0 or row==n-1 or column==0 or column==n-1:  #ถ้าrowเท่ากับ0 ให้แสดงบนสุด หรือ row==n-1 ให้แสดงล่างสุด
            print("x" ,end=" ")                              #ถ้าcolumnเท่ากับ0 ให้แสดงบนสุด หรือcolumn==n-1 ให้แสดงล่างสุด
        else : 
            print(" ", end=" ")
    print(" ")
 