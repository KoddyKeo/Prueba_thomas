import datetime

from networkdays import networkdays
# Para esta libreria instale Networkdays ya que facilita tener todas las fechas en una lista sin la necesidad de hacer ciclos para determinar las fechas en un rango y luego separarla por dias
# Comando de instalacion  <pip install python-networkdays>

from dateutil import tz


def date_format(date):
    return datetime.datetime.strptime(date, '%d/%m/%Y %H:%M:%S %z')


class Dates:
    def __init__(self, date_a, date_b):
        self.date_a = date_a
        self.date_b = date_b

    def process_date(self):

        try:
            print(f"\nFecha A: {self.date_a} \nFecha B: {self.date_b}")

            print('\nDiferencia de fechas')
            diff_date = self.diff_date(self.date_a, self.date_b)

            print('\nNúmero de días')
            count_days = self.frequency_days(self.date_a, self.date_b)

            print('\nHoras laborales')
            labor_hours = self.hours(self.date_a, self.date_b)

            date_a = self.date_a.replace(tzinfo=tz.tzlocal())
            date_b = self.date_b.replace(tzinfo=tz.tzlocal())

            print('\nDiferencia de fecha con zona horaria local')
            tz_local = self.diff_date(date_a, date_b)

        except:
            print("Error")

    def frequency_days(self, date_a, date_b):
        days = networkdays.Networkdays(datetime.date(date_a.year, date_a.month, date_a.day),
                                       datetime.date(date_b.year, date_b.month, date_b.day), holidays={}, weekdaysoff={
            })
        list_days = days.networkdays()
        total_days = [day.strftime("%A") for day in list_days]

        monday = total_days.count('Monday')
        tuesday = total_days.count('Tuesday')
        wednesday = total_days.count('Wednesday')
        thursday = total_days.count('Thursday')
        friday = total_days.count('Friday')
        saturday = total_days.count('Saturday')
        sunday = total_days.count('Sunday')

        print(
            f"\nLunes: {monday} \nMartes: {tuesday}\nMiercoles: {wednesday}\nJueves: {thursday}\nViernes: {friday}\nSabado: {saturday} \nDomingo: {sunday}")

    def hours(self, date_a, date_b):
        days = networkdays.Networkdays(datetime.date(date_a.year, date_a.month, date_a.day),
                                       datetime.date(date_b.year, date_b.month, date_b.day), holidays={},
                                       weekdaysoff={6, 7})
        list_days = days.networkdays()
        hours = len(list_days * 8)
        print(f"Horas: {hours}")

    def diff_date(self, date_a, date_b):

        diff_date = date_b - date_a
        days = diff_date.days
        seconds = diff_date.total_seconds()
        minutes = seconds / 60
        hours = minutes / 60

        print(f"\nSegundos: {seconds} \nMinutos: {minutes} \nHoras: {hours} \nDías: {days}")


def main():
    try:
        date_a = date_format(input("Fecha A Formato DD/MM/YYYY hh:mm:ss +xxxx: "))
        date_b = date_format(input("Fecha B Formato DD/MM/YYYY hh:mm:ss +xxxx: "))
        sort_words = Dates(date_a, date_b)
        sort_words.process_date()
    except:
        print('Error en formato de fechas')


if __name__ == '__main__':
    main()
