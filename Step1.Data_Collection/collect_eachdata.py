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
#    'E:/gitrepos/E-KNN/Dataset/466881-2023-11.csv',
#    'E:/gitrepos/E-KNN/Dataset/466881-2023-12.csv',
#    'E:/gitrepos/E-KNN/Dataset/466881-2024-01.csv',
#    'E:/gitrepos/E-KNN/Dataset/466881-2024-02.csv',
#    'E:/gitrepos/E-KNN/Dataset/466881-2024-03.csv',
#    'E:/gitrepos/E-KNN/Dataset/466881-2024-04.csv',
#]


#--- csv type : 讀取各縣市天氣'期間平均室外溫度(°)', '降水量(mm)', '日照時數(hour)', '期間平均太陽輻射量(kW/m²)'資料欄位
#--- read file for directory
input_files = []
for i in glob.glob("E:/git_repos/E-KNN/Dataset/467110-*.csv"):
    input_files.append(i)

input_sunfile = 'E:/git_repos/E-KNN/Dataset_sunelevation/sun_19kinmencounty.csv'

output_file = 'E:/git_repos/E-KNN/Dataset/combined_selected_columns_467110.csv'

#output_file2 = 'E:/gitrepos/E-KNN/Dataset/combined_selected_columns2_466990.csv'

data_columns = ['氣溫(℃)', '相對溼度(%)','降水量(mm)', '日照時數(hour)', '全天空日射量(MJ/㎡)', '能見度(km)', '總雲量(0~10)']

#data_columns2 = ['經度、緯度', '海拔']


dfs = pd.DataFrame(columns=data_columns)

def determine_weather(row):
    cloud_amount = row['總雲量(0~10)']
    humidity = row['相對溼度(%)']
    visibility = row['能見度(km)']
    precipitation = row['降水量(mm)']
    
    if cloud_amount < 4:
        if precipitation >= 1:
            weather = '晴有雨'
        elif humidity >= 75 and humidity <= 100 and visibility >= 1:
            weather = '晴有靄'
        else:
            weather = '晴天'
    elif 4 <= cloud_amount < 9:
        if precipitation >= 1:
            weather = '多雲有雨'
        elif humidity >= 75 and humidity <= 100 and visibility >= 1:
            weather = '多雲有靄'
        else:
            weather = '多雲'
    else:
        if precipitation >= 1:
            weather = '陰有雨'
        elif humidity >= 75 and humidity <= 100 and visibility >= 1:
            weather = '陰有靄'
        else:
            weather = '陰天'
        
    return weather


for input_file in input_files:
    #--- read csv
    df = pd.read_csv(input_file, encoding='utf-8')
    df_selected = df[data_columns]
    df_selected2 = df_selected.drop(index=0)#刪除第二列'Temperature', 'Precp', 'SunShine', 'GloblRad'
    #--- concat csv
    dfs=pd.concat([dfs,df_selected2], axis=0, ignore_index=True)

# Check if dfs is empty after concatenation
if dfs.empty:
    print("No files contained all the required columns.")
else:
    # Step 1: Add sun angle data
    sun_data = pd.read_csv(input_sunfile, encoding='utf-8')
    sun_data['日期'] = pd.to_datetime(sun_data['日期'])
    sun_data = sun_data[(sun_data['日期'] >= '2023-05-01') & (sun_data['日期'] <= '2024-04-30')]
    # 只选择仰角列并重复以匹配dfs的长度
    sun_angles = sun_data['仰角'].str.replace('S', '').str.replace('N', '').astype(int).values
    dfs['太陽高度角(°)'] = np.tile(sun_angles, int(np.ceil(len(dfs) / len(sun_angles))))[:len(dfs)]
    # Remove rows where '降水量(mm)'有'T'、'總雲量(0~10)'有'/'
    dfs = dfs[dfs['降水量(mm)'] != 'T']
    dfs = dfs[~dfs['總雲量(0~10)'].str.contains('/', na=False)]
    # Convert str to int
    columns_to_convert = ['降水量(mm)', '總雲量(0~10)', '相對溼度(%)', '能見度(km)']
    dfs[columns_to_convert] = dfs[columns_to_convert].apply(pd.to_numeric, errors='coerce')
    #--- compute 全天空日射量(MJ/㎡)
    #轉換'期間平均太陽輻射量(kW/m²)'資料型態為float並進行換算取至小數點第三位
    dfs['全天空日射量(MJ/㎡)'] = round(pd.to_numeric(dfs['全天空日射量(MJ/㎡)'], errors='coerce') / 3.6, 3)
    dfs['天氣現象'] = dfs.apply(determine_weather, axis=1)
    
    # Check if dataframe is not empty and save to CSV
    if dfs.empty:
        print("No files contained all the required columns.")
    else:
        dfs = dfs.rename(columns={'氣溫(℃)': '期間平均室外溫度(°)', '全天空日射量(MJ/㎡)': '期間平均太陽輻射量(kW/m²)'})
        dfs.insert(0, '經度', '118.2893°E')
        dfs.insert(1, '緯度', '24.4073°N')
        dfs['海拔(m)'] = 47.88
        dfs.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f'Selected columns combined and saved to {output_file}')

