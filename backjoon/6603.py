# import sys
# import itertools
#
# result = []
# while True:
#     input_str = sys.stdin.readline()
#     array = list(map(int, input_str.split()))
#     if array[0] == 0:
#         break
#     array2 = array.pop(0)
#     combi = []
#     for comb in itertools.combinations(array, 6):
#         combi.append(' '.join(map(str, comb)))
#     result.append(combi)
#     result.sort()
# for i in range(len(result)):
#     print('\n'.join(result[i]))
#     print()

from itertools import combinations

while True:
    s = list(map(int, input().split()))
    if len(s) == 1 and s == [0]: #입력 0 받으면 그만
        break
    k = s.pop(0) #맨앞 숫자 제거
    for data in list(combinations(s, 6)):
        print(*data)
    print()