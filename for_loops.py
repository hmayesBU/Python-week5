def divisibly_by_six():
    """
    Find all the numbers divisible by 6 between 0 and 100
    """
    divisor = 6
    num = 0
    num_list = []

    for x in range(0, 100, 6):
        num_list.append(x)
    
    num_list.remove(0)
    print(num_list)


divisibly_by_six()