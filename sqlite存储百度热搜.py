# __author__ = 'kohna'
# -*- coding:utf-8 -*-
import requests
import re
import sqlite3
import time

# Create at 2015-09-01

"""

* Get the Hot search of baidu

"""

sqlDB = 'hot.db3'


class GetHotPointList:
    def __init__(self):
        self.senddata = {'b': 1, 'hd_h_info': 1, 'line': 20}
        self.soucdata = ''
        self.re = '.\S.\w*.:.*.]'
        self.reres = ''
        self.evalres = ''
        self.sdcit = []

    def getdata(self):
        try:
            self.soucdata = requests.get("http://top.baidu.com/clip?", params=self.senddata)
            self.reres = re.findall(self.re, self.soucdata.text.encode('UTF-8'))
            self.evalres = eval(self.reres[0])
            for i in self.evalres:
                self.sdcit.append(i)
        except sqlite3.Error, e:
            print u'The Error from: %s', e.args[0]


class DBopt:
    def __init__(self):
        try:
            self.dbcon = sqlite3.connect(sqlDB)
        except sqlite3.Error, e:
            print u'Sqlit Databese error by ' + e.args[0]
            return

        self.dbcur = self.dbcon.cursor()
        self.sql = 'sql'

    def sqlexe(self):
        try:
            temp = self.dbcur.execute(self.sql)
        except sqlite3.Error, e:
            print u"Sqlit3 Databese execute sql error by" + e.args[0]
            return
        self.dbcon.commit()

        return temp

    def dbcolse(self):
        self.dbcon.close()


if __name__ == '__main__':

    hoy = GetHotPointList()
    hoy.getdata()

    iui = 0

    db = DBopt()
    db.sql = '''CREATE TABLE IF NOT EXISTS hot(id INTEGER PRIMARY KEY,title VARCHAR(32),trend VARCHAR(32),
    titurl VARCHAR(64),clicks INTEGER, cloc TIME)'''
    db.sqlexe()

    for ins in hoy.sdcit:
        title = hoy.sdcit[iui]['title'].decode('unicode-escape')
        trend = hoy.sdcit[iui]['trend']
        titurl = hoy.sdcit[iui]['tit_url'].replace('\\', '')
        detailurl = hoy.sdcit[iui]['detail_url']
        clicks = str(hoy.sdcit[iui]['clicks'])
        cloc = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        print title, trend, titurl, clicks, cloc

        db.sql = 'INSERT INTO hot(title,trend,titurl,clicks,cloc) VALUES ("' + title + '","' + trend + '","' + titurl +  '","' + clicks + '","' + cloc + '")'
        db.sqlexe()

        iui += 1
    db.dbcolse()
