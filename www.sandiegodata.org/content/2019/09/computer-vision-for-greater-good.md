---
title: "Computer Vision For Greater Good!"
date: 2019-09-04T10:00:39+00:00
draft: false
categories: ["Current Projects", "News"]
tags: ["homeless"]
author: "eric"
---

Use your Computer Vision skills to tackle homelessness. 

The Data Library is currently running a data project to convert [5 years of monthly homelessness person locations](<http://www.sandiegodata.org/2019/08/downtown-homelessness-dataset-progress/>) from scanned paper maps to a geographic dataset. The bulk of the work involves volunteers manually digitizing 350 scanned paper maps in two jobs, but we have enough data to build a computer vision solution. 

If you have skills, or motivated interest, in programming [OpenCV](<https://opencv.org/>) in Python, you can put your talents to service for humanity, by working on the computer vision portion of this project. 

Read on for a description of the current project work, and what you can use your computer vision skills for. 

## Current Project Work

Here is what one of the maps we are working with looks like: 

![](http://downtown-homelessness.sandiegodata.org/example-map.png)

Each handwritten number is a count of homeless sleepers, and the shape around the number indicates if the sleepers are on the ground, in a tent or structure, or in a vehicle. We are using an annotation tool, [VIA](<http://www.robots.ox.ac.uk/~vgg/software/via/>), to annotate these images for (1) key intersections that serve as ground control points and (2) each of the marks. For full details of this process, [try out one of the Github issues to complete these tasks](<https://github.com/sandiegodata-projects/downtown-partnership/issues/59>).

The results of that manual process is a set of pixel positions for intersections that have known geographic positions, for each map, the open and filled yellow squares on these maps: 

![](https://i0.wp.com/www.sandiegodata.org/uploads/7/2019/09/Screen-Shot-2019-09-03-at-4.43.45-PM.png?fit=1024%2C760&ssl=1)

With an association between the pixel locations for the 4 intersections and the corresponding geographic locations, we create an affine transformation with a linear equation solver to create a mapping from pixels to geographic coordinates, one for each map. Then, when other workers annotate the handwritten sleeper count numbers, we can convert the pixel locations of the handwritten marks to geographic locations, so this annotated image:

![](https://i1.wp.com/www.sandiegodata.org/uploads/7/2019/09/Screen-Shot-2019-09-03-at-4.55.15-PM.png?fit=1024%2C790&ssl=1)

becomes part of a full geographic dataset: 

![](/uploads/7/2019/08/Downtown-Homelessness-1024x652.png)

## Computer Vision Work

We've got a lot of images of maps, so I think we can use CV techniques to automatically recognize and register each of the neighborhoods for future count maps, and, because the dataset has (well, will have) about 10,000 examples of handwritten count marks, we should be able to recognize count marks. Some of the sub projects I've been working on include:

  * Registering and averaging maps, to extract just the base shape of the neighborhood. 
  * Extracting the handwritten marks and using OCR to check that the numbers are correct. 


### Registering And Averaging

Because we have road intersection annotations as ground control points, we can transform every map to the same coordinate system, then average them together to find the lines that are part of the base map. Here is what the processing for the East Village maps looks like. This is all of the maps for the Marina neighborhood transformed to the same coordinate system, and added together. 

![](/uploads/7/2019/09/Screen-Shot-2019-09-03-at-5.05.21-PM.png)

With a bit more processing we can extract lines. Here are the lines for the Marina neighborhood. 

![](https://i2.wp.com/www.sandiegodata.org/uploads/7/2019/09/Screen-Shot-2019-09-03-at-5.09.21-PM.png?fit=1024%2C637&ssl=1)

These lines form a "fingerprint" for the neighborhood. We can use a [feature matcher](<https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html#matcher>) to link these fingerprints to maps, to automatically determine which neighborhood a map is and register is to geographic coordinates. That would eliminate half of the tasks for converting a monthly dataset, since each of the maps could be automatically registered. 

###  Handwriting Recognition. 

Digitizing a maps involves manually drawing a circle around each of the handwritten marks and entering the number for the count in the mark. This produces a very detailed training dataset for recognizing both the handwritten number and the shape drawn around it. 

![](/uploads/7/2019/09/Screen-Shot-2019-09-03-at-5.18.07-PM.png)

There are two sub-projects using this information: 

  * Extract the handwritten marks and present them on a web page, for secondary confirmation that the number and type of sleeper was annotated correctly. 
  * Train an OCR algorithm to automatically recognize these marks. 


By combining these to Computer Vision projects, we should be able to make an automated first pass registering the image to geographic coordinates and recognizing the handwritten marks, converting a laborious manual process to a simpler process of review and correction. 

Can you help? Do you want to demonstrate your CV skills, or practice new skills? If so, please contact the project manager, Eric Busboom at [eric@sandiegodata.org](<mailto:eric@sandiegodata.org>), or 619 889 7571.
