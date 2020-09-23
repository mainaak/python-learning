# tuples are immutable, below are their implementations
list_of_tuples = [("id", 5), ("name", "Mainaak"), ("occupation", "Software Engineer")]

tuple_copy = ("inserting", "this element at last")
list_of_tuples.append(tuple_copy)
list_of_tuples.pop(1)
list_of_tuples.insert(1, tuple_copy)

len_list = len(list_of_tuples)-1
len_last_tuple = len(list_of_tuples[len_list]) - 1

print(list_of_tuples[len_list][len_last_tuple])
print(list_of_tuples)
