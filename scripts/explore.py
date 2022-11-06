import os
import pdfquery
import pandas as pd

# use below code to do exploration and get coordinates of text boxes

pdf = pdfquery.PDFQuery('/files/adp-pay-stub-template.pdf')
pdf.load()
pdf.tree.write('pdfXML.txt', pretty_print = True)

# replace 'DOLLARS' with keyword or neighboring keyword you'd like to search.
search_keyword = pdf.pq('LTTextLineHorizontal:contains("{}")'.format("DOLLARS"))[0]
x0 = float(search_keyword.get('x0',0))
y0 = float(search_keyword.get('y0',0))
x1 = float(search_keyword.get('x1',0))
y1 = float(search_keyword.get('y1',0))

found_keyword = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' % (x0, y0, x1, y1)).text()
print('Coordinates:')
print(x0,y0,x1,y1,sep=', ')
print('')
print('Keyword:')
print(found_keyword)

# adjust coordinates x0 y0 x1 y1 to find desired keyword and uncomment below lines to print keyword found
# test = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' % (96.023, 123.231, 330.046, 132.231)).text()
# print(test)