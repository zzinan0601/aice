import pandas as pd

# 1차원 데이터 (Series)
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# 2차원 표 데이터 (DataFrame) - 딕셔너리 활용
data = {
    '이름': ['지수', '제니', '로제'],
    '나이': [28, 27, 26],
    '부서': ['개발', '디자인', '기획']
}
df = pd.DataFrame(data)

print(df.head(2))     # 위에서부터 2행만 확인 (기본값은 5)
print(df.tail(2))     # 아래에서부터 2행만 확인
print(df.info())      # 열 이름, 데이터 타입, 결측치 여부 확인
print(df.describe())  # 수치형 데이터의 요약 통계(평균, 최댓값, 최솟값 등) 확인

# 열(Column) 선택
names = df['이름']             # 하나의 열 선택
subset = df[['이름', '부서']]  # 여러 열 선택 시 리스트로 묶음

# 행(Row) 선택
row_0 = df.iloc[0]    # iloc: 인덱스 '번호(숫자)'를 기준으로 첫 번째 행 가져오기


