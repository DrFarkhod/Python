#1

my_list = [10, None, -30, 'True', True, 9.5]


def my_type(element):
    for element in range(len(my_list)):
        print(type(my_list[element]))
    return

my_type(my_list)