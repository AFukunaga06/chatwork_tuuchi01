#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chatwork通知ボット制御スクリプト
ボットの開始・停止・状態確認を行う
"""

import subprocess
import sys
import os
import signal
import time

class ChatworkBotController:
    def __init__(self):
        self.bot_script = "chatwork_lunch_bot.py"
        self.pid_file = "/tmp/chatwork_bot.pid"

    def start_bot(self):
        """ボットを開始"""
        if self.is_running():
            print("ボットは既に実行中です")
            return False

        try:
            # バックグラウンドでボットを起動
            process = subprocess.Popen(
                [sys.executable, self.bot_script],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                preexec_fn=os.setsid
            )

            # PIDを保存
            with open(self.pid_file, 'w') as f:
                f.write(str(process.pid))

            print("Chatwork通知ボットを開始しました")
            print("スケジュール:")
            print("  12:03 - 「お昼休憩に入ります。」")
            print("  14:17 - 「休憩に入ります。」")
            print("  14:28 - 「休憩終わります。」")
            return True

        except Exception as e:
            print(f"ボットの開始に失敗しました: {e}")
            return False

    def stop_bot(self):
        """ボットを停止"""
        if not self.is_running():
            print("ボットは実行されていません")
            return False

        try:
            with open(self.pid_file, 'r') as f:
                pid = int(f.read().strip())

            # プロセスグループを終了
            os.killpg(os.getpgid(pid), signal.SIGTERM)

            # PIDファイルを削除
            os.remove(self.pid_file)

            print("Chatwork通知ボットを停止しました")
            return True

        except (FileNotFoundError, ProcessLookupError):
            # PIDファイルが存在しないか、プロセスが既に終了している
            if os.path.exists(self.pid_file):
                os.remove(self.pid_file)
            print("ボットは既に停止しています")
            return False
        except Exception as e:
            print(f"ボットの停止に失敗しました: {e}")
            return False

    def is_running(self):
        """ボットが実行中かチェック"""
        if not os.path.exists(self.pid_file):
            return False

        try:
            with open(self.pid_file, 'r') as f:
                pid = int(f.read().strip())

            # プロセスが存在するかチェック
            os.kill(pid, 0)
            return True

        except (FileNotFoundError, ProcessLookupError, ValueError):
            # PIDファイルが存在しないか、プロセスが存在しない
            if os.path.exists(self.pid_file):
                os.remove(self.pid_file)
            return False

    def status(self):
        """ボットの状態を表示"""
        if self.is_running():
            print("ボット状態: 実行中")
            print("スケジュール:")
            print("  12:03 - 「お昼休憩に入ります。」")
            print("  14:17 - 「休憩に入ります。」")
            print("  14:28 - 「休憩終わります。」")
        else:
            print("ボット状態: 停止中")

def main():
    """メイン関数"""
    controller = ChatworkBotController()

    if len(sys.argv) < 2:
        print("使用方法:")
        print("  python3 chatwork_control.py start   # ボット開始")
        print("  python3 chatwork_control.py stop    # ボット停止")
        print("  python3 chatwork_control.py status  # 状態確認")
        print("  python3 chatwork_control.py restart # ボット再起動")
        return

    command = sys.argv[1].lower()

    if command == "start":
        controller.start_bot()
    elif command == "stop":
        controller.stop_bot()
    elif command == "status":
        controller.status()
    elif command == "restart":
        print("ボットを再起動します...")
        controller.stop_bot()
        time.sleep(2)
        controller.start_bot()
    else:
        print(f"不明なコマンド: {command}")
        print("使用可能なコマンド: start, stop, status, restart")

if __name__ == "__main__":
    main()