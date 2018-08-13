# following wikipedia reference: https://en.wikipedia.org/wiki/Quicksort
def quicksort(unsorted):
    print("unsorted = ", unsorted)

    # for cases where the split is on an empty list or one element
    if len(unsorted) <= 1:
        return unsorted

    # pivot is usually the last element but results in O(n^2) performance for sorted arrays
    pivot = len(unsorted) - 1
    print("pivot = ", pivot)
    pivot_value = unsorted[pivot]
    print("pivot_value = ", pivot_value)

    for index in range(len(unsorted)):
        # case when pivot has already passed the current index
        if index >= pivot:
            break

        # check current index against moving pivot
        while unsorted[index] > pivot_value:
            # case where pivot has moved passed index
            if pivot <= index:
                break

            # move the index value to pivot position
            unsorted[pivot] = unsorted[index]
            # move pivot to next position
            pivot -= 1
            # move current pivot value to index position
            unsorted[index] = unsorted[pivot]

        # when all moves are done, move pivot value to current pivot position
        unsorted[pivot] = pivot_value
        print("current state : ", unsorted)

    less_half = quicksort(unsorted[: pivot])
    greater_half = quicksort(unsorted[pivot + 1:])

    return less_half + [pivot_value] + greater_half

print("finish : ", quicksort([3,7,8,5,2,1,9,5,4]))