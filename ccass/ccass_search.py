#!/usr/bin/env python3

import sys
import re
import requests
import urllib.parse
import json
import pandas as pd
import argparse
import textwrap
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def validate_arg_code(code):
    if code.isdigit() and len(code) <= 5:
        return code
    else:
        print('Invalid Stock Code')
        raise ValueError('Invalid Stock Code')

def validate_arg_start(start):
    pattern_str = r'^\d{4}/\d{2}/\d{2}$'
    try:
        if re.match(pattern_str, start) and bool(datetime.strptime(start, '%Y/%m/%d')):
            return start
        else:
            raise ValueError('Invalid Shareholding Start Date')
    except ValueError:
        print('Invalid Shareholding Start Date')
        raise

def validate_arg_end(end):
    pattern_str = r'^\d{4}/\d{2}/\d{2}$'
    try:
        if re.match(pattern_str, end) and bool(datetime.strptime(end, '%Y/%m/%d')):
            return end
        else:
            raise ValueError('Invalid Shareholding End Date')
    except ValueError:
        print('Invalid Shareholding End Date')
        raise

def searchsdw(today, txtShareholdingDate, txtstockCode, lang):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 'Content-Type': 'application/x-www-form-urlencoded'}
        if lang == 'c':
            url_address = 'https://www3.hkexnews.hk/sdw/search/searchsdw_c.aspx'
        else:
            url_address = 'https://www3.hkexnews.hk/sdw/search/searchsdw.aspx'
        data = '__EVENTTARGET=btnSearch&__EVENTARGUMENT=&today=' + today + '&sortBy=shareholding&sortDirection=desc&alertMsg=&txtShareholdingDate=' + txtShareholdingDate + '&txtStockCode=' + txtStockCode + '&txtStockName=&txtParticipantID=&txtParticipantName=&txtSelPartID='
        url = requests.request('POST',url_address, data=data, headers=headers)
        source = BeautifulSoup(url.text, 'html.parser')
        res = source.find_all('tbody')
        data = []
        for row in res[0]("tr"):
            items = {}
            items["id"] = row.find('td',attrs={'class','col-participant-id'}).find('div',attrs={'class','mobile-list-body'}).text.strip()
            items["name"] = row.find('td',attrs={'class','col-participant-name'}).find('div',attrs={'class','mobile-list-body'}).text.strip()
            items["shareholding"] = row.find('td',attrs={'class','col-shareholding'}).find('div',attrs={'class','mobile-list-body'}).text.strip()
            items["shareholding-percent"] = row.find('td',attrs={'class','col-shareholding-percent'}).find('div',attrs={'class','mobile-list-body'}).text.strip()
            items["matched"] = 'N'
            data.append(items)
        return data
    except:
        print("HKEX server issue. Please try again later")
        raise

