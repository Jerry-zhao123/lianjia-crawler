import numpy as np
import folium
from folium.plugins import HeatMap
import pandas as pd

# 加载CSV数据
df = pd.read_csv('Shenzhen_unique_house_data.csv')

# 对总价/万元进行对数变换
# df['总价对数'] = np.log1p(df['单价元/平'])
df['总价对数'] = np.log1p(df['总价/万元'])

# 创建一个列表，其中包含经纬度和对数变换后的总价
data = df[['WGS84纬度', 'WGS84经度', '总价对数']].values.tolist()

# 创建Folium地图对象，以数据的平均经纬度作为中心
map = folium.Map(location=[df['WGS84纬度'].mean(), df['WGS84经度'].mean()], zoom_start=13)

# 添加热力图层，使用对数变换后的总价作为权重
# HeatMap(data, radius=35, blur=20, max_zoom=1, min_opacity=0.7).add_to(map)
HeatMap(data).add_to(map)
# 保存地图为HTML文件
map.save('heatmap/Shenzhen_house_price_heatmap_log.html')
