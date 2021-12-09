import sys
import random

list = [0,1,2]
fist = int(input("請輸入石頭(0)，布(1)，剪刀(2):"))
def fun(ans,fist):
        if(ans==fist):
            return(4)
        elif(ans == 0 and fist == 2)or(ans == 1 and fist == 0)or(ans == 2 and fist == 1):
            return(5)
        elif(ans == 2 and fist== 0 )or(ans == 0 and fist== 1 )or(ans== 1 and fist== 2):
            return(6)
ans = random.choice(list)
a=fun(ans,fist)


while a!=6 :
    list = [0,1,2]
    if(ans==0):
        print("電腦出石頭")
    elif(ans==1):
        print("電腦出布")
    elif(ans==2):
        print("電腦出剪刀")
    if(fist==0):
        print("你出石頭")
    elif(fist==1):
        print("你出布")
    elif(fist==2):
        print("你出剪刀")
    if(a==4):
        print("平手")
        ans = random.choice(list)
        fist = int(input("請輸入石頭(0)，布(1)，剪刀(2):"))
        a=fun(ans,fist)
    elif(a==5):
        print("你輸了")
        ans = random.choice(list)
        fist = int(input("請輸入石頭(0)，布(1)，剪刀(2):"))
        a=fun(ans,fist)
    
if(ans==0):
    print("電腦出石頭")
elif(ans==1):
    print("電腦出布")
elif(ans==2):
    print("電腦出剪刀")
if(fist==0):
    print("你出石頭")
elif(fist==1):
    print("你出布")
elif(fist==2):
    print("你出剪刀")
print("你贏了")
    # print(ans)
    # print(fist)
    
    
