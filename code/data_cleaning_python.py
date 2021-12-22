import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format
pd.set_option('display.width', 65)
pd.set_option('display.max_columns', 8)

landtemps = pd.read_csv('../data/landtempssample.csv')
