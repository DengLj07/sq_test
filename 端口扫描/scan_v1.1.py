# -*- coding: utf-8 -*-
"""
@Time    : 2022/6/25 22:44
@File    : scan_v1.1.py
"""
import socket
import re
from time import time

"""
1.扫描多个端口
2.扫描域名格式
"""

def check_ip(ip):
    # 1.正则表达式判断ip是否正确
    ip_address = re.compile("(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)")
    if ip_address.match(ip) and len(ip) >= 0:
        return True
    else:
        return False

def check_domain(domain):
    # 1.正则表达式判断ip是否正确
    dm = re.compile("[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+.?")
    if dm.match(domain) and len(domain) >= 0:
        return True
    else:
        return False

def domain_to_ip(domain):
    # 获取域名ip
    server_ip = socket.gethostbyname(domain)
    # print(f"{domain}--{server_ip}")
    return server_ip

def scan_tool(ip, port:str):
    now = time()
    start_port, end_port = port.split(",")
    for one in range(int(start_port), int(end_port)+1):
        # 1.建立tcp连接
        TCP_sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        TCP_sk.settimeout(0.5)
        try:
            # 2.查看返回值
            conn = TCP_sk.connect_ex((ip, one))
            if conn == 0:
                print(f"服务器：{ip}，端口：{one}---已开放")
            else:
                print(f"服务器：{ip}，端口：{one}---未开放")
        except:
            print("扫描异常！")
        TCP_sk.close()
    end_time = time()
    print(f"扫描耗时---{str(end_time-now).split('.')[0]}s")

if __name__ == '__main__':
    ip = input("input ip:")
    port = input("input port:").strip()
    if check_ip(ip):
        scan_tool(ip, port)
    elif check_domain(ip):
        ip = domain_to_ip(ip)
        scan_tool(ip, port)
    else:
        print("输入有误")
