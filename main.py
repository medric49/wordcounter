# Author : Medric Sonwa

from sys import stdin
import os
import time
import re


def filter_text(text, url=True, num=True, currency=True, month=True):
    text = text.split(' ')
    new_text = []

    for word in text:
        if url and (word.startswith('www.') or word.endswith(('.com', '.fr', '.ca', '.org'))):
            new_text.append('__URL__')

        elif num and (re.fullmatch('^\d*\.?\d*$', word.replace(',', '')) is not None):
            new_text.append('__NUM__')

        elif currency and (word in ['$', '£', '€', '¥', '¢', '₩', 'Fr', 'Kr', '₿', '฿']):
            new_text.append('__CURRENCY__')

        elif month and (word in ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']):
            new_text.append('__MONTH__')

        else:
            new_text.append(word)

    return new_text


def get_vocabular(target_dir, sort=True, transformations=[]):
    files = os.listdir(target_dir)
    files = sorted(files)
    voc = {}

    tic = time.time()

    file_evol = [0]
    time_evol = [0]
    voc_evol = [0]

    nb_word = 0

    for i, file in enumerate(files):
        print(file)
        file_path = os.path.join(target_dir, file)

        with open(file_path) as f:
            text = f.read()
            text = text.replace('\n', ' ')

            for transformation in transformations:
                text = transformation(text)

            if not isinstance(text, list):
                text = text.split(' ')

            for word in text:
                voc[word] = 1 if word not in voc else voc[word] + 1
                nb_word += 1

        tac = time.time() - tic

        file_evol.append(i+1)
        time_evol.append(tac)
        voc_evol.append(len(voc))

    voc = voc.items()
    if sort:
        voc = sorted(voc, key=lambda x: x[1], reverse=True)

    print(f'Max time: {round(time_evol[-1], 2)}s ({round(time_evol[-1] / 60, 2)}min)')
    print(f'Max voc size: {voc_evol[-1]}')
    print(f'Number of words: { nb_word } ')

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


def save_evolution(target_dir, transformations):
    voc, evolution = get_vocabular(target_dir, sort=False, transformations=transformations)

    file_evol, time_evol, voc_evol = evolution

    with open('evolution.txt', 'w') as file:
        for i in file_evol:
            file.write(f'{i} {time_evol[i]} {voc_evol[i]}\n')


def freq_top_less(target_dir):
    voc, evolution = get_vocabular(target_dir, sort=True, transformations=[
        str.lower,
        lambda text: filter_text(text, url=True, num=True, currency=False, month=False)
    ])

    file = open('freq-top1000', 'w')
    for word, _ in voc[:1000]:
        file.write(f'{word} ')
    file.close()

    file = open('freq-less1000', 'w')
    for word, _ in voc[-1000:]:
        file.write(f'{word} ')
    file.close()

    file_evol, time_evol, voc_evol = evolution

    with open('evolution.txt', 'w') as file:
        for i in file_evol:
            file.write(f'{i} {time_evol[i]} {voc_evol[i]}\n')


if __name__ == '__main__':
    target_dir = stdin.read().split('\n')[0]
    save_evolution(target_dir, transformations=[
        lambda x: filter_text(x, url=False, num=False, currency=False, month=True)
        ]
    )


