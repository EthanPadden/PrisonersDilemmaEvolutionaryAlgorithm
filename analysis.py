import csv
import matplotlib.pyplot as plt


output_filename = 'output/output Y-06-17_13-02-35.csv'
def scatter_plot_objective_space():
    with open(output_filename, 'r') as file:
        reader = csv.reader(file)
        color_codes = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
        handles = []
        labels = []

        current_gen_num = 0
        gen_pts = [[]]
        for row in reader:
            if int(int(row[0])) != current_gen_num:
                if int(row[0]) != (current_gen_num+1):
                    raise Exception
                else:
                    # We are in the next generation
                    current_gen_num = current_gen_num + 1
                    gen_pts.append([])

            gen_pts[current_gen_num].append(int(row[2]))

        for gen_num in range(0, len(gen_pts)):
            scatter = plt.scatter(
                [gen_num]*len(gen_pts[gen_num]),
                gen_pts[gen_num],
                marker='o', color=color_codes[gen_num],label=f'{gen_num}'
            )
            handles.append(scatter)
            labels.append(gen_num)

        plt.title('Gen Player points')
        plt.xlabel('generation')
        plt.ylabel('points')
        plt.legend(handles, labels)  # Insert legend using handles and labels

        plt.show()


if __name__ == '__main__':
    scatter_plot_objective_space()