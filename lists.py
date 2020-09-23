# This will have all the list implementations
list_of_items = ["Mainaak", 'Is', 'Learning', 'Code', str(5), 899, 56.234]
print(list_of_items[2:])
print(list_of_items[:4])
print(list_of_items[2:4])

# Using extend function in lists
second_list = [1, 3, 4, 100, 99, "The", 'Start', 'Of', 'Something', "Beautiful"]
# concatenates two lists
second_list.extend(list_of_items)
# removes items with mentioned value
second_list.remove("Beautiful")
# removes element at mentioned index
second_list.pop(1)
# removes the last element in the list
second_list.pop()
print(second_list)
# adds an item to the list at the end
second_list.append('Added a new item here')
print(second_list[len(second_list) - 1])
# inserts an element to the mentioned index
second_list.insert(3, 'James Bond')
print(second_list)
print(second_list.index("Code"))
