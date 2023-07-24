# 리스트
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]

# 튜플
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (3, 2, 1)

# 집합
set1 = {1, 2, 3}
set2 = {1, 2, 3}
set3 = {3, 2, 1}

# 딕셔너리
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2, 'c': 3}
dict3 = {'c': 3, 'b': 2, 'a': 1}

# 리스트와 튜플 비교
print("리스트와 튜플 비교:")
# list1과 tuple1을 비교하면 False가 출력됩니다. 리스트와 튜플은 서로 다른 타입입니다.
print("list1 == tuple1:", list1 == tuple1)  # False
# 그러나 list1과 list2는 동일하므로 비교 결과는 True가 됩니다.
print("list1 == list2:", list1 == list2)    # True
# list1과 list3은 같은 요소를 가지지만 순서가 다르므로 비교 결과는 False입니다.
print("list1 == list3:", list1 == list3)    # False

# 리스트와 집합 비교
print("\n리스트와 집합 비교:")
# 리스트와 집합은 서로 다른 타입이므로 비교 결과는 항상 False입니다.
print("list1 == set1:", list1 == set1)      # False
print("list1 == set2:", list1 == set2)      # False

# 튜플과 집합 비교
print("\n튜플과 집합 비교:")
# 마찬가지로, 튜플과 집합은 서로 다른 타입이므로 비교 결과는 항상 False입니다.
print("tuple1 == set1:", tuple1 == set1)    # False
print("tuple1 == set2:", tuple1 == set2)    # False

# 집합 비교
print("\n집합 비교:")
# set1과 set2는 같은 요소를 동일한 순서로 가지므로 비교 결과는 True입니다.
print("set1 == set2:", set1 == set2)        # True
# set1과 set3은 같은 요소를 다른 순서로 가지지만 비교 결과는 True입니다.
print("set1 == set3:", set1 == set3)        # True

# 딕셔너리 비교
print("\n딕셔너리 비교:")
# 딕셔너리 dict1과 dict2의 키와 값은 동일하므로 비교 결과는 True입니다.
print("dict1 == dict2:", dict1 == dict2)    # True
# dict1과 dict3은 동일한 키-값 쌍을 가지지만 순서가 다르므로 비교 결과는 True입니다.
print("dict1 == dict3:", dict1 == dict3)    # True
