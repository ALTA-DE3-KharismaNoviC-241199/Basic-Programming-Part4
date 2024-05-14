def mean_median(array_input):
    mean = 1.0
    median = 1
    x = len(array_input)
    if x == 0:
        return None
    elif x % 2 == 0:
        median = (array_input[x//2]+array_input[x//2-1])/2
    else :
        median = array_input[x//2]
    mean = sum(array_input)/x
    return round(mean, 1), round(median, 1)

if __name__ == '__main__':
    print(mean_median([1, 2, 3, 4])) # (2.5, 2.5)
    print(mean_median([1, 2, 3, 4, 5])) # (3.0, 3)
    print(mean_median([7, 8, 9, 13, 15])) # (10.4, 9)
    print(mean_median([10, 20, 30, 40, 50])) # (30.0, 30)
    print(mean_median([15, 20, 30, 60, 120])) # (49.0, 30)