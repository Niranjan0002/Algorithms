import math
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def closestUtil(Px, Py, n):
    if n <= 3:
        return bruteForce(Px, n)
    mid = n // 2
    midPoint = Px[mid]
    Pyl = Py[:mid]
    Pyr = Py[mid:] 
    dl, closest_pairs_left = closestUtil(Px, Pyl, mid)
    dr, closest_pairs_right = closestUtil(Px[mid:], Pyr, n - mid)
    d = min(dl, dr)
    c_p = closest_pairs_left + closest_pairs_right
    strip = [point for point in Py if abs(point.x - midPoint.x) < d]
    min_dist_strip, closest_pairs_strip = stripClosest(strip, len(strip), d)
    if min_dist_strip < d:
        d = min_dist_strip
        c_p = closest_pairs_strip
    elif min_dist_strip == d:
        c_p += closest_pairs_strip
    return d, c_p

def bruteForce(P, n):
    min_dist = float('inf')
    c_p = set()

    for i in range(n):
        for j in range(i+1, n):
            d = dist(P[i], P[j])
            if d < min_dist:
                min_dist = d
                c_p = {(P[i], P[j])}
            elif d == min_dist:
                c_p.add((P[i], P[j]))

    return min_dist, list(c_p)

def stripClosest(strip, size, d):
    min_dist = d
    c_p = set()
    for i in range(size):
        for j in range(i+1, size):
            if strip[j].y - strip[i].y < min_dist:
                d = dist(strip[i], strip[j])
                if d < min_dist:
                    min_dist = d
                    c_p = {(strip[i], strip[j])}
                elif d == min_dist:
                    c_p.add((strip[i], strip[j]))
    
    return min_dist, list(c_p)

def closest(P, n):
    Px = sorted(P, key=lambda point: point.x)
    Py = sorted(P, key=lambda point: point.y)
    min_dist, c_p = closestUtil(Px, Py, n)
    return min_dist, c_p


P = [point(1, 2), point(3, 5), point(6, 9), point(8, 12), point(10, 15)]
n = len(P)
    

min_distance, c_p = closest(P, n)

if c_p:
    print(f"The smallest distance is {min_distance}")
    print("The closest pairs of points are:")
    p_p = set()
    for pair in c_p:
        sorted_pair = (pair[0], pair[1]) if pair[0].x <= pair[1].x else (pair[1], pair[0])
        if sorted_pair not in p_p:
            print(f"({pair[0].x}, {pair[0].y}) and ({pair[1].x}, {pair[1].y})")
            p_p.add(sorted_pair)
