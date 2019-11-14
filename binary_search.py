def search(list, n):
    lower = 0
    upper = len(list) - 1
    

    while lower <= upper:
        mid = (lower + upper) // 2
        if list[mid] == n:
            return mid
        else:
            if list[mid] < n:
                lower = mid
            else:
                upper = mid

numbers = [1,2,3,4,5,6,7,8,9,10]
position = search(numbers, 8)
print position
