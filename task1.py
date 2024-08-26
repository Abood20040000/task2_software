viseNumber=str(input("Enter the vise num:").strip())

sum=""
sum2=0
finalsum=0

for i in range(0,len(viseNumber),2):
    sum+=str(int(viseNumber[i])*2)
for i in range(0,len(sum)):
    sum2+=int(sum[i])      
finalsum=sum2
for i in range(1,len(viseNumber),2):
    
    finalsum+=int(viseNumber[i]*1)

if (finalsum%10==0):
    str(viseNumber)
    if (viseNumber[0:2]=="34" or viseNumber[0:2]=="37"):
        print("American Express")
    elif(viseNumber[0:2]=="51" or viseNumber[0:2]=="52" or viseNumber[0:2]=="53" or viseNumber[0:2]=="54" or viseNumber[0:2]=="55"):
        print("MasterCard")
    elif(viseNumber[0]=="4"):
        print("VISA")
else:
    print("NOT VALID")              





    


