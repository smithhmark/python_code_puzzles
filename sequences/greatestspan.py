
def simplest(vals):
    sz = len(vals)
    longest_so_far = 0
    for ii, left in enumerate(vals):
        for jj in range(sz-1, ii, -1):
            right = vals[jj]
            if right > left:
                if jj - ii > longest_so_far:
                    longest_so_far = jj - ii
    return longest_so_far

def linear(vals):
    sz = len(vals)
    smallestToLeft = [0] * sz
    largestToRight = [0] * sz

    smallestToLeft[0] = vals[0]
    for ii in range(1, sz):
        if vals[ii] < smallestToLeft[ii-1]:
            smallestToLeft[ii] = vals[ii]
        else:
            smallestToLeft[ii] = smallestToLeft[ii-1]
    #print("smallestToLeft:", smallestToLeft)
    largestToRight[-1] = vals[-1]
    for ii in range(sz-2,-1,-1):
        if vals[ii] > largestToRight[ii+1]:
            largestToRight[ii] = vals[ii]
        else:
            largestToRight[ii] = largestToRight[ii+1]
            #print("  largestToRight:", largestToRight)
    #print("largestToRight:", largestToRight)

    #tricky_val = [5,10,0,1,2,3,4]
    leftidx, rightidx = 0, 0
    max = -1
    while (leftidx < sz and rightidx < sz):
        smallestValSoFar = smallestToLeft[leftidx]
        biggestValToCome = largestToRight[rightidx]
        if smallestValSoFar < biggestValToCome:
            # it's safe to look for a further peak
            span = rightidx - leftidx
            if span > max:
                max = span
            rightidx += 1
        else:
            # looking for an even smaller left value
            leftidx += 1
    return max
