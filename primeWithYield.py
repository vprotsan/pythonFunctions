def genPrimes():
    primesN = []
    next = 2
    while True:
        isPrime = True
        print("next is: " + str(next))
        for n in primesN:
            print("num in array" + str(n))
            if (next % n) == 0:
                print("reminder is zero")
                isPrime = False
                break
        if isPrime:
            primesN.append(next)
            print(next)
            yield next
        next += 1

primeGenerator = genPrimes()
primeGenerator.next()
primeGenerator.next()
primeGenerator.next()
primeGenerator.next()
primeGenerator.next()
primeGenerator.next()
primeGenerator.next()
