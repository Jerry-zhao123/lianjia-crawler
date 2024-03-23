import folium
import pandas as pd

df = pd.read_csv('Shenzhen_unique_house_data_avg_price.csv')
# def price_range_color(price):
#     if price < 60000:
#         return 'blue'
#     elif price < 80000:
#         return 'green'
#     elif price < 100000:
#         return 'orange'
#     elif price < 120000:
#         return 'red'
#     else:
#         return 'black'

def price_range_color(price):
    if price < 400:
        return 'blue'
    elif price < 600:
        return 'green'
    elif price < 800:
        return 'orange'
    elif price < 1000:
        return 'red'
    else:
        return 'black'

map = folium.Map(location=[df['GCJ02纬度'].mean(), df['GCJ02经度'].mean()], zoom_start=12,
                 tiles='https://webrd04.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=7&x={x}&y={y}&z={z}',
                 attr='彩色版',
                 )

# for _, row in df.iterrows():
#     folium.Circle(
#         location=[row['GCJ02纬度'], row['GCJ02经度']],
#         radius=100,
#         color=price_range_color(row['单价元/平']),
#         fill=True,
#         fill_color=price_range_color(row['单价元/平'])
#     ).add_to(map)

for _, row in df.iterrows():
    folium.Circle(
        location=[row['GCJ02纬度'], row['GCJ02经度']],
        radius=100,
        color=price_range_color(row['总价/万元']),
        fill=True,
        fill_color=price_range_color(row['总价/万元'])
    ).add_to(map)

map.save('heatmap/Shenzhen_house_price_range_map.html')