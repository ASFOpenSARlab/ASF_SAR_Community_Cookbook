#! /usr/bin/python3

import hvplot.xarray  # noqa
from copy import deepcopy


def fr_view(plot_data, tiles, alpha):
    """
    fr_view expects a dictionary for `plot_data` like:
    {
        "show_fr": omega_web,
        "show_quality": quality_web
        "meta": {
            "bounds": {
                "x": (xmin, xmax),
                "y": (ymin, ymax)
            }
        }
    }
    """
    layers = deepcopy(tiles)

    for type, data in plot_data.items():
        if type == "show_fr":
            cmap = "RdBu_r"
            title = "Faraday Rotation"
            colorbar = False
        elif type == "show_quality":
            cmap = "viridis"
            title = "Faraday Rotation Quality"
            colorbar = True
        elif type == "meta":
            continue
        else:
            raise RuntimeError(f"Invalid dict in `fr_view`: {plot_data}")

        plot = data.hvplot.image(
            x="x",
            y="y",
            cmap=cmap,
            clim=(-5, 5),
            colorbar=colorbar,
            frame_width=700,
            frame_height=500,
            title=title,
        ).opts(
            alpha=alpha,
            xlim=(
                plot_data["meta"]["bounds"]["x"][0],
                plot_data["meta"]["bounds"]["x"][1],
            ),
            ylim=(
                plot_data["meta"]["bounds"]["y"][0],
                plot_data["meta"]["bounds"]["y"][1],
            ),
        )
        layers = layers * plot

    return layers
