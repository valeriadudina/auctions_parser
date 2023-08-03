import requests
from bs4 import BeautifulSoup
from lxml import etree
from data_worker import paymanet_to_number, format_date
'''
Дата - date
Участок - place
Регион - region
Статус - status
Срок подачи заявок - deadline
Взнос за участие в аукционе - payment
Организатор - organizator
'''
def parser():
    link = 'https://nedradv.ru/nedradv/ru/auction'
    base_url = 'https://nedradv.ru'
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    all_auktions = soup.find('tbody', class_='g-color-black-opacity-0_6')
    auction_data = []
    for tr in all_auktions.find_all('tr'):

        td = tr.findAll('td')
        date = td[0].find('a').text

        date_formatted = format_date(date)

        place = td[1].find('a').text.replace('\n', '')
        region = td[2].find('a').text.replace('\n', '')
        status = td[3].find('a').text.replace('\n', '')
        link = td[1].find('a').get('href')
        print(base_url+link)
        data = requests.get(base_url+link)
        soup_data = BeautifulSoup(data.text, "html.parser")
        dom = etree.HTML(str(soup_data))
        if 'открыт' in status.lower():
            deadline = dom.xpath('/html/body/main/section[3]/div/div[1]/div[1]/dl[8]/dd')[0].text

            deadline_formatted = format_date(deadline)
            if dom.xpath('/html/body/main/section[3]/div/div[1]/div[1]/dl[4]/dd')!=[] and dom.xpath('/html/body/main/section[3]/div/div[1]/div[1]/dl[4]/dd')[0].text is not None:
                payment = dom.xpath('/html/body/main/section[3]/div/div[1]/div[1]/dl[4]/dd')[0].text
                payment_number = paymanet_to_number(payment)
            else:
                payment_number = 0
            if dom.xpath('/html/body/main/section[3]/div/div[1]/div[1]/dl[6]/dd')!=[] and dom.xpath('/html/body/main/section[3]/div/div[1]/div[1]/dl[6]/dd')[0].text is not None:
                organizator = dom.xpath('/html/body/main/section[3]/div/div[1]/div[1]/dl[6]/dd')[0].text.replace('\n', '')
            else:
                organizator = ""
        else:
            deadline_formatted = ""
            if dom.xpath('/html/body/main/section[3]/div/div[1]/div[1]/dl[4]/dd')!= [] and dom.xpath('/html/body/main/section[3]/div/div[1]/div[1]/dl[4]/dd')[0].text is not None:
                payment = dom.xpath('/html/body/main/section[3]/div/div[1]/div[1]/dl[4]/dd')[0].text
                payment_number = paymanet_to_number(payment)
            else:
                payment_number = 0

            if dom.xpath('/html/body/main/section[3]/div/div[1]/div[1]/dl[6]/dd')!=[] and dom.xpath('/html/body/main/section[3]/div/div[1]/div[1]/dl[6]/dd')[0].text is not None:

                organizator = dom.xpath('/html/body/main/section[3]/div/div[1]/div[1]/dl[6]/dd')[0].text.replace('\n', '')
            else:
                organizator = ""



        auction_data.append((date_formatted, place, status, deadline_formatted, payment_number, organizator))
    return auction_data