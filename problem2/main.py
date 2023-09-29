#Fungsi Exponen dengan Tc = O(log(n)) dan Sc = O(1)
def pow(x, n):
    result = 1
    if n == 0:
        return result
    else:    
        if n > 0:
            while n> 0:
                if n % 2 == 1:
                    result *= x
                x *= x
                n //= 2
        if n < 0 :
            n = -n
            x = 1/x
            for i in range (n):
                result *= x
        return result

if __name__ == '__main__':
    print(pow(2, 3)) # 8
    print(pow(7, 2)) # 49
    print(pow(10, 5)) # 100000
    print(pow(17, 6)) # 24137569
    print(pow(5, 3)) # 125
    print(pow(7, 0))
    print(pow(3, -2))