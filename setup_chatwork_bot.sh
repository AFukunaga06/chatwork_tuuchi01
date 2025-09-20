#!/bin/bash
# Chatwork昼休憩ボットのセットアップスクリプト

echo "=== Chatwork昼休憩ボット セットアップ ==="

# 必要なパッケージをインストール
echo "必要なパッケージをインストール中..."
pip3 install requests schedule

# 実行権限を付与
chmod +x chatwork_lunch_bot.py

echo ""
echo "=== セットアップ完了 ==="
echo ""
echo "次の手順で設定してください:"
echo ""
echo "1. ChatworkのAPIトークンを取得:"
echo "   - Chatworkの設定 > API設定 でトークンを生成"
echo ""
echo "2. ルームIDを取得:"
echo "   - 対象のチャットルームのURLから数字の部分を確認"
echo "   - 例: https://www.chatwork.com/#!rid123456 → ルームIDは 123456"
echo ""
echo "3. chatwork_lunch_bot.py を編集:"
echo "   - API_TOKEN = \"あなたのAPIトークン\""
echo "   - ROOM_ID = \"あなたのルームID\""
echo ""
echo "4. ボットを開始:"
echo "   python3 chatwork_lunch_bot.py"
echo ""
echo "5. バックグラウンドで実行する場合:"
echo "   nohup python3 chatwork_lunch_bot.py > chatwork_bot.log 2>&1 &"
echo ""