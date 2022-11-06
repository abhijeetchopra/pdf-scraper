import os
import pdfquery
import pandas as pd

# functions takes file as input and returns row of desired fields
def pdfscrape(pdf):
    # extract each field individually from file; add more fields here as desired
    pay_date = pdf.pq('LTTextLineHorizontal:overlaps_bbox("454.600, 709.937, 499.636, 718.937")').text()
    net_pay  = pdf.pq('LTTextLineHorizontal:overlaps_bbox("500.000, 120.014, 600.000, 130.537")').text()

    # write fields into one dataframe row
    page = pd.DataFrame({
                         'pay_date': pay_date,
                         'net_pay': net_pay,
                       }, index=[0])
    return(page)

# empty dataframe to hold results
master = pd.DataFrame()

# scan directory for files and for each file do the following
with os.scandir('/files') as files:
    for file in files:
        print('Reading file: ',file.name,sep=' ')
        pdf = pdfquery.PDFQuery(file)
        pdf.load()
        page = pdfscrape(pdf)
        master = pd.concat((master, page), axis = 0)

# write results to output file in csv format
master.to_csv('output.csv', index = False)

print('Output file created.')
