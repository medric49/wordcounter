# Author : Medric Sonwa
import sys
from sys import stdin
import os
import time
from matplotlib import pyplot as plt


def get_vocabular(target_dir, sort=True, ):
    files = os.listdir(target_dir)
    files = sorted(files)
    voc = {}

    tic = time.time()

    file_evol = [0]
    time_evol = [0]
    voc_evol = [0]


    for i, file in enumerate(files):
        print(file)
        file_path = os.path.join(target_dir, file)

        with open(file_path) as f:
            text = f.read()
            text = text.replace('\n', ' ')
            words = text.split(' ')
            for word in words:
                voc[word] = 1 if word not in voc else voc[word] + 1

        tac = time.time() - tic


        file_evol.append(i+1)
        time_evol.append(tac)
        voc_evol.append(len(voc))

    voc = voc.items()
    if sort:
        voc = sorted(voc, key=lambda x: x[1], reverse=True)

    return voc, (file_evol, time_evol, voc_evol)


def words_and_types(target_dir):
    voc, _ = get_vocabular(target_dir, sort=False)
    count = 0
    for word, freq in voc:
        count += freq
    print(f'Nb. types: {len(voc)}')
    print(f'Nb. words: {count}')


def freq_1bshort(target_dir):
    sorted_voc, _ = get_vocabular(target_dir)

    file = open('freq-1bshort', 'w')
    for i in range(100):
        word, freq = sorted_voc[i]
        file.write(f'{freq} {word}\n')
    file.close()


def show_evolution(target_dir):
    voc, evolution = get_vocabular(target_dir, sort=False)

    file_evol, time_evol, voc_evol = evolution

    figure, axis = plt.subplots(1, 2, figsize=(14, 5))

    axis[0].plot(file_evol, time_evol, color='blue')
    axis[0].set_xlim((0, 10))
    axis[0].set_ylim(0)
    axis[0].set_xlabel('Nb. tranches')
    axis[0].set_ylabel('Temps exécution')

    axis[1].plot(file_evol, voc_evol, color='green')
    axis[1].set_xlim((0, 10))
    axis[1].set_ylim(0)
    axis[1].set_xlabel('Nb. tranches')
    axis[1].set_ylabel('Taille voc.')

    plt.savefig('evolution.png')


if __name__ == '__main__':
    target_dir = stdin.read().split('\n')[0]
    show_evolution(target_dir)


