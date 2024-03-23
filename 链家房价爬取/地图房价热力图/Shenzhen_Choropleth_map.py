import folium
import pandas as pd

df = pd.read_csv('Shenzhen_unique_house_data.csv')
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

map = folium.Map(location=[df['WGS84纬度'].mean(), df['WGS84经度'].mean()], zoom_start=12,
                 # tiles='https://server.arcgisonline.com/arcgis/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}.png',
                 # attr='彩色版',
                 )

# for _, row in df.iterrows():
#     folium.Circle(
#         location=[row['WGS84纬度'], row['WGS84经度']],
#         radius=100,
#         color=price_range_color(row['单价元/平']),
#         fill=True,
#         fill_color=price_range_color(row['单价元/平'])
#     ).add_to(map)

for _, row in df.iterrows():
    folium.Circle(
        location=[row['WGS84纬度'], row['WGS84经度']],
        radius=100,
        color=price_range_color(row['总价/万元']),
        fill=True,
        fill_color=price_range_color(row['总价/万元'])
    ).add_to(map)

map.save('heatmap/Shenzhen_house_price_range_map.html')
search_text = "cdn.jsdelivr.net"
replace_text = "gcore.jsdelivr.net"
# 使用 open() 函数以只读模式打开文本文件
with open(r'heatmap/Shenzhen_house_price_range_map.html', 'r', encoding='UTF-8') as file:
    # 使用 read() 函数读取文件内容并将它们存储在一个新变量中
    data = file.read()
    # 使用 replace() 函数搜索和替换文本
    data = data.replace(search_text, replace_text)
# 以只写模式打开文本文件以写入替换的内容
with open(r'heatmap/Shenzhen_house_price_range_map.html', 'w', encoding='UTF-8') as file:
    # 在文本文件中写入替换的数据
    file.write(data)
