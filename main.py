import myfitnesspal
import datetime
import pandas

def get_data(client, start_date, end_date, columns):
    print('Retrieving data...')
    data = []
    dates = []
    current_date = start_date
    while current_date <= end_date:
        
        day = current_date.day
        month = current_date.month
        year = current_date.year
        print(f"{month}/{day}/{year}")

        dates.append(f"{month}/{day}/{year}")
        macros = client.get_date(year,month,day)
        macros = macros.totals
        d = []
        for c in columns:
            d.append(value_or_default(macros,c))
        data.append(d)
        # Advancing current date by one day
        current_date += datetime.timedelta(days=1)

    print(f"Total data = {len(data)}")
    print(f"Total dates = {len(dates)}")
    return data, dates

def value_or_default(map=None, key=None, default_val=""):
    if key in map:
        return map[key]
    return default_val

def handler():
    print("Connecting to MyFitnessPal...")
    # Client(id, pass)
    client = myfitnesspal.Client('', password='')
    print("Connected.")

    start_date = datetime.date(year=2021, month=9, day=1)
    end_date   = datetime.date(year=2022, month=1, day=3)

    data = []
    index = []
    columns = ['calories', 'carbohydrates', 'fat', 'protein', 'sodium', 'sugar']

    data, dates = get_data(client, start_date, end_date, columns)
    df = pandas.DataFrame(data, index=dates, columns=columns)
    df.to_csv('output.csv')

handler()




