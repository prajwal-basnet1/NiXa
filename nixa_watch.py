#!/usr/bin/python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
from itertools import cycle
from colorama import Fore,Style
from pyfiglet import figlet_format
#Simple script made by anonymous person.
indicator=None
up=None
#u can type urllink,bs4obj,htmlfile up here which can make a program faster by removing inside funtion.
def market_check():
    urllink="http://www.nepalstock.com/"
    htmlfile=urlopen(urllink)
    bs4obj=BeautifulSoup(htmlfile,"html.parser")
    notice_bar=bs4obj.find(id="top-notice-bar").get_text(strip=True)
    if notice_bar== "Market Open" or "Open" in notice_bar:
        up="yes"
        print(Fore.GREEN+Style.BRIGHT+"                                                    Market Status: OPEN")
    else:
        up="no"
        print(Fore.RED+Style.BRIGHT+"                                                      Market Status: CLOSED")
    print(" ".center(135,"*"))

market_dicts={}
def market_summary():
    
    urllink="http://www.nepalstock.com/"
    htmlfile=urlopen(urllink)
    bs4obj=BeautifulSoup(htmlfile,"html.parser")
    table=bs4obj.find(class_="table table-hover table-condensed",width="100%")
    j=1
    
    for i in table.findAll('td'):
        value=i.get_text(strip=True)
        if j==1:
            pass
        elif j%2==0:
            temp_store=value
        else:
            market_dicts[temp_store]=value
        j+=1
    print(Fore.BLUE+Style.BRIGHT+"MARKET SUMMARY".center(135,"*"))
    for i,j in market_dicts.items():
        print(Fore.BLUE+Style.BRIGHT+f"{i:>60} : {j}")
    print()
    print("END".center(135,"*"))
    print()
    print()
    print(Fore.RESET)

def index_information():
    urllink="http://www.nepalstock.com/"
    htmlfile=urlopen(urllink)
    bs4obj=BeautifulSoup(htmlfile,"html.parser")
    
    table=bs4obj.find(class_="table table-hover table-condensed",cellpadding="3")
    indexes=[]
    global indicator;
    nepse=[]
    sensetive=[]
    floating=[]
    sensetive_float=[]
    j=1

    print(Fore.BLUE+Style.BRIGHT+"INDEX INFORMATION".center(135,"*"))
    for i in table.findAll('td'):
        value=i.get_text(strip=True)
        if value=="":
            pass
        elif j<5:
            indexes.append(value)
        elif j>5 and j<10:
            nepse.append(value)
        elif j>10 and j<15:
            sensetive.append(value)
        elif j>15 and j<20:
            floating.append(value)
        else:
            sensetive_float.append(value)
        j+=1
    

    if float(nepse[2])>0:
        for i in range(len(nepse)):
            print(Fore.GREEN+Style.BRIGHT+"\t\t\t\t\t\t\t"+str(indexes[i])+" : "+str(nepse[i]))
        print()
        print()

        for i in range(len(nepse)):
            print(Fore.GREEN+Style.BRIGHT+"\t\t\t\t\t\t\t"+str(indexes[i])+" : "+str(sensetive[i]))

        print()
        print()

        for i in range(len(nepse)):
            print(Fore.GREEN+Style.BRIGHT+"\t\t\t\t\t\t\t"+str(indexes[i])+" : "+str(floating[i]))


        print()
        print()

        for i in range(len(nepse)):
            print(Fore.GREEN+Style.BRIGHT+"\t\t\t\t\t\t\t"+str(indexes[i])+" : "+str(sensetive_float[i]))
    else:

        for i in range(len(nepse)):
            print(Fore.RED+Style.BRIGHT+"\t\t\t\t\t\t\t"+str(indexes[i])+" : "+str(nepse[i]))
        print()
        print()



        for i in range(len(nepse)):
            print(Fore.RED+Style.BRIGHT+"\t\t\t\t\t\t\t"+str(indexes[i])+" : "+str(sensetive[i]))

        print()
        print()

        for i in range(len(nepse)):
            print(Fore.RED+Style.BRIGHT+"\t\t\t\t\t\t\t"+str(indexes[i])+" : "+str(floating[i]))


        print()
        print()

        for i in range(len(nepse)):
            print(Fore.RED+Style.BRIGHT+"\t\t\t\t\t\t\t"+str(indexes[i])+" : "+str(sensetive_float[i]))
    print()
    print()
    print("END".center(135,"*"))
    print()
    print()

