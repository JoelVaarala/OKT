import json
import urllib.request
from datetime import datetime

json_url = 'http://open-api.myhelsinki.fi/v1/events/?limit=250'


def get_events():
    with urllib.request.urlopen(json_url) as response:
        return json.loads(response.read())


def partition(event_list, low, high):
    i = (low-1)
    if event_list[high]['event_dates']['starting_day'] is not None:
        pivot = event_list[high]['event_dates']['starting_day']
    else:
        while True:
            x = high-1
            pivot = event_list[x]['event_dates']['starting_day']
            x = x-1
            if pivot is not None:
                break

    for j in range(low, high):

        if event_list[j]['event_dates']['starting_day'] is not None and \
                event_list[j]['event_dates']['starting_day'] <= pivot:

            i = i+1
            event_list[i], event_list[j] = event_list[j], event_list[i]

    event_list[i+1], event_list[high] = event_list[high], event_list[i+1]
    return (i+1)


def quickSort(event_list, low, high):
    if len(event_list) == 1:
        return event_list
    if low < high:

        pi = partition(event_list, low, high)

        quickSort(event_list, low, pi-1)
        quickSort(event_list, pi+1, high)


def main():
    # hakee kamat get_events functiosta
    events = get_events()
    # luodaan lista saadusta 'data' osiosta (= eventit)
    event_list = events['data']
    # n = listan pituus, (tarvitaan parametriksi)
    n = len(event_list)
    # kutsutaan lajittelu algoritmia, parametreina lista ja sen ääripäiden indeksit
    quickSort(event_list, 0, n-1)

    # tulostetaan listan sisältö
    print("\nTapahtumat kronologisessa järjestyksesä: \n")

    # alkuarvo pvm
    current_date = '2000-01-01'

    for i in range(n):

        # skipataan puutteelliset tapahtumat (huomioidaan tässä tapauksessa vain: date -> true && name_fi -> true)
        if event_list[i]['event_dates']['starting_day'] is not None and event_list[i]['name']['fi'] is not None:

            # pomitaan ISO datetime
            isoDate = event_list[i]['event_dates']['starting_day']
            # otetaan talteen pvm
            isoDateOnly = isoDate[0:10]
            # otetaan talteen aika
            isoTimeOnly = isoDate[11:16]
            # otetaan talteen tapahtuman nimi
            name = event_list[i]['name']['fi']

            # tulostetaan pvm vain kerran n määrälle tapahtumia
            if isoDateOnly > current_date:
                print('\n'+isoDateOnly)
                # sijoitetaan uusi indeksi pvm
                current_date = isoDateOnly
            # tulostetan jokaisen tapahtuman aloitus kellonaika ja nimi
            print('\t\t' + isoTimeOnly + '  ' + name),


if __name__ == '__main__':
    main()
