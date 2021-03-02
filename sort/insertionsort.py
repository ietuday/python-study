def insertion_sort(array):

    # We start from 1 since the first element is trivially sorted
    for index in range(1, len(array)):
        currentValue = array[index]41
        print("currentValue",currentValue)
        currentPosition = index 2
        print("currentPosition",currentPosition)

        # As long as we haven't reached the beginning and there is an element
        # in our sorted array larger than the one we're trying to insert - move
        # that element to the right
        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            print("array[currentPosition]",array[currentPosition])
            currentPosition = currentPosition - 1
            print("currentPosition",currentPosition)


        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index currentPosition - 1.
        # Either way - we insert the element at currentPosition
        array[currentPosition] = currentValue
        print("array[currentPosition]",array[currentPosition])


array = [4, 22, 41, 40, 27,0]
insertion_sort(array)
print("sorted array: " + str(array))
