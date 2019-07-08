
list0 = []

list1 = input("Enter an integer (1/4).")
list2 = input("Enter an integer (2/4).")
list3 = input("Enter an integer (3/4).")
list4 = input("Enter an integer (4/4).")

list0.extend([list1, list2, list3, list4])

int_list = [int(float(each)) for each in list0]

print(int_list)

target = input("Input the target integer.")
int_target = [int(float(each)) for each in target]

def find_target(int_list, target):
    for each in int_list:
        p_list1 = sum(list1 + int_list[3])
        print(p_list1)

find_target(int_list, target)
