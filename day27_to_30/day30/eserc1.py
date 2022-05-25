fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
#in case of index error print "Fruit Pie"
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print ("Fruit Pie")
    else:
        print (fruits[index] + " Pie")


make_pie(4)
for i in range(len(fruits)):
    make_pie(i)


