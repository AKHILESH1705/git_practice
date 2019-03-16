
# prime number 

num = int(input("enter number : "))
for i in range(2,num):
    if (num % i == 0):
        print("number is not prime")
        break
        
else:
    print("number is prime") 