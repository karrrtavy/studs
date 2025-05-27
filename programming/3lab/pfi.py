import matplotlib.pyplot as plt
import argparse
import csv
import sys
from matplotlib.ticker import ScalarFormatter

def visualize_from_file(filename, output_image=None):
    data = {'rows': [], 'variety': [], 'no_index': [], 'with_index': []}
    
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data['rows'].append(int(row['Rows']))
            data['variety'].append(int(row['Variety']))
            data['no_index'].append(float(row['TimeNoIndex']))
            data['with_index'].append(float(row['TimeWithIndex']))
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 15))
    
    # График 1: Время выполнения без индекса
    for variety in sorted(set(data['variety'])):
        rows = []
        no_index = []
        for i, v in enumerate(data['variety']):
            if v == variety:
                rows.append(data['rows'][i])
                no_index.append(data['no_index'][i])
        ax1.plot(rows, no_index, 'o-', label=f'Variety={variety}')
    
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_title('Время выполнения без индекса')
    ax1.set_ylabel('Время (сек)')
    ax1.grid(True, which="both", ls="-")
    ax1.legend()
    
    # График 2: Время выполнения с индексом
    for variety in sorted(set(data['variety'])):
        rows = []
        with_index = []
        for i, v in enumerate(data['variety']):
            if v == variety:
                rows.append(data['rows'][i])
                with_index.append(data['with_index'][i])
        ax2.plot(rows, with_index, 's--', label=f'Variety={variety}')
    
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.set_title('Время выполнения с индексом')
    ax2.set_ylabel('Время (сек)')
    ax2.grid(True, which="both", ls="-")
    ax2.legend()
        
    plt.show()

def main():
    parser = argparse.ArgumentParser(description='Визуализация результатов лабораторной работы №3')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', help='CSV файл с результатами (из C++ программы)')
    group.add_argument('-d', '--data', nargs='+', help='Данные в формате: rows1 variety1 no_index1 with_index1 rows2...')
    parser.add_argument('-o', '--output', help='Файл для сохранения графиков')
    
    args = parser.parse_args()
    
    visualize_from_file(args.file, args.output)

if __name__ == "__main__":
    main()