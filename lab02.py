dataArray = [-110,-503,15,-7,11,13,17,-19,2,29,31,37,41,4,-3,10]

def bg(i,r):
    if dataArray[i] >= dataArray[r] and r >= 0:
        # print(dataArray[i] ,">=",dataArray[r])เช็คค่า
        return bg(i,r-1)
    elif dataArray[i] < dataArray[r] and r >= 0:
        return bg(r,r-1)
    return dataArray[i]      
print("the biggest number is :",bg(len(dataArray)-1,len(dataArray)-2))

def summ(i,r):
    if i < len(dataArray):

        if dataArray[i] >= 0   :
            return summ(i+1,r)
        elif dataArray[i] < 0   :
            r+=dataArray[i]
            return summ (i+1,r)
        
    print("the sum is negative is",r)
summ(0,0)     