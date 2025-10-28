import os
import requests
from bs4 import BeautifulSoup

def get_hawks_result():
    url = "https://baseball.yahoo.co.jp/npb/teams/30/schedule"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    # 最新の試合（直近の試合行を取得）
    latest_game = soup.select_one("tr.bb-score__row")
    if not latest_game:
        return "試合情報が取得できませんでした"

    opponent = latest_game.select_one(".bb-score__team--away").get_text(strip=True)
    score = latest_game.select_one(".bb-score__score").get_text(strip=True)

    try:
        hawks_score, opp_score = map(int, score.split("-"))
    except:
        return "スコアの取得に失敗しました"

    if hawks_score > opp_score:
        result = "たかほー！"
    elif hawks_score < opp_score:
        result = "まけほー"
    else:
        result = "引き分けでした"

    return f"今日は{opponent}との対戦！{score}でホークスの{result}"

def send_line_message(text):
    url = "https://api.line.me/v2/bot/message/broadcast"
    headers = {
        "Authorization": "Bearer " + os.environ["LINE_TOKEN"],  # Secretsから読み込み
        "Content-Type": "application/json"
    }
    payload = {
        "messages": [{"type": "text", "text": text}]
    }
    requests.post(url, headers=headers, json=payload)

if __name__ == "__main__":
    result = get_hawks_result()
    send_line_message(result)
