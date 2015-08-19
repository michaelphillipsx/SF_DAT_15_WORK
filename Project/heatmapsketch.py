# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 21:09:34 2015
@author: michaelphillips
"""

import heatmap
import random

if __name__ == "__main__":    
    pts = []
    for x in range(50):
        pts.append((random.uniform(37.7833,37.7832), random.uniform(122.4167,122.4166) ))

    print "Processing %d points..." % len(pts)

    hm = heatmap.Heatmap()
    img = hm.heatmap(pts)
    img.save("classic.png")
    
    
    hm = heatmap.Heatmap()
    hm.heatmap(pts, scheme='classic').save("classictest.png")
    
    
    
