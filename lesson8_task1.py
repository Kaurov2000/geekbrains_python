class Date:
    @classmethod
    def date_to_int(cls, ds):
        date_list = [int(el) for el in ds.split('-')]
        Date.check_date(date_list)
        return date_list
    @staticmethod
    def check_date(dl):
        if dl[0] < 1 or dl[0] > 31:
            print("День введен неверно")
            raise ValueError
        elif dl[1] < 1 or dl[1] > 12:
            print("Месяц введен неверно")
            raise ValueError
        elif dl[2] < 1:
            print("Год введен неверно")
            raise ValueError

print(Date.date_to_int('20-11-2019'))
try:
    print(Date.date_to_int('32-11-2019'))
except ValueError:
    pass