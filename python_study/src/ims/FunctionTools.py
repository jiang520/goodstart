#encoding=gb2312
from ims.model.dbArticleType import ArticleType, dbArticleType

__author__ = 'jiang'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import xlwt
import xlrd
#'''����ָ����tablewiget�����ݵ��ļ���'''
def ExportTableWidgetData(tableWidget, filepath):
    if filepath == None or len(filepath) <= 0: return
    if tableWidget == None : return
    model = tableWidget.model()
    rowCount = model.rowCount()
    colCount = model.columnCount()
    import codecs
    fileExport = codecs.open(filepath, 'w', 'utf-8')
    for col in range(colCount):
        str = model.headerData(col, Qt.Horizontal)
        str = u'%s,'%str.toString()
        fileExport.write(str)
        fileExport.write(',')
    fileExport.write('\r\n')
    for row in range(rowCount):
        for col in range(colCount):
            index = model.index(row, col)
            data = model.data(index, Qt.DisplayRole)
            #print data.toString()
            fileExport.write(u'%s,'%data.toString())
        fileExport.write('\r\n')
    fileExport.close()

#����ʱ�Զ�ѡ���ļ���,������ʾ�����Ƿ�ɹ�
def ExportTableToExcel(tableWidget):
    filePath = QFileDialog.getSaveFileName(None, u'�������', u'��ѡ��һ�������ļ�·��', u"*.xls")
    if not filePath: return
    filePath = ('%s'%filePath).rstrip('.xls')
    filePath = filePath+('.xls')
    if ExportTableWidgetDataToExcel(tableWidget, filePath):
        QMessageBox.information(None, u'tips', u'�����ɹ�')
    else:
        QMessageBox.critical(None,u'error', u'����ʧ��,�뻻��·������')


#����ָ����tablewiget�����ݵ��ļ���
def ExportTableWidgetDataToExcel(tableWidget, filepath):
    if filepath == None or len(filepath) <= 0: return False
    if tableWidget == None : return False
    model = tableWidget.model()
    rowCount = model.rowCount()
    colCount = model.columnCount()
    book = xlwt.Workbook()
    if book is None : return  False
    workSheet = book.add_sheet(u'table')
    if workSheet is None: return  False
    style = xlwt.XFStyle()
    #������ͷ
    for col in range(colCount):
        data = model.headerData(col, Qt.Horizontal)
        str2 = u'%s'%data.toString()
        workSheet.write(0, col, str2)
    #����������
    for row in range(rowCount):
        for col in range(colCount):
            index = model.index(row, col)
            data = model.data(index, Qt.DisplayRole)
            str2 = u'%s'%data.toString()
            workSheet.write(row+1, col, str2, style)
    book.save(filepath)
    return  True

#�����ļ�
def ImportArticleTable(filepath):
    if filepath==None or len(filepath)==0: return  False
    book = xlrd.open_workbook(filepath)
    sheet = book.sheet_by_index(0)
    if sheet is None: return  False
    headers = ['�ͺ�','��װ','���','Ʒ��','��λ','��ע']

    for row in range(sheet.row()):
        for col in range(sheet.col):
            print sheet.cell(row,cel),','

def ImportClientTalbe(filepath):
    pass
def ImportInoutRecord(filePath):
    pass

def ImportArticleType(filepath):
    if filepath==None or len(filepath)==0: return  False
    book = xlrd.open_workbook(filepath)
    sheet = book.sheet_by_index(0)
    if sheet is None: return  False
    headers = ['���']
    if sheet.ncols!=0 or sheet.cell_value(0, 0)!='���':
        raise Exception("cols must be 1count and contain type'�ļ�����Ҫ��Ϊ1,����ֻ��һ��<���>")
        return
    type1set = set()
    typeslist2 = []
    for row in range(1, sheet.nrows):
        for col in range(sheet.ncols):
            print sheet.cell_value(row,col)
            types = sheet.cell_value(row,col)
            t1t2 = types.split('-')
            if len(t1t2)!= 2:
                raise Exception("invadate type")
                return
            if(t1t2[0]==''):
                raise Exception("invadate type1")
                return
            type1set.add(t1t2[0])

    db = dbArticleType()
    for text in type1set:
        typeinfo = ArticleType()
        typeinfo.parentid = 0
        typeinfo.text=text
        db.insert(typeinfo)

    for row in range(1,sheet.nrows):
        for col in range(sheet.ncols):
            print sheet.cell_value(row,col)
            types = sheet.cell_value(row,col)
            t1t2 = types.split('-')
            if len(t1t2)!= 2: break
            parent_type = db.getArticleTypeInfoByTypeName(t1t2[0])
            if parent_type is None:
                raise Exception("invadate parent type")
                return
            type = ArticleType()
            type.parentid= parent_type.id
            type.text=t1t2[1]
            typeslist2.append(type)

    for item in typeslist2:  db.insert(item)


if __name__=="__main__":
    filepath = "d:\\test.xls"
    ImportArticleType('D:\\type.xlsx')
    #ImportArticleTable(filepath)





