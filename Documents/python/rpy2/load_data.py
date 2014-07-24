#!/usr/bin/python
#coding:utf8
import MySQLdb
import rpy2.robjects as robjects
conn = MySQLdb.connect(host = "localhost",user="leo",passwd="104064")
cur = conn.cursor()
cur.execute('use exe1')

