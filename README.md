# `roxel`

This miniature project is an investigation into perception of shapes from motion.

Can you see a pattern in the following picture?

![Roxel square gif, frame 0.png](https://github.com/jakelevi1996/roxel/blob/main/outputs/protected/square_gif/frames/Roxel%20square%20gif%2C%20frame%200.png "Roxel square gif, frame 0.png")

No? How about in the following picture?

![Roxel square gif, frame 31.png](https://raw.githubusercontent.com/jakelevi1996/roxel/main/outputs/protected/square_gif/frames/Roxel%20square%20gif%2C%20frame%2031.png "Roxel square gif, frame 31.png")

What about in the following GIF?

![Roxel square gif.gif](https://raw.githubusercontent.com/jakelevi1996/roxel/main/outputs/protected/square_gif/Roxel%20square%20gif.gif "Roxel square gif.gif")

You should be able to see a pattern, that you weren't able to see from looking at the individual frames of the GIF.

That is to say, it is only by perceiving the **motion** of the animation, that you were able to see the pattern.

What does this tell us about human visual perception? Would modern AI approaches to computer vision be able to demonstrate this behaviour?

The images and animations above can be generated with the following command:

```
python scripts/make_square_gif.py
```

## Another example

Here is another example (the pattern in this one is more complex, and slightly harder to spot):

![Roxel Hollie gif.gif](https://github.com/jakelevi1996/roxel/blob/main/outputs/protected/hollie_gif/Roxel%20hollie%20gif.gif "Roxel Hollie gif.gif")

## Flashing messages

```
python scripts/flashing_msg.py
```

![](outputs/flash_msg/signals.png)

![](outputs/flash_msg/frame_3.png)

![](outputs/flash_msg/frame_16.png)

![](outputs/flash_msg/shuffle.gif)

![](outputs/flash_msg/ordered.gif)

```
python scripts/flashing_msg.py --text_str "MERRY\nCHRIS\nTMAS!" --output_dir outputs/flash_msg_xmas
```

![](outputs/flash_msg_xmas/frame_3.png)

![](outputs/flash_msg_xmas/frame_16.png)

![](outputs/flash_msg_xmas/shuffle.gif)

![](outputs/flash_msg_xmas/ordered.gif)
