import requests
from bs4 import BeautifulSoup

respons = requests.get("https://www.ceneo.pl/71299208#tab=reviews")

page_dom = BeautifulSoup(respons.text, 'html.parser')

#print(page_dom.prettify())

reviews = page_dom.select("div.js_product-review")
print(type(reviews))
review = reviews.pop(0)
print(type(review))

review_id = review["data-entry-id"]
author = review.select_one("span.user-post__author-name").text.strip()
recommendation = review.select_one("span.user-post__author-recomendation").text.strip()
stars = review.select_one("span.user-post__score-count").text.strip()
content = review.select_one("div.user-post__text").text.strip()
pros = review.select("div.review-feature__title--positives ~ div.review-feature__item")
cons = review.select("div.review-feature__title--negatives ~ div.review-feature__item")
useful = review.select_one("button.vote-yes").text.strip()
useless = review.select_one("button.vote-no").text.strip()
review_date = review.select_one("span.user-post__published > time:nth-child(1)["datetime"]).strip()
purchase_date = review.select_one("span.user-post__published > time:nth-child(2)["datetime"]).strip()

print(review_id, author, recommendation, stars, content, pros, cons, useful, useless, purchase_date, review_date)