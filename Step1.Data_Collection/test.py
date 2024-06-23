import pandas as pd

def ods_to_csv(ods_file_path, csv_file_path):
    # Read the ODS file
    df = pd.read_excel(ods_file_path, engine='odf')
    
    # Write to CSV file
    df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

# Define file paths
ods_file_path = 'E:/git_repos/E-KNN/Dataset_sunelevation/sun_20lienchiangcounty.ods'
csv_file_path = 'E:/git_repos/E-KNN/Dataset_sunelevation/sun_20lienchiangcounty.csv'

# Convert the ODS file to CSV
ods_to_csv(ods_file_path, csv_file_path)

print(f"Converted {ods_file_path} to {csv_file_path}")

# # 转换上传的文件
# files = [
#     ('E:/git_repos/E-KNN/Dataset_sunelevation/sun_19kinmencounty.ods', 'E:/git_repos/E-KNN/Dataset_sunelevation/sun_19kinmencounty.csv'),
#     ('E:/git_repos/E-KNN/Dataset_sunelevation/sun_18penghucounty.ods', 'E:/git_repos/E-KNN/Dataset_sunelevation/sun_18penghucounty.csv'),
#     ('E:/git_repos/E-KNN/Dataset_sunelevation/sun_20lienchiangcounty.ods', 'E:/git_repos/E-KNN/Dataset_sunelevation/sun_20lienchiangcounty.csv')
# ]