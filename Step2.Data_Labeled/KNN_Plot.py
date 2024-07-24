import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


df = pd.read_csv('E:/git_repos/E-KNN/Test/test7_v3.csv', encoding = 'Big5')

# 提取需要的欄位
x = df['日照率(%)'].values  # 日照率(%)
y = df['期間平均太陽輻射率(%)'].values  # 期間平均太陽輻射率(%)
sizes = df['天氣發電時間(h)'].values  # 固定裝置容量_天氣發電時間(h)
labels = df['標記'].values  # 合理性標籤

# 設定圖表屬性
plt.figure(figsize=(8, 8))
plt.rcParams['font.size'] = 14
plt.title('Solar Power Generation Data')

# 統計標籤種類和數量
unique_labels = df['標記'].unique()
label_counts = df['標記'].value_counts()

# 顏色設定
colors = {1: cm.Dark2.colors[1], 0: cm.Dark2.colors[0]}
label_names = {1: 'Reasonable', 0: 'Unreasonable'}

# 根據 outcome 繪製資料點和加上圖例
for label in unique_labels:
    mask = labels == label
    label_name = label_names[label]
    count = label_counts[label]
    plt.scatter(x[mask], y[mask], s=50, color=colors[label], 
                label=f'Label={label} ({label_name}), {count} data')
# 設置標籤和圖例
plt.xlabel('Sunshine Rate(%)')
plt.ylabel('Average Solar Radiation Ratio(%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
