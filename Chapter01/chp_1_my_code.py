import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.width', 65)
pd.set_option('display.max_columns', 8)

landtemps = pd.read_csv('data/landtempssample.csv',
                        names=['stationid', 'year', 'month',
                               'avgtemp', 'latitude', 'longitude',
                               'elevation', 'station', 'countryid',
                               'country'],
                        skiprows=1,
                        parse_dates=[['month', 'year']],
                        low_memory=False)

landtemps.rename(columns={'month_year': 'measuredate'}, inplace=True)

landtemps.dropna(subset=['avgtemp'], inplace=True)
landtemps.shape
