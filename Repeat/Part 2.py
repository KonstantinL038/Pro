# Task 1
def min_path():
    length = [input() for _ in range(3)]
    return min(length[0] + length[1] + length[2], 2*(length[0] + length[1]), 2*(length[1] + length[2]),
               2*(length[0] + length[2]))


# Task 2
def language():
    eng, rus = 'AaBCcEeHKMOoPpTXxy', 'АаВСсЕеНКМОоРрТХху'
    letters = [input() for _ in range(3)]
    let_eng, let_rus = 0, 0

    for letter in letters:
        if letter in eng:
            let_eng += 1
        else:
            let_rus += 1

    if let_eng == 3:
        return 'en'
    elif let_rus == 3:
        return 'rus'
    else:
        return 'mix'


# Task 3
def reverse_num():
    n, x, y, a, b = [int(i) for i in input().split(' ')]
    nums = list(range(1, n+1))

    part_1, part_2, part_3 = nums[:x-1], nums[x-1:y][::-1], nums[y:]
    nums = part_1 + part_2 + part_3
    part_1,part_2, part_3 = nums[:a-1], nums[a-1:b][::-1], nums[b:]
    return ' '.join(map(str, part_1 + part_2 + part_3))


print(reverse_num())
