#Fungsi index yang dijumlah = target dengan Tc = O(n) dan Sc = O(1)
def pair_sum(arr, target):
    first_index=0
    last_index=(len(arr)-1)
    pair = []
    while first_index  < last_index:
        do = arr[first_index] + arr[last_index]
        if do == target:
            pair += [first_index,last_index]
        if do < target:
            first_index +=1
        else:
            last_index -=1
    if pair == []:
        return None
    return pair

if __name__ == '__main__':
    print(pair_sum([1, 2, 3, 4, 6], 6)) # [1, 3]
    print(pair_sum([2, 5, 9, 11], 11)) # [0, 2]
    print(pair_sum([1, 3, 5, 7], 12)) # [2, 3]
    print(pair_sum([1, 4, 6, 8], 10)) # [1, 2]
    print(pair_sum([1, 5, 6, 7], 6)) # [0, 1]
    print(pair_sum([1, 2, 3, 4, 6], 11))