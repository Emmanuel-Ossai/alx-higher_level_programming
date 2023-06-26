#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                value_1 = my_list_1[i]
                value_2 = my_list_2[i]

                if not isinstance(value_1, (int, float)) or not isinstance(value_2, (int, float)):
                    print("wrong type")
                    result_list.append(0)
                elif value_2 == 0:
                    print("division by 0")
                    result_list.append(0)
                else:
                    result_list.append(value_1 / value_2)

            except IndexError:
                print("out of range")
                result_list.append(0)

    except:
        pass

    return result_list[:list_length]
