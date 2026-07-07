def add_two_numbers() -> int:
    comma_seperated_nums = input()
    num_list = comma_seperated_nums.split(",")
    int_list = []
    for num in num_list:
        int_list.append(int(num))
    return sum(int_list)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
