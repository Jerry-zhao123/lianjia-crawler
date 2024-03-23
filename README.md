# lianjia-crawler

## 项目描述
本项目旨在爬取链家网站上关于各片区房价的信息，并基于这些数据生成层次图和热力图。

## 主要文件及使用顺序

1. `链家房价爬取 Ver4.0.py`
   - 根据`深圳分区链接.csv`中的内容，自动爬取每个链接中的所有页面房价信息，并将结果单独保存至`Crawling-temp`文件夹中对应的csv文件里。
   - `深圳分区链接.csv`需用户根据链家网站的导航栏内容自行爬取和替换。

2. `数据清洗 Ver2.0.py`
   - 对爬取的数据进行清洗，并添加前缀以提高后续坐标获取的准确度。
   - 若爬取内容非深圳市，需要进行相应的修改。

3. `百度API获取经纬度 Ver2.0.py`
   - 需要在[百度地图API控制台](https://lbsyun.baidu.com/apiconsole/key#/home)获取地理编码的WebAPI的AK。可以使用`APIKey测试.py`进行测试。
   - 推荐使用腾讯地图API获取经纬度，因为其每日免费额度为1万条，且使用的坐标系为GCJ-02，与folium底图更兼容。

4. `坐标协议转换.py`
   - 将百度的BD-09坐标转换为folium底图默认的WGS84坐标。转换后的坐标将新增两列保存于原有文件中。

5. `小区去重 Ver2.0.py`
   - 对数据进行精简，使得每个小区只有一个数值进行绘制，避免地图资源的过度占用。

6. `Shenzhen_Choropleth_map.py` / `Shenzhen_heatmap_log.py`
   - 根据房价总价/单价绘制层次图或热力图。

