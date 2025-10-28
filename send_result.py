import requests

def get_hawks_result():
    # ここでAPIやスクレイピングで試合結果を取得
    return "今日はオリックスとの対戦！2-3でオリックスの勝利。まけほー"

def send_line_message(text):
    url = "https://api.line.me/v2/bot/message/broadcast"
    headers = {
        "Authorization": "Bearer " + "<LINE_TOKEN>",
        "Content-Type": "application/json"
    }
    payload = {
        "messages": [{"type": "text", "text": text}]
    }
    requests.post(url, headers=headers, json=payload)

if __name__ == "__main__":
    result = get_hawks_result()
    send_line_message(result)
