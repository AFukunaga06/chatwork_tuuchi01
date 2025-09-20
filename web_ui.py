#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chatwork通知ボット Web UI
ブラウザから簡単にボットを制御できるWebインターフェース
"""

from flask import Flask, render_template, jsonify, request
import subprocess
import sys
import os
import json
from datetime import datetime

app = Flask(__name__)

class ChatworkBotWebController:
    def __init__(self):
        self.bot_script = "chatwork_lunch_bot.py"
        self.control_script = "chatwork_control.py"

    def execute_command(self, command):
        """制御コマンドを実行"""
        try:
            result = subprocess.run(
                [sys.executable, self.control_script, command],
                capture_output=True,
                text=True,
                cwd=os.path.dirname(os.path.abspath(__file__))
            )
            return {
                "success": result.returncode == 0,
                "output": result.stdout.strip(),
                "error": result.stderr.strip() if result.stderr else None
            }
        except Exception as e:
            return {
                "success": False,
                "output": "",
                "error": str(e)
            }

    def get_status(self):
        """ボットの状態を取得"""
        result = self.execute_command("status")
        is_running = "実行中" in result["output"]
        return {
            "running": is_running,
            "status_text": result["output"],
            "last_check": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

controller = ChatworkBotWebController()

@app.route('/')
def index():
    """メインページ"""
    return render_template('index.html')

@app.route('/api/status')
def api_status():
    """ボット状態API"""
    return jsonify(controller.get_status())

@app.route('/api/control', methods=['POST'])
def api_control():
    """ボット制御API"""
    data = request.get_json()
    command = data.get('command')

    if command not in ['start', 'stop', 'restart']:
        return jsonify({
            "success": False,
            "message": "無効なコマンドです"
        }), 400

    result = controller.execute_command(command)
    return jsonify({
        "success": result["success"],
        "message": result["output"] if result["success"] else result["error"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)