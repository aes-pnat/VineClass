import pandas as pd
import dataset.DatasetGenerator as DG

def service_func():
    DG.generate()

if __name__ == '__main__':
    service_func()
    pd.options.display.max_rows = 9999
    df = pd.read_csv('in_out.csv')

    print(df)