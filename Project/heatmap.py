# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 21:09:34 2015

@author: michaelphillips
"""
import pandas as pd
import heatmap
import random

accidents = pd.read_csv('https://raw.githubusercontent.com/michaelphillipsx/SF_DAT_15_WORK/master/Project/SFDAT15_Project.csv')
accidents.info()
accidents.head()

accidents.coord = accidents.coord.str.replace(';',',')
accidents.head()


hm = heatmap.Heatmap()
pts = [accidents.coord]
img = hm.heatmap(pts, scheme='classic')
img.save("SFbikes.png")
img.saveKML("SFbikes.kml")
