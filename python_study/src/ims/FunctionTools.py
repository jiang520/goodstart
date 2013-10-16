#encoding=gb2312

__author__ = 'jiang'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import xlwt
#'''导出指定的tablewiget的数据到文件中'''
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

#导出时自动选择文件夹,并且提示导出是否成功
def ExportTableToExcel(tableWidget):
    filePath = QFileDialog.getSaveFileName(None, u'导出表格', u'请选择一个导出文件路径', u"*.xls")
    if not filePath: return
    filePath = ('%s'%filePath).rstrip('.xls')
    filePath = filePath+('.xls')
    if ExportTableWidgetDataToExcel(tableWidget, filePath):
        QMessageBox.information(None, u'tips', u'导出成功')
    else:
        QMessageBox.critical(None,u'error', u'导出失败,请换个路径再试')


#导出指定的tablewiget的数据到文件中
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
    #输出表格头
    for col in range(colCount):
        data = model.headerData(col, Qt.Horizontal)
        str2 = u'%s'%data.toString()
        workSheet.write(0, col, str2)
    #输出表格数据
    for row in range(rowCount):
        for col in range(colCount):
            index = model.index(row, col)
            data = model.data(index, Qt.DisplayRole)
            str2 = u'%s'%data.toString()
            workSheet.write(row+1, col, str2, style)
    book.save(filepath)
    return  True

