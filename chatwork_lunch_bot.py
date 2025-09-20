#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chatwork 昼休憩通知ボット
毎日12:00に「お昼休憩に入ります。」をChatworkに送信
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

    def send_test_message(self):
        """テストメッセージを送信"""
        message = "テストです"
        self.send_message(message)

    def start_scheduler(self):
        """スケジューラーを開始"""
        # 毎日12:03に実行
        schedule.every().day.at("12:03").do(self.send_lunch_break_message)

        print("Chatwork昼休憩ボットを開始しました")
        print("毎日12:03に「お昼休憩に入ります。」を送信します")
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