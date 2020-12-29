from bs4 import BeautifulSoup
import os
import requests
url = "https://movie.douban.com/cinema/later/beijing/"  
fake_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; '\
'WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
}
response = requests.get(url, headers=fake_headers)
soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
all_movies = soup.find('div', id="showing-soon")
srcObj = []
imgObj = []
# i = 0
for each_movie in all_movies.find_all('div', class_="item"):
    imgObj.append(each_movie.find("img"))
    srcObj.append(all_img[0]['src'])
# #     s = str(imgObj[i])[19:-3]
#     s = str(imgObj[i]).split('"')[-2]
#     i = i + 1
# #     print(s[19:-1])    
#     srcObj.append(s)
# print(srcObj)
for src in srcObj:
    print(src)
    with open("./Pictures/"+os.path.basename(src),'wb') as f:
        f.write(requests.get(src).content)
#     print("cheng")
