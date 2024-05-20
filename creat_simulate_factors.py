import pandas as pd
import numpy as np
import csv
import random





#數據處理
file_path = 'path/to/your/466881-2023-05.csv'
df = pd.read_csv(file_path, encoding='latin-1')










# 創建隨機數據的函數
def generate_random_data():
    # 隨機經度和緯度
    longitude = random.uniform(-180, 180)
    latitude = random.uniform(-90, 90)
    
    # 隨機選擇南北半球
    hemisphere = random.choice(['北半球', '南半球'])
    if latitude > 0:
        hemisphere = '北半球'
    elif latitude < 0:
        hemisphere = '南半球'
    
    # 隨機生成其他數據
    
    capacity = random.randint(1, 10000)  # 設備容量，1到500 kW
    weather = random.choice(['9', '8', '7', '6', '5', '4', '3', '2', '1'])  # 天氣現象
    avg_temp = np.random.normal(25, 10)  # 平均溫度25度，標準差10 
    panel_temp = avg_temp + np.random.normal(0, 5)  # 面板溫度通常高於周圍溫度
    sunlight_hours = np.random.normal(12, 3)  # 假設平均日照時數為12小時，標準差為3
    avg_radiation = np.random.normal(0.5, 0.1) * sunlight_hours  # 輻射量與日照時數成比例 
    rainfall = random.randint(0, 200)  # 降雨量
    cloud_cover = 100 - (sunlight_hours / 24 * 100)  # 雲層覆蓋率與日照時數成反比
    shading = random.randint(0, 100)  # 遮蔽率
    failure_rate = random.randint(0, 100)  # 故障率
    angle = random.randint(0, 90)  # 擺放角度
    sun_angle = random.randint(0, 90)  # 太陽照射角度
    altitude = random.randint(-100, 8850)  # 海拔

    #generation_time =   # 參考公式

    return [f'{longitude},{latitude}', hemisphere, generation_time, capacity,
            weather, panel_temp, avg_temp, avg_radiation, rainfall, cloud_cover,
            shading, failure_rate, angle, sunlight_hours, sun_angle, altitude]

# 寫入CSV檔案
with open('Simulate_Factors_Data.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # 寫入標題行
    csv_writer.writerow(['經度,緯度', '南北半球', '產生時間(mins)', '設備容量(kW)', '天氣現象', '面板溫度(°)', '期間平均室外溫度(°)', '期間平均太陽輻射量(kW/m2)', '期間降雨量(mm)', '雲層覆蓋率(%)', '遮蔽率(%)', '故障率(%)', '擺放角度(°)', '期間平均日照時數(h)', '太陽照射角度(°)', '海拔(m)'])
    
    # 隨機生成數據並寫入檔案
    num_records = 100  # 生成100筆數據
    for _ in range(num_records):
        csv_writer.writerow(generate_random_data())
