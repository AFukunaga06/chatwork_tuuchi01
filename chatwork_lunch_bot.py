#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chatwork 休憩通知ボット
複数の時間に休憩開始・終了メッセージをChatworkに送信
"""

import requests
import schedule
import time
import datetime
from typing import Optional

class ChatworkLunchBot:
    def __init__(self, api_token: str, room_id: str):
        """
        Chatworkボットの初期化

        Args:
            api_token: ChatworkのAPIトークン
            room_id: 送信先のルームID
        """
        self.api_token = api_token
        self.room_id = room_id
        self.base_url = "https://api.chatwork.com/v2"
        self.headers = {
            "X-ChatWorkToken": self.api_token,
            "Content-Type": "application/x-www-form-urlencoded"
        }

    def send_message(self, message: str) -> bool:
        """
        Chatworkにメッセージを送信

        Args:
            message: 送信するメッセージ

        Returns:
            送信成功の場合True、失敗の場合False
        """
        url = f"{self.base_url}/rooms/{self.room_id}/messages"
        data = {"body": message}

        try:
            response = requests.post(url, headers=self.headers, data=data)
            response.raise_for_status()
            print(f"[{datetime.datetime.now()}] メッセージ送信成功: {message}")
            return True
        except requests.exceptions.RequestException as e:
            print(f"[{datetime.datetime.now()}] メッセージ送信失敗: {e}")
            return False

    def send_lunch_break_message(self):
        """昼休憩メッセージを送信"""
        message = "お昼休憩に入ります。"
        self.send_message(message)

    def send_afternoon_break_start_message(self):
        """午後の休憩開始メッセージを送信"""
        message = "休憩に入ります。"
        self.send_message(message)

    def send_afternoon_break_end_message(self):
        """午後の休憩終了メッセージを送信"""
        message = "休憩終わります。"
        self.send_message(message)

    def start_scheduler(self):
        """スケジューラーを開始"""
        # 12:03 - 昼休憩開始
        schedule.every().day.at("12:03").do(self.send_lunch_break_message)
        # 14:17 - 午後の休憩開始
        schedule.every().day.at("14:17").do(self.send_afternoon_break_start_message)
        # 14:28 - 午後の休憩終了
        schedule.every().day.at("14:28").do(self.send_afternoon_break_end_message)

        print("Chatwork通知ボットを開始しました")
        print("スケジュール:")
        print("  12:03 - 「お昼休憩に入ります。」")
        print("  14:17 - 「休憩に入ります。」")
        print("  14:28 - 「休憩終わります。」")
        print("停止するには Ctrl+C を押してください")

        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # 1分ごとにチェック
        except KeyboardInterrupt:
            print("\nボットを停止しました")

def main():
    """メイン関数"""
    # 設定値
    API_TOKEN = "def8dbcb03eccca5cd8151ef405ac21f"  # ChatworkのAPIトークン
    ROOM_ID = "309791878"                            # ルームID

    # 設定チェック
    if API_TOKEN == "YOUR_CHATWORK_API_TOKEN" or ROOM_ID == "YOUR_ROOM_ID":
        print("エラー: API_TOKENとROOM_IDを設定してください")
        print("\n設定方法:")
        print("1. ChatworkでAPIトークンを取得")
        print("2. 送信したいルームのIDを取得")
        print("3. このスクリプトの API_TOKEN と ROOM_ID を更新")
        return

    # ボット開始
    bot = ChatworkLunchBot(API_TOKEN, ROOM_ID)
    bot.start_scheduler()

if __name__ == "__main__":
    main()