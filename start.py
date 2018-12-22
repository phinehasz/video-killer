# coding=UTF-8
from lib import url_parser, download
import sys

if __name__ == '__main__':
    url = sys.argv[1:][0]
    if 'https://v.qq.com/x/page/' in url:
        download_url, video_name = url_parser.tecent_parse(url)
    else:
        print("it's not supported")
    download.down(download_url, video_name)
