# -*- coding: utf-8 -*-
"""
@Time    : 2022/7/3 19:56
@File    : api_test_utils.py
"""
import json
import requests
import threading
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile


class HttpClient:

    def __init__(self, ui_name="接口测试工具.ui"):
        self.q_file = QFile(ui_name)
        self.q_file.open(QFile.ReadOnly)
        self.ui = QUiLoader().load(self.q_file)
        self.q_file.close()
        self.ui.show()
        self.ui.send.clicked.connect(self.send)

    def send(self):
        self.ui.response.clear()
        method = self.ui.method.currentText().upper()
        url = self.ui.url.text()
        headers = self.ui.headers.toPlainText()
        if headers != "":
            headers = json.loads(headers)
        payload = self.ui.body.toPlainText()
        if payload != "":
            payload = json.loads(payload)

        resp = requests.Request(method, url, headers=headers, data=payload)
        prepare = resp.prepare()
        s = requests.Session()
        # 多线程
        t = threading.Thread(target=self.thread_send, args=(s, prepare))
        t.start()

    def show_response(self, resp):
        resp.encoding = "utf-8"
        self.ui.response.append(
            "HTTP/1.1 {} \n{}\n\n".format(
                resp.status_code,
                "\n".join("{}:{}".format(k, v) for k, v in resp.headers.items()),
            )
        )

    def thread_send(self, s, p):
        resp = s.send(p)
        self.show_response(resp)

app = QApplication([])
http = HttpClient()
app.exec_()

