from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator



def index(request):
    return redirect(reverse('bus_stations'))

def read_csv_files(file):
    all_rows = []
    try:
        with open(file, encoding='utf-8', newline="") as f:
            dict_info = csv.DictReader(f)
            for row in dict_info:
                all_rows.append(row)
        return all_rows
    except FileNotFoundError as error:
        print(f'Файл не найден. Ошибка {error}')
        return []
    except Exception as e:
        print(f'Ошибка {e}')
        return []

def bus_stations(request):
    page = request.path
    page_number = int(request.GET.get('page', 1))

    stations = read_csv_files('data-398-2018-08-30.csv')
    if not stations:
        return render(request, 'stations/index.html', {'bus_stations': [], 'page': page})

    paginator = Paginator(stations, 10)
    page_obj = paginator.get_page(page_number)

    context = {
        'bus_stations': page_obj,
        'page': page,
    }
    return render(request, 'stations/index.html', context)







