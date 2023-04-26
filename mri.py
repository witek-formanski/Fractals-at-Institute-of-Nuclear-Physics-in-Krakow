import matplotlib.pyplot as plt
from fractals import fractal_dimension
from plot_utils import save_plot, create_image_gallery
import os


def calculate_mri_fractal_dimension(thresholds, images, markers, crucial_debug, debug, q):
    DIR = os.path.dirname(__file__)
    for threshold in thresholds:
        print(f"threshold = {threshold}")
        processed_images = []
        for imgname, marker in zip(images, markers):
            rel_path = f"data/MRI/{imgname}.png"
            df, processed_image = fractal_dimension(
                rel_path, threshold=threshold, min_depth=2, max_depth=11, label=imgname, marker=marker, return_image=True, debug=debug, q=q)
            processed_images.append(processed_image)
            print(f"image {imgname}, fractal dimension = {df:.2f}")

        background = create_image_gallery(processed_images)
        if crucial_debug: background.show()
        background.save(f"analysis/MRI/debug_MRI_threshold_{threshold}.png")

        plt.legend()
        plt.title(f"detection threshold = {threshold}, q = {q}")
        save_plot(plt, f"analysis/MRI/MRI_graph_threshold_{threshold}_q_{q}.png", axis=True)
        if crucial_debug: plt.show()
        print()


def main():
    calculate_mri_fractal_dimension(
        [150, 180, 200], ['a', 'b', 'c', 'd'], ['o', 'x', 'D', '^'], crucial_debug=True, debug=False, q=0)


if __name__ == '__main__':
    main()