# a = 0

# def b():
#     global a 
#     #함수 내에서 전역변수를 호출하기 위해선 global 선언을 해주어야한다
#     global b #함수내에서 전역변수를 선안히면 전역에서 사용가능
#     b = 2
    
#     while True:
#         print(b)
#         if a > -5:
#             a -= 1
#             print(a)
#         else:
#             break
#     print(a)
#     # print("헬로")
# b()
# print(b)
# def c():
#     global b
#     print(b)

# c()

# def sumab(a, b):
#     return a * b

# print(sumab(2, 4))


for col in range(2, 10): #range(2, 10) col 2로 시작 10까지
    if col > 5: #col이 5이상되면 브레이크
        break
    for row in range(1, 10): #row 1에서 10까지
        print(col, "x", row, "=", col * row)

i = 1
while i < 10: #조건 i < 10
    print(i)
    i = i +1 # i++
    
primes = [2, 3, 5, 8]

print(primes)

for p in primes: #primes length 만큼 반복
    print(p) #primes 리스트 요소를 하나씩 출력
    print(len(primes)) #primes length




print("나눔선")

for j in primes:
    if j == 2:
        continue
    else:
        print(j)

for b in range(1, 50):
    print("난 틀이 아니야")
c = 0
while c < 100:
    print("난 틀이 아니야")
    c = c + 1


def 응애(응, 애):
    print(응+"?"+애)

응애("응", "애")



def 몰루(몰, 루):
    return 몰+"?"+루

응애("몰","루")



def ddd(*var): #가변매개변수 *는 매개변수로 튜플을 사용 **은 딕셔너리로 사용 
    
    print(var)
    
    total = 0
    
    for hug in var:
    
        total += hug
    
    return total

print(ddd(1,2,3))

def add(*paras):

    print(paras)

    total = 0

    for para in paras:

        total += para

    return total    

 

 

# print(add(10))

# print(ddd(10, 20))

# print(add(10, 100, 1000))


# def print_map(**dicts):

#     for item in dicts:
#         print(dicts)
#         print(item)
            
# print_map(하나=1)

# print_map(one=1, two=2)

# print_map(하나=1, 둘=2, 셋=3)




#딕셔너리 함수

def rrr(**dictionary): # **딕셔너리 함수
    for abc in dictionary.items():
        if abc != ('b', 2):
            print(abc)
rrr(a = 1, b = 2, c = 3)



global global_var
global_var = "전역변수" #함수에서 사용가능 전역변수

local_var = "지역변수"
print(global_var)
def 예시():
    print(global_var)
    print(local_var) # 자바에서는 사용불가능 파이선에선 사용가능

예시()

def 전역변수예시():
    localvar = 1
    global globalvar
    globalvar = 2
    print(localvar) #출력됨

전역변수예시()
print(globalvar)
print(localvar) #출력불가
