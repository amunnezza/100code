'''Dictionary in List
Instructions
You are going to write a program that adds to a travel_log. 
You can see a travel_log which is a List that contains 2 Dictionaries.
Write a function that will work with the following line of code on line 21 to add the entry for
 Russia to the travel_log.

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
You've visited Russia 2 times.

You've been to Moscow and Saint Petersburg.

DO NOT modify the travel_log directly. You need to create a function that modifies it.

Hint
Look at the function call above to see what the name of the function should be.
The inputs for the function are positional arguments. The order is very important.
Feel free to choose your own parameter names.
Test Your Code
Before checking the solution, try copy-pasting your code into this repl:
[https://repl.it/@appbrewery/day-9-2-test-your-code]
This repl includes my testing code that will check if your code meets this assignment's objectives.'''

travel_log = [

{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#DO NOT change the code above 👆

#TODO: Write the function that will allow new countries
#to be added to the travel_log.
def add_new_country(name, visit_count, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = visit_count
  new_country["cities"] = cities_visited
  travel_log.append(new_country)

#Do not change the code below 👇
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)














# Tests
import unittest
from unittest.mock import patch
from io import StringIO

class MyTest(unittest.TestCase):
# Testing Print output
    def test_1(self): 
        with patch('sys.stdout', new = StringIO()) as fake_out:
          print(travel_log)
          expected_print = "[{'country': 'France', 'visits': 12, 'cities': ['Paris', 'Lille', 'Dijon']}, {'country': 'Germany', 'visits': 5, 'cities': ['Berlin', 'Hamburg', 'Stuttgart']}, {'country': 'Russia', 'visits': 2, 'cities': ['Moscow', 'Saint Petersburg']}]\n"
          self.assertEqual(fake_out.getvalue(), expected_print) 



print("\n")
print('Running some tests on your code:')
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)