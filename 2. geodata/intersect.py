import shapefile
# documentation: https://github.com/GeospatialPython/pyshp

from shapely.geometry import Polygon
# documentation: http://toblerity.org/shapely/manual.html



## Load data
    # read data.shp from the data/ directory
    # HINT: use shapefile's Reader function



## Create Python data structures
    # put all features from data/data.shp in a Python list

    # extract the main feature you'll be checking for intersections
    # HINT: which list function removes an item from a list while returning it to you?



## Calculate areas and perimeter
    # calculate the main feature's area and perimeter using Shapely
    # HINT: create a Shapely Polygon and call its area and length parameters (i.e. use .area)
    # HINT: what input does the Shapely's Polygon object require?

    # print the feature's id
    # HINT: look it up in the attribute table through shapefile.Reader.records()



## Check for intersections
    # Use Shapely's intersection function to check
    # whether your main feature intersects any of the other features.
    # HINT: use the Shapely is_empty function to check whether an
    # intersection between two geometries exists

    # Store each intersection in a list
intersections = []



## Save the intersections to a file
# add the intersections to data.shp and store them as polygons.shp
e = shapefile.Editor(shapefile="data/data.shp")

for intersection in intersections:

    # create a new shapefile polygon using the shapefile.Editor.poly function

    # HINT: you'll need to convert the intersection's Shapely geometry into
    # a format that fits into the shapefile.Editor.poly function
    # NOTE: Shapely Polygon geometries are made of interior and exterior rings

    # Populate the attribute table
    e.record("", "intersect", intersection.area)

    # print the intersection's area and compare it to Simeon's values


# write the changes to data/data.shp to a new file
e.save("data/polygons.shp")
