import os
import random
import time

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    import __init__
from roxel import Roxel
from shapes import Square
from gif import Gif

CURRENT_DIR         = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR            = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
OUTPUT_DIR          = os.path.join(ROOT_DIR, "outputs", "square_gif")
OUTPUT_FRAME_DIR    = os.path.join(OUTPUT_DIR, "frames")

def main():
    # Initialise square
    square = Square(0.5, 0.5, 0.5)
    # Initialise number of roxel rotations per second
    abs_rotations_per_second = 1
    # Initialise number of roxels in each dimension and axis limits
    n_x = 20
    n_y = 20
    x_min = 0
    x_max = 1
    y_min = 0
    y_max = 1
    # Initialise ratio of white space to roxels, and diameter of each roxel
    s = 0.5
    d = 1 / (n_x + ((n_x + 1) * s))
    # Initialise list of roxels
    random.seed(0)
    roxel_list = []
    for i_x in range(n_x):
        for i_y in range(n_y):
            x = ((i_x + 1) * s * d) + ((i_x + 0.5) * d)
            y = ((i_y + 1) * s * d) + ((i_y + 0.5) * d)
            phase = random.uniform(0, 2 * np.pi)
            if square.is_inside_square(x, y):
                rotations_per_second = -2*abs_rotations_per_second
            else:
                rotations_per_second = -abs_rotations_per_second / 3
            roxel = Roxel(x, y, d * 0.5, phase, rotations_per_second)
            roxel_list.append(roxel)

    # Create frames of the gif
    print("Making gif frames...", flush=True)
    fps = 25
    duration = 3
    n_frames = fps * duration
    gif = Gif()
    if not os.path.isdir(OUTPUT_FRAME_DIR):
        os.makedirs(OUTPUT_FRAME_DIR)

    for i in range(n_frames):
        t = i / fps
        # Create figure
        plt.figure(figsize=[8, 6])
        # Plot roxels
        for roxel in roxel_list:
            x1, y1, x2, y2 = roxel.get_end_points(t)
            plt.plot([x1, x2], [y1, y2], c="k")

        # Format, save and close the figure
        plt.axis("square")
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.tick_params(
            bottom=False,
            labelbottom=False,
            left=False,
            labelleft=False,
        )
        output_filename = "Roxel square gif, frame %i.png" % i
        output_path = os.path.join(OUTPUT_FRAME_DIR, output_filename)
        plt.savefig(output_path)
        plt.close()
        gif.add_frame_filename(output_path)
        print_str = "\r" + ((i + 1) * "#") + ((n_frames - i - 1) * ".")
        print(print_str, end="", flush=True)

    # Make gif
    print("\nMaking gif...")
    gif_filename = "Roxel square gif"
    ms_per_s = 1000
    gif.make_gif(gif_filename, OUTPUT_DIR, ms_per_s/fps)


if __name__ == "__main__":
    t0 = time.perf_counter()
    main()
    t1 = time.perf_counter()
    print("Time elapsed = %.1f s" % (t1 - t0))
