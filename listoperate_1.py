# 自定义一堆垃圾函数做题外挂，实现对一组数据的求和、求乘积、求平均数、求方差、求加权平均数（未定）、同时加/减一个数
# A collection of custom helper functions for summing, multiplying, averaging, finding variance and weighted averages (planned), and adding/subtracting a number from a dataset.

# 亲测真实有效 listpresum()
# Verified to work in practice: listpresum()
def listpresum(domlist,n):
    """对指定列表的前（后）n项求和
    Sum the first (or last) n items of the specified list."""
    try:
        listlength = len(domlist)
        if n < 0:
            return sum(domlist[n - 1:])
        elif n == 0:
            return 0
        elif n == listlength:
            return sum(domlist)
        else:
            return sum(domlist[0:n])
    except ValueError:
        return 0

# 亲测真实有效 listpreeq()
# Verified to work in practice: listpreeq()
def listpreeq(domlist,n):
    """对指定列表的前（后）n项求乘积
    Multiply the first (or last) n items of the specified list."""
    try:
        listlength = len(domlist)
        preeq = 1
        if n < 0:
            for x in domlist[n:]:
                preeq *= x
        if n < listlength and n > 0:
            for x in domlist[0:n]:
                preeq *= x
        if n == listlength:
            for x in domlist[:]:
                preeq *= x
        if n > listlength:
            raise IndexError
        return preeq
    except ValueError:
        return 0

# 亲测真实有效 listpreav()
# Verified to work in practice: listpreav()
def listpreav(domlist,n):
    """对指定列表的前（后）n项求平均值
    Calculate the average of the first (or last) n items of the specified list."""
    try:
        listlength = len(domlist)
        listsum = 0
        if n < 0:
            for x in domlist[n:]:
                listsum += x
            preav = listsum/n
            preav = round(preav,3)
            return preav
        if n < listlength and n > 0:
            for x in domlist[0:n]:
                listsum += x
            preav = listsum/n
            preav = round(preav,3)
            return preav
        if n == listlength:
            for x in domlist[:]:
                listsum += x
            preav = listsum/n
            preav = round(preav,3)
            return preav
        if n > listlength:
            return 0
    except ValueError:
        return 0

# 亲测真实有效 listpres()
# Verified to work in practice: listpres()
def listpres(domlist,n):
    """对指定列表的前n项求方差（默认求整个列表的方差）
    Calculate the variance of the first n items (the whole list by default)."""
    try:
        listlength = len(domlist)
        listsum , listav , carry , temp , pres = 0 , 0 , 0 , 0 , 0
        if n < 0:
            for x in domlist[n:]:
                listsum += x
            listav = listsum/n
            for y in domlist[-n:]:
                carry = (y-listav)**2
                temp += carry
            pres = temp/n
            pres = round(pres,3)
            return pres
        if n < listlength and n > 0:
            for x in domlist[0:n]:
                listsum += x
            listav = listsum/n
            for y in domlist[0:n]:
                carry = (y-listav)**2
                temp += carry
            pres = temp/n
            pres = round(pres,3)
            return pres
        if n == listlength:
            for x in domlist[:]:
                listsum += x
            listav = listsum/n
            for y in domlist[:]:
                carry = (y-listav)**2
                temp += carry
            pres = temp/n
            pres = round(pres,3)
            return pres
        if n > listlength:
            return 0
    except ValueError:
        return 0

# 亲测真实有效 listprepup()
# Verified to work in practice: listprepup()
def listprepup(domlist,n,number):
    """对指定列表的前（后）n项加一常数，这会对列表永久性修改
    Add a constant to the first (or last) n items of the specified list; this permanently modifies the list."""
    try:
        listlength = len(domlist)
        index = 0
        if n < 0:
            index = -1
            for i in range(-n):
                domlist[index] = domlist[index]+number
                index -= 1
        if n < listlength and n > 0:
            for i in range(n):
                domlist[index] = domlist[index]+number
                index += 1
            return domlist
        if n == listlength:
            for i in range(n):
                domlist[index] = domlist[index]+number
                index += 1
            return domlist
        if n > listlength:
            return 0
    except ValueError:
        return 0

# 亲测真实有效 listpreequp()
# Verified to work in practice: listpreequp()
def listpreequp(domlist,n,number):
    """对指定列表的前n项乘以一常数实现翻倍效果，这会对列表永久性修改
    Multiply the first n items of the specified list by a constant; this permanently modifies the list."""
    try:
        listlength = len(domlist)
        index = 0
        if n < 0:
            index = -1
            for i in range(-n):
                domlist[index] = domlist[index]*number
                index -= 1
            return domlist
        if n < listlength:
            for i in range(n):
                domlist[index] = domlist[index]*number
                index += 1
            return domlist
        if n == listlength:
            for i in range(listlength):
                domlist[index] = domlist[index]*number
                index += 1
            return domlist
        if n > listlength:
            return 0
    except ValueError:
        return 0

