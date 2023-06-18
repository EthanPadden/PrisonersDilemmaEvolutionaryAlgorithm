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
            if int(row[0]) != current_gen_num:
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

def line_graph_points():
    with open(output_filename, 'r') as file:
        reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
        color_codes = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
        handles = []
        labels = []
        cgen = 0
        alpha = []
        row = next(reader, None)

        while row:
            cplr = 0
            while row[0] == cgen:
                # While were in the same generation
                if cgen == 0:
                    alpha.append([])

                # regardless
                alpha[cplr].append(int(row[2]))
                cplr += 1
                row = next(reader, None)
                if not row:
                    break

            if not row:
                break
            if row[0] != (cgen + 1):
                raise Exception
            cgen += 1

        gen_nums = []
        for i in range(0, (cgen+1)):
            gen_nums.append(i)
        for i in range(0, len(alpha)):
            color_code = color_codes[i % len(color_codes)]
            beta = alpha[i]
            plt.plot(gen_nums, beta, marker='o', linestyle='-', color=color_code, label=i)

        plt.title('Points')
        plt.xlabel('generation')
        plt.ylabel('points')
        plt.show()


def line_graph_points_stats():
    with open(output_filename, 'r') as file:
        reader = csv.reader(file)


        gen_nums = [0]
        avg_points = [0]
        best_points = [0]
        worst_points = [0]

        current_gen_num = 0
        for row in reader:
            if int(row[0]) != current_gen_num:
                if int(row[0]) != (current_gen_num+1):
                    raise Exception
                else:
                    # We are in the next generation
                    current_gen_num = current_gen_num + 1
                    gen_nums.append(current_gen_num)
                    avg_points.append(0)
                    best_points.append(0)
                    worst_points.append(0)

                avg_points[current_gen_num] += int(row[2])
                current_best_pts = best_points[current_gen_num]
                best_points[current_gen_num] = max(current_best_pts, int(row[2]))
                current_worst_pts = worst_points[current_gen_num]
                worst_points[current_gen_num] = min(current_worst_pts, int(row[2]))

        for avg_pts_gen_num in range(0, len(avg_points)):
            total_pts = avg_points[avg_pts_gen_num]
            avg_points[avg_pts_gen_num] = total_pts/current_gen_num

        plt.plot(gen_nums, avg_points, marker='o', linestyle='-', color='b', label='avg')
        plt.plot(gen_nums, best_points, marker='o', linestyle='-', color='g', label='best')
        plt.plot(gen_nums, worst_points, marker='o', linestyle='-', color='r', label='worst')

        plt.title('Points')
        plt.xlabel('generation')
        plt.ylabel('points')
        plt.show()

if __name__ == '__main__':
    line_graph_points()