if __name__ == "__main__":

    try:
        # Prepare the args
        parser=argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=textwrap.dedent('''\
                You can search for CCASS shareholding information in the past 12 months.

                Please provide following informaiton:
                -------------------------------------------------
                -c CODE               Stock Code (example: 1)
                -s START              Shareholding Start Date (example: 2024/12/30)
                -e END                Shareholding End Date (example: 2024/12/31)
                --lang                Display Language (default: c)
                                      Options:
                                        e: English
                                        c: Chinese
                --sort                Sort by value (default: change)
                                      Options:
                                        id: Participant Id
                                        name: Participant Name
                                        start: Shareholding Start
                                        end: Shareholding End
                                        change: Shareholding Change
                                        change-percent: Shareholding Change Percent
                '''),
            epilog="And that's how you'd foo a bar"
        )
        parser.add_argument('-c', dest='code', required=True, type=validate_arg_code)
        parser.add_argument('-s', dest='start', required=True, type=validate_arg_start)
        parser.add_argument('-e', dest='end', required=True, type=validate_arg_end)
        parser.add_argument('--lang', dest='lang', choices=['e','c'], default='c',)
        parser.add_argument('--sort', dest='sort', choices=['id','name','start','end','change','change-percent'], default='change')
        args=parser.parse_args()

        txtStockCode = "{:05d}".format(int(args.code))
        txtShareholdingDateStart = urllib.parse.quote(args.start, safe='')
        txtShareholdingDateEnd = urllib.parse.quote(args.end, safe='')
        today = format(datetime.utcnow() + timedelta(hours=8), '%Y%m%d')

        # Call HTTP request to get data from HKEX
        json_start = searchsdw(today, txtShareholdingDateStart, txtStockCode, args.lang)
        json_end = searchsdw(today, txtShareholdingDateEnd, txtStockCode, args.lang)
        
        # Megre JSONs
        data = []
        table = []
        index = []
        for entry_json_start in json_start:
            for entry_json_end in json_end:
                if entry_json_start["id"] == entry_json_end["id"] and entry_json_start["name"] == entry_json_end["name"]:
                    entry_json_start["matched"] = 'Y'
                    entry_json_end["matched"] = 'Y'
                    shareholding_start = int(entry_json_start["shareholding"].replace(',',''))
                    shareholding_end = int(entry_json_end["shareholding"].replace(',',''))
                    shareholding_change = shareholding_end - shareholding_start
                    shareholding_change_percent = shareholding_change / shareholding_start * 100
                    items = {}
                    items["id"] = entry_json_start["id"] 
                    items["name"] = entry_json_start["name"]
                    items["start"] = shareholding_start
                    items["start-display"] = entry_json_start["shareholding"] + ' (' + entry_json_start["shareholding-percent"] + ')'
                    items["end"] = shareholding_end
                    items["end-display"] = entry_json_end["shareholding"] + ' (' + entry_json_end["shareholding-percent"] + ')'
                    items["change"] = shareholding_change
                    items["change-percent"] = shareholding_change_percent
                    items["change-display"] = f"{shareholding_change:,}" + ' (' + f'{round(shareholding_change_percent,2):.2f}' + '%)'
                    data.append(items)
        for entry_json_start in json_start:
            if entry_json_start["matched"] == 'N':
                shareholding_start = int(entry_json_start["shareholding"].replace(',',''))
                shareholding_end = 0
                shareholding_change = shareholding_end - shareholding_start
                shareholding_change_percent = -100
                items = {}
                items["id"] = entry_json_start["id"] 
                items["name"] = entry_json_start["name"]
                items["start"] = shareholding_start
                items["start-display"] = entry_json_start["shareholding"] + ' (' + entry_json_start["shareholding-percent"] + ')'
                items["end"] = shareholding_end
                items["end-display"] = '0 (0.00%)'
                items["change"] = shareholding_change
                items["change-percent"] = shareholding_change_percent
                items["change-display"] = f"{shareholding_change:,}" + ' (-100.00%)'
                data.append(items)
        for entry_json_end in json_end:
            if entry_json_end["matched"] == 'N':
                shareholding_start = 0
                shareholding_end = int(entry_json_end["shareholding"].replace(',',''))
                shareholding_change = shareholding_end - shareholding_start
                shareholding_change_percent = 100
                items = {}
                items["id"] = entry_json_end["id"] 
                items["name"] = entry_json_end["name"] 
                items["start"] = shareholding_start
                items["start-display"] = '0 (0.00%)'
                items["end"] = shareholding_end
                items["end-display"] = entry_json_end["shareholding"] + ' (' + entry_json_end["shareholding-percent"] + ')'
                items["change"] = shareholding_change
                items["change-percent"] = shareholding_change_percent
                items["change-display"] = f"{shareholding_change:,}" + ' (100.00%)'
                data.append(items)

        # Sort result JSON
        data.sort(key=lambda k: k[args.sort], reverse=True)

        # Prepare display table
        for json_data_sort_item in data:
            table.append([json_data_sort_item["start-display"],json_data_sort_item["end-display"],json_data_sort_item["change-display"]])
            index.append(json_data_sort_item["id"] + ' - ' + json_data_sort_item["name"] if len(json_data_sort_item["id"]) > 0 else json_data_sort_item["name"])

        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 2000)
        pd.set_option('display.max_colwidth', None)
        pd.set_option("display.unicode.east_asian_width", True)
        
        if args.lang == 'c' :
            df = pd.DataFrame(table, columns = [args.start, args.end, '持股量 (%)'], index=index)
        else:
            df = pd.DataFrame(table, columns = [args.start, args.end, 'Shareholding (%)'], index=index)
        
        print(df)

        pd.reset_option('display.max_rows')
        pd.reset_option('display.max_columns')
        pd.reset_option('display.width')
        pd.reset_option('display.max_colwidth')

    except Exception as error:

        print("An exception occurred:", error)