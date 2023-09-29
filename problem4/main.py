#Fungsi muncul sekali dengan Tc = O(n) dan Sc = O(n)
def muncul_sekali(angka):
    angka_set = set()
    list = []

    for digit in angka:
        digit_int = int(digit)  # Mengonversi karakter menjadi integer
        if digit_int not in angka_set:
            angka_set.add(digit_int)
            list.append(digit_int)
        else:
            if digit_int in list:
                list.remove(digit_int)

    return list
            

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]