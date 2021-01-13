import requests

url = "https://api.yonyoucloud.com/apis/dst/checkPhoneIfNullByMobiles/getPhoneIfNullByMobiles"

payload="{\"Content-Type\":\"application/json\",\"mobiles\":\"13402933281,18710508177,13991005150\"}"
headers = {
  'apicode': '6d212ec044eb43219555878fa06bedfd',
  'Content-Type': 'application/json',
  'Cookie': 'SERVERID=2651794d8e79974471ac0037cf5a859d|1608084794|1608083213; acw_tc=2760827716080853646574163e8b8ed7fa4f19e00d93535f9cefd80737eb06'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
