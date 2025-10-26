# append
my_list = [1,2,3]
my_list.append(4)
print(my_list)

# extend
my_list = [1,2,3]
my_list.extend([4,5])
print(my_list)

# +=
my_list = [1, 2, 3]
my_list += [4, 5]
print(my_list)

# insert
my_list = [1, 2, 3]
my_list.insert(len(my_list), 4)
print(my_list)

# unpackin
my_list = [1, 2, 3]
new_list = [*my_list, 4, 5]
print(new_list)

# list
my_list = [1, 2, 3]
my_list = list(my_list) + [4]
print(new_list)

# copy
lst = [1, 2, 3]
# ساخت یک کپی جدید
new_list = lst.copy()
new_list.append(4)
print("orginal list: ", lst)
print("new list: ",new_list),

# list
my_list = [1, 2, 3]
my_list = list(my_list) + [4]
print(new_list)
