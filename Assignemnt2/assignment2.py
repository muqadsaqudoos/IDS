#Part1 
def user_names(list_1):
    new_list = []
    for user in list_1:
        if (user[2]>30) and (user[3] == "USA" or user[3] == "Canada"):
            new_list.append(user[1])


    return new_list

def age_sort(list_1):
    duplicates = []
    sorted_age = sorted(list_1, key=lambda x: x[2])

    for i in list_1:
        if i[1] not in duplicates:
            duplicates.append(i[1])
        else:
            print(i[1])

    return sorted_age[-1:-11:-1]


