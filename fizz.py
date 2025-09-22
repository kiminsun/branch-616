# fizzbuzz
# 1부터 임의양 정수
# i가 3 배수 ,fizz
# i가 5 배수 , buzz
# i 15 , fizzbuzz
for i in range(1,15+1):
    if i % 3 ==0:
        print('fizz')
    elif ((i % 3 != 0) & (i % 5 ==0)):
        print('buzzii')
    else:
        print(i)
