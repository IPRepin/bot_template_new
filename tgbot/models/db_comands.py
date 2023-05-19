from typing import List

from xella_bot.content_manage.models import Stocks, Services
from asgiref.sync import sync_to_async

'''Команды управления акциями'''


@sync_to_async()
def select_all_stocks():
    stocks = Stocks.objects.all()
    return stocks


@sync_to_async()
def select_stock(id: int):
    stock = Stocks.objects.filter(id=id).first()
    return stock


@sync_to_async()
def get_name_stocks() -> List[Stocks]:
    return Stocks.objects.distinct('name')


'''Команды управления услугами'''


@sync_to_async()
def select_all_services():
    services = Services.objects.all()
    return services


@sync_to_async()
def select_service(id: int):
    service = Services.objects.filter(id=id).first()
    return service


@sync_to_async()
def get_name_services() -> List[Services]:
    return Services.objects.distinct('name')
