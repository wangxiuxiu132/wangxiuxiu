import requests
url="https://v0.yiketianqi.com/api"
data={
    "appid":"55121823Q",
    "appsecret":"f4Xoduz", 
    "version":"v61"
}
result=requests.get(url=url,params=data)
print(result.json())




