import numpy as np
import folium
from folium.plugins import HeatMap
import pandas as pd

# 加载CSV数据
df = pd.read_csv('Shenzhen_unique_house_data_avg_price.csv')

# 对总价/万元进行对数变换
# df['总价对数'] = np.log1p(df['单价元/平'])
df['总价对数'] = np.log1p(df['总价/万元'])

# 创建一个列表，其中包含经纬度和对数变换后的总价
data = df[['GCJ02纬度', 'GCJ02经度', '总价对数']].values.tolist()

# 创建Folium地图对象，以数据的平均经纬度作为中心
map = folium.Map(location=[df['GCJ02纬度'].mean(), df['GCJ02经度'].mean()], zoom_start=12,
                 tiles='https://webrd04.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',
                 attr='彩色版',
                 )
                 
# 添加热力图层，使用对数变换后的总价作为权重
# HeatMap(data, radius=35, blur=20, max_zoom=1, min_opacity=0.7).add_to(map)
HeatMap(data).add_to(map)
# 保存地图为HTML文件
map.save('heatmap/Shenzhen_house_price_heatmap_log.html')
