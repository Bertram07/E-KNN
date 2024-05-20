import numpy as np
import pandas as pd
import glob

#input_files = [
#    'E:/gitrepos/E-KNN/Dataset/466881-2023-05.csv',
#    'E:/gitrepos/E-KNN/Dataset/466881-2023-06.csv',
#    'E:/gitrepos/E-KNN/Dataset/466881-2023-07.csv',
#    'E:/gitrepos/E-KNN/Dataset/466881-2023-08.csv',
#    'E:/gitrepos/E-KNN/Dataset/466881-2023-09.csv',
#    'E:/gitrepos/E-KNN/Dataset/466881-2023-10.csv',
#    'E:/gitr epos/E-KNN/Dataset/466881-2023-11.csv',
#    'E:/gitrepos/E-KNN/Dataset/466881-2023-12.csv',
#    'E:/gitrepos/E-KNN/Dataset/466881-2024-01.csv',
#    'E:/gitrepos/E-KNN/Dataset/466881-2024-02.csv',
#    'E:/gitrepos/E-KNN/Dataset/466881-2024-03.csv',
#    'E:/gitrepos/E-KNN/Dataset/466881-2024-04.csv',
#]

#--- csv type : 讀取各縣市天氣'期間平均室外溫度(°)', '降水量(mm)', '日照時數(hour)', '期間平均太陽輻射量(kW/m²)'資料欄位
#--- read file for directory
input_files = []
for i in glob.glob("E:/gitrepos/E-KNN/Dataset/466990-*.csv"):
    input_files.append(i)

output_file = 'E:/gitrepos/E-KNN/Dataset/combined_selected_columns_466990.csv'

data_columns = ['氣溫(℃)', '降水量(mm)', '日照時數(hour)', '全天空日射量(MJ/㎡)']

dfs = pd.DataFrame(columns=data_columns)

for input_file in input_files:
    #--- read csv
    df = pd.read_csv(input_file, encoding='utf-8')
    df_selected = df[data_columns]
    df_selected2 = df_selected.drop(index=0)#刪除第二列'Temperature', 'Precp', 'SunShine', 'GloblRad'
    
    #--- compute 全天空日射量(MJ/㎡)
    #轉換'期間平均太陽輻射量(kW/m²)'資料型態為float並進行換算取至小數點第三位
    df_selected2['全天空日射量(MJ/㎡)'] = round(pd.to_numeric(df_selected2['全天空日射量(MJ/㎡)'], errors='coerce') / 3.6, 3).apply(str)
    
    #--- concat csv
    dfs=pd.concat([dfs,df_selected2], axis=0, ignore_index=True)

# 檢查summary DataFrame is empty
# is not emtpy , output file (and rename column)
if dfs.empty:
    print("No files contained all the required columns.")
else:
    dfs=dfs.rename(columns={'氣溫(℃)':'期間平均室外溫度(°)','全天空日射量(MJ/㎡)': '期間平均太陽輻射量(kW/m²)'})
    dfs.to_csv(output_file, index=False, encoding='utf-8')
    #print(f'output file count:{dfs.index}')
    print(f'Selected columns combined and saved to {output_file}')

