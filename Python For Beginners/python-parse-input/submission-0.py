from typing import List

def read_integers() -> List[int]:
    inp = input()
    my_list = inp.split(",")
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
    return my_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
