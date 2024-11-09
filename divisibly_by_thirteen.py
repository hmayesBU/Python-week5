def divisible_by_thirteen():
    """
    Loop between 2000 and 3000 (ie [2000, 2001, ..., 2999])
    find the first number that is divisible by 13 and print it
    """

    for num in range(2000, 3000):
        if num % 13 == 0:
            print (num)
            break


divisible_by_thirteen()