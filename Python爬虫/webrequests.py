import requests
import random
# 获取网页数据文本信息,返回值为网页内容
'''def send_request(company_id, page):
    url = 'https://www.jobui.com/company/{0}/jobs/?n={1}/'.format(company_id, page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 404:
        return None
    return resp.text
'''
def get_data(url,encoding='utf8'):
    # TODO 补充内容
    headers = {'User-Agent': get_headers()}
    try:
        response = requests.get(url,headers=headers)
        response.encoding = encoding
        data = response.text
        return data
    except Exception as e:
        print("出错:", e)
        return None



#随机获取headers，避免同一浏览器请求次数太多被列入黑名单
def get_headers():
    headers_list= [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"]

    return random.choice(headers_list)
if __name__ == '__main__':
   print(get_data('https://www.jobui.com/jobs?jobKw=Python工程师&cityKw=北京'))