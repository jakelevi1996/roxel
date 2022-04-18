""" Module containing the Gif class for making a gif """

import os
import PIL

class Gif:
    def __init__(self):
        self._frame_filename_list = []

    def add_frame_filename(self, frame_filename):
        self._frame_filename_list.append(frame_filename)

    def make_gif(
        self,
        output_name,
        output_dir,
        duration=100,
        optimise=False,
    ):
        """ Make gif using pre-existing image files, and save to disk. The gif
        will loop indefinitely.

        Inputs:

        -   output_name: filename for the output gif (not including .gif file
            extension)
        -   output_dir: directory that the output gif will be saved to
        -   duration: the duration each frame of the gif should last for, in
            milliseconds. Default is 100 seconds
        -   optimise: if True, attempt to compress the palette by eliminating
            unused colors. Default is False
        """
        image_list = [PIL.Image.open(f) for f in self._frame_filename_list]
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)
        output_path = os.path.join(output_dir, "%s.gif" % output_name)
        image_list[0].save(
            output_path,
            format="gif",
            save_all=True,
            append_images=image_list[1:],
            duration=duration,
            optimise=optimise,
            loop=0,
        )
