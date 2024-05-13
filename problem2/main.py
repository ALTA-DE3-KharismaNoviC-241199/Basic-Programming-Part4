def draw_xyz(N):
    pattern = ""
    for i in range(N):
        for j in range (N) :
            pattern += chr(88 + (i+j)% 3)+ " "
        pattern += "\n"
    return pattern

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """