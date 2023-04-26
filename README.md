# Fractals-at-Institute-of-Nuclear-Physics-in-Cracow
## Introduction
Results of scientific workshops at IFJ PAN in Cracow.
The code was created by Jakub Halfar and me under the eye of Phd Eng Paweł Oświęcimka (https://scholar.google.pl/citations?user=i2uGj0YAAAAJ&hl=pl).
Our goal was to use box-counting method in order to calculate fractal dimension of an object shown on a picture.

We focused on 4 domains: 
1. Magnetic Resonance Imaging (MRI) - we succeeded to notice a notable change in fractal dimension of brain picture before and during dementia.
2. Paintings of Jackson Pollock - we found a significant change in fractal dimension between his early artworks (figurative to some extent) and his subsequent (and most famous) works, which were entirely abstract, yet somehow fractal. Fractal properties of Pollock's art were observed by many researchers earlier, that's why our algorithm has proven its reliability.
3. Analysis of city infrastracture from a bird's eye view - we processed maps and tried to find fractal properties in layout of streets and buildings.
4. Analysis of stock chart, which is said to also have presumably some fractal properties.

Everything happend in 2022, thanks to scholarship program "Krajowy Fundusz na Rzecz Dzieci", which I have pleasure to be part of.

## Usage guide
- fractals.py 
  The most important function is 'fractal_dimension()', which performs box-counting in order to return fractal dimension value of given image. Its key parameters are:
  - imgname: file path
  - q (float): an arbitrary value to use as exponent for distorting the data
  - threshold: detection threshold - the higher it is, the fewer dark boxes are counted
  - min_depth, max_depth: - extreme exponents of 2, specifying the lower and upper limit of number of boxes
  - debug: if 'True', images showing detected boxes at every iteration step would be displayed
- mri.py
  The function 'calculate_mri_fractal_dimension()' takes a list of tresholds and a list of image names and calculates fractal dimension for each file iteratively for every threshold. In corresponding data/MRI folder there are four exemplary MRI scans - first two show brain of patient with early dementia, two other - with late dementia. There can be observed a significant shift in the fractal dimension between these two states.
It is worth to mention, that by setting 'crucial_debug' parameter to 'True', displaying additional graphs and key stages is enabled.
- pollock.py
  Similarly to MRI, 'calculate_pollock_fractal_dimension()' returns fractal dimension values, but in this case for Jackson Pollock's paintings. It is interesting, that the correlation between the stage of the artist's work and the fractal dimension can be observed. The later the artwork (and thus - the more abstract), the greater the value of the fractal dimension.
