numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [number**2 for number in numbers]

#Write your code 👆 above:

print(squared_numbers)



"""Instructions
You are going to write a List Comprehension to create a new list called result. 
This new list should only contain the even numbers from the list numbers."""
result = [number for number in numbers if number%2 == 0]
print(result)