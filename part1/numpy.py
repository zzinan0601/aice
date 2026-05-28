import numpy as np
# 리스트를 활용한 1차원 배열 생성
arr1 = np.array([1, 2, 3, 4, 5])

# 중첩 리스트를 활용한 2차원 배열 생성
arr2 = np.array([[1, 2, 3], 
                 [4, 5, 6]])

# 연속된 숫자로 배열 생성 (0부터 9까지)
arr_range = np.arange(10)

# 모든 값이 0인 2x3 배열 생성
arr_zeros = np.zeros((2, 3))

# 모든 값이 1인 3x3 배열 생성
arr_ones = np.ones((3, 3))

print(arr2.shape)  # 배열의 형태 반환 -> (2, 3)
print(arr2.ndim)   # 배열의 차원 반환 -> 2
print(arr2.size)   # 배열의 전체 원소 개수 반환 -> 6
print(arr2.dtype)  # 배열 원소의 데이터 타입 반환 -> int64 (운영체제에 따라 다를 수 있음)

arr = np.array([10, 20, 30, 40, 50])

# 인덱싱: 특정 위치의 값 가져오기
print(arr[0])      # 첫 번째 값 -> 10
print(arr[-1])     # 마지막 값 -> 50

# 슬라이싱: [시작:끝:간격] 으로 데이터 추출 (끝 인덱스는 포함되지 않음)
print(arr[1:4])    # 인덱스 1부터 3까지 -> [20, 30, 40]
print(arr[:3])     # 처음부터 인덱스 2까지 -> [10, 20, 30]
print(arr[::-1])   # 배열 역순으로 뒤집기 -> [50, 40, 30, 20, 10]

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 기본적인 사칙연산
print(a + b)  # [5, 7, 9]
print(a - b)  # [-3, -3, -3]
print(a * b)  # [4, 10, 18]
print(a / b)  # [0.25, 0.4, 0.5]

# 1. 배열과 스칼라(단일 숫자)의 연산
arr = np.array([1, 2, 3])
print(arr + 10)  # [11, 12, 13] (10이 [10, 10, 10]으로 확장되어 계산됨)

# 2. 2차원 배열과 1차원 배열의 연산
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6]])
vector = np.array([10, 20, 30])

# vector가 행렬의 각 행마다 더해짐
print(matrix + vector)
# 출력:
# [[11, 22, 33],
#  [14, 25, 36]]

data = np.array([10, 20, 30, 40, 50])

print(np.sum(data))   # 합계 -> 150
print(np.mean(data))  # 평균 -> 30.0
print(np.max(data))   # 최댓값 -> 50
print(np.min(data))   # 최솟값 -> 10


