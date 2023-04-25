#Write your code below this line 👇





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
def prime_checker(number):
    is_prime = True
    for i in range (2, number//2 + 1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print (f"{number} is prime")
    else :
        print (f"{number} is not a prime")
prime_checker(n)
#test

for number in range(1,11):
    prime_checker(number)


