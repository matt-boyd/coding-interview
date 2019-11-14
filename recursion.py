def adding(n, total_sum):
    if n == 11: 
        return total_sum
    else: 
        return adding(n + 1, total_sum + n)

test = adding(1,0)
print test
