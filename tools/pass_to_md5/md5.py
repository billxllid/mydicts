from hashlib import md5

file = 'pass.txt'  # 密码文件
target = '81c47be5dc6110d5087dd4af8dc56552'  # 要爆破的目标md5

with open(file, 'r') as f:
    for l in f.readlines():
        s = l.replace('\n', '')
        ms = md5(s.encode('utf8'))
        if ms.hexdigest().__str__() == target:
            print(ms)
