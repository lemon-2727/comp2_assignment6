import csv
import numpy as np

# input  : 없음
# output : 파일명에 적힌 것과 동일한 실시년도 반환
# 주의   : 사용자는 수능년도를 부를 때의 관습대로 실시년도에 +1 더한 상태를 안내 받고 입력함
#          따라서 리턴값은 관습 수능년도에서 1 뺀 실시년도(파일명의 연도와 동일)를 반납함

def select_year():
    
    years = [2021, 2022, 2023, 2024]

    print("\n이 수능 데이터가 존재하는 연도는 [   ", end='')

    for year in years:
        print("%d년도   " %year, end='')

    print("] 입니다. 조회를 원하시는 연도를 선택해 주세요. 예시 : 2024")

    input_year = int(input())

    print("이 수능 데이터는 %d 년도 수능의 데이터입니다. (%d년 실시)" %(input_year, input_year - 1))
    
    # 실시년도로 반환 (파일명에 적힌 것과 동일한 연도)
    return input_year - 1




#input  : file handle, selected year(type:int)
#output : [과목 분류, 세부 과목명] 이 과목별로 저장되어 있는 2차원 ndarray 

def find_subjects(file, input_year):
    columns = [0, 1]
    subjects = np.genfromtxt(file, delimiter=',', usecols=columns, skip_header=1, dtype=str, encoding='CP949')
    
    # 공백 제거
    unique_subjects = np.char.strip(subjects)
    unique_subjects = np.unique(unique_subjects, axis=0)

    if input_year == 2021:
        order = ['국어', '수학', '사회탐구', '과학탐구', '직업탐구', '제2외국어 한문']
    else:
        order = ['국어', '수학', '사회탐구', '과학탐구', '직업탐구']

    order_dict = {key: i for i, key in enumerate(order)}

    # 안전한 정렬 인덱스 생성
    sort_indices = np.argsort([order_dict.get(row[0], float('inf')) for row in unique_subjects])

    sorted_subjects = unique_subjects[sort_indices]

    return sorted_subjects


# input  : sjt_arr - [과목 분류, 세부 과목명] 이 과목별로 저장되어 있는 2차원 ndarray,
#          input_sjt : 사용자가 입력한 세부 과목명
#          selected_subjects : [선택된 과목의 분류, 선택된 세부 과목명] 형태의 1차원 배열
# output : 사용자가 입력한 세부 과목명의 존재 여부
def input_subject_check(sjt_arr, input_sjt, selected_subjects):

    extc = False

    if input_sjt in sjt_arr[:, 1]:
        extc = True 
        index = np.where(sjt_arr[:, 1] == input_sjt)[0][0]
        selected_subjects[0] = sjt_arr[index][0]
        selected_subjects[1] = sjt_arr[index][1]
    
    return extc


# input  : file handle, selected year
# output : [과목 분류, 세부 과목명] 이 과목별로 저장되어 있는 2차원 ndarray
def select(file, input_year):

    sjt_arr = find_subjects(file, input_year)

   

    for subject in sjt_arr:
        print(subject[0], ":", subject[1])

    print("\n이 수능 데이터에 존재하는 과목은 위와 같습니다.\n조회를 원하시는 세부과목을 선택하세요.")
    input_subject = input()

    selected_subjects = [0, 0]
    while not input_subject_check(sjt_arr, input_subject, selected_subjects):
        print("그런 과목명은 없습니다. 다시 입력해 주세요.")
        input_subject = input()
        
    return selected_subjects



    

