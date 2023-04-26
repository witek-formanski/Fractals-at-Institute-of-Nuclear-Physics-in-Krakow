import matplotlib.pyplot as plt
from fractals import fractal_dimension
from plot_utils import save_plot, create_image_gallery, calculate_q_plot
from PIL import ImageOps
import numpy as np


def calculate_pollock_fractal_dimension(threshold, q, crucial_debug, debug):
    images = []
    df_list = []
    for i in range(0, 9):
        df, img = fractal_dimension(f'data/Pollock/{i}.jpg', q=q, threshold=threshold, min_depth=5, max_depth=11,
                                    label=i, return_image=True, debug=debug,
                                    transformation=lambda x: ImageOps.grayscale(x).convert("RGB"))
        print(f"painting {i}, fractal dimension = {df:.4f}")
        images.append(img)
        df_list.append(df)

    background = create_image_gallery(images)
    if crucial_debug: background.show()
    background.save(f"analysis/Pollock/debug_Pollock_threshold_{threshold}_q_{q}.png")

    plt.legend()
    plt.title(f"detection threshold = {threshold}")
    save_plot(plt, f"analysis/Pollock/Pollock_graph_threshold_{threshold}_q_{q}.png", axis=True)
    if crucial_debug: plt.show()

    y = np.array(df_list)
    x = np.array([t for t in range(len(y))])
    plt.plot(y, marker='o')
    ax = plt.gca()
    ax.set_xticklabels(
        [0, 1935, 1937, 1941, 1943, 1946, 1948, 1952, 1955, 1955])
    a, b = np.polyfit(x, y, 1)
    y_fit = a*x + b
    plt.xlabel("Year of the painting creation")
    plt.ylabel(f"$D_{q}$")
    plt.title("The fractal evolution of Pollock's work over time", fontsize=16)
    plt.plot(x, y_fit, ':', color='r')
    plt.grid('on')
    save_plot(plt, f"analysis/Pollock/evolution_graph_threshold_{threshold}_q_{q}.png", axis=True)
    if crucial_debug: plt.show()


def main():
    calculate_pollock_fractal_dimension(threshold=350, q=0, crucial_debug=True, debug=False)


if __name__ == '__main__':
    main()
