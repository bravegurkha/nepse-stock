#!/usr/bin/env python 

"""
Copyright (C) 2016  Puskar Adhikari

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

from bs4 import BeautifulSoup
import requests

print "Enter the stock Symbol: ",
symbol = raw_input()
url = "http://www.nepalstock.com/company/"
req = requests.post(url, data={"stock_symbol":symbol}, verify=False)
response = req.text
soup = BeautifulSoup(response, "lxml")
table = soup.find("table")
print "\n"
print "\n"
print "Company: ",table.findAll("td")[0].string
for row in table.findAll("tr")[4:]:
    col = row.findAll("td")
    print col[0].string,": ",col[1].string
print "\n"
print "\n"
