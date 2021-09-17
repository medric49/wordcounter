# Author : Medric Sonwa

from sys import stdin
import os
import time



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


def save_evolution(target_dir):
    voc, evolution = get_vocabular(target_dir, sort=False)

    file_evol, time_evol, voc_evol = evolution

    with open('evolution.txt', 'w') as file:
        for i in file_evol:
            file.write(f'{i} {time_evol[i]} {voc_evol[i]}\n')


if __name__ == '__main__':
    target_dir = stdin.read().split('\n')[0]
    save_evolution(target_dir)


