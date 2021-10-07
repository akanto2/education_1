import pandas as pd

# csv 파일 읽기
df = pd.read_csv('../Data/Salaries.csv')

# 1. 필터링 -- 내셔널리그의 선수연봉 데이터만 필터링
# df = df.loc[df['lgID'] == 'NL']

# 2. 필터링 -- 2012년도 PIT 데이터만 필터링
df = df.loc[(df['yearID'] == 2012) & (df['teamID'] == 'PIT')]
print(df)

# df 작업 후 저장 (to scv)
df.to_csv('./Data/result_salaries_lad.csv', index=False)
print('csv saved..')
# df 엑셀로 저장 (to excel)
df.to_excel('./data/result_salaries_excel_lad.xlsx', index=False)
print('excel saved..')
