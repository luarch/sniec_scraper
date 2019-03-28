import os
import os.path
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup
from icalendar import Calendar, Event


def _getHtmlData(month, page=1, lang_cn=False):
    lang = ''
    if lang_cn:
        lang = 'cn'

    url = "http://www.sniec.net/{}/visit_exhibition.php?month={}&page={}".format(lang, month, page)
    response = requests.get(url)
    return response.text

def getEventData(month, page=1, lang_cn=False):
    soup = BeautifulSoup(_getHtmlData(month, page, lang_cn), features='html.parser')
    upcom_dom = soup.find('ul', {'id': 'upcom'})
    dns = upcom_dom.find_all('div', {'class': 'dn'})
    if not dns:
        return None
    res = []
    for dn in dns:
        title = dn.find('h2')
        dn = dn.find_all('td', {'class': 'padr15'})[1]
        detail = dn.find_all('span', {'class': 'sarial'})
        timeSpan = detail[0].text.split(" - ")
        res.append({
            'title': title.text,
            'startDate': timeSpan[0],
            'endDate': timeSpan[1],
            'location': detail[1].text
        })
    return res

def createCalendar(month, lang_cn=False):
    dateFormat = '%Y/%m/%d'

    lang_spec = 'EN'
    if lang_cn:
        lang_spec = 'CN'

    cal = Calendar()
    cal.add('prodid', '-//Chienius.com//SNIEC Calendar//{}'.format(lang_spec))
    cal.add('version', '2.0')

    page = 1
    while True:
        raw_events = getEventData(month, page, lang_cn)
        page = page+1

        if not raw_events:
            break

        for raw_event in raw_events:
            evt = Event()
            evt.add('summary', raw_event['title'])
            evt.add('dtstart', datetime.strptime(raw_event['startDate'], dateFormat))
            evt.add('dtend', datetime.strptime(raw_event['endDate'], dateFormat) + timedelta(days=1))
            evt.add('location', raw_event['location'])
            cal.add_component(evt)
    return cal

def createIcsFile(filename, month, lang_cn=False):
    cal = createCalendar(month, lang_cn)
    with open(filename, 'wb') as f:
        f.write(cal.to_ical(sorted=True))

if __name__ == "__main__":
    print(getEventData('2019-03', 1))
