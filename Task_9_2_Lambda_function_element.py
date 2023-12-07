from functools import reduce

test_list = [1, 2, 3, "blue", 4, "black", 5, "grey", 6]

string_instances = reduce(lambda acc, elem: acc + [elem] if isinstance(elem, str) else acc, test_list, [])
print("The string instances: " + str(string_instances))

int_instances = reduce(lambda acc, elem: acc + [elem] if isinstance(elem, int) else acc, test_list, [])
print("The integer instances: " + str(int_instances))