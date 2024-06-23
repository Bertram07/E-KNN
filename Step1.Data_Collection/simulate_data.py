import numpy as np
import pandas as pd



file_path = 'E:/git_repos/E-KNN/Dataset/combined_selected_columns_467110.csv'
df = pd.read_csv(file_path, encoding='utf-8-sig')

output_file = 'E:/git_repos/E-KNN/Dataset/combined_simulated_columns_467110.csv'

# 設定欄位
equipment_capacity = []
failure_rate = []
shading_rate = []
placement_angle = []
panel_temp = []

# 設定筆數
num_rows = len(df)
np.random.seed(18)   # 規律隨機

# 模擬數據
for index, row in df.iterrows():
    equipment_capacity.append(np.random.uniform(1, 10000))
    failure_rate.append(np.random.beta(1, 99))
    shading_rate.append(np.random.uniform(0, 100))

    lat = row['緯度']
    lat = float(lat.split('°')[0])
    placement_angle.append(lat + np.random.uniform(-2, 2))

    outdoor_temp = row['期間平均室外溫度(°)']
    panel_temp.append(outdoor_temp + np.random.uniform(10, 30))
    

# 將模擬數據加入欄位中
df['設備容量(kW)'] = equipment_capacity
df['故障率(%)'] = failure_rate
df['遮蔽率(%)'] = shading_rate
df['擺放角度(°)'] = placement_angle
df['面板溫度(°)'] = panel_temp

if df.empty:
    print("No files contained all the required columns.")
else:
    #dfs=dfs.rename(columns={'氣溫(℃)':'期間平均室外溫度(°)','全天空日射量(MJ/㎡)': '期間平均太陽輻射量(kW/m²)'})
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f'Selected columns combined and saved to {output_file}')
