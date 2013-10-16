#encoding=gb2312

__author__ = 'jiang'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import xlwt
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