def sector_information():
    urllink="http://www.nepalstock.com/"
    htmlfile=urlopen(urllink)
    bs4obj=BeautifulSoup(htmlfile,"html.parser")

    table=bs4obj.find(class_="table table-hover table-condensed",cellpadding="3").find_next_sibling()
    header=[]
    changes=[]
    j=1
    
    for i in table.findAll("td"):
        value=i.get_text(strip=True)
        if value=="":
            pass;
        elif j<5:
            header.append(value)
        else:
            changes.append(value)
        j+=1

    result = dict(zip(changes, cycle(header)))
    print(Fore.BLUE+Style.BRIGHT+"SECTOR INFORMATION".center(135,"*"))
    print(Fore.GREEN)
    if indicator==1:
        for j,i in result.items():
            print("\t\t\t\t\t\t\t"+str(i)+" : "+str(j))
            if i=="%Change":
                print(Fore.GREEN+Style.BRIGHT+"*********".center(120,"*"))
    else:
        for j,i in result.items():
            print("\t\t\t\t\t\t\t"+str(i)+" : "+str(j))
            if i=="%Change":
                print(Fore.GREEN+Style.BRIGHT+"*********".center(120,"*"))

    print()
    print()
    print("END".center(135,"*")) 
    print()
    print()
    #key value are in opposite order.
turnover_link="http://www.nepalstock.com/turnovers"
topgainer_link='http://www.nepalstock.com/gainers'
toploser_link='http://www.nepalstock.com/losers'
def top_gainers():
    header=[]
    data=[]
    htmlfile=urlopen(topgainer_link)
    gainer=BeautifulSoup(htmlfile,"html.parser")
    table=gainer.find(class_="dataTable table")

    
    print(Fore.GREEN+Style.BRIGHT+"TOP GAINER".center(135,"*"))
    for i in table.findAll('td'):
        value=i.get_text(strip=True)
        if value.startswith("As of"):
            date=value
            pass;
        elif value=="Symbol" or value=="LTP" or value=="% Change":
            header.append(value)
        else:
            data.append(value)
    symbol=data[::3]
    ltp=data[1::3]
    change=data[2::3]
    
    symbol[0]=header[0]
    ltp[0]=header[1]
    change[0]=header[2]
    print(Fore.GREEN+Style.BRIGHT+f"{date.upper():>70}")
    print(Fore.GREEN+"".center(135,"*"))
    
    print(Fore.GREEN+Style.BRIGHT+"                                                    TOP GAINER")
    res = "\n".join("{:>50}||{:>20}||{:>20} %|".format(x, y,z) for x, y,z in zip(symbol, ltp,change))
    print(Fore.GREEN+Style.BRIGHT+str(res))
    print()
    print()
    print("END".center(135,"*")) 
    print()
    print()
print(Fore.RESET)
def top_losers():

    header=[]
    data=[]

    htmlfile=urlopen(toploser_link)
    loser=BeautifulSoup(htmlfile,"html.parser")
    table=loser.find(class_="dataTable table")
    print(Fore.RED+Style.BRIGHT+"TOP LOSERS".center(135,"*"))
    for i in table.findAll('td'):
        value=i.get_text(strip=True)
        if value.startswith("As of"):
            date=value
            pass;
        elif value=="Symbol" or value=="LTP" or value=="% Change":
            header.append(value)
        else:
            data.append(value)
    symbol=data[::3]
    ltp=data[1::3]
    change=data[2::3]
    
    symbol[0]=header[0]
    ltp[0]=header[1]
    change[0]=header[2]
    
    print(Fore.RED+Style.BRIGHT+f"{date.upper():>70}")
    print(Fore.BLUE+"".center(135,"*"))

    print(Fore.RED+Style.BRIGHT+"                                                    TOP LOSERS")
    res = "\n".join("{:>50}||{:>20}||{:>20} %|".format(x, y,z) for x, y,z in zip(symbol, ltp,change))
    print(Fore.RED+Style.BRIGHT+str(res))
    print(Fore.RESET)
    print()
    print("END".center(135,"*")) 
    print()
    print()

def top_turnover():
        header=[]
        data=[]

        htmlfile=urlopen(turnover_link)
        topshares=BeautifulSoup(htmlfile,"html.parser")
        table=topshares.find(class_="dataTable table").tbody
        print(Fore.GREEN+Style.BRIGHT+"Top 10 Stocks by Turnover".center(135,"*"))
        print()
        for i in table.findAll('td'):
            value=i.get_text(strip=True)
            if value.startswith("As of"):
                date=value
                pass;
            elif value=="Symbol" or value=="Turn Over" or value=="Closing Price":
                header.append(value)
            else:
                data.append(value)
        symbol=data[::3]
        turn_over=data[1::3]
        closing=data[2::3]
        
        symbol[0]=header[0]
        turn_over[0]=header[1]
        closing[0]=header[2]
        
        print(Fore.GREEN+Style.BRIGHT+f"{date.upper():>70}")
        print(Fore.BLUE+"".center(135,"*"))
        res = "\n".join("{:>50}||{:>20}||{:>20} |".format(x, y,z) for x, y,z in zip(symbol, turn_over,closing))
        print(Fore.GREEN+Style.BRIGHT+str(res))
        print()
        print()

