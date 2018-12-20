# coding=UTF-8
from lib import url_parser, download

if __name__ == '__main__':
    url = 'https://v.qq.com/x/page/i0145lvzyj0.html'
    download_url, video_name = url_parser.tecent_parse(url)
    download.down(download_url, video_name)
