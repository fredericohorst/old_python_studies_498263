
# import ftplib

# def catch_files(server, dir):
#    ftp = ftplib.FTP(server)
#    ftp.login("Guest")
#    ftp.cwd(dir)
#    print ftp.retrlines('LIST')

#catch_files("ftp://ftp.ibge.gov.br/", "/Precos_Indices_de_Precos_ao_Consumidor/INPC")



#
# import os
# import ftplib
# import zipfile
# import csv
#
# def extractfile(file):
#     zfile = zipfile.ZipFile(file)
#     zfile.extractall("/Users/frederico/PycharmProjects/indicadores/db")
#
#
# def getfiles (site):
#     ftp = ftplib.FTP(site)
#     ftp.login()
#     ftp.cwd("/marketdata/BMF/")
#     for filename in ftp.nlst("NEG*.zip"):
#         fhandle = open(filename, 'wb')
#         print ('Getting ' + filename)
#         if not os.path.isfile(filename):
#             ftp.retrbinary('RETR ' + filename, fhandle.write)
#         if os.path.isfile(filename):
#             extractfile(filename)
#         fhandle.close()
#
#
# os.chdir("/Users/frederico/PycharmProjects/indicadores/db")
# getfiles("ftp.bmf.com.br")





import os
import ftplib
import zipfile
import csv

def extractfile(file):
    zfile = zipfile.ZipFile(file)
    zfile.extractall("/Users/frederico/PycharmProjects/indicadores/db")

def getfiles (site):
    ftp = ftplib.FTP(site)
    ftp.login()
    ftp.cwd("/Precos_Indices_de_Precos_ao_Consumidor/INPC")
    for filename in ftp.nlst("NEG*.zip"):
        fhandle = open(filename, 'wb')
        print ('Getting ' + filename)
        if not os.path.isfile(filename):
            ftp.retrbinary('RETR ' + filename, fhandle.write)
        if os.path.isfile(filename):
            extractfile(filename)
        fhandle.close()


os.chdir("/Users/frederico/PycharmProjects/indicadores/db")
getfiles("ftp://ftp.ibge.gov.br/")