def top_share_trade():
        header=[]
        data=[]

        htmlfile=urlopen(turnover_link)
        topshares=BeautifulSoup(htmlfile,"html.parser")
        table=topshares.find(class_="dataTable table").tbody.findNext('tbody')
        print(Fore.GREEN+Style.BRIGHT+"Top 10 Stocks by Share Traded".center(135,"*"))
        print()
        for i in table.findAll('td'):
            value=i.get_text(strip=True)
            if value.startswith("As of"):
                date=value
                pass;
            elif value=="Symbol" or value.startswith("Share") or value=="Closing Price":
                header.append(value)
            else:
                data.append(value)
        symbol=data[::3]
        share_traded=data[1::3]
        closing=data[2::3]
        
        symbol[0]=header[0]
        share_traded[0]=header[1]
        closing[0]=header[2]
        
        print(Fore.GREEN+Style.BRIGHT+f"{date.upper():>70}")
        print(Fore.BLUE+"".center(135,"*"))
        res = "\n".join("{:>50}||{:>20}||{:>20} |".format(x, y,z) for x, y,z in zip(symbol,share_traded,closing))
        print(Fore.GREEN+Style.BRIGHT+str(res))
        print()
        print()

def top_transaction():
        header=[]
        data=[]

        htmlfile=urlopen(turnover_link)
        topshares=BeautifulSoup(htmlfile,"html.parser")
        table=topshares.find(class_="dataTable table").tbody.findNext('tbody').findNext('tbody')
        print(Fore.GREEN+Style.BRIGHT+"Top 10 Stocks by No. Of Transaction".center(135,"*"))
        print()
        for i in table.findAll('td'):
            value=i.get_text(strip=True)
            if value.startswith("As of"):
                date=value
                pass;
            elif value=="Symbol" or value.startswith("No") or value=="Closing Price":
                header.append(value)
            else:
                data.append(value)
        symbol=data[::3]
        transaction=data[1::3]
        closing=data[2::3]
        
        symbol[0]=header[0]
        transaction[0]=header[1]
        closing[0]=header[2]
        
        print(Fore.GREEN+Style.BRIGHT+f"{date.upper():>70}")
        print(Fore.BLUE+"".center(135,"*"))
        res = "\n".join("{:>50}||{:>20}||{:>20} %|".format(x, y,z) for x, y,z in zip(symbol, transaction,closing))
        print(Fore.GREEN+Style.BRIGHT+str(res))
        print()
        print()

def main():
    options=["Market check","Market Summary","Index Information","Sector Information","Top Gainers","Top Losers","Top Turnover","Top Share Trade","Top Transaction","All","EXIT"]
    print(Fore.MAGENTA+"<--------------------------------------------------coded by Anonymous--------------------------------------------->")
    while True:
        j=1
        print()
        print()
        print(Fore.BLUE+"<------------------------------------------------------------------------------------------------>")
        print()
        for i in range(len(options)):
            print(Fore.YELLOW+str(j)+" ) "+str(options[i]))
            j+=1
        print()
        print(Fore.BLUE+"<------------------------------------------------------------------------------------------------>")
        print()
        print(Fore.CYAN+Style.BRIGHT+"Enter the option#")
        user_input=int(input(">>"))
        print(Fore.BLUE+Style.BRIGHT+"                                          PROGRAM RUNNING...")
        if user_input==1:
            market_check()
        elif user_input==2:
            market_summary()
        elif user_input==3:
            index_information()
        elif user_input==4:
            sector_information()
        elif user_input==5:
            top_gainers()
        elif user_input==6:
            top_losers()
        elif user_input==7:
            top_turnover()
        elif user_input==8:
            top_share_trade()
        elif user_input==9:
            top_transaction()
        elif user_input==10:
            try:
                market_check()
            except:
                print("Something went wrong while checking market(please wait).")
            try:
                market_summary()
            except:
                print("Something went wrong while checking market information(please wait).")
            try:
                index_information()
            except:
                print("Something went wrong while checking index information(please wait).")
            try:
                sector_information()
            except:
                print("Something went wrong while checking sector information(please wait).")
            try:
                top_gainers()
            except:
                print("Something went wrong while checking top gainers(please wait).")
            try:
                top_losers()
            except:
                print("Something went wrong while checking top losers(please wait).")
            try:
                top_turnover()
            except:
                print("something went wrong while checking top turnover(please wait).")
                print("it might be avilable after 3pm.")
            try:
                top_share_trade()
            except:
                print("Something went wrong while cheking top share trade company(please wait).")
                print("it might be avialable after 3pm.")
            try:
                top_transaction()
            except:
                print("Something went wrong while checking top transaction company.")
                print("it might be avilable after 3pm.")
            exit()
        elif user_input==len(options):
            print("***************************************************BYE*******************************************************")
            exit()
        else:
            print("Please enter the valid input.")

if __name__=="__main__":
    print((Fore.BLUE+figlet_format("NiXa_watch",font="bulbhead")))
    main()
