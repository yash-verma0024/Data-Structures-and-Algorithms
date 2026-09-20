def reverseDegree(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    count = 0

    hash_table = {
        "a":26, "b":25, "c":24, "d":23,
        "e":22, "f":21, "g":20, "h":19,
        "i":18, "j":17, "k":16, "l":15,
        "m":14, "n":13, "o":12, "p":11,
        "q":10, "r":9, "s":8, "t":7,
        "u":6, "v":5, "w":4, "x":3,
        "y":2, "z":1
    }

    for i in range(n):
        char = s[i]
        add = hash_table[char]
        idx = i+1
        count += (add*idx)
    return count
