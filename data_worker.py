from datetime import datetime
def paymanet_to_number(payment:str):
    number_string = ''.join(filter(lambda x: x.isdigit(), payment))

    number = int(number_string)
    return number


def parse_month(month: str):
    out = ''
    if month == 'января': out = 'jan'
    if month == 'декабря': out = 'dec'
    if month == 'февраля': out = 'feb'
    if month == 'марта': out = 'mar'
    if month == 'апреля': out = 'apr'
    if month == 'мая': out = 'may'
    if month == 'июня': out = 'jun'
    if month == 'июля': out = 'jul'
    if month == 'августа': out = 'aug'
    if month == 'сентября': out = 'sep'
    if month == 'октября': out = 'oct'
    if month == 'ноября': out = 'nov'
    if month == 'декабря': out = 'dec'
    return out
def format_date(date: str):
    print(date)
    if 'до' in date:
        date = date.split('до ')[1]
    if ',' in date:
        date = date.split(',')[0]
    if 'года' in date:
        date = date.split('года')[0]
    date_string = date.strip()

    day, month_name, year = date_string.split()
    month = parse_month(month_name)

    date_format = '%d %b %Y'

    date_formatted = datetime.strptime(f'{day} {month} {year}', date_format).strftime("%d/%m/%Y")
    return date_formatted