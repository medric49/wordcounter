# Author : Medric Sonwa
import sys
from sys import stdin
import os


if __name__ == '__main__':
    target_dir = stdin.read().split('\n')[0]
    files = os.listdir(target_dir)
    files = sorted(files)

    voc = set()

    for file in files:
        print(file)
        file_path = os.path.join(target_dir, file)

        with open(file_path) as f:
            text = f.read()
            words = text.split(' ')
            voc = voc.union(words)

    print(len(voc))


