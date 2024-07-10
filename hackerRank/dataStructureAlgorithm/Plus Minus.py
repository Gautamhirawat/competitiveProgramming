def plusMinus(arr):
    n = len(arr)
    pos_count = 0
    neg_count = 0
    zero_count = 0
    
    for num in arr:
        if num > 0:
            pos_count += 1
        elif num < 0:
            neg_count += 1
        else:
            zero_count += 1
    
    print(f"{pos_count / n:.6f}")
    print(f"{neg_count / n:.6f}")
    print(f"{zero_count / n:.6f}")
