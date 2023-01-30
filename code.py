def gamingArray(arr):
    peak, bob = 0, False
    for a in arr:
        if a > peak:
            bob = not bob
            peak = a
    return 'BOB' if bob else 'ANDY'

