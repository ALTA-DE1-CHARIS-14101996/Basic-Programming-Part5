#Fungsi remove duplicate dengan Tc = O(n^2) dan Sc = O(n)
def join_array_remove_duplicate(arrayA, arrayB):
    # your code here
    combine = arrayA + arrayB
    compare = []
    for i in combine:
        if i not in compare:
            compare.append(i)
    return compare

if __name__ == '__main__':
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]


    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
    # ["samsung", "apple", "sony", "xiaomi"]


    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))
    # ["football", "basketball"]
