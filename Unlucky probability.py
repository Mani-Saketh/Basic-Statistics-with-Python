def unlucky_probability(my_data):
    number=len(my_data)
    factorial=1
    for i in range(1,number+1):
        factorial=factorial*i
    return factorial
my_data=[1,2,3,4,5,6,7,8,9,10]
factorial= unlucky_probability(my_data)
wrong_data=((factorial-1)/factorial)*100
print("The probability that none of the napkins match is ",str(round(wrong_data,1)),"%")        

