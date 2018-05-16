#!/usr/bin/env python  
# encoding: utf-8  

""" 
@author: Xiang Xiao
@contact: btxiaox@gmail.com
@site:  
@file: excel_util.py 
@time: 16/5/18 01:22 
"""
import sys
from json import *
reload(sys)
sys.setdefaultencoding('utf-8')

import xlrd

def format_tp(filepath):
    """
    对excel结构进行封装
    :param filepath:
    :return:
    """
    workbook = xlrd.open_workbook(filepath)
    table = workbook.sheet_by_index(0)
    content = []
    indexs = table.row(0)
    cursor = 1
    current_articles_index = 0
    while True:
        if current_articles_index != table.cell(cursor, 0).value:
            #新的一篇article
            articles = []
            content.append(articles)
            current_articles_index = table.cell(cursor, 0).value
        article = {}
        rows = table.row(cursor)
        for i in range(1, table.ncols):
            key = indexs[i].value
            if key == 'article' or 'template':
                article[key] = str(rows[i].value).encode('utf-8').strip().split(',')
            else:
                article[key] = JSONEncoder.encode(str(rows[i].value).encode('utf-8').strip()).split(',')
        articles.append(article)
        if cursor < table.nrows-1:
            cursor = cursor+1
        else:
            break
    return content


if __name__ == '__main__':
    format_tp('tp1.xlsx')


