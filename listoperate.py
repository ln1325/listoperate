# 自定义一堆垃圾函数做题外挂，实现对一组数据的求和、求乘积、求平均数、求方差、求加权平均数（未定）、同时加/减一个数

# 亲测真实有效 listpresum()
def listpresum(domlist,n):
    """对指定列表的前n项求和（其实这个还不如直接用sum()来求和）"""
    try:
        listlength = len(domlist)
        presum = 0
        if n < listlength:
            for x in domlist[0:n]:
                presum += x
            return presum
        if n == listlength:
            for x in domlist[:]:
                presum += x
            return presum
        if n > listlength:
            return 0
    except ValueError:
        return 0

# 亲测真实有效 listpreeq()
def listpreeq(domlist,n):
    """对指定列表的前n项求乘积"""
    try:
        listlength = len(domlist)
        preeq = 1
        if n < listlength:
            for x in domlist[0:n]:
                preeq *= x
            return preeq
        if n == listlength:
            for x in domlist[:]:
                preeq *= x
            return preeq
        if n > listlength:
            return 0
    except ValueError:
        return 0

# 亲测真实有效 listpreav()
def listpreav(domlist,n):
    """对指定列表的前n项求平均值"""
    try:
        listlength = len(domlist)
        listsum = 0
        if n < listlength:
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
def listpres(domlist,n):
    """对指定列表的前n项求方差（默认求整个列表的方差）"""
    try:
        listlength = len(domlist)
        listsum , listav , carry , temp , pres = 0 , 0 , 0 , 0 , 0
        if n < listlength:
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
def listprepup(domlist,n,number):
    """对指定列表的前n项加一常数，这会对列表永久性修改"""
    try:
        listlength = len(domlist)
        index = 0
        if n < listlength:
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
def listpreequp(domlist,n,number):
    """对指定列表的前n项乘以一常数实现翻倍效果，这会对列表永久性修改"""
    try:
        listlength = len(domlist)
        index = 0
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
    """对指定列表的前n项求第p百分位数，不提供p则默认求中位数（第50百分位数）"""
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
            """
            if i%ii!=0:
                i = round(i)
                k = i-1
                prepnum = temp(k)
                return prepnum
            """
                i为整数时，temp的第i项temp[j]与第i+1项temp[i]的平均数就是原列表前n项的第p百分位数,
                最终结果使用者请自行保留所需小数位数
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
            """i不为整数时对i四舍五入取整，domlist的第i项就是第p百分位数"""
            if i%ii!=0:
                i = round(i)
                k = i-1
                prepnum = domlist[k]
                return prepnum
            """
                i为整数时，domlist的第i项domlist[j]与第i+1项domlist[i]的平均数就是原列表的第p百分位数,
                最终结果使用者请自行保留所需小数位数
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

def listprepowav(domlist,n,powerlist):
    """对列表前n项按权重求加权平均数，若求整个操作列表的加权平均数则要求操作列表与权重列表长度相同"""
    try:
        chk = sum(powerlist)
        listlength = len(domlist)
        powerlistlength = len(powerlist)
        if n < listlength:
            """加权平均数：初中最直接的计算方法，每个数乘以对应的权重后求和"""
            if chk == 1:
                for i in range(n):
                    a=domlist[i]
                    b=powerlist[i]
                    prepowav+=(a*b)
                return prepowav
            if chk == 100:
                for i in range(n):
                    a=domlist[i]
                    b=powerlist[i]
                    c+=a*b
                prepowav=c/100
                return prepowav
            if (chk > 1) or (chk > 100):
                return 0
        if (n==listlength):
            """
            加权平均数：权重归一化（求一整个列表的加权平均数原始权重之和不是1的情况下使用）
            计算整个列表的加权平均数，第一个if是对 原始权重之和不为1的情况 对应的处理（共两个if分支）
            """
            if (chk != 1)or(chk != 100):
                temp = []
	          	# 归一化（第一个for循环就是归一化过程）后的权重分别与domlist的每一项相乘后求和
                for x in range(n):
                    y = powerlist[x]/chk
                    temp.append(y)
                for j in range(n):
                    a=domlist[j]
                    b=temp[j]
                    prepowav+=a*b
                return prepowav
                # 以上11行未完工，因为归一化之后的计算过程我还不知道
            if (chk == 1):
                for i in range(n):
                    prepowav += (domlist[i]*powerlist[i])/chk
                return prepowav
            if chk == 100:
                for i in range(n):
                    prepowav += (domlist[i]*powerlist[i])/100
                return prepowav
        if n > listlength:
            return 0
    except ValueError:
        return 0
    except IndexError:
        return 0

def emptylist(length,fillwith=None):
    """创建空列表，fillwith可以指定给列表统一填充的值(未定）"""
    temp = []
    if fillwith != None:
        for i in range(length):
            temp.append(fillwith)
    if fillwith == None:
        for i in range(length):
            temp.append('')
    return temp

# 亲测真实有效：listidxget()
def listidxget(domlist,obj,sortkey=None):
    """
    查找指定元素在指定列表中的位置（索引）
    可选第三参数sortkey指定升序或降序排序情况下指定元素在指定列表中的位置
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
    """
    temp =[1,1]
    a,b=1,1
    m=n-3
    if n==0:
        return 0
        """以下的三个if分支为防痴呆代码。。。"""
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
        """以下的三个if分支为防痴呆代码。。。"""
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
        """以下的三个if分支为防痴呆代码。。。"""
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
        """以下的三个if分支为防痴呆代码。。。"""
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
        """以下的三个if分支为防痴呆代码。。。"""
        if (listreq==False)and(start!=0):
            return 0
        if (listreq==False)and(endup!=-1):
            return 0
        if (listreq==False)and(start!=0)and(endup!=-1):
            return 0

def listobjcount(domlist,n,obj):
    """计算列表中前n项的某个元素出现次数"""
    listlength=len(domlist)
    searchobj=obj
    turns=0
    if n < listlength:
        prenlist=domlist[0:n]
        if obj in prenlist:
            for ob in prelist:
                if ob==searchobj:
                    turns+=1
            return turns
        if obj not in prenlist:
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
    当 kickout=True ,即要求剔除指定元素时，返回剔除所有该元素的列表
    """
    turns = 0
    if obj in domlist:
        if kickout:
            temp = domlist[:]
            for x in temp:
                if x == obj:
                    temp.remove(x)
            # 二次检查
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