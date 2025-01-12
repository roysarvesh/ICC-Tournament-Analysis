# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 02:46:56 2020

@author: shiva
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1=pd.read_csv('1.csv', encoding = "ISO-8859-1", engine='python')
df2=pd.read_csv('2.csv')
df3=pd.read_csv('3.csv')
df4=pd.read_csv('4.csv')

#MAIN MENU
def mainmenu():
    i=0
    while i !='d':
        print('    ICC-WORLD CUP 2019           ')
        print('1) Display Data')
        print('2) Data Visualization')
        print('3) Data Analysis')
        print('4) Exit')
        i=input('Select Option')
        if i=='1':
            print('Displaying Data')
            print(df1)
            print(df2)
            print(df3)
            print(df4)
        elif i=='2':
            submenu2()
        elif i=='3':
            submenu3()
        elif i=='4':
            print('successfully exited from the menu')
        else:
            print('INVALID')
            
def submenu2():
        print('       DATA VISUALISATION MENU           ')
        print('1) Line Graph')
        print('2) Bar plot')
        print('3) Pie Plot')
        print('4) Main Menu')
        ch2=int(input('Choose Your Option'))

        if ch2==1:
             plt.plot(df1['Team'],df1['Points'],color='k',marker='o',markerfacecolor='red',label='Points',markersize=3,linewidth=1)
             plt.title('ICC World Cup')
             plt.xlabel('Teams',fontsize=15)
             plt.ylabel('Points',fontsize=15)
             plt.show()
             plt.plot(df1['Team'],df1['Rating'],color='g',marker='o',markerfacecolor='black',label='Rating',markersize=3,linewidth=1)
             plt.title('ICC World Cup')
             plt.xlabel('Teams',fontsize=15)
             plt.ylabel('Rating',fontsize=15)
             plt.show()
             plt.plot(df1['Team'],df1['Weight'],color='r',marker='o',markerfacecolor='blue',label='Weighted Matches',markersize=3,linewidth=1)
             plt.title('ICC World Cup')
             plt.xlabel('Teams',fontsize=15)
             plt.ylabel('Weighted Matches',fontsize=15)
             plt.show()
             plt.plot(df1['Team'],df1['Position'],color='y',marker='o',markerfacecolor='yellow',label='Position',markersize=3,linewidth=1)
             plt.title('ICC World Cup')
             plt.xlabel('Teams',fontsize=15)
             plt.ylabel('Position',fontsize=15)
             plt.show()

        elif ch2==2:
            plt.bar(df2['Team'],df2['Mat'],label='Total Matches',color=['k','r','y','g','r','c','g','k','m','c'])
            plt.grid(False)
            plt.legend()
            plt.xlabel('Teams',fontsize=15)
            plt.xticks(fontsize=9,rotation=30)
            plt.ylabel('No of matches',fontsize=15)
            plt.title('Total Matches',fontsize=20)
            plt.show()

            plt.bar(df2['Team'],df2['Won'],label='Wins',color=['k','r','y','g','r','c','g','k','m','c'])
            plt.grid(False)
            plt.legend()
            plt.xlabel('Teams',fontsize=15)
            plt.xticks(fontsize=9,rotation=30)
            plt.ylabel('No. of wins',fontsize=15)
            plt.title('Wins',fontsize=20)
            plt.show()

            plt.bar(df2['Team'],df2['Lost'],label='Loses',color=['k','r','y','g','r','c','g','k','m','c'])
            plt.grid(False)
            plt.legend()
            plt.xlabel('Teams',fontsize=15)
            plt.xticks(fontsize=9,rotation=30)
            plt.ylabel('No. of lost matches',fontsize=15)
            plt.title('Lost',fontsize=20)
            plt.show()


            plt.bar(df2['Team'],df2['Tied'],label='Tied',color=['k','r','y','g','c','r','g','k','m','c'])
            plt.grid(False)
            plt.legend()
            plt.xlabel('Teams',fontsize=15)
            plt.xticks(fontsize=9,rotation=30)
            plt.ylabel('No. of tied matches',fontsize=15)
            plt.title('Tied',fontsize=20)
            plt.show()

        elif ch2==3:
            
            plt.pie(df4['No. Of Wins'],labels=df4['Team'],radius=1.2,autopct='%0.0f%%',shadow=False,explode=[0.1,0.1,0.1,0.1,0.1])
            plt.title('Winners',color='r',fontsize=20)
            plt.show()
        elif ch2==4:
            mainmenu()        
        else:
            print('Please input a valid option')
def submenu3():
    print('                 DATA ANAYLSIS MENU                    ')
    print('1) Find the maximum,minimum,mean,sum of - Points')
    print('2) Find the maximum,minimum,mean,sum of - Rating')
    print('3) Find the maximum,minimum,mean,sum of - Tied Matches ')
    print('4) Find the name of those 3 teams which have highest wins')
    print('5) Find the name of those 3 teams which have lowest wins')
    print('6) Find the name of those 3 teams which have highest loss the matches')
    print('7) Find the name of those 3 teams which have lowest loss the matches')
    print('8.I Quantile,II Quantile and III Quantile of Rating')
    print('9.Pivot Table - World Cup won by different teams Analysis')
    print('10.To export csv file')
    print('11.Back to main menu')
    p=int(input('\nChoose a option for data analysis'))
    if p==1:
           print('maximum,minimum,mean,sum of - Points')
           print(df1.aggregate({'Points':['max','min','mean','sum']}))
    elif p==2:
           print('maximum,minimum,mean,sum of - Rating')
           print(df1.aggregate({'Rating':['max','min','mean','sum']}))
    elif p==3:
           print('maximum,minimum,mean,sum of - Tied Matches')
           print(df2.aggregate({'Tied':['max','min','mean','sum']}))
    elif p==4:
              print('Name of those 3 teams which have highest wins')
              print(df2.sort_values('Won',ascending=False).head(3))  
    elif p ==5:
            print('Name of those 3 teams which have lowest wins')
            print(df2.sort_values('Won',ascending=True).head(3))
    elif p==6:
              print('Name of those 3 teams which have highest loss the matches')
              print(df2.sort_values('Lost',ascending=False).head(3))  
    elif p ==7:
            print('Name of those 3 teams which have lowest loss the matches')
            print(df2.sort_values('Lost',ascending=True).head(3))  
    elif p==8:
             print('I Quantile,II Quantile and III Quantile of Rating')
             print(df1['Rating'].quantile([0.25,0.50,0.75]))              
    elif p ==9:
             print('Pivot Table - World Cup won by different teams ')
             print(df4.pivot_table(index= 'Team', values= "No. Of Wins"))
    elif p==10:
             df1.to_csv(r'C:\Users\user\Desktop\I File.csv')
             df2.to_csv(r'C:\Users\user\Desktop\II File.csv')
             df3.to_csv(r'C:\Users\user\Desktop\III File.csv')
             df4.to_csv(r'C:\Users\user\Desktop\IV File.csv')
    elif p ==11:
               mainmenu()              
    else:
         print('Please input a valid option')
mainmenu()
