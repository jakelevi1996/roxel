import numpy as np
from jutility import plotting, util, cli

def main(args: cli.Namespace):
    seed, n, size, t_max, dt, num_periods, text_str, output_dir = args.get(
        "seed, n, size, t_max, dt, num_periods, text_str, output_dir",
    )
    assert isinstance(seed,         int)
    assert isinstance(n,            int)
    assert isinstance(size,         int)
    assert isinstance(t_max,        float)
    assert isinstance(dt,           float)
    assert isinstance(num_periods,  float)
    assert isinstance(text_str,     str)
    assert isinstance(output_dir,   str)

    rng = np.random.default_rng(seed)

    x = np.linspace(0, 3, n)
    s = (2 * x) % 2
    t = np.where(s < 1, s, 2 - s)
    m = np.arange(n) & 1
    h = (x + m/2) % 1

    kw = {"m": ".", "ls": ""}
    mp = plotting.MultiPlot(
        plotting.Subplot(
            plotting.Line(x, t, c="b", **kw),
            plotting.Line(x, h, c="r", **kw),
            title="Signals",
        ),
        plotting.Subplot(
            plotting.Line(x[1:], (np.diff(t)/np.diff(x)), c="b", **kw),
            plotting.Line(x[1:], (np.diff(h)/np.diff(x)), c="r", **kw),
            title="Derivatives",
        ),
        plotting.Subplot(
            plotting.Hist(t, np.linspace(0, 1, 15), c="b"),
            title="Distribution",
        ),
        plotting.Subplot(
            plotting.Hist(h, np.linspace(0, 1, 15), c="r"),
            title="Distribution",
        ),
        legend=plotting.FigureLegend(
            plotting.Line([], **kw, c="b", label="Low frequency"),
            plotting.Line([], **kw, c="r", label="High frequency"),
        ),
        figsize=[10, 6],
    )
    mp.save("signals", output_dir)

    mp = plotting.MultiPlot(
        plotting.Subplot(
            plotting.Text(
                x=0,
                y=0,
                s=text_str.replace("\\n", "\n"),
                center_align=True,
                size=size,
                weight="bold",
            ),
            xlim=[-1, 1],
            ylim=[-1, 1],
            axis_off=True,
        ),
        figsize=[5, 5],
        dpi=80,
    )
    i = mp.get_image_array()
    i = i[..., :-1]
    i = (i - i.min()) / (i.max() - i.min())
    assert isinstance(i, np.ndarray)
    x0 = rng.uniform(0, 1, i.shape)

    num_t = int(t_max/dt)
    x_shape = [num_t] + ([1] * len(i.shape))
    x = np.linspace(0, num_periods, num_t, False).reshape(x_shape) + x0

    s = (2 * x) % 2
    t = np.where(s < 1, s, 2 - s)
    m = np.arange(num_t).reshape(x_shape) & 1
    h = (x + m/2) % 1

    y = (1 - i) * t + (i) * h

    time_list = np.linspace(0, t_max, num_t, endpoint=False).tolist()
    gif = plotting.Gif()
    for i, ti in enumerate(time_list):
        mp = plotting.plot(
            plotting.ImShow(y[i], vmin=0, vmax=1),
            title="t = %.2f s" % ti,
            save_close=False,
        )
        gif.add_multiplot_frame(mp)
        if i in [3, 16]:
            mp.save("frame %i" % i, output_dir)

        mp.close()

    gif.save("ordered", output_dir, frame_duration_ms=(1000 * dt))
    gif.shuffle(rng)
    gif.save("shuffle", output_dir, frame_duration_ms=(1000 * dt))

if __name__ == "__main__":
    parser = cli.ObjectParser(
        cli.Arg("seed",         type=int,   default=0),
        cli.Arg("n",            type=int,   default=300),
        cli.Arg("size",         type=int,   default=90),
        cli.Arg("dt",           type=float, default=1/30),
        cli.Arg("t_max",        type=float, default=2.0),
        cli.Arg("num_periods",  type=float, default=2.0),
        cli.Arg("text_str",   type=str, default="Happy\nChan\nukah!".upper()),
        cli.Arg("output_dir", type=str, default="outputs/flash_msg"),
    )
    args = parser.parse_args()

    with util.Timer("main"):
        main(args)
