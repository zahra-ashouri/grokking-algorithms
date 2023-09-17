

def get_sums(li):
    summ = 0
    length = len(li)
    seen = set()

    for x in l:
        summ += x
        seen.add(x)

    sum_to_be = (length * (length + 1)) / 2
    print("sum:", summ)
    print("sum_to_be:", sum_to_be)
    if summ == sum_to_be:
        print("No Missing Number")
        return summ

    diff = sum_to_be - summ
    if diff not in seen:
        return diff


l = [0, 1, 2]
print(get_sums(l))
