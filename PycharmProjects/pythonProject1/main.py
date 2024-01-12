# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

 def find_sum(numbers, sum):
    for i in range(len(numbers) - 1):
        if sum - numbers[i] in numbers:
            return True

    return False

def test_find_sum():
    assert find_sum([1, 2, 9], 3) == True
    assert find_sum([1, 2, 9], 12) == False

def generate_multiple(number, count):
    multi = [number]

    for i in range(2, count + 1):
    multi.append(number*i)

    return multi

def test_generate():
    assert generate_multiple(3, 4) == [3, 6, 9, 12]
    assert generate_multiple(2, 2) == [2, 4]

def big_sum(a, b):
    s = 0
    t = 0
    p = 1

    for i in range(len(a) - 1, -1, -1)
        sum = a[i] + b[i] + t

        if sum > 9:
            t = 1
        else:
            t = 0

        s = (sum % 10) + s
        p *= 10



    return str(s)

def test_big_sum():
    assert big_sum('123', '123') == '246'
    assert big_sum('123', '129') == '252'
    assert big_sum('999', '101') == '1100'
 def main():
     pass
 test_find_sum()
 test_big_sum()
 test_generate()
main()

