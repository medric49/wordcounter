from matplotlib import pyplot as plt


def show_evolution(evolution_file):
    with open(evolution_file, 'r') as file:
        file = file.read().split('\n')

    file_evol = []
    time_evol = []
    voc_evol = []

    for l in file:
        if l == '':
            continue
        file_i, time, voc_size = l.split()
        file_evol.append(int(file_i))
        time_evol.append(float(time))
        voc_evol.append(int(voc_size))

    print(f'Max time: {round(time_evol[-1], 2)}s ({round(time_evol[-1]/60, 2)}min)')
    print(f'Max voc size: {voc_evol[-1]}')

    figure, axis = plt.subplots(1, 2, figsize=(14, 5))

    axis[0].plot(file_evol, time_evol, color='blue')
    axis[0].set_xlim(0)
    axis[0].set_ylim(0)
    axis[0].set_xlabel('Nombre de tranches')
    axis[0].set_ylabel('Temps exécution (s)')

    axis[1].plot(file_evol, voc_evol, color='blue')
    axis[1].set_xlim(0)
    axis[1].set_ylim(0)
    axis[1].set_xlabel('Nombre de tranches')
    axis[1].set_ylabel('Nombre de types')

    plt.show()


def show_evolution_2(evolution_1, evolution_2):
    with open(evolution_1, 'r') as file:
        file = file.read().split('\n')

    file_1 = []
    time_1 = []
    voc_1 = []
    for l in file:
        if l == '':
            continue
        file_i, time, voc_size = l.split()
        file_1.append(int(file_i))
        time_1.append(float(time))
        voc_1.append(int(voc_size))

    with open(evolution_2, 'r') as file:
        file = file.read().split('\n')

    time_2 = []
    voc_2 = []
    for l in file:
        if l == '':
            continue
        _, time, voc_size = l.split()
        time_2.append(float(time))
        voc_2.append(int(voc_size))

    figure, axis = plt.subplots(1, 2, figsize=(14, 5))

    axis[0].plot(file_1, time_1, color='blue', label='Avant pré-traitement')
    axis[0].plot(file_1, time_2, color='red', label='Après pré-traitement')
    axis[0].set_xlim(0)
    axis[0].set_ylim(0)
    axis[0].legend()
    axis[0].set_xlabel('Nb. tranches')
    axis[0].set_ylabel('Temps exécution (s)')

    axis[1].plot(file_1, voc_1, color='blue', label='Avant pré-traitement')
    axis[1].plot(file_1, voc_2, color='red', label='Après pré-traitement')
    axis[1].set_xlim(0)
    axis[1].set_ylim(0)
    axis[1].legend()
    axis[1].set_xlabel('Nb. tranches')
    axis[1].set_ylabel('Taille voc.')

    plt.show()


if __name__ == '__main__':
    show_evolution_2('evolution_default.txt', 'evolution_final.txt')

