#encoding='utf-8'
import jieba as jb

def loadStopWords(fileName):
    dataMat = []
    fr = open(fileName,'r',encoding= 'utf-8')
    words   = fr.read()
    print(words)
    result = jb.cut(words,cut_all= True)
    newWords = []
    for s in result:
        if s not in newWords:
            newWords.append(s)
    #newWords.extend([u'(',u')',u'（',u'）',u'{',u'}'])
    print(newWords)
    frw = open('writeName.txt','w',encoding='utf-8')
    for line in newWords :
        frw.write(line + '\n')
    frw.write('\n')
    return newWords

def wordsCut(words,stopWordFile):
    result = jb.cut(words)
    newWords = []
    stopWords = loadStopWords(stopWordFile)
    for s in result:
        if s not in stopWords:
            newWords.append(s)
    print (newWords)
    return newWords


# 把样本文件做分词处理，并写文件
def fileCut(fileName, writeFile, stopWordsFile):
    dataMat = []
    fr = open(fileName)
    frW = open(writeFile, 'w')
    for line in fr.readlines():
        curLine = line.strip()
        curLine1 = curLine.upper()  # 把字符串中的英文字母转换成大写
        cutWords = wordsCut(curLine1, stopWordsFile)
        for i in range(len(cutWords)):
            frW.write(cutWords[i])
            frW.write('\t')
        frW.write('\n')
        dataMat.append(cutWords)
    frW.close()



def main():
    loadStopWords('all_log.txt')


if __name__ == "__main__":
    main()