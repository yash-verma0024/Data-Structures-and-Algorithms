def arm():
    num = int(input("Enter the number: "))
    n = num
    nod = len(str(n))
    total = 0
    while n > 0:
        ld = n % 10
        total = total + (ld ** nod)
        n = n // 10 

    print("True" if total == num else "False")

arm()