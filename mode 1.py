def mode(my_data):
        if my_data==[]:
            return None
        else:
            return max(set(my_data), key=my_data.count)
my_data=[1,3,2,3,4,5,6,7,8,9]
print(mode(my_data))
