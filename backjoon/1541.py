equation = input().split('-')#-를 기준으로 슬라이싱
# print(equation)

answer = 0
for i in equation[0].split('+'): #-전 첫번쨰 요소 더하기
    answer += int(i)
    # print(answer)

for i in equation[1:]:
    for j in i.split('+'):
        # print('i는 -> ',i)
        # print('j는 -> ', j)
        answer -= int(j)

print(answer)

#55-50+40
#일단 입력받고 - 기준으로 슬라이싱
# ['55','50+40']
