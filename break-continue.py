

#break  สั่งให้ออกจากloop เมื่อเงื่อนไขเป็นจริง  
#continue สั่งให้กระโดดข้ามรอบนั้นที่เรากำหนดเมื่อเงื่อนไข้เป็นจริง

'''
#break with while
i=1
while i<= 10:
    print(i) #แสดงผล
    if i == 5: 
        break
    i+=1  # เพิ่มค่าที่หลัง


#continue with while
i=1
while i<=10:
    i+=1  # เพิ่มค่าก่อน
    if i==5:
        continue
    print(i) #ค่อยแสดงผล



# break with for
for i in range(1,10):
    print(i)  #แสดงผลก่อน
    if i==5:
        break
    i+=1   #ค่อยมาบวก

# continue with  for
for i in range(1,10):
    i+=1  # เพิ่มก่อน
    if i==5:
        continue
    print(i) #แสดงผลที่หลัง
    '''
i=1
while i <=10:
    
    print(i%2 )
    i+=1