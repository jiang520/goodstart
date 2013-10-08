#encoding=gb2312
__author__ = 'jiang'

from PyQt4.QtCore import *
'''导出指定的tablewiget的数据到文件中'''
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