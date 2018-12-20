# coding=UTF-8
from urllib import request


def down(download_url,video_name):
    request.urlretrieve(download_url, filename=video_name, reporthook=report, data=None)


def report(a, b, c):
    '''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)