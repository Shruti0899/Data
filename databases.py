# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import sqlite3 as sql
import pandas as pd

os.chdir('C:\\Users\\Sneha\\Desktop\\Django\\django_env')


print("Playing With DataBases")


class Data:
    
    def __init__(self):
        self.menu()
            
        
    def menu(self):
        op=int(input("\nChoose an option \n1.Extract\n2.Exit\n"))
        if op==1:
            dbs=input("\nChoose your database:\n")
            con=sql.connect(dbs)
            cur=con.cursor()
            tables_list=cur.execute("select name from sqlite_master where type='table'")
            t=tables_list.fetchall()
            if len(t)==0:
                print("EMPTY database!!")
                self.menu()
            else:
                print(len(t))
                for i in range(len(t)):
                    print(i, t[i][0]);
                table=int(input("\nChoose the index of the table from the list above\n"))
                tb=cur.execute("select * from {}".format(t[table][0]))
                print("Table data is as follows\n")
                t_l = tb.fetchall();
                print(t_l)
                rows=[i for i in t_l]
                print(rows)
                print("\nShowing the column names below:\n")
                col_names=cur.execute("PRAGMA TABLE_INFO({})".format(t[table][0]))
                data = col_names.fetchall();
                con.close()
                print(data)
                col=[i[1] for i in data]
                print(col)
                df=pd.DataFrame(rows,columns=col)
                print(df)
                df.to_csv(input("enter file name"))
            
                self.menu()
        
        else:
            exit()
myobj= Data()
            
                            
            
            
myobj= Data()
            
            
                
        
