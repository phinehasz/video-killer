# coding=UTF-8
from urllib import request
import json


tecent_template_url = 'http://vv.video.qq.com/getinfo?vids=%s&platform=101001&charge=0&otype=json&defn=shd'


def tecent_parse(target_url):
    vid = target_url[len('https://v.qq.com/x/page/'):-5]
    response = request.urlopen(request.Request(tecent_template_url % vid)).read().decode('utf-8')
    json_data = response[len('QZOutputJson='):-1]
    json_obj = json.loads(json_data)
    download_url = json_obj['vl']['vi'][0]['ul']['ui'][0]['url'] + json_obj['vl']['vi'][0]['fn'] + '?vkey=' + \
                   json_obj['vl']['vi'][0]['fvkey']
    video_name = json_obj['vl']['vi'][0]['ti'] + "." + json_obj['fl']['fi'][1]['name']
    return download_url, video_name
