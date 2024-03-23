import requests
import pandas as pd
from tqdm import tqdm
import os

# 百度地图API配置
host = "https://api.map.baidu.com"
uri = "/geocoding/v3"
ak = ""  # 请替换为你的实际AK
# 设定输入和部分处理后的文件路径
original_file_path = '../格式处理/Shenzhen_cleaning.csv'
partial_file_path = 'Shenzhen_data_laln_partial.csv'
final_file_path = 'Shenzhen_data_laln_final.csv'

# 检查是否存在部分处理的文件
if os.path.exists(partial_file_path):
    print("找到部分处理的文件。从上次保存的状态继续...")
    df = pd.read_csv(partial_file_path)
else:
    print("未找到部分处理的文件。从头开始...")
    df = pd.read_csv(original_file_path)
    if '经度' not in df.columns or '纬度' not in df.columns:
        df['经度'] = pd.NA
        df['纬度'] = pd.NA

# 设置保存进度的阈值
save_threshold = 100

for index, row in tqdm(df.iterrows(), total=df.shape[0]):
    if pd.isna(row['经度']) or pd.isna(row['纬度']):
        params = {
            "address": row['位置'],
            "output": "json",
            "ak": ak,
        }

        response = requests.get(url=host + uri, params=params)
        if response:
            json_data = response.json()
            if json_data['status'] == 0:
                print(json_data['result']['location']['lng'], json_data['result']['location']['lat'])
                df.at[index, '经度'] = json_data['result']['location']['lng']
                df.at[index, '纬度'] = json_data['result']['location']['lat']
            else:
                print(f"获取位置时出错{row['位置']}: {json_data}")
        else:
            print(f"请求失败{row['位置']}")

    if index % save_threshold == 0 or index == df.shape[0] - 1:
        df.to_csv(partial_file_path, index=False)
        print(f"当前保存进度索引:{index}.")

# 最终保存所有数据
df.to_csv(final_file_path, index=False)
print("所有数据均已保存")
