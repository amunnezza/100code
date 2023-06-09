fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
#in case of index error print "Fruit Pie"
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print ("Fruit Pie")
    else:
        print (fruits[index] + " Pie")


for i in range(len(fruits) + 1):#esco fuori range
    print (i)
    make_pie(i)


