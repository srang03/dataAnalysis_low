# 데이터 분석에 이용하기
# 작품 A와 B를 모두 시청한 사람의 수, 둘 중 하나만 시청한 사람의 수를 이용하면 두 작품의 유사도를 유추할 수 있다.
# 리스트와 딕셔너리 대신 집합을 사용하면 이를 훨씬 쉽게 구할 수 있다.

# 집합을 생성하고 원소를 추가, 삭제하는 함수를 작성하시오.

# 1. 정수 3과 5를 갖는 새로운 집합 생성
my_set = {1, 3}


# 2. 정수 5를 my_set에 추가
my_set.add(5)

# 3. new_numbers 리스트의 원소를 my_set에 추가
new_nubmers = [1, 2, 3, 4, 5, 6]

# 4. my_set 집합에서 짝수를 제거
my_set = [num for num in my_set if num % 2 != 0]

print(my_set)




# 파이썬의 set은 집합을 나타내는 데이터 구조이다.
# 집합은 순서와 중복이 없는 데이터 구조로, 데이터 분석에서 중복을 무시해야하는 경우에 사용한다.