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
reload(sys)
sys.setdefaultencoding('utf-8')
import excel_util
import pycurl
import codecs
from jinja2 import Template
from json import *
from StringIO import StringIO



# 微信公众号access_token
__access_token = u'9_XYKcHiKl_6fugF4KorgIy7eD1ySvo0g_e1zGlTXjscPeu3k7-3ZjpglHPo28I12jqFveCOsJbOtaijZvVe0mACOHyE0Sinc3zBDqgPvXtmyBjvroc0Z2DaAqWhhKdGFWfJpi6Aa1emb5Be30PNOdACADBC'

def _post_data(url,data):
    #
    # 基础POST方法，给微信接口发请求
    #
    url = url+__access_token
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    post_data = data
    c.setopt(c.CUSTOMREQUEST, "POST")
    c.setopt(c.HTTPHEADER, ['Content-Type: application/json,charset=utf-8'])
    c.setopt(c.POSTFIELDS, post_data)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue()
    return body


def _get_meida(media_id):
    url = u'https://api.weixin.qq.com/cgi-bin/material/get_material?access_token='
    post_data = '{"media_id":"'+media_id+'"}'
    return _post_data(url, post_data)


def add_media(media):
    url = u'https://api.weixin.qq.com/cgi-bin/material/add_news?access_token='
    res = _post_data(url, media.strip())
    try:
        media_id = json.loads(res)[u'media_id']
        result = media_id
    except StandardError, e:
        errcode = json.loads(res)[u'errcode']
        result = errcode
    return result


def _get_temp(temp):
    f = codecs.open(str(temp)+'.jinjia', 'r', 'utf8')
    fstring = f.read()
    return Template(fstring)

def assemble_article(articles):
    r = "{\"articles\": ["
    end = "]}"
    for article in articles:
        template = _get_temp(article['template'][0])
        mediastr = template.render(content=article)
        r = r + mediastr
    r = r.strip(',')+end
    return r


def get_img_media_id(img):
#
# 获取图片地址，type=1 为链接，type=2为文件路径
    pass





if __name__ == '__main__':
    print _get_meida("xPxyLKFXP3ppHr6qnyMCuTfUqf4JEW7I1JDBbYDYonI")

    contents = excel_util.format_tp('config.xlsx')
    for content in contents:
        post_data = assemble_article(content)
        add_media(post_data)


