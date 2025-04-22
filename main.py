import requests
from bs4 import BeautifulSoup

# 目标网站的登录页面和数据提交地址（action）

target_url = 'https://java-ent-search-cloud-test.kailinesb.com/java-ent-search-cloud/mainentsearch/mainEnt'  # 登录后想要访问的数据页面
target_url1 = 'https://java-saascard-cloud-external-test.kailinesb.com/java-saasCard-cloud/employee/getMyEntity'  # 登录后想要访问的数据页面


# 创建一个session对象
session = requests.Session()

# 自定义的HTTP头部信息，包含认证信息
headers_with_auth = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Content-Type': 'application/json',
    'Platform': 'PC-ADMIN'
}

# 登录参数
payload = {
  "phone": "18996929332",
  "secret": "a53416620"
}

# 登录url
login_url = 'https://java-saascard-cloud-external-test.kailinesb.com/java-saasCard-cloud/pcLogin/secretLogin'

# 登录
response = session.post(login_url, json=payload, headers=headers_with_auth, verify= False)

# 检查是否登录成功
if response.status_code == 200:
    print("登录成功")
    data = response.json()
    # 访问选择企业界面
    
    payload2 = {
        "current": 1,
        "entityId": "",
        "size":100
    }
    resData = data.get('data')
    headers_with_auth["Authorization"] = resData.get("token")
    # 访问登录后的页面
    
    resData = session.post(target_url1, json = payload2, headers = headers_with_auth, verify= False).json().get('data')
    entityId = resData.get('records')[0].get('id')
    payload2['entityId'] = entityId
    # 访问登录后的页面
    payload3 = {"current":1,"size":10}
    payload3['entityId'] = entityId
    headers_with_auth["entityId"] = str(entityId)
    response_data = session.post(target_url,json = payload3,headers=headers_with_auth, verify= False)
    records = response_data.json().get('data').get('content')
    # 使用BeautifulSoup解析响应内容
    soup = BeautifulSoup(response_data.text, 'lxml')
    print(soup.prettify())
    # 解析数据
    print(soup)
        
else:
    print(f"登录失败: {response.status_code}")
    
    
    