print("="*50)
print("NUMBER ANALISER:")
print("="*50)

def shivam():
    yes=input("""ARE YOU READY TO PLAY WITH SHIVAM` NUMBER ANALYSER
    yes or no :""")
    if yes=="yes":
         
         num=int(input("enter a number for analising:"))

         print("="*50)
         num2=int(input("""choose for operation at this number:
         TABLE: 1
         POSITIVE OR NOT:2
         SQUARE:3
         EVEN OR ODD:4
         SUM OF DIGITS OF NUMEBER:5
         CUBE OF NUMBER:6
         CHOOSE ALL:7
         GALTI SE AAA GYA:8
         """))
         if num2==1:
          
          for i in range(1,11):
                    print(f"{num}*{i}={num*i}")
         elif num2==2:
             
             if num>0:
                    print(num,"is positive")
             else:
                    print(num,"is negative")
         elif num2==3:
                print(f"square of {num} is {num*num}")
         elif num2==4:
                
                if num%2==0:
                    print(num,"is even")
                else:
                    print(num,"is odd")
         elif num2==5:
                sum=0
                for i in range(1,num+1):
                    sum=sum+i
                print(sum,"is suum of all digits of number in",num)
         elif num2==6:
                print(f"cube of {num} = {num*num*num}")
         elif num2==7:
                print("TABLE==========")
                for i in range(1,11):
                    print(f"{num}*{i}={num*i}")
                if i%2==0:
                    print(num,"is even")
                else:
                    print(num,"is odd")
                print(f"square of {num} = {num*num}")
                if num>0:
                    print(num,"is positive")
                else:
                    print(num,"is negative")
                sum=0
                for i in range(1,num+1):
                    sum=sum+i
                print(sum,"is sum of all digits which is in",num)
                print(f"cube of {num} is {num*num*num}")
         elif num2==8:
                print("koi baat nhi aaa gye too ,,,,,, hame accha laga aap aye thankuu bye ")
    elif yes=="no":
         print("bye fir aya hi kyu chutiye ")

shivam()



   