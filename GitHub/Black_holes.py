import numpy as np
import itertools


def checkio(data):
    def distance(bh):
        p1, p2 = np.array(bh[0][:2]), np.array(bh[1][:2])
        d = np.linalg.norm(p1-p2)
        return d

    def s(r):
        return np.pi * r**2

    def intersection(bh):
        lr, sr, d = max(bh[0][2], bh[1][2]), min(bh[0][2], bh[1][2]), distance(bh)
        if sr + d <= lr:
            return 1, s(lr) / s(sr)
        elif d < lr:
            sd, ld = (d**2 - lr**2 + sr**2) / d / 2, (d**2 - sr**2 + lr**2) / d / 2
            sradian, lradian = np.arccos(sd / sr), np.arccos(ld / lr)
            area = sradian/np.pi * s(sr) + lradian/np.pi * s(lr) - d * lr * np.tan(lradian)
            return area / s(sr), s(lr) / s(sr)
        return 0, 0

    def merge(bh):
        sbh, lbh = min(bh, key=lambda x: x[2]), max(bh, key=lambda x: x[2])
        lr = np.sqrt((s(sbh[2]) + s(lbh[2])) / np.pi)
        return sbh, lbh, (lbh[0], lbh[1], lr)

    def form(data):
        return [(x[0], x[1], round(x[2], 2)) for x in data]

    while True:
        if len(data) == 1:
            return form(data)
        begin = len(data)
        combination = itertools.combinations(data, 2)
        pairs = []
        for bh in combination:
            temp = intersection(bh)
            if temp[0] >= 0.55 and temp[1] >= 1.2:
                pairs.append(bh)
        if pairs:
            closestbh = min(pairs, key=distance)
            sbh, lbh, newbh = merge(closestbh)
            data.remove(sbh)
            data[data.index(lbh)] = newbh
        if len(data) == begin:
            return form(data)



if __name__ == "__main__":
    assert checkio([(0, 0, 2.1)]) == [(0, 0, 2.1)]
    assert checkio([(2, 4, 2), (3, 9, 3)]) == [(2, 4, 2), (3, 9, 3)]
    assert checkio([(3, 3, 3), (2, 2, 1), (3, 5, 1.5)]) == [(3, 3, 3.5)]