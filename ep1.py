


'''#หา
max,min= 1,10

while True:
    num=int(input("Enter = "))
    if num<1:
        break
    if num>max:
        max=num
    if num<min:
        min=num

print(max)
print(min)'''
'''
#ทำตัวเลขขั้นบันได
l= int(input("Enter = ")) #5

for row in range(1,l+1):
    for column in range(1,row+1):
        print(column,end="") #edn ทำให้เป็นแนวนอน
    print("")
'''



n=int(input("Enter = "))

for row in range(n):
    for column in range(n):
        print("x" , end=" ")
    print(" ")