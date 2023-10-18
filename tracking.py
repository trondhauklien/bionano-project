import pims
import trackpy as tp
from pathlib import Path

basePath = Path(__file__).parent.parent.__str__()


def analyze_video(frames):
    f = tp.batch(frames, diameter=35, minmass=1000)
    t = tp.link(f, search_range=35, memory=5)
    print("Before:", t["particle"].nunique())
    t = tp.filter_stubs(t, 25)
    print("After:", t["particle"].nunique())

    return t


def archive_dataframe(dataframe, filename):
    """Store the particle tracking data in a binary file (ie. pickle file) for later use."""
    dataframe.to_pickle(f"{basePath}/project/data/" + filename + ".pkl")


def main():
    directory = "project/results/Paint Particles/processed/"
    filename = "processed_darkf_sampleB_03_40x_5ms"
    filetype = ".tif"

    frames = pims.as_gray(pims.open(f"{basePath}/{directory}{filename}/*{filetype}"))

    t = analyze_video(frames)

    archive_dataframe(t, filename)


if __name__ == "__main__":
    main()
