import os
import copy

class Main:

    def __init__(self):
        pass

    def get_content(self, filename):
        with open(filename, encoding='utf8') as f:
            tmp = [d.replace('\n', '') for d in f.readlines()]
            return tmp

    def main(self):
        file_list = [
            './passwords3.txt',
            './passwords4.txt',
            './top500.txt',
            './top1000.txt',
            './top3000.txt',
            './top6000.txt',
            './top19576.txt',
        ]
        dict_a = self.get_content('./pass.txt')
        for f in file_list:
            dict_b = self.get_content(f)
            ori_b = copy.deepcopy(dict_b)
            diff = set(dict_b) & set(dict_a)
            print('file: {}, count: {}, diff: {}, persent: {:.2}%'.format(f, len(ori_b), len(diff), len(diff) / len(ori_b)))
            for d in diff:
                print(' {}: {}'.format(d, ori_b.index(d) + 1))


if __name__ == "__main__":
    Main().main()