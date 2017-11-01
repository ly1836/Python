import  requests
from bs4 import BeautifulSoup

def figure():
    url = "http://nanrenvip.net/e/action/get_more_nvyou.php"
    data = {"next": 10000, "table": "nvyou", "action": "getmorenvyou", "limit": 10, "small_length": 10,
            "orderby": "onclick"}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    respone = requests.post("http://nanrenvip.net/e/action/get_more_nvyou.php", data=data)

    if respone.text.__len__() > 1:
        print(respone.text.__len__())
        soup = BeautifulSoup(respone.text, 'lxml')
        ips = soup.find_all('li')

        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('a')
            print("别名:%s" % tds[0].attrs['href'])
            print("名字:%s" % tds[0].text)
            print("图片:%s" % tds[0].next_element.attrs['src'])
    else:
        print("null")
        pass




if __name__ == "__main__":
    figure()



