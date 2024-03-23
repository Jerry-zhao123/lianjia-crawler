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

def gcj02_to_wgs84(gcj_lon, gcj_lat):
    a = 6378245.0
    ee = 0.00669342162296594323
    dLat = transform_lat(gcj_lon - 105.0, gcj_lat - 35.0)
    dLon = transform_lon(gcj_lon - 105.0, gcj_lat - 35.0)
    radLat = gcj_lat / 180.0 * math.pi
    magic = math.sin(radLat)
    magic = 1 - ee * magic * magic
    sqrtMagic = math.sqrt(magic)
    dLat = (dLat * 180.0) / ((a * (1 - ee)) / (magic * sqrtMagic) * math.pi)
    dLon = (dLon * 180.0) / (a / sqrtMagic * math.cos(radLat) * math.pi)
    wgs_lat = gcj_lat - dLat
    wgs_lon = gcj_lon - dLon
    return wgs_lon, wgs_lat

def bd09_to_wgs84(bd_lon, bd_lat):
    gcj_lon, gcj_lat = bd09_to_gcj02(bd_lon, bd_lat)
    wgs_lon, wgs_lat = gcj02_to_wgs84(gcj_lon, gcj_lat)
    return wgs_lon, wgs_lat

def transform_lat(lon, lat):
    ret = -100.0 + 2.0 * lon + 3.0 * lat + 0.2 * lat * lat + 0.1 * lon * lat + 0.2 * math.sqrt(abs(lon))
    ret += (20.0 * math.sin(6.0 * lon * math.pi) + 20.0 * math.sin(2.0 * lon * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * math.pi) + 40.0 * math.sin(lat / 3.0 * math.pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * math.pi) + 320 * math.sin(lat * math.pi / 30.0)) * 2.0 / 3.0
    return ret

def transform_lon(lon, lat):
    ret = 300.0 + lon + 2.0 * lat + 0.1 * lon * lon + 0.1 * lon * lat + 0.1 * math.sqrt(abs(lon))
    ret += (20.0 * math.sin(6.0 * lon * math.pi) + 20.0 * math.sin(2.0 * lon * math.pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lon * math.pi) + 40.0 * math.sin(lon / 3.0 * math.pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lon / 12.0 * math.pi) + 300.0 * math.sin(lon * math.pi / 30.0)) * 2.0 / 3.0
    return ret

# 加载CSV数据
csv_file_path = '../百度地图经纬度获取/Shenzhen_data_laln_partial.csv'  # 请根据实际路径调整
df = pd.read_csv(csv_file_path)

# 应用坐标转换
df['WGS84经度'], df['WGS84纬度'] = zip(*df[['经度', '纬度']].apply(lambda x: bd09_to_wgs84(x['经度'], x['纬度']), axis=1))

# 显示结果
df.to_csv('temp/Shenzhen_data_bd09_to_wgs84.csv', index=False)

print("转换完成，结果已保存到 temp/Shenzhen_data_bd09_to_wgs84.csv")
