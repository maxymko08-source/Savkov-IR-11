def find_kth_largest(array, k):
    n = len(array)
    if k < 1 or k > n:
        raise ValueError(f"k must be between 1 to {n}")

    temp = array.copy()
    
    if k <= n // 2:
        for _ in range(k):
            target_val = temp[0]
            for x in temp:
                if x > target_val:
                    target_val = x
            temp.remove(target_val)
            
    else:
        k_smallest = n - k + 1 
        
        for _ in range(k_smallest):
            target_val = temp[0]
            for x in temp:
                if x < target_val:
                    target_val = x
            temp.remove(target_val)

    kth_value = target_val
    position = array.index(kth_value)

    return kth_value, position