import pandas as pd
import numpy as np

def get_subj_gen(arr,subtype, subname, gender):
  if gender == "여성":
    gender = 0
  else:
    gender = 1

  return arr[(arr[:, 0] == subname) & (arr[:, 1] == subtype) & (arr[:, 4] == gender)]
    
  
def get_arr(file_name):
    data = pd.read_csv(file_name,encoding="CP949")
    #array 모양 예시: [영역, 유형, 표준편차, 명, 성별]
    arr = data.to_numpy()

    #female: 0, male:1 
    arr_male = arr.copy()
    arr_male[:, -1] = 1

    arr_female = arr.copy()
    arr_female[:, -2] = arr_female[:, -1]
    arr_female[:, -1] = 0

    arr = np.vstack((arr_female,arr_male))

    return arr
    
    
    