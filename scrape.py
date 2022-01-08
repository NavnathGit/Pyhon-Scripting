import requests
from bs4 import BeautifulSoup
import pprint  # python inbult library to print in nice way

# request module allows to download the webssite date
# bs4- scrape data

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup.body.contents)
# print(soup.find_all('div')) # returns all div tags
# print(soup.find_all('div'))  # returns all a tags
# print(soup.select('.score'))  # css selector - learn more

links = soup.select('.titlelink')
subtext = soup.select('.subtext')

links2 = soup2.select('.titlelink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
