import math
import subprocess
import os
def clearScr():
    if os.name in ('nt','dos'):
        subprocess.call("cls")
    elif os.name in ('linux','osx','posix'):
        subprocess.call("clear")

dividend = int(input("Enter dividend:"))
divisor = int(input("Enter divisor:"))



quotient = dividend//divisor
quo_list = []
divi_list = []

#divide quotient string into tokens
for i in str(quotient):
    quo_list.append(int(i))

for i in str(dividend):
    divi_list.append(i)

# print intial divide surface


#flag for keeping margin at first iteration of loop

# loop based upon quotient

def digitLen(arg):
    return len(str(arg))



def func(arg_list,arg_divi,arg_quo):
    clearScr()
    temp = "0"
    space = len(str(divisor))
    print(dividend," ","\u0332".join("|"+str(divisor)+(space*" ")))
    space = 0
    flag_out = False
    while arg_list:
        flag = False
        while divisor*int(arg_list[0]) > int(temp):
            if not arg_divi:
                flag = True
                break
            else:
                if temp=="0":
                    temp=""
                temp += str(arg_divi.pop(0))
                if flag_out:
                    space+=1     
        if flag:
           print(space*" ",temp)
           break
        
        #change outer flag value to increase margin on next steps
    
        divide = divisor * int(arg_list.pop(0))

        #if quotient is zero just move to next iteration as value of divide is zero
        if not divide:
            if arg_divi and not arg_list:
               print(space*" ",arg_divi.pop()) 
            continue
        
        if not flag_out:
            print("\u0332".join(str(divide)+(digitLen(dividend)+digitLen(divisor))*" "),arg_quo)
            flag_out=True
        else:
            print(space*" ",temp) 
            gimp = (space+1)*" "        
            print("\u0332".join((gimp+str(divide))))
        # subtract by multiplying with
        temp = str(int(temp) - divide) 
        
        if not arg_list:
            print(space*" ",temp)
            break        
    if arg_divi: #empty show result to user
        return True
    else:
        return False             

user_quo=[]

while True:
    user_quo.append(str(int(input("Enter next quotient value:"))))
    res = func(user_quo.copy(),divi_list.copy(),"".join(user_quo))
    if not res:
        if str("".join(user_quo)) == str(quotient):
            print("Your Answer is corrent")
            break
        else:
            print("Your quotient sequence is incorrect")
            inp = input("wanna see right answer (y/n):")
            if inp=="y":
                temp = "0"
                func(quo_list,divi_list,quotient)
                break
            else:
                print("Program ended")
                exit()                      