import requests
cont = True

URL = 'https://api.covid19api.com/summary'

covid19 = requests.get(URL)
covid19_global = covid19.json()["Global"]
covid19 = covid19.json()["Countries"]

tytles = ([item for item in list(covid19[0].keys()) if item not in [
          'ID', 'CountryCode', 'Slug', 'Date', 'Premium']])


def output():
    for item in tytles:
        if item == 'Country':
            print("{0:_^35s}".format(item), end='')
        else:
            print("{0:_^20s}".format(item), end='')
    else:
        print(' ')

    for item in covid19:
        for key in item:
            if key in tytles:
                if key == 'Country':
                    print("{0:<31}".format(item[key]), end='')
                else:
                    print("{0:>20}".format(item[key]), end='')
        else:
            print('')


def country_search(Country):
    for item in covid19:
        for key in item:
            if item[key] == Country:
                print(item[key])
                for element in item:
                    print(element, '     ', item[element])


def global_info():
    new_confirmed = 0
    total_confirmed = 0
    new_deaths = 0
    total_deaths = 0
    new_recovered = 0
    total_recovered = 0
    div1 = '                        '
    div2 = '            '
    for item in tytles:
        if item == 'Country':
            print("{0:_^35s}".format(item), end='')
        else:
            print("{0:_^20s}".format(item), end='')
    else:
        print(' ')

    for item in covid19:
        for key in item:
            if key in tytles:
                if key == 'NewConfirmed':
                    new_confirmed += item[key]
                elif key == 'TotalConfirmed':
                    total_confirmed += item[key]
                elif key == 'NewDeaths':
                    new_deaths += item[key]
                elif key == 'TotalDeaths':
                    total_deaths += item[key]
                elif key == 'NewRecovered':
                    new_recovered += item[key]
                elif key == 'TotalRecovered':
                    total_recovered += item[key]
    print("All countries", div1, new_confirmed, div2, total_confirmed, div2,
          new_deaths, div2, total_deaths, div2, new_recovered, div2, total_recovered)


while cont:
    ask = int(input('''
Меню:
1. Показати інформацію по ковід.
2. Відсортувати інформацію по нових підтверджених.
3. Отримати детальну інформацію по назві країни.
4. Показати глобальну інформацію.
0. Вихід.
'''))

    if ask == 1:
        output()

    if ask == 2:
        def byNewConfirmed_key(covid19):
            return covid19["NewConfirmed"]
        covid19 = sorted(covid19, key=byNewConfirmed_key, reverse=True)
        output()

    if ask == 3:
        country = input('Введіть назву країни: ')
        country_search(country)

    if ask == 4:
        global_info()

    if ask == 0:
        cont = False
