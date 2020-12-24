from .base_page import BasePage


class MainPage(BasePage):
    # заглушка. Можно просто pass
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)  # super сигнализирует, что мы вызываем
        # и передаем в класс-предок все аргументы, которые были переданы в MainPage
