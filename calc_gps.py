import geopy
import geopy.distance

from math import tan ,atan,radians ,degrees,sqrt, pow


class gps(object):
    fov_x=56.71524
    fov_y=44.35683
    size_x=640
    size_y=480

    def compute_gps(self,px, py, bear, alti, cent_lat, cent_lon,frame_shape):

        height,width,depth=frame_shape
        gps.size_x=width
        gps.size_y=height
        x_dist_per_pixle = 2 *alti* tan(radians(gps.fov_x / 2)) / gps.size_x
        y_dist_per_pixle = 2 *alti* tan(radians(gps.fov_y / 2)) / gps.size_y
        x = float((px - (gps.size_x / 2)))
        y = float((py - (gps.size_y / 2)))

        theta = atan(x / y)
        theta = degrees(theta)
        newbear=bear
        if (y < 0):
            newbear = bear - theta

        if (y > 0):
            newbear = bear + 180 - theta

        # bearing has to be between 0 and 360
        if (newbear > 360):
            newbear -= 360
        if (newbear < 0):
            newbear += 360
        #comment next line for onboard code
        #newbear=bear

        x *= x_dist_per_pixle
        y *= y_dist_per_pixle
        dist = sqrt(pow(x, 2) + pow(y, 2))
        dist /= 1000

        pt = geopy.Point(cent_lat,cent_lon)
        obj = geopy.distance.VincentyDistance(kilometers=dist)
        target_li = list(obj.destination(point=pt, bearing=newbear))

        return target_li[0],target_li[1]

    def __init__(self):
        pass
        


if __name__ == "__main__":
    #obj = gps(4800,2555,48.8,20.5,28.75119395,77.11790875,(5312,2800))
    #obj.algo()
    pass
