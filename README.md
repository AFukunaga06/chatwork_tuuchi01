# Chatwork休憩通知ボット

Chatworkに休憩開始・終了メッセージを自動送信するボットです。

## 機能

- **12:03** - 「お昼休憩に入ります。」
- **14:17** - 「休憩に入ります。」
- **14:28** - 「休憩終わります。」

## セットアップ

1. 必要なパッケージをインストール:
```bash
pip3 install requests schedule
```

2. Chatworkの設定:
   - APIトークンを取得
   - 送信先ルームIDを確認
   - `chatwork_lunch_bot.py` の設定値を更新

## 使用方法

### Web UI（推奨）

1. Web UIを起動:
```bash
./start_web_ui.sh
# または
python3 web_ui.py
```

2. ブラウザで `http://localhost:5000` にアクセス

3. ボタンをクリックしてボットを制御:
   - **開始** - ボットを開始
   - **停止** - ボットを停止
   - **再起動** - ボットを再起動

### コマンドライン

```bash
# ボット開始
python3 chatwork_control.py start

# ボット停止
python3 chatwork_control.py stop

# 状態確認
python3 chatwork_control.py status

# ボット再起動
python3 chatwork_control.py restart
```

### 直接実行

```bash
# フォアグラウンドで実行（デバッグ用）
python3 chatwork_lunch_bot.py
```

## ファイル構成

- `chatwork_lunch_bot.py` - メインボットスクリプト
- `chatwork_control.py` - ボット制御スクリプト
- `web_ui.py` - Web UIサーバー
- `start_web_ui.sh` - Web UI起動スクリプト
- `templates/index.html` - Web UIテンプレート
- `setup_chatwork_bot.sh` - 初期セットアップスクリプト
- `README.md` - このファイル

## 設定

`chatwork_lunch_bot.py` の以下の値を環境に合わせて変更してください:

```python
API_TOKEN = "your_api_token_here"
ROOM_ID = "your_room_id_here"
```

## 注意事項

- ボットは1分間隔でスケジュールをチェックします
- エラーが発生した場合はログが出力されます
- ボットプロセスはバックグラウンドで実行されます