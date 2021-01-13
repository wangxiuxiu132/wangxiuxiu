import requests
url="https://api.yonyoucloud.com/apis/dst/checkPhoneIfNullByMobiles/getPhoneIfNullByMobiles"
header={
    "Content-Type":"application/json",
    "apicode":"6d212ec044eb43219555878fa06bedfd"
}
data={
    "mobiles":"13402933281,18710508177,13991005150"
}
result=requests.post(url=url,headers=header,data=data)
print(result.text)
