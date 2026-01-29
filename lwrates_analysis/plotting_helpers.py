import logging
from matplotlib import pyplot as plt
from pathlib import Path

log = logging.getLogger(__name__)


def save_plot_to_path(fig: plt.Figure, plot_file_path: Path) -> None:
    """
    Save a figure to a path, sending a warning log in case the a file at that location already exists.
    Parameters
    ----------
    fig : plt.Figure
        The figure to save.
    plot_file_path : Path
        The path where the figure has to be saved.
    """
    if plot_file_path.is_file():
        log.warning("The path provided already corresponds to a file, it will be overwritten.")
    else:
        plot_file_path.parent.mkdir(exist_ok=True, parents=True)
        log.info("The plot will be saved at the location %s.", plot_file_path)
    fig.savefig(plot_file_path, dpi=100, bbox_inches="tight")