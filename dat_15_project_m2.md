SF_DAT_15 Course Project

San Francisco Cycling Safety -- Michael Phillips


Cycling is an increasingly popular sport and mode of transit in America; and particularly in dense cities that don’t require car ownership, it can be the fastest and most cost effective means of travel to work and many other destinations. In part because of the recent increase in cycling popularity, there has been a staggering increase in the percentage of all injury causing collisions that bicycles are involved in, while the total injury volume across all vehicle collisions has remained comparatively flat (http://j.mp/1If0zJ2):

```
Year, Total Injuries, Bicycle %
2000, 4182, 9
2001, 3917, 10
2002, 3777, 9
2003, 3511, 10
2004, 3038, 10
2005, 3227, 12
2006, 2869, 11
2007, 3021, 15
2008, 3010, 16
2009, 2877, 18
2010, 3081, 19
2011, 3111, 21
```

San Francisco is beginning to take steps towards making the city a more bike friendly place, but so far, many of these efforts have been controversially focused on cracking down on cyclists that violate traffic laws (http://j.mp/1If0Ifw).

In contrast, significant attention has been given to studying particular areas where motor vehicle collisions occur, and that has greatly impacted how the city plans construction and times traffic lights (http://j.mp/1If0zJ2).

In this project, I am analyzing reports of cycling injuries throughout the city, along with location data, in order to plot the most dangerous locations and routes. I’ll also look at Bay Area Bike Share data (http://j.mp/1KlQ62j) in order to examine the most heavily traveled areas, and then weigh the safety ratings based on popularity. Furthermore, the Bike Share data include weather information, which can be used to determine whether any outliers could be attributable to particularly bad environmental circumstances.


Sample JSON location data:

```
 {     
"lat":37.7724134,
"severity":"u'INJURY",
"street1":"11th St",
"street2":"Market",
"image_id":1,
"year":"2012",
"date":"u'20120419",
"lng":-122.4147158
},
```


I’ve also already analyzed general SFPD incident data and plotted location, and I plan to extend and apply that project to this specific topic.

