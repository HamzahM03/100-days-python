from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # load variables from .env

#Blog Post to help create a telegram bot to start sending messages -> https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e
BOT_TOKEN = os.getenv("API_KEY")
BOT_CHATID = os.getenv("CHAT_ID")


def telegram_bot_sendtext(bot_message):
    send_text = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    params = {
        'chat_id': BOT_CHATID,
        'parse_mode': 'Markdown',
        'text': bot_message
    }
    response = requests.get(send_text, params=params)
    return response.json()



# Live Hacker News site
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# Get all story title blocks
articles = soup.find_all(name="span", class_="titleline")

# Get all subtext blocks (contains upvotes and other metadata)
subtexts = soup.find_all(class_="subtext")

article_texts = []
article_links = []
article_upvotes = []

for i in range(len(articles)):
    # Get title and link
    title_tag = articles[i].find("a")
    title = title_tag.getText()
    link = title_tag.get("href")

    article_texts.append(title)
    article_links.append(link)

    # Get upvote count (if available)
    subtext = subtexts[i]
    score_span = subtext.find("span", class_="score")

    if score_span:
        upvotes = int(score_span.getText().split()[0])
    else:
        upvotes = 0  # No upvotes yet

    article_upvotes.append(upvotes)

# Find the article with the highest upvotes
max_upvotes = max(article_upvotes)
top_index = article_upvotes.index(max_upvotes)

# Print all articles
for i in range(len(article_texts)):
    print(f"Title: {article_texts[i]}, Link: {article_links[i]}, Upvotes: {article_upvotes[i]} points")

# Print the top story
print("\n\n🔝 Highest Upvoted Article Of The Day:")
print(f"Title: {article_texts[top_index]}")
print(f"Upvotes: {article_upvotes[top_index]} points")
print(f"Link: {article_links[top_index]}")

#Message to send using telegram bot
message = f"""
🔝 *Top Hacker News Story Today*:

*{article_texts[top_index]}*
👍 {article_upvotes[top_index]} points
🔗 [Read it here]({article_links[top_index]})
"""
telegram_bot_sendtext(message)
