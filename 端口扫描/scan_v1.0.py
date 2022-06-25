# -*- coding: utf-8 -*-
"""
@Time    : 2022/6/25 22:26
@File    : scan_v1.0.py
"""
"""
1.建立tcp连接
2.查看连接返回
3.判断连接返回值
4.循环扫描剩余端口
"""
import socket


def scan_tool(ip, port):
    # 1.建立tcp连接
    TCP_sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP_sk.settimeout(0.5)
    try:
        # 2.查看返回值
        conn = TCP_sk.connect_ex((ip, port))
        print(conn)
        if conn == 0:
            print(f"服务器：{ip}，端口：{port}---已开放")
        else:
            print(f"服务器：{ip}，端口：{port}---未开放")
    except:
        print("扫描异常！")

if __name__ == '__main__':
    ip = input("input ip:")
    port = int(input("input port:").strip())
    scan_tool(ip, port)
