import os
import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text")

    if text:
        send_message(chat_id, "GGT-бот на связи 🌳")

    return "ok"

@app.route("/", methods=["GET"])
def index():
    return "Bot is running"
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
