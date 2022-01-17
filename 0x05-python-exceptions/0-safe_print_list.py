def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if count < x:
                print("{:d}".format(my_list[count]), end="")
                count += 1
        print("")
    except TypeError:
        pass
    return count
