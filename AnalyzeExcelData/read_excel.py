#"encoding:utf-8"
import xlrd
import xlwt
import nltk

def open_excel(file ='log.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e)


def read_excel(file='file.xls',by_index = 0):

    data = open_excel(file)
    print('sheet_name:',data.sheet_names())
    #tab = data.sheets()
    tab1 = data.sheet_by_name("Sheet1")   #get name
    print('sheet_1:',tab1)
    # tab2 = data.sheet_by_name("Sheet2")
    # print('sheet_2:',tab2)
    # tab3 = data.sheet_by_name("Sheet3")
    # print('sheet_3:',tab3)
    value_i = []
    value1 = []
    #stemmer = PorterStemmer()
    print('value2 type:',type(value_i))
    nrow = tab1.nrows       #获取行数
    ncol = tab1.ncols       #获取列数
    print('Sheet1  row: %d , col: %d'%(nrow,ncol))
    for x in range(0, nrow):
        for y in range(0, ncol):
            # value_i = tab1.cell(x,y).value.split('] ')  #第一种分词方法
            #value_i = sent_tokenize(tab1.cell(x,y).value)  #第二种分词方法 分出的结果很粗糙
            #value_i = word_tokenize(tab1.cell(x, y).value)  #第三种分词方法 分出的结果太细
            #value_i = stemmer.stem(tab1.cell(x, y).value)  # 第四种分词方法 词干提取法 会把每一个log当作一个List
            value_i = tab1.cell(x, y).value.split('] ',7)  #把所有信息读入list
            value1.append(value_i) #
    print('value1:',type (value1) )
    print('the length of value1: ',len(value1))
    print('type & legth : ',type(value1),len(value1))
    return value1

def write_2_excel(value):            #把信息写入Excel
    excel_log = xlwt.Workbook(encoding= 'utf-8')
    sheet1 = excel_log.add_sheet(u'Sheet1',cell_overwrite_ok= True)
    cater = ['1','2','3','4','5','6','7','8','9']   #表头
    for x in range(0,len(cater)):
        sheet1.write(0,x,cater[x])

    for y in range(0,len(value)):
        num = 0
        for z in range(0,len(value[y])):
            if not z == len(value[y])-1:
                sheet1.write(y+1 ,num,value[y][z]+']')        #简单数据处理
            else:
                sheet1.write(y + 1, num, '    [' + value[y][z] + ']')
            num += 1
    excel_log.save('write_2_log.xls')


def extract_data(file='file.xls'):    #分析数据 形成表格

    excel_file = open_excel(file)
    tab = excel_file.sheet_by_name(u'Sheet1')
    nrow = tab.nrows
    ncol = tab.ncols
    print('Extract Tab row: %d, col: %d'%(nrow,ncol))
    #row3 = tab.row_value(3)
    excel_extractor = xlwt.Workbook (encoding= 'utf-8')    #创建excel
    sheet1 = excel_extractor.add_sheet(u'Sheet1',cell_overwrite_ok= True)

    cater = [ 'TID','应用系统', '项目名', '主机地址', '环境','跟踪码','异常内容','内容长度']  #表头
    for x in range(0, len(cater)):
        sheet1.write(0, x, cater[x])

    col = []
    for i in range(1,9):
        col.append(tab.col_values(i))  #读取列表中的数据

    for i in range(len(col)):    #统计出现的词频和类别
        print("The freq of Ld ist%d is："%(i+3))
        k = 0
        freq = nltk .FreqDist (col[i][1:])
        for key,val in freq.items():
            k += 1
            sheet1.write(k, i, (str(key) + ':' + str(val)))
            print (str(key) + ':' + str(val))

    excel_extractor.save('write_2_extractor.xls')

# def Fix_data(file='file.xls',by_index = 0): #把原始数据中的中文数据转换为英文数据
#     excel_file = open_excel(file)
#     tab = excel_file.sheet_by_name('Sheet1')
#     data_col = tab.row_values(by_index)
#     print("data type: ",type(data_col))
#     num = 0
#     for i in range(len(data_col)):
#         num += 1
#
#         print(data_col[i])
#         # #print(type(data[i]))
#         for j in range(len(data_col[i])):
#             print(data_col[i][j])
#         #     print(type(data[i]))
#         #     #data[i].split('系统异常')
#
#     print('totle fix: %d'%num)
def log_length(value):  #统计每条log的长度
   #value is a list
   print(value)
   for x in range(len(value)):
       #for y in range(len(value[x])):
       value[x].append(str(len(value[x][7])))
       print(value[x][8])
   return value



def main():
    value = read_excel('log1.xlsx',0)  # 读取原始日志,最终返回一个包含信息所有list
    # write_2_excel(value)  # 把日志数据按属性写到excel里，返回一个把所有属性分开的excel表格
    #extract_data('write_2_log.xls')  #分析种类与词频，返回一个包含有分析数据的excel表格
    log_length(value)
    write_2_excel(value)
    extract_data('write_2_log.xls')

if __name__=='__main__':
    main()