#!/usr/bin/env python
# encoding: utf-8

import pycurl
import codecs
from jinja2 import Template

import json
#from urllib import urlencode
from StringIO import StringIO



# 微信公众号access_token
__access_token = u'abc'

def _post_data(url,data):
    #
    # 基础方法，给微信接口发请求
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
    url = 'https://api.weixin.qq.com/cgi-bin/material/get_material?access_token='+__access_token
    post_data = '{"media_id":"'+media_id+'"}'
    return _post_data(url, post_data)


def add_media(media):
    url = 'https://api.weixin.qq.com/cgi-bin/material/add_news?access_token='
    res = _post_data(url, media.encode('utf-8').strip())
    try:
        media_id = json.loads(res)[u'media_id']
        result = media_id
    except StandardError, e:
        errcode = json.loads(res)[u'errcode']
        result = errcode
    return result


def get_temp(temp_id):
    f = codecs.open('template_'+str(temp_id)+'.jinjia','r','utf8')
    fstring = f.read()
    return Template(fstring)

def assemble_article(template,content):
    media = template.render(content=content)
    return media


def get_img_media_id(img):
#
# 获取图片地址，type=1 为链接，type=2为文件路径
    pass





if __name__ == '__main__':
    #print get_meida("rBbdElSo6RPHf5UG-WXGoAJNxjDSzL0yil_LtwWA4KI")
    #rBbdElSo6RPHf5UG-WXGoIwuWxaBvtG_hZ1MOGbXFu4
    print _get_meida('rBbdElSo6RPHf5UG-WXGoIwuWxaBvtG_hZ1MOGbXFu4')
    #content = {'title': 'abc', 'thumb_media_id': 'rBbdElSo6RPHf5UG-WXGoIwuWxaBvtG_hZ1MOGbXFu4', 'author': '','digest': 'cde','link_url':'www.baidu.com'}
    #add_media(assemble_article(get_temp(1),content))

