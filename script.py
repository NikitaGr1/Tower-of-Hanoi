def move(n, x, y):
    # define a recursive function move
    if n == 1:
        print(n, x, y)
        # if at this stage it remains to move the upper disk, we describe this move
    else:
        move((n - 1), x, 6 - (x + y)) 
        """
        if you need to move more than one disk, you must first move the previous disk to the third (free) rod; the function will call itself until n is equal to 1
        """
        print(n, x, y) 
        # describe the parent function
        move((n - 1), 6 - (x + y), y)


print('input the number of disks')
n = int(input())
# entering the number of disks
move(n, 1, 3)
