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
    show_evolution('evolution.txt')

