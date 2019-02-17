def sumintervals(intervals):
 number=[]
 for interval in intervals:
    
    l=len(interval)
    for j in range(interval[0],interval[l-1]):
        number.append(int(j))
 print (len(set(number)))

intervals = [[1,5], [10, 20], [1, 6], [16, 19], [5, 11]]
sumintervals(intervals)