def listprepnum(domlist,n,p=50):
    """对指定列表的前n项求第p百分位数，不提供p则默认求中位数（第50百分位数）
    Find the pth percentile of the first n items; if p is omitted, find the median (the 50th percentile)."""
    try:
        listlength = len(domlist)
        if n < listlength:
            temp = []
            for x in domlist[0:n]:
                temp.append(x)
            temp.sort()
            i = n*(p/100)
            ii = int(i)
            """
                i不为整数时对i四舍五入取整，temp的第i项就是原列表前n项的第p百分位数
                If i is not an integer, round it to the nearest integer; the i-th item in temp is then the pth percentile of the first n items in the original list.
            """
            if i%ii!=0:
                i = round(i)
                k = i-1
                prepnum = temp(k)
                return prepnum
            """
                i为整数时，temp的第i项temp[j]与第i+1项temp[i]的平均数就是原列表前n项的第p百分位数,
                最终结果使用者请自行保留所需小数位数
                If i is an integer, the pth percentile of the first n items in the original list is the average of the i-th item temp[j] and the (i+1)-th item temp[i].
                The caller should round the result to the desired number of decimal places.
            """
            if i%ii==0:
                j = i-1
                a = temp[j]
                b = temp[i]
                prepnum = (a+b)/2
                return prepnum
        if n == listlength:
            domlist.sort()
            i = n*(p/100)
            ii = int(i)
            """i不为整数时对i四舍五入取整，domlist的第i项就是第p百分位数
            If i is not an integer, round it to the nearest integer; the i-th item in domlist is the pth percentile."""
            if i%ii!=0:
                i = round(i)
                k = i-1
                prepnum = domlist[k]
                return prepnum
            """
                i为整数时，domlist的第i项domlist[j]与第i+1项domlist[i]的平均数就是原列表的第p百分位数,
                最终结果使用者请自行保留所需小数位数
                If i is an integer, the pth percentile of the original list is the average of the i-th item domlist[j] and the (i+1)-th item domlist[i].
                The caller should round the result to the desired number of decimal places.
            """
            if i%ii==0:
                j = i-1
                a = domlist[j]
                b = domlist[i]
                prepnum = (a+b)/2
                return prepnum
            if n > listlength:
                return 0
    except ValueError:
        return 0

# 验证过有效，未实测
# Verified to work, but not yet tested.
def listprepowav(domlist,n,powerlist):
    """计算列表前 n 项的加权平均数。
    Calculate the weighted average of the first n items in the list.

    ``powerlist`` 中的权重可以是小数（例如 ``0.2``）或百分数
    （例如 ``20``），函数会自动按实际权重总和进行归一化。
    Weights in ``powerlist`` can be decimals (for example, ``0.2``) or percentages
    (for example, ``20``); the function automatically normalizes by the sum of the weights.
    当 n 等于列表长度时，权重列表也必须与数据列表等长。
    When n equals the list length, the weight list must have the same length as the data list.
    """
    try:
        if isinstance(n,int):
            # n是bool类型时，返回0，因为 bool类型在Python中是int的子类，True和False分别对应1和0，这可能会导致意外的计算结果。
            # Return 0 when n is a bool: bool is a subclass of int in Python, with True and False corresponding to 1 and 0, which could cause unintended results.
            if isinstance(n,bool):
                return 0
            if n < 0:
                listprepowav(domlist,-n,powerlist)
            listlength = len(domlist)
            if n <= 0 or n > listlength:
                return 0
            powerlistlength = len(powerlist)
            if powerlistlength < n:
                return 0
            if n == listlength and powerlistlength != listlength:
                return 0
            values = domlist[:n]
            weights = powerlist[:n]
            weight_sum = sum(weights)
            if weight_sum == 0:
                return 0
            return sum(value * weight for value, weight in zip(values, weights)) / weight_sum
        else:
            return 0
    except ValueError:
        return 0
    except IndexError:
        return 0
    except TypeError:
        return 0
    except ZeroDivisionError:
        return 0

def emptylist(length,fillwith=None):
    """创建空列表，fillwith可以指定给列表统一填充的值(未定）
    Create a list of the specified length; fillwith optionally sets the value used to fill it (not finalized)."""
    temp = []
    if fillwith != None:
        for i in range(length):
            temp.append(fillwith)
    if fillwith == None:
        for i in range(length):
            temp.append('')
    return temp

