import pandas as pd
import math

# 定义坐标转换函数
def bd09_to_gcj02(bd_lon, bd_lat):
    x_pi = 3.14159265358979324 * 3000.0 / 180.0
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gcj_lon = z * math.cos(theta)
    gcj_lat = z * math.sin(theta)
    return gcj_lon, gcj_lat

# 加载CSV数据
csv_file_path = '../百度地图经纬度获取/Shenzhen_data_laln_partial.csv'  # 请根据实际路径调整
df = pd.read_csv(csv_file_path)

# 应用坐标转换
df['GCJ02经度'], df['GCJ02纬度'] = zip(*df[['经度', '纬度']].apply(lambda x: bd09_to_gcj02(x['经度'], x['纬度']), axis=1))

# 显示结果并保存
df.to_csv('temp/Shenzhen_data_bd09_to_gcj02.csv', index=False)

print("转换完成，结果已保存到 temp/Shenzhen_data_bd09_to_gcj02.csv")
