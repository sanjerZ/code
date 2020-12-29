import requests
import os
from bs4 import BeautifulSoup

url = 'https://unsplash.com/t/nature/'
fake_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}
response = requests.get(url, headers=fake_headers)  # 请求参数里面把假的请求header加上
soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
all_photos = soup.find('div', class_="qztBA")
# print(all_photos)
imgObj = []
# conObj = all_photos.find_all('div', class_="nDTlD")
# print(conObj)
for each_photo in all_photos.find_all('div', class_="nDTlD"):
    imgObj.append(each_photo.find('a', class_="_2Mc8_")['href'])
# print(imgObj)

for img in imgObj:
    print(img)
    src ='https://unsplash.com'+img+'/download'
    with open("./img/"+os.path.basename(img)+".jpg",'wb')as f:
        f.write(requests.get(src).content)
    print("finish")
