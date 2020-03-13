
import time

def fib2(n):
    res = [0,1]
    for i in range(n):
        res.append(res[-1] + res[-2])
    return res[-1]

def fib3(n):
    a = 0; b = 1;
    for i in range(n):
        t = a + b
        a = b
        b = t
    return b
    
        
if __name__ == "__main__":
    n = int(input(""))

    # t1 = time.time()
    # for i in range(n):
    #     fib2(i)
    # t2 = time.time()

    # print(t2 - t1)
    
    print(fib3(10))