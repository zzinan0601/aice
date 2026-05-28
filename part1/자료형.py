# 리스트 생성 및 데이터 추가
my_list = [10, 20, 30]
my_list.append(40)      # 맨 뒤에 40 추가 -> [10, 20, 30, 40]

# 특정 위치에 데이터 삽입 및 삭제
my_list.insert(1, 15)   # 인덱스 1 위치에 15 삽입 -> [10, 15, 20, 30, 40]
my_list.pop()           # 맨 마지막 요소 꺼내기(삭제) -> 40 반환, 리스트는 [10, 15, 20, 30]

# 리스트 컴프리헨션 (List Comprehension) - 간결하게 리스트 만들기
# 1부터 5까지의 숫자를 제곱한 리스트 생성
squared = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]

# 딕셔너리 생성
student = {
    '이름': '김코딩',
    '나이': 25,
    '전공': '데이터사이언스'
}

# 데이터 접근 및 수정
print(student['이름'])      # '김코딩' 출력
student['나이'] = 26        # 기존 값 수정

# 새로운 데이터(키-값 쌍) 추가
student['학점'] = 'A+'      

# 모든 키와 값 확인하기
print(student.keys())       # dict_keys(['이름', '나이', '전공', '학점'])
print(student.values())     # dict_values(['김코딩', 26, '데이터사이언스', 'A+'])

# 튜플 (Tuple): 생성 후 수정 불가능 (데이터를 안전하게 보호할 때 사용)
my_tuple = (1, 2, 3)
print(my_tuple[0])  # 인덱싱 가능 -> 1
# my_tuple[0] = 10  # 에러 발생! 튜플은 값을 바꿀 수 없습니다.

# 집합 (Set): 순서가 없고 중복을 허용하지 않음
set1 = {1, 2, 2, 3}
print(set1)         # 중복이 제거됨 -> {1, 2, 3}

# 집합의 연산 (교집합, 합집합)
set2 = {3, 4, 5}
print(set1 & set2)  # 교집합 -> {3}
print(set1 | set2)  # 합집합 -> {1, 2, 3, 4, 5}

# 문자를 정수나 실수로 변환
str_num = "100"
actual_num = int(str_num)       # 정수 100으로 변환
float_num = float(str_num)      # 실수 100.0으로 변환

# 숫자를 문자로 변환
age = 25
age_str = str(age)              # 문자열 "25"로 변환

# 활용 예시: 리스트의 중복 요소 제거를 위한 형변환
raw_data = [1, 1, 2, 2, 3]
unique_data = list(set(raw_data))  # 리스트 -> 집합(중복제거) -> 다시 리스트로 변환
# unique_data 결과: [1, 2, 3]
