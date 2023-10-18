# bionano-project
Repository for source code used to analyse the particle tracking data recorded in the first part of the bionano project.

## Image pre-processing with ImageJ
Videos from the microscope are processed using ImageJ using these simple steps:
1. Adjust auto contrast/brightness
2. Create Z-projection stack from average pixel values
3. Subtract the average image from all frames in the video, yelding a black backdrop with clearly visible particles.
4. Adjust auto contrast/brightness
Export the video as an image sequence of .tif files, the data format which was most stable during TrackPy batch processing.

Record the pixel per micron value to the `metadata.yml` file by using the line tool (draw a line between the grids) and choose "Analyze > Set Scale...".

## Particle tracking
Create an conda environment using the `environment.yml` file:
```
conda env create -f environment.yml
```
Run the `tracking.py` file for each image sequence. Update the hardcoded path to where the frames are stored. 
Rembember to adjust the parameters in the `tp.batch()` command such as `diameter` and `minmass` to remove any spurious particles.

## Data processing
Use the notebook to process the data.

The `tp.emsd()` utility function does not work because it uses some deprecated Pandas function. This can be solved by downgrading Pandas, change the `motion.py` file in TrackPy or by soft-matter actually merging [the pull request](https://github.com/soft-matter/trackpy/pull/740) solving this issue.
