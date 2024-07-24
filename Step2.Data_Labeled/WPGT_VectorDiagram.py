import pandas as pd
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt


#繪製圖形
def plot_correlation(data, x_labels, y_labels):
    # 初始化圖形
    rcParams['figure.figsize'] = 15, 20
    fig, ax = plt.subplots()   #製作圖形和軸
    sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)   #矩正圖
    ax.set_xticklabels(x_labels, rotation=45, horizontalalignment='right')
    ax.set_yticklabels(y_labels, rotation=0)
    plt.show()
    fig.savefig('corr.png')

#資料路徑
file_path = r'E:/git_repos/E-KNN/Test/test7_v3.csv'
data = pd.read_csv(file_path, encoding='unicode_escape')
print("列名:", data.columns)

data_subset = data.iloc[:, 4:17]  # E欄到P欄
print("子集列名:", data_subset.columns)

# XY軸欄位名稱
x_labels = ['Average Outdoor Temperature Ratio (%)', 'Precipitation Ratio (%)', 'Sunshine Rate (%)', 'Average Solar Radiation Ratio (%)', 'Cloud Cover Ratio (%)', 'Optimal Tilt Angle Ratio (%)', 'Panel Temperature Ratio (%)', 'Failure Rate (%)', 'Shading Ratio (%)','Device Power Generation Time (h)','Weather Power Generation Time (h)','Outcome']
y_labels = x_labels
#繪製
plot_correlation(data_subset, x_labels, y_labels)