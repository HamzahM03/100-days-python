from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

# Get all story links
story_links = soup.find_all(name="a", class_="storylink")

# Get all score elements (upvotes)
score_spans = soup.find_all(name="span", class_="score")

list_of_scores = [int(score_spans[i].getText().split()[0]) for i in range(len(score_spans))]


stories = []

for i in range(len(story_links)):
    title = story_links[i].getText()
    link = story_links[i].get("href")

    # Not all stories have upvotes (e.g., ads or job posts)
    try:
        upvote = score_spans[i].getText()
    except IndexError:
        upvote = "0 points"

    stories.append(f"Title: {title}, Link: {link}, Upvotes: {upvote}")

# Print them all
for story in stories:
    print(story)

highest_upvote_index = list_of_scores.index(max(list_of_scores))
print(f"\n\nHighest Upvoted Story\nTitle: {story_links[highest_upvote_index].getText()}, Link: {story_links[highest_upvote_index].get('href')}, votes: {max(list_of_scores)}")



#---------------------------------- BASIC SOUP TUTORIAL BELOW AKA WEBSCRAPING USING BeautifulSoup CLASS-----------------------------
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a) Finds first anchor tag in our website.
# #soup.element, finds first element tag in our website
# #but to find all the specific element tag, such as all paragraph tags, or all anchor tags do
# #the following.
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href")) #Grabs the value of the attribute you pass in
#
# heading = soup.find(name="h1", id="name") #Another way to grab a specific element. Find returns the first match
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)




