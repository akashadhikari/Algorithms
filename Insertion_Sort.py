import time


def sorting(alist):

    # We'll apply insertion sort to a list called alist = [5, 2, 4, 6, 1, 3]

    then = time.time()

    for index in range(1, len(alist)):

        # We'll first track the current positional value
        current_value = alist[index]

        # We just checked if the index of current position is greater than 0 AND 
        # previous positional value is  greater than current
        while index > 0 and alist[index-1] > current_value:

            # if thats the case, sort them
            alist[index] = alist[index-1]

            # We just deducted the index by 1
            index = index - 1
        
        # set the changed index value to current
        alist[index] = current_value

    print (time.time() - then)

alist = [5, 2, 4, 6, 1, 3]

sorting(alist)

print(alist)