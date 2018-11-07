#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 10:57:40 2018

@author: u6527752
"""

books_numbers = input('Enter the number of books: ')
books_numbers_int = int(books_numbers)
if books_numbers_int <= 0 :
    print ("wrong number")
elif books_numbers_int == 1:
    books_price_total = 24.95*0.4
    shipping_price = 3
else:
    books_price_total = books_numbers_int * 24.95 * 0.4
    shipping_price = 3+(books_numbers_int-1)*0.75

total_price = books_price_total + shipping_price
print (total_price)