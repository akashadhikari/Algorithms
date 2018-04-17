def merge_sort(alist):

    print("Splitting ",alist)

    if len(alist)>1:

        mid = len(alist)//2
        left_half = alist[:mid]
        right_half = alist[mid:]

        # recursive call to respective halves

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):

            if left_half[i] < right_half[j]:
                alist[k]=left_half[i]
                i=i+1
            else:
                alist[k]=right_half[j]
                j=j+1
            k=k+1

        while i < len(left_half):

            alist[k]=left_half[i]
            i=i+1
            k=k+1

        while j < len(right_half):

            alist[k]=right_half[j]
            j=j+1
            k=k+1

    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]

merge_sort(alist)

print(alist)
