import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def plot_stock_prices(stock_data):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Amazon Stock Price', color='blue')
    plt.title('Amazon Stock Prices - Last 3 Months')
    plt.xlabel('Date')
    plt.ylabel('Stock Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
   
    ticker = 'AMZN'
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')

  
    stock_data = get_stock_data(ticker, start_date, end_date)

    
    plot_stock_prices(stock_data)

if __name__ == "__main__":
    main()
