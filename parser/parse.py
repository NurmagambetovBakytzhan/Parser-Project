import requests
from . import models
from datetime import datetime
from bs4 import BeautifulSoup


def parse_news() -> list[models.Item]:
    resources = models.Resource.objects.all()
    for r in resources:
        response = requests.get(r.resource_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        links = soup.select(r.top_tag)
        titles = [title.get_text().strip().replace('\n', '').replace('"', '') for title in soup.select(r.title_cut)]
        dates = [date['datetime'][:10] for date in soup.select(r.date_cut)]
        news_list = []
        for i in range(len(links)):
            news_url = links[i]['href']

            news_response = requests.get(news_url)
            news_soup = BeautifulSoup(news_response.content, 'html.parser')
            news_title = titles[i]
            news_content = [paragraph.get_text(strip=True) for paragraph in news_soup.select(r.bottom_tag)]
            news_content = ''.join(news_content)

            news_date = datetime.strptime(dates[i], '%Y-%m-%d')
            new_item = models.Item(
                link=news_url,
                title=news_title,
                content=news_content,
                nd_date=news_date,
                not_date=news_date.date(),
                resource=r
            )
            old_item = models.Item.objects.filter(link=new_item.link).first()
            if old_item is None:
                new_item.save()
            else:
                new_item.id = old_item.id
                new_item.s_date = old_item.s_date
            news_list.append(new_item)

        return news_list