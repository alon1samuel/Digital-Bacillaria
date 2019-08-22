## Digital Bacillaria

<p align="center">
  <img width="239" height="211" src="https://user-images.githubusercontent.com/19001437/57882552-960c8900-77e9-11e9-9f10-9ab687f6391e.jpg"><BR>
</p>

_Bacillaria_ is a diatom genus in the [Bacillariaceae family](http://tolweb.org/Bacillariaceae/125684). [Diatoms](http://tolweb.org/Diatoms/) are a group of [Eukaryotic](https://en.wikipedia.org/wiki/Eukaryote) microorganisms composed of cells with silica walls and that exhibit a unique life-history [1].

## Species
We are working with images from the species _Bacillaria paradoxa_, also known as _Bacillaria paxillifer_ [2].

<p align="center">
  <img width="160" height="270" src="https://user-images.githubusercontent.com/19001437/58395892-f2ed1800-800f-11e9-9a64-4cd517ea57ac.png"><BR>
</p>
  
Drawing by Muller (circa 1792) [3]. Click to enlarge.  

### Description of _Bacillaria_
Cells are elongated and motile, sliding along each other, in stacked colonies. Cells are rectangular in side view. Two large plate-like chloroplasts are present, one near each end of the cell. The nucleus is located centrally. Cells are yellow-brown in colour. 

<p align="center">
  <img width="210" height="166" src="https://user-images.githubusercontent.com/19001437/58396330-ca661d80-8011-11e9-80fe-e0f9fde60dc1.png"><BR>
</p>

Examples of _Bacillaria_ colonies and close-up images of single cells using [Scanning Electron Microscopy (SEM)](https://en.wikipedia.org/wiki/Scanning_electron_microscope). Courtesy Figures 27-30 in [4]. Click to enlarge.  

The stacked colony moves by pairs of individual filaments sliding against each other. This movement is like an accordian in that the displacement ripples across the extent of the colony and results in large positional changes. This results in cyclic gliding movements resulting from the action of actin filament motors [5]. The primary movement pattern also has a number of interesting properties, including the potential for explosive kinetics resulting from [higher-order derivatives of motion](https://en.wikipedia.org/wiki/Jerk_(physics)#Higher_derivatives).

### Our Goal
The deliverable here would be to use machine learning techniques to segment individual cells in these movies, and establish the trajectory and orientation of each cell from one movie frame to the next. After that we can create models to define motility of _Bacillaria_.

Additionally, we aim to define five points on each cell:

* the two ends of the cell (1 and 2).

* the midpoint of the line formed between 1 and 2 (3).

* the edges of a cell (4 and 5) defined by drawing a line perpendicular to the axis defined by points 1, 2, and 3.

<p align="center">
  <img width="141" height="211" src="https://user-images.githubusercontent.com/19001437/60073556-66a14400-96e6-11e9-913d-188015b3f8f1.jpg"><BR>
</p>
  
A diagram showing the five points on a sample cell. Click to enlarge.
  

To get more information about what is currently going on, check out the issues and subdirectories of this repository.

### Using digital data to understand biology
One of our goals is to use the data extracted from microscopy images to better understand biological processes such as the movement of a _Bacillaria_ colony. One such example that has been conducted with coarse-grained phenotypic models is to model the hydrodynamics of filament movement through the water column [6].

<p align="center">
  <img width="466" height="414" src="https://user-images.githubusercontent.com/19001437/58767418-47345280-8550-11e9-987c-9e302567e55c.png"><BR>
</p>
  
Examples of _Bacillaria_ filament moving through the water column (represented as a flow field). Click to enlarge. 
  

## REFERENCES (numbered in alphabetical order):
[1] Sabater, S. (2009). [Diatoms](https://www.sciencedirect.com/science/article/pii/B9780123706263001356). _Encyclopedia of Inland Waters_, 149-156. doi:10.1016/B978-012370626-3.00135-6

[2] Jahn, R. and Schmid, A.M.M. (2007). [Revision of the brackish-freshwater diatom genus _Bacillaria Gmelin_ (Bacillariophyta) 
with the description of a new variety and two new species](https://www.researchgate.net/publication/249026177_Revision_of_the_brackish-freshwater_diatom_genus_Bacillaria_Gmelin_Bacillariophyta_with_the_description_of_a_new_variety_and_two_new_species). _European Journal of Phycology_, 42(3), 295-312. doi:10.1080/09670260701428864.

[3] Ussing, A.P., R. Gordon, L. Ector, K. Buczko, A.G. Desnitskiy and S.L. Van Landingham (2005) The colonial diatom _Bacillaria 
paradoxa_: chaotic gliding motility, Lindenmeyer Model of colonial morphogenesis, and bibliography, with translation by O.F. 
Muller (1783). _Diatom Monographs_, 5, 1-139.

[4] Gordon, R. (2016). [Partial synchronization of the colonial diatom _Bacillaria paradoxa_](https://riojournal.com/article/7869/). _Research Ideas and Outcomes_, 2, e7869.

[5] Poulsen, N.C., Spector, I., Spurck, T.P., Schultz, T.F., and Wetherbee, R (1999). Diatom gliding is the result of an actin-myosin motility system. Cell Motility and the Cytoskeleton, 44(1), 23-33.

[6] Kapinga, M.R.M. and Gordon, R. (1992). [Cell Motility Rhythms in _Bacillaria Paxillifer_](https://www.tandfonline.com/doi/abs/10.1080/0269249X.1992.9705215). _Diatom Research_, 7(2), 221-225.

## Additional References

<p align="center">
  <img width="330" height="261" src="https://user-images.githubusercontent.com/19001437/60072607-a1ee4380-96e3-11e9-9187-77a4c69d8f4a.png"><BR>
</p>
  
[Dr. Thomas Harbich's](https://diatoms.de/en/site-notice) Internet Resource for [Diatoms](https://diatoms.de/en/)
