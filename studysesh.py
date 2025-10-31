def update_data(my_list):
    my_list = ['x', 'y', 'z']
    my_list.append('d')
    return my_list

data = ['a', 'b', 'c'] # ['a', 'b', 'c', 'd']
new_data = update_data(data)

print(data) # ['a', 'b', 'c', 'd']
print(new_data) # ['x', 'y', 'z']