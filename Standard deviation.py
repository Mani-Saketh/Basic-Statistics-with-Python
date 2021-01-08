def standarddeviation(my_data):
    mean = sum(my_data)/len(my_data)
    tot = 0.0
    for i in my_data:
        tot = tot + (i - mean)**2
    return (tot/len(my_data))**0.5
my_data=[1,2,3,4,5,6,7,8,9,10]
print(standarddeviation(my_data))
