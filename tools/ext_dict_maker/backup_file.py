"""
生成备份文件字典：

1. 宁夏各地市的缩写
2. 网站域名的各种拼接
"""

import datetime
import tldextract


def normal_to_dict(ext_dict=[]):
    dict = ['www', 'web', 'webapps', 'site', 'wangzhan', 'portal', 'test', 'beifen', 'back', 'backup', 'bak', 'conf', 'config']
    dict.extend(ext_dict)
    dict.extend([i.capitalize() for i in dict])
    dict.extend([i.upper() for i in dict])
    return dict

def url_to_dict(url):
    dict = []
    b = tldextract.extract(url)
    if not b:
        return []
    dict.append(b.subdomain)
    dict.append(b.subdomain.capitalize())
    dict.append(b.subdomain.upper())
    dict.append(b.domain)
    dict.append(b.domain.capitalize())
    dict.append(b.domain.upper())
    dict.append(b.suffix)
    dict.append(b.fqdn)
    dict.append('{0}.{1}'.format(b.subdomain, b.domain))
    dict.append('{0}.{1}'.format(b.domain, b.suffix))
    for i in dict:
        if '.' in i:
            dict.append(i.replace('.', '_'))
            dict.append(i.replace('.', '-'))
    return dict

def year_to_dict():
    """
    '2017', '2018', '2019', '2020', '2021'
    """
    dict = []
    current_year = datetime.datetime.today().year
    dict.extend([str(i) for i in range(2001, current_year + 1)])
    return dict

def num_to_dict(bit=1):
    """
    '0', '1', '2', '00', '01', '02', '66', '88'
    """
    dict = []
    num_map = range(0, 10)
    for i in range(0, bit):
        if i == 0:
            zero = ''
        if i == 1:
            zero = '0'
        dict.extend(['{0}{1}'.format(zero, i) for i in num_map])
        zero = zero + '0'
    return dict

def letter_to_dict():
    """
    'a', 'b', 'c'
    """
    dict = []
    letter_map = 'abcdefghigklmnopqrstuvwxyz'
    dict.extend([i for i in letter_map])
    dict.extend(['{0}{1}'.format(i, i) for i in letter_map])
    return dict

def mix():
    """
    'www' => "www01"
    """
    dict = []
    num_dict = num_to_dict(2)
    for i in normal_to_dict():
        for j in num_dict:
            dict.append('{0}{1}'.format(i, j))
    return dict


def mix_ext(d):
    dict = []
    ext = ['zip', 'rar', 'war', 'old', 'bak', 'sql', 'tar.gz', 'tar.bz2']
    for i in ext:
        for j in d:
            dict.append('{0}.{1}'.format(j, i))
    return dict

def save(path, d):
    with open(path, 'w') as f:
        for i in d:
            f.write(i)
            f.write('\n')
    print('write dict: {}'.format(len(d)))


data = 'https://ningxia.tianditu.gov.cn/portal/home/'
final_name = []
final_name.extend(normal_to_dict(['home', '10.6.1']))
final_name.extend(url_to_dict(data))
final_name.extend(year_to_dict())
final_name.extend(num_to_dict(3))
final_name.extend(letter_to_dict())
# final_name.extend(mix())

save('./01.txt', mix_ext(final_name))
