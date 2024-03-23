import requests

# 服务地址
host = "https://api.map.baidu.com"

# 接口地址
uri = "/geocoding/v3"

# 此处填写你在控制台-应用管理-创建应用后获取的AK
ak = ""

params = {
    "address":    "广东省深圳市南山区深圳湾公馆",
    "output":    "json",
    "ak":       ak,

}

response = requests.get(url = host + uri, params = params)
if response:
    print(response.json())