def fancy_divide(numbers, index):
    try:
        print("inside first try")
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            print('right before func calling again')
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
        print("end of inside first try")
    except ZeroDivisionError:
        print("-2")


# fancy_divide([0, 2, 4], 4)
fancy_divide([0, 2, 4], 0)
