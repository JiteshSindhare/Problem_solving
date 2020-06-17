class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import math
        dist_to_point = {}
        extra_points = {}
        distances = []
        for i in range(len(points)):
            x, y = points[i]
            dist = ((x - 0) ** 2) + ((y - 0) ** 2)
            if dist in dist_to_point.keys():
                tem = []
                temp = dist_to_point[dist]
                tem.append(temp)
                tem.append(points[i])
                dist_to_point[dist] = tem
                extra_points[dist] = True
            else:
                dist_to_point[dist] = points[i]
                extra_points[dist] = False
            distances.append(dist)

        distances = sorted(distances)
        j = 0
        res = []
        for z in range(len(distances)):
            if j < K:
                if extra_points[distances[z]]:
                    # len(dist_to_point[distances[z]])>1
                    for m in range(len(dist_to_point[distances[z]])):
                        if j < K:
                            res.append(dist_to_point[distances[z]][m])
                            j += 1
                else:
                    res.append(dist_to_point[distances[z]])
                    j += 1

        return res
