print("hello world")
'''
Main.py:
Will ask user for portfolio info:
    either inputting manually, or
    through a .csv file (check that merrill can do this) 

    User should provide list of tickers held, and since when

    if .csv file, read data on a separate read_data file/

    Then with that data call on compute ticker asset info on separate file for each ticker

    then finally produce summary of data (format_data.py)

    and plot data (plot.py)

'''



def retrieve_tickers():
    tickers_str = input("Please enter a comma separated list of tickers: \n").replace(' ', '')
    print(tickers_str)
    print(tickers_str.split(','))

if __name__ =='__main__' :
    retrieve_tickers()  