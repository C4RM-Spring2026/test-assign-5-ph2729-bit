import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    y /= ppy
    couponRate /= ppy
    m = int(m * ppy)
    cf = face * couponRate
    t = np.arange(1, m + 1)
    discount = (1 + y) ** (-t)
    
    pvcf = cf * discount
    pvcf[-1] += face * discount[-1]
    pvcfsum = pvcf.sum()
    
    duration = (t * pvcf).sum() / pvcfsum
    
    duration /= ppy
    return duration


