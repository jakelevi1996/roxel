import os
import random
import time

import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    import __init__
from roxel import Roxel
from gif import Gif

CURRENT_DIR         = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR            = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
OUTPUT_DIR          = os.path.join(ROOT_DIR, "outputs", "hollie_gif")
OUTPUT_FRAME_DIR    = os.path.join(OUTPUT_DIR, "frames")

block_size = 3

def add_block_to_set(pixel_set, x_left, y_bottom, width=1, height=1):
    for x in range(x_left*block_size, (x_left + width)*block_size):
        for y in range(y_bottom*block_size, (y_bottom + height)*block_size):
            pixel_set.add((x, y))

def main():
    # Initialise number of roxels in each dimension and axis limits
    n_x = 13 * block_size
    n_y = 13 * block_size
    # Initialise ratio of white space to roxels, and diameter of each roxel
    s = 0.5
    d = 1 / (n_x + ((n_x + 1) * s))
    # Create set of fast pixel locations (TODO: define separate classes in the
    # shapes module for each letter, and add function/class for a Roxel pattern
    # which combines multiple shapes, instead of defining each letter manually)
    fast_pixel_set = set()
    # H
    add_block_to_set(fast_pixel_set, 1, 7, 1, 5)
    add_block_to_set(fast_pixel_set, 2, 9, 1, 1)
    add_block_to_set(fast_pixel_set, 3, 7, 1, 5)
    # O
    add_block_to_set(fast_pixel_set, 5, 8, 1, 3)
    add_block_to_set(fast_pixel_set, 6, 7, 1, 1)
    add_block_to_set(fast_pixel_set, 6, 11, 1, 1)
    add_block_to_set(fast_pixel_set, 7, 8, 1, 3)
    # L
    add_block_to_set(fast_pixel_set, 9, 7, 1, 5)
    add_block_to_set(fast_pixel_set, 10, 7, 2, 1)
    # L
    add_block_to_set(fast_pixel_set, 1, 1, 1, 5)
    add_block_to_set(fast_pixel_set, 2, 1, 2, 1)
    # I
    add_block_to_set(fast_pixel_set, 5, 1, 3, 1)
    add_block_to_set(fast_pixel_set, 5, 5, 3, 1)
    add_block_to_set(fast_pixel_set, 6, 2, 1, 3)
    # E
    add_block_to_set(fast_pixel_set, 9, 1, 1, 5)
    add_block_to_set(fast_pixel_set, 10, 1, 2, 1)
    add_block_to_set(fast_pixel_set, 10, 3, 2, 1)
    add_block_to_set(fast_pixel_set, 10, 5, 2, 1)

    # Initialise list of roxels
    random.seed(0)
    roxel_list = []
    for i_x in range(n_x):
        for i_y in range(n_y):
            x = ((i_x + 1) * s * d) + ((i_x + 0.5) * d)
            y = ((i_y + 1) * s * d) + ((i_y + 0.5) * d)
            phase = random.uniform(0, 2 * np.pi)
            if (i_x, i_y) in fast_pixel_set:
                rotations_per_second = -2
            else:
                rotations_per_second = -1 / 4
            roxel = Roxel(x, y, d * 0.5, phase, rotations_per_second)
            roxel_list.append(roxel)

    # Create frames of the gif
    print("Making gif frames...", flush=True)
    fps = 25
    duration = 2
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
        output_filename = "Roxel hollie gif, frame %i.png" % i
        output_path = os.path.join(OUTPUT_FRAME_DIR, output_filename)
        plt.savefig(output_path)
        plt.close()
        gif.add_frame_filename(output_path)
        print_str = "\r" + ((i + 1) * "#") + ((n_frames - i - 1) * ".")
        print(print_str, end="", flush=True)

    # Make gif
    print("\nMaking gif...")
    gif_filename = "Roxel hollie gif"
    ms_per_s = 1000
    gif.make_gif(gif_filename, OUTPUT_DIR, ms_per_s/fps)


if __name__ == "__main__":
    t0 = time.perf_counter()
    main()
    t1 = time.perf_counter()
    print("Time elapsed = %.1f s" % (t1 - t0))
