# coding=UTF-8
from urllib import request
import json




def tecent_parse(target_url):
    tecent_video_prefix = 'https://v.qq.com/x/page/'
    template_url = 'http://vv.video.qq.com/getinfo?vids=%s&platform=101001&charge=0&otype=json&defn=shd';
    vid = target_url[len(tecent_video_prefix):-5]
    response = request.urlopen(request.Request(template_url % vid)).read().decode('utf-8')
    json_data = response[len('QZOutputJson='):-1]
    json_obj = json.loads(json_data)
    download_url = json_obj['vl']['vi'][0]['ul']['ui'][0]['url'] + json_obj['vl']['vi'][0]['fn'] + '?vkey=' + \
                   json_obj['vl']['vi'][0]['fvkey']
    video_name = json_obj['vl']['vi'][0]['ti'] + "." + json_obj['fl']['fi'][1]['name']
    return download_url,video_name


