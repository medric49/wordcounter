# Author : Medric Sonwa

from sys import stdin
import os


if __name__ == '__main__':
    target_dir = stdin.read().split('\n')[0]
    files = os.listdir(target_dir)
    files = sorted(files)

    print(files)

