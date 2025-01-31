#!/usr/bin/python3
# coding: utf-8

import sys
import requests
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer

class BalanceChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.update_balance()

    def initUI(self):
        self.layout = QVBoxLayout()

        # フォントサイズを大きく設定し、右揃えに設定
        self.balance_label = QLabel("Fetching balance...", self)
        self.balance_label.setStyleSheet("font-size: 36px; font-weight: bold; color: #333; text-align: right;")  # 文字サイズ・色設定
        self.layout.addWidget(self.balance_label)

        self.jpy_label = QLabel("", self)
        self.jpy_label.setStyleSheet("font-size: 24px; color: #333; text-align: right;")  # 文字サイズ・色設定
        self.layout.addWidget(self.jpy_label)

        self.setLayout(self.layout)
        self.setWindowTitle('今のモネロ')
        self.setGeometry(100, 100, 200, 100)  # ウィンドウサイズを少し大きく調整

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_balance)
        self.timer.start(600000)  # 10分

    def update_balance(self):
        xmr_url_left = "https://api.nanopool.org/v1/xmr/balance/"
        xmr_adress = "" #あなたのアドレスを追加してね☆
        xmr_url = xmr_url_left + xmr_adress
        jpy_url = "https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=jpy"  # 正しい為替レートAPIのURL

        try:
            xmr_response = requests.get(xmr_url)
            jpy_response = requests.get(jpy_url)

            if xmr_response.status_code == 200 and jpy_response.status_code == 200:
                xmr_data = xmr_response.json()
                jpy_data = jpy_response.json()

                balance = xmr_data.get('data', 'N/A')
                xmr_to_jpy = jpy_data['monero'].get('jpy', 'N/A')

                if balance != 'N/A' and xmr_to_jpy != 'N/A':
                    balance_xmr = float(balance)
                    balance_jpy = balance_xmr * xmr_to_jpy

                    self.balance_label.setText(f"{balance_xmr:.8f} XMR")
                    self.jpy_label.setText(f"{balance_jpy:.2f} JPY")
                else:
                    self.balance_label.setText("Balance not available")
                    self.jpy_label.setText("JPY rate not available")
            else:
                self.balance_label.setText(f"Failed to fetch balance (HTTP {xmr_response.status_code})")
                self.jpy_label.setText(f"Failed to fetch JPY rate (HTTP {jpy_response.status_code})")
        except requests.exceptions.RequestException as e:
            self.balance_label.setText(f"Request error: {str(e)}")
            self.jpy_label.setText("JPY rate not available")
        except ValueError:
            self.balance_label.setText("Failed to parse JSON response")
            self.jpy_label.setText("Failed to parse JPY rate")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BalanceChecker()
    ex.show()
    sys.exit(app.exec_())
