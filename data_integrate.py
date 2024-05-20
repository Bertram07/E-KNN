import numpy as np
import pandas as pd

#數據整合
file_paths = [
    'E:/gitrepos/E-KNN/Dataset/466881-2023-05.csv',
    'E:/gitrepos/E-KNN/Dataset/466881-2023-06.csv',
    'E:/gitrepos/E-KNN/Dataset/466881-2023-07.csv',
    'E:/gitrepos/E-KNN/Dataset/466881-2023-08.csv',
    'E:/gitrepos/E-KNN/Dataset/466881-2023-09.csv',
    'E:/gitrepos/E-KNN/Dataset/466881-2023-10.csv',
    'E:/gitrepos/E-KNN/Dataset/466881-2023-11.csv',
    'E:/gitrepos/E-KNN/Dataset/466881-2023-12.csv',
    'E:/gitrepos/E-KNN/Dataset/466881-2024-01.csv',
    'E:/gitrepos/E-KNN/Dataset/466881-2024-02.csv',
    'E:/gitrepos/E-KNN/Dataset/466881-2024-03.csv',
    'E:/gitrepos/E-KNN/Dataset/466881-2024-04.csv',
]

columns = ['氣溫(℃)', '降水量(mm)', '日照時數(hour)', '全天空日射量(MJ/㎡)']
dfs = []

for file_path in file_paths:
    df = pd.read_csv(file_path, encoding='utf-8')
    df_selected = df[columns]
    df_selected2 = df_selected.drop(index=0)#刪除第二列'Temperature', 'Precp', 'SunShine', 'GloblRad'
    df_selected2 = df_selected2.rename(columns={'氣溫(℃)':'期間平均室外溫度(°)','全天空日射量(MJ/㎡)': '期間平均太陽輻射量(kW/m²)'})
    df_selected2['期間平均太陽輻射量(kW/m²)'] = round(pd.to_numeric(df_selected2['期間平均太陽輻射量(kW/m²)']) / 3.6, 3) #轉換'期間平均太陽輻射量(kW/m²)'資料型態為float並進行換算取至小數點第三位
    dfs.append(df_selected2)

# 檢查是否有任何DataFrame被加入到列表中
if dfs:
    # 合併所有 DataFrame
    df_combined = pd.concat(dfs, ignore_index=True)
    # 將合併後的 DataFrame 寫入新的 CSV 文件
    output_file = 'E:/gitrepos/E-KNN/Dataset/466881_combined_selected_columns.csv'
    df_combined.to_csv(output_file, index=False, encoding='utf-8')
    #with open(output_file, 'w', encoding="utf-8") as file:
        #for row in dfs:
            #file.write(str(row))
        #file.write('n') #這樣column會重複

    print(f'Selected columns combined and saved to {output_file}')
else:
    print("No files contained all the required columns.")