# 亲测真实有效：listidxget()
# Verified to work in practice: listidxget()
def listidxget(domlist,obj,sortkey=None):
    """
    查找指定元素在指定列表中的位置（索引）
    Find the position (index) of a specified element in a specified list.
    可选第三参数sortkey指定升序或降序排序情况下指定元素在指定列表中的位置
    The optional third parameter, sortkey, specifies the element's position when the list is sorted in ascending or descending order.
    """
    temp = domlist[:]
    turns = 0
    idx = []
    if obj in temp:
        if sortkey==None:
            for x in temp:
                if x == obj:
                    idx.append(turns)
                else:
                    turns += 1
            length = len(idx)
            if length == 1:
                index = idx[0]
            if length != 1:
                return idx
        if sortkey:
            temp.sort(reverse=True)
            for x in temp:
                if x == obj:
                    idx.append(turns)
                else:
                    turns += 1
            if len(idx) == 1:
                index = idx[0]
                return index
            if len(idx) != 1:
                return idx
        if not sortkey:
            temp.sort(reverse=False)
            for x in temp:
                if x == obj:
                    idx.append(turns)
                else:
                    turns += 1
            if len(idx) == 1:
                index=idx[0]
                return index
            else:
                return idx

def fibarrlist(n,listreq=False,start=0,endup=-1):
    """
    求斐波那契数列第n项，若listreq为True时为求斐波那契数列的前n项，
    此时返回值为前n项组成的列表，在此情况下才能使用参数start和endup参数
    Return the nth Fibonacci number. If listreq is True, return a list of the first n Fibonacci numbers;
    only in this case can the start and endup parameters be used.
    """
    temp =[1,1]
    a,b=1,1
    m=n-3
    if n==0:
        return 0
        """以下的三个if分支为防痴呆代码。。。
        The following three if branches are defensive checks against invalid parameter combinations."""
        if (listreq==False)and(start!=0):
            return 0
        if (listreq==False)and(endup!=-1):
            return 0
        if (listreq==False)and(start!=0)and(endup!=-1):
            return 0
    if n==1:
        if listreq==False:
            return a
        if listreq==True:
            temp.pop()
            return temp
        """以下的三个if分支为防痴呆代码。。。
        The following three if branches are defensive checks against invalid parameter combinations."""
        if ((listreq==False)and(start!=0)):
            return 0
        if ((listreq==False)and(endup!=-1)):
            return 0
        if ((listreq==False)and(start!=0)and(endup!=-1)):
            return 0
    if n==2:
        if listreq==False:
            return b
        if listreq==True:
            return temp
        """以下的三个if分支为防痴呆代码。。。
        The following three if branches are defensive checks against invalid parameter combinations."""
        if ((listreq==False)and(start!=0)):
            return 0
        if ((listreq==False)and(endup!=-1)):
            return 0
        if ((listreq==False)and(start!=0)and(endup!=-1)):
            return 0
    if n==3:
        if listreq==False:
            c=a+b
            return c
        if listreq==True:
            c=a+b
            temp.append(c)
            return temp
        """以下的三个if分支为防痴呆代码。。。
        The following three if branches are defensive checks against invalid parameter combinations."""
        if ((listreq==False)and(start!=0)):
            return 0
        if ((listreq==False)and(endup!=-1)):
            return 0
        if ((listreq==False)and(start!=0)and(endup!=-1)):
            return 0
    else:
        if not listreq:
            for i in range(m):
                a=a+b
                b=b+a
            if m%2!=0:
                return a
            if m%2==0:
                return b
        if listreq:
            for i in range(m):
                a=a+b
                temp.append(a)
                b=b+a
                temp.append(b)
            if m%2!=0:
                temp.pop(-1)
                return temp[start:endup]
            if m%2==0:
                return temp[start:endup]
        """以下的三个if分支为防痴呆代码。。。
        The following three if branches are defensive checks against invalid parameter combinations."""
        if (listreq==False)and(start!=0):
            return 0
        if (listreq==False)and(endup!=-1):
            return 0
        if (listreq==False)and(start!=0)and(endup!=-1):
            return 0

def listobjcount(domlist,n,obj):
    """计算列表中前n项的某个元素出现次数
    Count how many times a specified element appears in the first n items of the list."""
    listlength=len(domlist)
    searchobj=obj
    turns=0
    if n < listlength:
        prelist=domlist[0:n]
        if obj in prelist:
            for ob in prelist:
                if ob==searchobj:
                    turns+=1
            return turns
        if obj not in prelist:
            return 0
    if n == listlength:
        if obj in domlist:
            for ob in domlist:
                if ob==searchobj:
                    turns+=1
            return turns
        if obj not in domlist:
            return 0
    if n > listlength:
        return 0

def listobjcatch(domlist,obj,kickout=False):
    """
    当 kickout=False ，即不要求剔除指定元素时，返回元素在列表中出现次数。
    When kickout=False, return the number of times the specified element appears in the list.
    当 kickout=True ,即要求剔除指定元素时，返回剔除所有该元素的列表
    When kickout=True, return a list with all occurrences of the specified element removed.
    """
    turns = 0
    if obj in domlist:
        if kickout:
            temp = domlist[:]
            for x in temp:
                if x == obj:
                    temp.remove(x)
            # 二次检查
            # Perform a second check.
            for y in temp:
                if y == obj:
                    temp.remove(y)
            return temp
        if not kickout:
            for x in domlist:
                if x == obj:
                    turns += 1
            return turns
    if obj not in domlist:
        return 0