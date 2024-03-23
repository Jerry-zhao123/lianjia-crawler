import pandas as pd

csv_file_path = 'temp/Shenzhen_data_bd09_to_wgs84.csv'
df = pd.read_csv(csv_file_path)

# 按“位置”分组，并计算每个小区的“总价/万元”平均值
df_avg_price = df.groupby('位置')['总价/万元'].mean().reset_index()

# 将原始DataFrame中的“总价/万元”列替换为计算出的平均值
df_unique = df.drop_duplicates(subset='位置', keep='first').drop(columns=['总价/万元'])
df_merged = pd.merge(df_unique, df_avg_price, on='位置', how='left')

# 保存去重后且已更新总价平均值的数据到新CSV文件
df_merged.to_csv('Shenzhen_unique_house_data_avg_price.csv', index=False)

print("去重后且总价平均值已更新的数据已保存到 Shenzhen_unique_house_data_avg_price.csv")
