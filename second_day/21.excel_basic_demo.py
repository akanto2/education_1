import openpyxl

# 엑셀파일을 오픈
workbook = openpyxl.load_workbook('../Data/result_salaries_excel.xlsx')
# 액티브 시트를 확보
active_sheet = workbook.active  # 시트명을 직접 입력할 시, active_sheet = workbook['Sheet1']
# F2 셀에 값을 읽기
print(active_sheet['F2'].value)
# H2 셀에 '안녕하세요' 적용
active_sheet['H2'].value = '안녕하세요'
# 워크북(엑셀)을 저장하고 닫아준다.
workbook.save('./Data/result_salaries_excel.xlsx')
workbook.close()

print('job completed..')

