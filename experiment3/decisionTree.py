
import operator
import numpy as np

name2type = {'Iris-setosa' : 0, 'Iris-versicolor' : 1, 'Iris-virginica': 2}
names = {'Iris-setosa',  'Iris-versicolor', 'Iris-virginica'}
labels = ['Sepal Length','Sepal Width','Petal Length','Petal Width']  #四个特征

#读取数据函数,返回list类型的数据集
def loadData():
    data=[]
    f = open("/iris.data.txt")
    lines = f.readlines()
    for line in lines:
        lineData=line.strip('\n').split(sep = ',')
        tmp=[float(i) for i in lineData[:-1]]
        tmp.append(name2type[lineData[-1]])
        data.append(tmp)
    return data


def calEntropy(dataSet):  # 计算数据的熵(entropy)
    num=len(dataSet)  # 数据条数
    labelCounts={}
    for featureVec in dataSet:
        currentLabel=featureVec[-1] # 每行数据的最后一个字（类别）
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1  # 统计有多少个类以及每个类的数量
    Ent=0
    for key in labelCounts:
        prob=float(labelCounts[key])/num # 计算单个类的熵值
        Ent=Ent-prob*np.log2(prob) # 累加每个类的熵值
    return Ent

def calInfogain(dataSet,point):
    info=[]
    numFeatures = len(dataSet[0])-1
    baseEntropy = calEntropy(dataSet)  # 原始的熵
    for j in range(numFeatures):
        type1 = []
        type2 = []
        featList = [example[j] for example in dataSet]
        for i in range(0,len(featList)):
            if featList[i]<point:
                type1.append(dataSet[i])
            else:
                type2.append(dataSet[i])
        temp1 = len(type1)/len(featList)*calEntropy(type1)
        temp2 = len(type2)/len(featList)*calEntropy(type2)
        infogain = baseEntropy - temp1 - temp2
        info.append(infogain)
    return info

def calBestsplit(dataSet):  #计算最优的分类方式
    maxInfo4=0
    bestValue4=0
    bestFeature = 0
    numFeatures = len(dataSet[0])-1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        bestValue=0
        maxInfo = 0
        for value in uniqueVals:
            info=calInfogain(dataSet, value)
            if(info[i]>maxInfo):
                maxInfo=info[i]
                bestValue=value
        if(maxInfo>maxInfo4):
            maxInfo4=maxInfo
            bestValue4=bestValue
            bestFeature=i
    return bestValue4,bestFeature

def splitDataSet(dataSet,axis,value,flag): # 按某个特征分类后的数据
    retDataSet=[]
    if flag==1:
        for featVec in dataSet:
            if featVec[axis]<value:
                reducedFeatVec =featVec[:axis]
                reducedFeatVec.extend(featVec[axis+1:])
                retDataSet.append(reducedFeatVec)
    if flag==2:
        for featVec in dataSet:
            if featVec[axis]>=value:
                reducedFeatVec =featVec[:axis]
                reducedFeatVec.extend(featVec[axis+1:])
                retDataSet.append(reducedFeatVec)
    return retDataSet #retDataSet 最后返回的是小于或大于等于value值的所有除了label[axis]的特征和label

def majorityCnt(classList):    #按分类后类别数量排序,哪类最多则分类结果是哪类
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def buildTree(dataSet,labels):
    m='a'
    classList = [example[-1] for example in dataSet]  # list是最后一列name：0,1,2 代表三种类型
    if classList.count(classList[0]) == len(classList):  #判断分类后数据类型是否被划分开，
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestVal,bestFeat = calBestsplit(dataSet)  # 选择最优特征
    bestFeatLabel = labels[bestFeat]   #字符
    myTree = {bestFeatLabel: {}}  # 分类结果以字典形式保存
    print(myTree)
    del (labels[bestFeat])   # 删除最优特征
    for flag in range(1,3):
        subLabels = labels[:]    #删除完bestfeature后还剩的特征
        if flag==1:
            m='< %.2f'%(bestVal)
        if flag==2:
            m='>=%.2f'%(bestVal)
        myTree[bestFeatLabel][m] = buildTree(splitDataSet(dataSet, bestFeat, bestVal,flag), subLabels)
    return myTree


if __name__=='__main__':
    dataSet=loadData()  # 创造示列数据
    print(buildTree(dataSet,labels))  # 输出决策树模型结果