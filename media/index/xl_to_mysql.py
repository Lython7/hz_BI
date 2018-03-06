import xlrd, pymysql

class ExcelToMysql(object):

    # def __init__(self, host="localhost", user="root", passwd="2531", db="hz_BI"):
    #     # 连接数据库
    #     database = pymysql.connect(host=host, user=user, passwd=passwd, db="hz_BI")
    #     cursor = database.cursor()

    def readExcel(self, filename, sheetname):
        # 获取excelData文件夹中上传了的excel文件
        datalist = []
        try:
            excelFile = xlrd.open_workbook('./excelData/' + filename)
            sheet = excelFile.sheet_by_name(sheetname)
            for i in range(1,sheet.nrows):
                dic = {}
                for j in range(sheet.ncols):
                    dic[sheet.cell(0,j)] = sheet.cell(i,j)
                datalist.append(dic)
        except:
            print('excel读取过程中有问题')

    def jsonhandle(self):
        pass