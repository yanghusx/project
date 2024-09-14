import requests

S = "current"

url = "http://www.xinfadi.com.cn/getPriceData.html"


def save_data(data_list):
    with open("vegetable.csv", "w", encoding="utf-8") as f:
        for i in data_list:
            f.write(str(i))
            f.write("\n")
def downloads_data(url):
    heads = {"content-type": "application/x-www-form-urlencoded; charset=UTF-8", "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
    response = requests.post(url, headers=heads)
    data = response.json()
    print(data.get("list"))
    save_data(data.get("list"))


if __name__ == '__main__':
    downloads_data(url)