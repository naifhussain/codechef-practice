try:
    for _ in range(int(input())):
        N = int(input())
        fact = 1
        while(N>0):
            fact *= N
            N-=1
        print(fact)
except:
    pass
