def test_find_str(target, source):
    for i in range(len(target) - len(source) + 1):
        cnt = 0
        j = i
        for idx in range(len(source)):
            if target[i] == source[idx]:
                cnt += 1
            j += 1
        if cnt == len(source):
            return i
    return -1

def test_find_str():
    assert find_str('string', 'ing') == 3
    assert find_str('string', 'ing') == -1

 def find_str_evn_better(target, source):


def main():
    pass