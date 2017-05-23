#!/usr/bin/python

#Program file: stephan_s_stock_quote.py
#Author: Stephan Stylianides
#Date: February 26th, 2017
#Assignment: Moderately complex Python assignment
#Objective: This program displays the price of a stock ticker and other relevant data such as market capitalization,
            # P/E, average volume, today's volume, percent change, and earnings per share.
            # This program also creates a CSV file of the stock tickers from the user input

#IMPORTANT: you must install one package before running this script.
            # please install yahoo-finance package
            # You can easily install the package in the terminal.
            # Example: pip install yahoo-finance --user
            # follow the instructions in the terminal to complete
            # I have also provided the package in the zip drive to manually install if you have trouble using the terminal to install with pip
            # Once you have installed the package, type python stock_quote.py followed by the ticker that you want from the command line.
            # you can request multiple symbols
              # Example: python stephan_s_stock_quote.py goog ibm


#use all necessary libraries
from yahoo_finance import Share
import sys
import locale
import csv


def main():
  # this adds commas to all numbers greater than one thousand
	locale.setlocale(locale.LC_ALL, 'en_US')
  # if statement that checks for args. error/help message will appear if no args
	if(len(sys.argv)==1):
		print "\nPlease supply one or more tickers. Example: python stephan_s_stock_quote.py GOOG\n"

	else:
		for counter in range(1,len(sys.argv)):
        # this is where we fetch our stocks from
  			y = Share(sys.argv[counter])
        # this is the output along with a message regarding the CSV file
  			print "\nSymbol: " + str(sys.argv[counter])

  			print "Company Name: " + str(y.get_name())

  			print "Market Capitalization: $" + str(y.get_market_cap())

  			print "Earnings Per Share: $" + str(locale.format("%d", float(y.get_earnings_share()), grouping=True))

  			print "P/E Ratio: " + str(y.get_price_earnings_ratio())

  			print "Average Volume: " + str(locale.format("%d", float(y.get_avg_daily_volume()), grouping=True))

  			print "Today's Volume: " + str(locale.format("%d", float(y.get_volume()), grouping=True))

  			print "Today's Closing Price: $" + str(y.get_price())

  			print "Percent Change: " + str(y.get_percent_change()) + "\n"
  	   
        print "A CSV file of your selected stock tickers has been downloaded to your computer under the name 'stocks.csv'. " + "\n"
       
        print "The CSV file will be downloaded to the same folder that this program was stored in." + "\n"

# code that creates the CSV file
with open('stocks.csv', 'w') as fp:
	outputFile = csv.writer(fp)
	data1 = [['Symbol', 'Company Name', 'Market Capitalization', 'Earnings Per Share', 'P/E Ratio', 'Average Volume', 
	'Today\'s Volume', 'Today\'s Closing Price', 'Percent Change']]
	outputFile.writerows(data1)
	for counter in range(1,len(sys.argv)):
         y = Share(sys.argv[counter])
         
         data2 = [[str(sys.argv[counter]), str(y.get_name()), str(y.get_market_cap()), str(y.get_earnings_share()), 
         str(y.get_price_earnings_ratio()), str(y.get_avg_daily_volume()), str(y.get_volume()), str(y.get_price()), str(y.get_percent_change())]]
		

         
         
         outputFile.writerows(data2)
    		

if __name__ == '__main__':
	main()