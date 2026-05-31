def min_eating_speed(piles, h):

    max_pile = piles[0]
    for p in piles:
        if p > max_pile:
            max_pile = p

    left = 1
    right = max_pile
    result = right

    while left <= right:
        k = (left + right) // 2
        
        hours = 0
        for p in piles:
            hours += (p + k - 1) // k

        if hours <= h:
            if k < result:
                result = k
            
            right = k - 1
        else:
            left = k + 1

    return result