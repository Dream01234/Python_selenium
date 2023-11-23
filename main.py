import json
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import requests
import jsonpath

# 请求头
Headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
         }
# 测试地址
url = 'https://devtest3.buildingqm.com/uc/app/verify_login/'

# 测试数据
data = {
    'device_id':'351564297070492',
    'username':'kentestgrp10',
    'password':'12345678'
}

# 发送请求
r = requests.post(url,data=data,headers=Headers)
json_data = r.json()
print(json_data)

# 提取token
token = '$.data.token'
token1 = jsonpath.jsonpath(json_data,token)

# 将list类型转换为str
token2 = "".join(token1)
print(token1)

# 设置手机模拟器模式
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation',{'deviceName':'iPhone X'})

# 创建浏览器驱动对象
driver = webdriver.Chrome(options=options)

url2 = 'https://devtest3.buildingqm.com/public/app3/bpm/app/nav.html?lang=zh_CN&token='+token2+'&project_id=100496&team_id=100338&group_id=100337&en_name=bsi_rfi&page_level=project&show_other=1'
# # 打开百度首页
driver.get(url2)

sleep(5)
driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[1]/ul/li/div").click()

# 浏览器窗口最大化
# driver.maximize_window()

# 休眠2s
sleep(5)

# 关闭窗口
driver.quit()