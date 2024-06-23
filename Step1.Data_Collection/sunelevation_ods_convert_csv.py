import pandas as pd
from odf.opendocument import load
from odf.table import Table, TableRow, TableCell
from odf.text import P

def ods_to_df(file_path):
    doc = load(file_path)
    data = []

    for sheet in doc.spreadsheet.getElementsByType(Table):
        for row in sheet.getElementsByType(TableRow):
            row_data = []
            for cell in row.getElementsByType(TableCell):
                # Get cell text, if any
                cell_text = ""
                for p in cell.getElementsByType(P):
                    for text in p.childNodes:
                        cell_text += str(text.data)
                row_data.append(cell_text)
            data.append(row_data)

    # Create DataFrame
    df = pd.DataFrame(data)
    df.columns = df.iloc[0]  # Set the first row as the column headers
    df = df[1:]  # Remove the first row from the data
    return df

# List of file paths
ods_files = [
    'E:/git_repos/E-KNN/Dataset/sun_01taipeicity.ods',
    'E:/git_repos/E-KNN/Dataset/sun_02newtaipeicity.ods',
    'E:/git_repos/E-KNN/Dataset/sun_03taoyuancity.ods',
    'E:/git_repos/E-KNN/Dataset/sun_06taichungcity.ods',
    'E:/git_repos/E-KNN/Dataset/sun_07changhuacounty.ods',
    'E:/git_repos/E-KNN/Dataset/sun_08nantoucounty.ods',
    'E:/git_repos/E-KNN/Dataset/sun_10chiayicity.ods',
    'E:/git_repos/E-KNN/Dataset/sun_11tainancity.ods',
    'E:/git_repos/E-KNN/Dataset/sun_12kaohsiungcity.ods',
    'E:/git_repos/E-KNN/Dataset/sun_13pingtungcounty.ods'
]

# Convert each ODS file to a CSV file
csv_files = []
for ods_file in ods_files:
    csv_file = ods_file.replace('.ods', '.csv')
    df = ods_to_df(ods_file)
    df.to_csv(csv_file, index=False, encoding='utf-8-sig')
    csv_files.append(csv_file)
    print(f'Converted {ods_file} to {csv_file}')