#Part1 
def user_names(list_1):
    new_list = []
    for user in list_1:
        if (user[2]>30) and (user[3] == "USA" or user[3] == "Canada"):
            list_1.pop(user)
            new_list.append(user[1])


    return new_list,list_1

def age_sort(list_1):
    duplicates = []
    sorted_age = sorted(list_1, key=lambda x: x[2])

    for i in list_1:
        if i[1] not in duplicates:
            duplicates.append(i[1])
        else:
            print(i[1])

    return sorted_age[-1:-11:-1]

#part2

def total_number(list_2):
    count = 1
    users = []
    for transaction in list_2:
        if transaction[1] not in users:
            count += 1
        users.append(transaction[1])

    return count

def highest_amount(list_2):
    max = 0 
    for transaction in list_2:
        if max < transaction[2]:
            max = transaction[2]

    return max

def two_tuples(list_2):
    users_list = []
    transactions_list = []
    for transaction in list_2:
        for j in range(len(transaction)):
            if j == 1:
                users_list.append(transaction[j])
            if j == 0:
                transactions_list.append(transaction[j])

    return users_list,transactions_list

#part3
def set_1(setA,setB,setC):
    new_set = setA & setB
    new_set1 = setA.symmetric_difference(setC)

    return new_set,new_set1

def set_2(setA,new_user_id):
    return setA.update(new_user_id)

def set3(setB,remove_users_id):
    return setB.difference_update(remove_users_id)













