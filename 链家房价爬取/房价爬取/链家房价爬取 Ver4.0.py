import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
import pandas as pd

df = pd.read_csv('深圳分区链接.csv')

base_url_template = "https://sz.lianjia.com/{}/pg"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}

for suffix in df['后缀']:
    # 清理和转换后缀以用作文件名
    safe_suffix = suffix.replace('/', '_').strip('_')

    base_url = base_url_template.format(suffix)
    response = requests.get(base_url + '1', headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        page_data = soup.find('div', class_='page-box house-lst-page-box')['page-data']
        total_pages = eval(page_data)['totalPage']

        # 为每个后缀创建一个新的CSV文件
        csv_file_name = f'Crawling-temp/house_data_{safe_suffix}.csv'
        with open(csv_file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['位置', '房屋信息', '总价/万元', '单价元/平'])

            for page in tqdm(range(1, total_pages + 1), desc=f"保存进度{suffix}"):
                current_url = base_url + str(page)
                page_response = requests.get(current_url, headers=headers)
                if page_response.status_code == 200:
                    page_soup = BeautifulSoup(page_response.content, 'lxml')
                    listings = page_soup.select('.info')
                    for listing in listings:
                        position_info = ' - '.join([a.text for a in listing.select('.positionInfo a')])
                        house_info = listing.select_one('.houseInfo').text.strip()
                        total_price_info = listing.select_one('.totalPrice').text.strip()
                        unit_price_info = listing.select_one('.unitPrice span').text.strip()

                        writer.writerow([position_info, house_info, total_price_info, unit_price_info])

        print(f"所有页面的数据已保存到{csv_file_name}")
