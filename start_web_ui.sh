#!/bin/bash
# Web UI起動スクリプト

echo "=== Chatwork通知ボット Web UI ==="
echo ""
echo "Web UIを起動します..."
echo "ブラウザで http://localhost:5000 にアクセスしてください"
echo ""
echo "停止するには Ctrl+C を押してください"
echo ""

cd "$(dirname "$0")"
python3 web_ui.py