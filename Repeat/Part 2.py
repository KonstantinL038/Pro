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


# Task 4
def more_one():
    nums = sorted([int(i) for i in input().split(' ')])
    nums_2 = []
    for num in nums:
        if nums.count(num) > 1:
            nums_2.append(num)
    print(*sorted(set(nums_2)))


# Task 5
def max_group():
    dict_num = {}

    for num in range(1, int(input())+1):
        my_sum = sum(map(lambda x: int(x), str(num)))
        if my_sum not in dict_num:
            dict_num[my_sum] = dict_num.get(my_sum, [num])
        else:
            dict_num[my_sum].append(num)

    return len(max(dict_num.values(), key=len))


