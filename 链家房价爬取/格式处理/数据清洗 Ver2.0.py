import pandas as pd
import re
import os
import glob

# 设定包含原始CSV文件的目录
directory = "../房价爬取/Crawling-temp"
# 设定输出目录
output_directory = "Cleaning-temp"
# 设定汇总文件的路径
summary_file_path = "Shenzhen_cleaning.csv"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)
summary_df = pd.DataFrame()

# 遍历指定目录下的所有CSV文件
for file_path in glob.glob(os.path.join(directory, "house_data_ershoufang_*.csv")):
    # 读取CSV文件
    df = pd.read_csv(file_path, header=0, names=['位置', '房屋信息', '总价/万元', '单价元/平'])
    for col in df.columns:
        df[col] = df[col].apply(lambda x: x.replace(' ', '') if isinstance(x, str) else x)
    df['位置'] = df['位置'].apply(lambda x: "广东省深圳市" + re.sub('-.*', '', x.split(',')[0]))
    df['总价/万元'] = df['总价/万元'].str.replace("参考价:", "").str.replace("万", "")
    df['单价元/平'] = df['单价元/平'].str.replace(",", "").str.replace("元/平", "")

    summary_df = pd.concat([summary_df, df], ignore_index=True)

    # 构建输出文件的路径
    output_file_path = os.path.join(output_directory, os.path.basename(file_path).replace(".csv", "_after.csv"))
    df.to_csv(output_file_path, index=False)

# 保存汇总的数据到单独的CSV文件
summary_df.to_csv(summary_file_path, index=False)

print("所有文件的数据清洗完成，并已保存到新的文件中。")
