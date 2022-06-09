print('Lists')

my_list0 = [1, 1577, 87, 18.92, 751]
my_list1 = list(['python', 'TOGFire', 'T O G'])
my_list2 = [1, 2, 3, 'python', 'gaming', 'coding']
'''
print(my_list0)
print(my_list1)
'''
#Basics of list command
'''
print(my_list2[:])
print(my_list2[0:3])
print(my_list2[2:5])
print(my_list2[::-1])
print(my_list2[3:5:1])
print(my_list2[3][4])
'''
#Addressing the list
'''
my_list0.append([666, 12])
print(my_list0)
print(len(my_list0))

my_list1.extend([542, 19])
print(my_list1)
print(len(my_list1))

my_list2.insert(1, 'insert_example')
print(my_list2)
print(my_list2 + ['just an example!'])
print(my_list2 * 3)
'''
#Append, extand and insert
'''
del my_list0[4]
print(my_list0)

my_list1.remove('T O G')
print(my_list1)

a = my_list2.pop(2)
print('Popped elements:', a, 'Listing remaining:', my_list2)

my_list1.clear()
print(my_list1)
'''
#Deleting things from list
'''
print(sorted(my_list0))
print(my_list0)

my_list0.sort(reverse=True)
print(my_list0)
my_list0.reverse()
print(my_list0)
'''
#Sorting the list
'''
my_list3 = my_list2.copy()
print(my_list3)
'''
#Copying the list