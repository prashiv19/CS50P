#Integers

#x = int(input("What is x? "))99
#y = int(input("What is y? "))
#print(x + y)

#Float

#x = float(input("What is x? "))
#y = float(input("What is y? "))


#round
#z = round(x + y)

#Specify commas in numbers
#print(f"{z:,}")


#z = x / y

#print(f"{z:.2f}")



def main():
    x = int(input('What is x?'))
    print("x squared is,", square(x))
    
    
def square(n):
    return n * n
    
main()