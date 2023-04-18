#loop ซ้อน lopp
'''i=1
while i<=3:
    print("รอบที่ = ",i )
    j=1
    while j<=5:
        print("ตำแหน่ง.  = ",j)
        j+=1
    i+=1
   '''
'''
for i in range(1,4):
    print("รอบที่ = ", i)
    for j in range(1,6):
        print("ตำแหน่งที่ = ",j) '''


'''for m in range(2,4):
    print("แม่", m)
    for x in range(1,13):
        print(m,"x",x," = " ,(m*x))'''



#ทำแม่สูตรคูณแม่ 2 ด้วยการใช้ for
print("แม่3")
for m in range(1,13):
    
    print("3 x", m ," = ", 3*m)

print("แม่4") 
for m in range(1,13):
    print("4 x", m ," = ", 4*m)
    

'''#ทำแม่สูตรคูณแม่2-12ในคั้งเดียว ด้วยการใช้ for ซ้อน for
for i in range(2,13):
    print("แม่", i)
    for j in range(1,13):
        print(i,"x",j," = ", i*j)'''