#!/usr/bin/python3

from urllib.request import urlopen
import urllib
import urllib.error
import os,time,math,time,traceback
from bs4 import BeautifulSoup
from colorama import Fore,Back,Style,init
#init(convert=True)                    it seems like some windows computer have problem with color so uncommenting this can fix the issue.
from pyfiglet import figlet_format
import nixa_watch
#Simple script made by anonymous person.
try:
    #all the sectors
    def getting_sector():
        global ticker_link
        global names;
        global values;
        global sectors;
        global all_sector;
        global user_input;
        global listed_companies;
        global all_sector;
        global user_input;
        all_sector=None;
        
        print((Fore.MAGENTA+figlet_format("NiXa",font="caligraphy")))
        #printing all the sectors on screen for user input.
        print(Fore.MAGENTA+Style.BRIGHT+"                    {------------------{+} Coded by Little Brave Stainee{+}---------------}")
        print("                   {------------------{+} With Great Power Comes Great Responsibility. {+}--------------}")
        print()
        print()
        #time.sleep(1.5)

        sectors={"Commercial Banks":"1","Finance":"2","Hotels":"3","Manufacturing":"4","other":"5","Hydropower":"6","Trading":"7","Non life insurance":"8","Devlopment bank":"9","Goverment bond":"10","Corporate_bond":"11","Preferrd stock":"12","Mutual fund":"13","Microfinance":"16","Life insurance":"17","Investment":"18","Market Status":"","All":"","Exit":""} 
        names=list(sectors.keys()) #getting all the names of company from the dictionary. 
        print(Fore.MAGENTA+Style.BRIGHT+"<"+"Avilable Sector".center(80,"-")+">")
        print(Fore.RESET)
        j=1
        for i in sectors.keys():
            print(Fore.CYAN+str(j)+". "+str(i))
            j+=1
        print("")
        
        print(Fore.MAGENTA+Style.BRIGHT+"<"+"".center(80,"-")+">")
        print(Fore.RESET)
        user_input=int(input(Fore.BLUE+"Enter the sector >>"))
        if user_input==18:
            pass;
        elif user_input==19:
            exit();
        
        #change sector id according to the sector,16 for microfinance.
        else:
            pass

    def get_ticker(link):
        print(Fore.BLUE+"                               IT MIGHT TAKE SOME TIME PLEASE WAIT!                        ")
        print(Fore.BLUE+"                               Program running...                     ")
        
        global ticker_list;
        tickerhtml=urlopen(link)           #opening the link from nepse to get all the company ticker.
        ticker_bs4=BeautifulSoup(tickerhtml,"lxml")
        tickertable=ticker_bs4.find('table')       #finding the table from nepse website


        whole_list=[]
        for i in tickertable.findAll("td"):           #getting the table data from nepse website.
            tickervalue=i.get_text(strip=True)
            whole_list.append(tickervalue)

        ticker_list=[]
        for i in whole_list[2:]:
            if i.isupper()==True and len(i)<13:      #excuding first 2 items we are only seleting ticker from list.
                ticker_list.append(i)
            else:
                pass;

        if not(ticker_list):
            print(Fore.RED+"None of the company listed in this sector.")
            exit()

    #creating the name for testfile.
    #***********************************************ticker selected*********************************************************

    def web_scraping(link):
        try:
            time.sleep(0.5)
            htmlfile=urlopen(link)
            if htmlfile==None:
                print("[-] Page not found")

        except urllib.error.HTTPError as f:
            print("[-] Error:"+str(f))

        try:
            bs4obj=BeautifulSoup(htmlfile,"html.parser")
            table=bs4obj.find('table',{"id":"accordion"})

            with open(filenames,'a') as k:          #opening the testfile 
                k.write('Company name: '+"\n")        #writing the company name on first.
                k.write(com_name+"\n")

            #filtering the able and from that only selecting the necessary value.
            
            def getting_cash():
                temp_lists_fiscal=[]
                cash_table=bs4obj.find(id="dividend-panel")
                for i in cash_table.findAll("td"):
                    temp_value=i.get_text(strip=True)
                    if temp_value.startswith("#Fiscal"):
                        pass
                    else:
                        temp_lists_fiscal.append(temp_value)
                if len(temp_lists_fiscal)==0:
                    cash_dividend="No cashdividend yet!!"
                else:
                    temp_cash_dividend=temp_lists_fiscal[1::3]
                    year=temp_lists_fiscal[2::3]
                    
                    cash_dividend=[i+"  "+j for i,j in zip(temp_cash_dividend,year)]
                return cash_dividend
            cash_dividend_var=getting_cash()
            if type(cash_dividend_var)==str:
                cash_dividend=cash_dividend_var
            else:
                cash_dividend=""
                for i in cash_dividend_var:
                    cash_dividend=cash_dividend+i+" , "
                
            
            def getting_bonus():
                temp_lists_fiscal=[]
                bonus_table=bs4obj.find(id="bonus-panel")
                for i in bonus_table.findAll("td"):
                    temp_value=i.get_text(strip=True)
                    if temp_value.startswith("#Value"):
                        pass
                    else:
                        temp_lists_fiscal.append(temp_value)
                if len(temp_lists_fiscal)==0:
                    bonus_share="No bonus dividend yet!!"
                else:
                    temp_bonus_share=temp_lists_fiscal[1::3]
                    year=temp_lists_fiscal[2::3]
                    
                    bonus_share=[i+"  "+j for i,j in zip(temp_bonus_share,year)]    
                return bonus_share
            bonus_share_var=getting_bonus()
            if type(bonus_share_var)==str:
                bonus_share=bonus_share_var
            else:
                bonus_share=""
                for i in bonus_share_var:
                    bonus_share=bonus_share+i+" , "

            def getting_rightshare():
                temp_lists_fiscal=[]
                right_table=bs4obj.find(id="right-panel")
                for i in right_table.findAll("td"):
                    temp_value=i.get_text(strip=True)
                    if temp_value.startswith("#ValueFiscal"):
                        pass
                    else:
                        temp_lists_fiscal.append(temp_value)
                if len(temp_lists_fiscal)==0:
                    right_share="No right share yet!!"
                else:
                    temp_right_share=temp_lists_fiscal[1::3]
                    year=temp_lists_fiscal[2::3]
                    
                    right_share=[i+"  "+j for i,j in zip(temp_right_share,year)]
                return right_share    
            right_share_var=getting_rightshare()
            if type(right_share_var)==str:
                right_share=right_share_var;
            else:
                right_share=""
                for i in right_share_var:
                    right_share=right_share+i+" , "

            for i in table.findAll({"th","td"}):
                value=i.get_text(strip=True)
                if (value.startswith("#")==True or value=="Value" or value=="Fiscal Year"):
                    pass;
                else:
                    with open(filenames,'a') as f:
                        f.write(value+"\n")
            #writing cash dividend,bonus share,right share at the end of trash file.

            with open(filenames,'a') as k:
                k.write("Cash Dividend= "+str(cash_dividend)+"\n")
                k.write("Bonus Share= "+str(bonus_share)+"\n")
                k.write("Right Share= "+str(right_share)+"\n")
        except Exception as e:
            print("Error [-]: "+str(e))

    #sending the every copmpany ticker to web_scraping .
   # u dont need to write in testfile can directly integrate into dictionary but i am just bored to integrate that now for my automation. 
    def calling_websraping():
        global filenames;
        global com_name;
        global real_names

        real_names=[]
        #either u can put _ on dictionary by hand or u can do this.
        for i in names:
            if " " in i:
                i=i.split()
                real_names.append(i[0]+"_"+i[1])
            else:
                real_names.append(i)
        
        for i in real_names:
            if os.path.isfile("testfile_"+str(i)):
                os.remove('testfile_'+str(i))
        
        if all_sector is not None:
            filenames="testfile_"+real_names[all_sector]
        else:
            filenames="testfile_"+real_names[user_input-1]

        new_ticker_list=[]
        for i in ticker_list:
            try:
                com_name=i
                web_scraping(f'https://merolagani.com/CompanyDetail.aspx?symbol={i}')
            except:
                print("Invalid url on "+str(i))
    #***********************************************retriving the value**********************************************

    def retrive_value():
        company_name=[]
        pe_list=[]
        market_capitalization=[]
        eps_list=[]
        market_price=[]
        pb_value=[]
        average_180=[]
        share_outstanding=[]
        Last_trade=[]
        book_value=[]
        year_high_low_price=[]
        today_change=[]
        cash_dividend_list=[]
        bonus_share_list=[]
        right_share_list=[]
        
        if all_sector is not None:
            filenames="testfile_"+real_names[all_sector]
        else:
            filenames="testfile_"+real_names[user_input-1]
        #opening the testfile and getting the well formatted file from it.
        with open(filenames) as p:
            content=p.readlines()
            #print(content)
            m=0
            for i in range(len(content)):
                
                if content[m].strip()=="Company name:":
                    company_name.append(content[m+1].strip("\n"))

                #if content[m].strip()=="P/E Ratio":
                #    pe_list.append(content[m+1].strip("\n"))

                elif content[m].strip()=="Shares Outstanding":
                    share_outstanding.append(content[m+1].strip("\n"))
                
                elif content[m].strip()=="EPS":
                    if (content[m+1].strip("\n"))=="":
                        eps_list.append("0")
                    else:
                        eps_list.append(content[m+1].strip("\n"))
                
                elif content[m].strip()=="Market Price":
                    if (content[m+1].strip("\n")==""):
                        market_price.append("0")
                    else:
                        market_price.append(content[m+1].strip("\n"))
                
                elif content[m].strip()=="PBV":
                    pb_value.append(content[m+1].strip("\n"))
                
                elif content[m].strip()=="180 Day Average":
                    average_180.append(content[m+1].strip("\n"))
                
                elif content[m].strip()=="Book Value":
                    if content[m+1].strip("\n")=="":
                        book_value.append("0")
                    else:
                        book_value.append(content[m+1].strip("\n"))
                
                
                elif content[m].strip()=="Last Traded On":
                    Last_trade.append(content[m+1].strip("\n"))
                
                elif content[m].strip()=="52 Weeks High - Low":
                    year_high_low_price.append(content[m+1].strip("\n"))
                
                
                elif content[m].strip()=="% Change":
                    today_change.append(content[m+1].strip("\n"))
                elif content[m].strip().startswith("Cash Dividend="):
                    cash_content=(content[m].strip("\n")).split("=")
                    cash_dividend_list.append(cash_content[1])
                 
                elif content[m].strip().startswith("Bonus Share="):
                    bonus_content=(content[m].strip("\n").split("="))
                    bonus_share_list.append(bonus_content[1])
                
                elif content[m].strip().startswith("Right Share="):
                    right_content=(content[m].strip("\n").split("="))
                    right_share_list.append(right_content[1])
                else:
                    pass
                m+=1
        def getting_marketcap(marketprice,shareoutstanding):
                for i in range(len(shareoutstanding)):
                    if(shareoutstanding[i]==""):
                        market_capitalization.append(0)
                    else:
                        temp_shareoutstanding=round(float((shareoutstanding[i][:-3]).replace(",","")),2)
                        temp_marketprice=round(float(marketprice[i].replace(",","")),2)

                        temp_marketcap=round(float(temp_marketprice)*float(temp_shareoutstanding),2)
                        temp_marketcap="{:,}".format(temp_marketcap)
                        market_capitalization.append(temp_marketcap)

        getting_marketcap(market_price,share_outstanding)

        def getting_real_pe(eps,market_price):
            
            for i in range(len(market_price)):
                temp_marketprice=round(float(market_price[i].replace(",","")),2)
                eps_for_pe=round(float(eps[i].split("(")[0].replace(",","")),0)
                
                if eps_for_pe==0.0:
                    pe_list.append(0)
                else:
                    real_pe=round(float(temp_marketprice)/float(eps_for_pe),2)
                    pe_list.append(real_pe)
        getting_real_pe(eps_list,market_price)

        os.remove(filenames)               
        def getting_intrinsic():
            global valuable_stocklist;
            global price_to_intinsic;
            global intrinsic_value;
            intrinsic_value=[]
            for i in range(len(eps_list)):
                eps_for_intrinsic=eps_list[i].split("(")[0]
                book_values=book_value[i].replace(",","")
                try:
                    intrinsic=round(math.sqrt(22.5*math.ceil(float(eps_for_intrinsic))*math.ceil(float(book_values))),2)
                except ValueError :
                    #print(round(math.sqrt(22.5*math.ceil(float(eps_for_intrinsic))*math.ceil(float(book_value[i]))),2))
                    intrinsic="0 (Negative number)"
                intrinsic_value.append(intrinsic) 

            valuable_stocklist={}
            for i in range(len(intrinsic_value)):
                temp_intrinsic=intrinsic_value[i]
                if temp_intrinsic=="0 (Negative number)":
                    temp_intrinsic="0"
                if math.ceil(float(market_price[i].replace(",","")))<math.ceil(float(temp_intrinsic)):
                    valuable_stocklist[company_name[i].replace(",","")]=market_price[i]
            
            price_to_intinsic=[]
            for i in range(len(intrinsic_value)):
                temp_intr_price=intrinsic_value[i]
                if temp_intr_price=="0 (Negative number)":
                    temp_intr_price="0"
                try:
                    intrinsic_ratio=round(math.ceil(float(market_price[i].replace(",","")))/math.ceil(float(temp_intr_price)),2)
                except ZeroDivisionError as f:
                    intrinsic_ratio="0 (Negative number)"
                price_to_intinsic.append(intrinsic_ratio)

        getting_intrinsic() 

        def getting_valueablebond():
            global valuable_bond
            valuable_bond={}
            if user_input==11 or all_sector==10:
                for i in range(len(market_price)):
                    temp_marketprice=float(market_price[i].replace(",",""))
                    if temp_marketprice!=0 and temp_marketprice<=1000:             # u can change the number whatever u want for coporate bond whose face value is usually 1000 so i would recommend dont put above 1050 when stock market is doing good and definely check the intrest yield.
                        valuable_bond[company_name[i]]=market_price[i]
        getting_valueablebond()
        
        def dictionay_format():
            global dict_value;
            dict_value={}
            m=1
            for i in range(len(company_name)):
                dict_value[m]={}
                dict_value[m]["Company name"]=company_name[i]
                dict_value[m]["Shares Outstanding"]=share_outstanding[i]
                dict_value[m]["Market Price"]=market_price[i]
                dict_value[m]["Market Capitalization"]=market_capitalization[i]
                dict_value[m]["Graham number"]=intrinsic_value[i]
                dict_value[m]["Price to Graham number"]=price_to_intinsic[i]
                dict_value[m]["EPS"]=eps_list[i]
                dict_value[m]["P/E Ratio"]=pe_list[i]
                dict_value[m]["Book Value"]=book_value[i]
                dict_value[m]["PBV"]=pb_value[i]
                dict_value[m]["180 Day Average"]=average_180[i]
                dict_value[m]["Last Traded On"]=Last_trade[i]
                dict_value[m]["52 Weeks High - Low"]=year_high_low_price[i]
                dict_value[m]["%Change"]=today_change[i]
                dict_value[m]["Cash Dividend"]=cash_dividend_list[i]
                dict_value[m]["Bonus Share"]=bonus_share_list[i]
                dict_value[m]["Right Share"]=right_share_list[i]
                m+=1
            print()
            temp="Company Id"
            if all_sector is not None:
                print(Fore.GREEN+f"*******************************{(names[all_sector]).upper()}**************************************".center(90," "))
            else:
                print(Fore.GREEN+f"*********************************************************************".center(90," "))
            for i,j in dict_value.items():
                
                print(f"{temp:>50s} : "+str(i) )
                for k in j:
                    print(f"{str(k):>50s} : {str(j[k])}")
                print()
                print(Fore.GREEN+"************************************************************************************".center(90," "))
        dictionay_format()
        
        print(Fore.BLUE+"                                                          [ REPORT: ]                                 ")
        if user_input==11:
            if valuable_bond:              #bond first priroty
                print("".center(120,"*"))
                print(Fore.GREEN+Style.BRIGHT+"The valuable bond trading less than 1000(face value): ")
                for i,j in valuable_bond.items():
                    print(Fore.GREEN+Style.BRIGHT+"    "+str(i)+" : "+str(j))
            else:
                print(Fore.RED+Style.BRIGHT+"Remainder:None of the valuable bond found less that 1000(face value).")
        elif valuable_stocklist:
            print("".center(120,"*"))
            print(Fore.GREEN+Style.BRIGHT+"The valueable stocks according to graham are: ")
            for i,j in valuable_stocklist.items():
                print(Fore.GREEN+"    "+str(i)+" : "+str(j))
        else:
            print(Fore.RED+Style.BRIGHT+"Remainder:None of the valueable stock found according to graham formula.")
        print(Fore.RED+Style.BRIGHT+"Remainder:Dont Forget to analyze the company.")
        print("")
        print(Fore.RESET)
        print("END".center(150,"*"))

        time_of_file=time.strftime("%y_%m_%d_%H_%M")


        if all_sector is not None:
            format_filenames="formatted_"+real_names[all_sector]+"_"+time_of_file
            if intrinsic_input=="y" or intrinsic_input=="yes":
                if valuable_stocklist:
                    for i,j in valuable_stocklist.items():
                        with open('intrinsic_stocks','a') as g:
                            g.write(str(i)+" : "+str(j)+"\n")
                            g.write("*********************************************"+"\n")
                elif all_sector==10:
                    if valuable_bond:
                        for i,j in valuable_bond.items():
                            with open('intrinsic_stocks','a') as k:
                                k.write(str(i)+" : "+str(j)+"\n")
                                k.write("********************************************"+"\n")
        else:
            format_filenames="formatted_"+real_names[user_input-1]+"_"+time_of_file
        

        with open(format_filenames,'a') as l:
            j=0
            for i in range(len(company_name)):
                l.write("Company Name : "+str(company_name[j])+"\n")
                l.write("Share outstanding : "+str(share_outstanding[j])+"\n")
                l.write("Market price : "+str(market_price[j])+"\n")
                l.write("Market Capitalization : "+str(market_capitalization[j])+"\n")
                l.write("Eps : "+str(eps_list[j])+"\n")
                l.write("PE Ratio : "+str(pe_list[j])+"\n")
                l.write("Book Value : "+str(book_value[j])+"\n")
                l.write("Price to book value : "+str(pb_value[j])+"\n")
                l.write("Graham number : "+str(intrinsic_value[i])+"\n")
                l.write("Price to Graham number : "+str(price_to_intinsic[i])+"\n")
                l.write("Last Traded On : "+str(Last_trade[j])+"\n")
                l.write("'%' change : "+str(today_change[j])+"\n")
                l.write("average 180 : "+str(average_180[j])+"\n")
                l.write("52 weeks high-low : "+str(year_high_low_price[j])+"\n")
                l.write("Cash Dividend : "+str(cash_dividend_list[i])+"\n")
                l.write("Bonus Share : "+str(bonus_share_list[i])+"\n")
                l.write("Right Share : "+str(right_share_list[i])+"\n")
                l.write("***********************************************************************"+"\n")
                j+=1

    def program_sequnce():        

        getting_sector()
        if user_input<17:
            global listed_companies;
            global ticker_list
            ticker_link=f"http://nepalstock.com/company/index/1/stock-symbol/asc/YTo0OntzOjEwOiJzdG9jay1uYW1lIjtzOjA6IiI7czoxMjoic3RvY2stc3ltYm9sIjtzOjA6IiI7czo5OiJzZWN0b3ItaWQiO3M6MToiOCI7czo2OiJfbGltaXQiO3M6MzoiMzAwIjt9?stock-name=&stock-symbol=&sector-id={sectors[names[user_input-1]]}&_limit=300%22"
            try:
                get_ticker(ticker_link);
            except:
                listed_companies={1:['ADBL', 'BOKL', 'CBL', 'CCBL', 'CZBIL', 'EBL', 'GBIME', 'HBL', 'JBNL', 'KBL', 'LBL', 'MBL', 'MEGA', 'NABIL', 'NBB', 'NBL', 'NCCB', 'NIB', 'NICA', 'NMB', 'PCBL', 'PRVU', 'SANIMA', 'SBI', 'SBL', 'SCB', 'SRBL'],2:['BFC', 'CEFL', 'CFCL', 'CFL', 'CMB', 'GFCL', 'GMFIL', 'GUFL', 'HATH', 'HFL', 'ICFC', 'JFL', 'LFC', 'MFIL', 'MPFL', 'NFS', 'NSM', 'PFL', 'PROFL', 'RLFL', 'SFC', 'SFCL', 'SFFIL', 'SIFC', 'SYFL', 'UFL'],3:['CGH', 'OHL', 'SHL', 'TRH', 'YHL'],4:['AVU', 'BNL', 'BNT', 'BSL', 'BSM', 'FHL', 'GRU', 'HBT', 'HDL', 'JSM', 'NBBU', 'NKU', 'NLO', 'NVG', 'RJM', 'SBPP', 'SHIVM', 'SRS', 'UNL'],5:['NFD', 'NRIC', 'NTC'],6:['AHPC', 'AKJCL', 'AKPL', 'API', 'BARUN', 'BHL', 'BNHC', 'BPCL', 'CHCL', 'CHL', 'DHPL', 'DORDI', 'GHL', 'GLH', 'GVL', 'HDHPC', 'HPPL', 'HURJA', 'JOSHI', 'KKHC', 'KPCL', 'LEC', 'MBJC', 'MEN', 'MHNL', 'MKJC', 'NGPL', 'NHDL', 'NHPC', 'NYADI', 'PMHPL', 'PPCL', 'RADHI', 'RFPL', 'RHPC', 'RHPL', 'RRHP', 'RURU', 'SAHAS', 'SHEL', 'SHPC', 'SJCL', 'SPC', 'SPDL', 'SSHL', 'TPC', 'UMHL', 'UMRH', 'UNHPL', 'UPCL', 'UPPER'],7:['BBC', 'NTL', 'NWC', 'STC'],8:['AIL', 'EIC', 'GIC', 'HGI', 'IGI', 'LGIL', 'NICL', 'NIL', 'NLG', 'PIC', 'PICL', 'PRIN', 'RBCL', 'SGI', 'SIC', 'SICL', 'SIL', 'UIC'],9:['BHBL', 'CORBL', 'EDBL', 'GBBL', 'GDBL', 'GRDBL', 'HAMRO', 'JBBL', 'KNBL', 'KRBL', 'KSBBL', 'LBBL', 'MDB', 'MLBL', 'MNBBL', 'NABBC', 'NIDC', 'ODBL', 'SADBL', 'SAPDBL', 'SBBLJ', 'SHBL', 'SHINE', 'SINDU', 'TMDBL'],10:[],11:['ADBLB', 'ADBLB86', 'ADBLB87', 'ADBLD83', 'BOKD2079', 'BOKD86', 'CCBD88', 'CIZBD86', 'GBBD85', 'GBD80/81', 'GBILD86/87', 'GWFD83', 'HBLD83', 'ICFCD83', 'JBBD87', 'KBLD86', 'KSBBLD87', 'LBLD86', 'LBLD88', 'MBLD2085', 'MBLD87', 'MFLD85', 'MND84/85', 'NBBD2085', 'NBLD82', 'NBLD85', 'NBLD87', 'NCCD86', 'NIBD2082', 'NIBD84', 'NICAD 85/86', 'NICAD8182', 'NICAD8283', 'NICD83/84', 'NICD88', 'NMBD2085', 'NMBD87/88', 'NMBEB92/93', 'PBD85', 'PBLD84', 'PBLD86', 'PBLD87', 'RBBD83', 'SAND2085', 'SBD87', 'SBIBD86', 'SBLD2082', 'SBLD83', 'SBLD84', 'SDBD87', 'SRBLD83', 'SRD80'],12:['EBLCP'],13:['CMF1', 'CMF2', 'GIMES1', 'KEF', 'LEMF', 'LUK', 'MMF1', 'NBF2', 'NBF3', 'NEF', 'NIBLPF', 'NIBSF2', 'NICBF', 'NICGF', 'NICSF', 'NMB 50', 'NMB50', 'NMBHF1', 'PSF', 'RMF1', 'SAEF', 'SBCF', 'SEF', 'SEOS', 'SFMF', 'SIGS2', 'SLCF'],14:['ACLBSL', 'AKBSL', 'ALBSL', 'AMFI', 'CBBL', 'CLBSL', 'CYCL', 'DDBL', 'FMDBL', 'FOWAD', 'GBLBS', 'GGBSL', 'GILB', 'GLBSL', 'GMFBS', 'ILBS', 'JALPA', 'JBLB', 'JSLBB', 'KLBSL', 'KMCDB', 'LLBS', 'MERO', 'MKLB', 'MLBBL', 'MLBS', 'MLBSL', 'MMFDB', 'MSLB', 'MSMBS', 'NADEP', 'NAGRO', 'NESDO', 'NICLBSL', 'NLBBL', 'NMBMF', 'NMFBS', 'NSLB', 'NUBL', 'RMDC', 'RSDC', 'RULB', 'SABSL', 'SAMAJ', 'SDESI', 'SDLBSL', 'SKBBL', 'SLBBL', 'SLBS', 'SLBSL', 'SMATA', 'SMB', 'SMFBS', 'SMFDB', 'SPARS', 'SWBBL', 'SWMF', 'ULBSL', 'USLB', 'VLBS', 'WNLB'],15:['ALICL', 'GLICL', 'JLI', 'LICN', 'NLIC', 'NLICL', 'PLI', 'PLIC', 'RLI', 'SLI', 'SLICL', 'ULI'],16:['CHDC', 'CIT', 'ENL', 'HIDCL', 'NIFRA', 'NRN']}
                ticker_list=listed_companies[user_input]

            calling_websraping()
            retrive_value()
        elif user_input==17:
            nixa_watch.main()
        elif user_input==18:
            global intrinsic_input;
            global all_sector;
            intrinsic_input=input("Would you want to save all the stock below intrinsic value to seprate file [y/n]:").lower()
            all_sector=0
            for i in range(user_input-1):
                ticker_link=f"http://nepalstock.com/company/index/1/stock-symbol/asc/YTo0OntzOjEwOiJzdG9jay1uYW1lIjtzOjA6IiI7czoxMjoic3RvY2stc3ltYm9sIjtzOjA6IiI7czo5OiJzZWN0b3ItaWQiO3M6MToiOCI7czo2OiJfbGltaXQiO3M6MzoiMzAwIjt9?stock-name=&stock-symbol=&sector-id={sectors[names[all_sector]]}&_limit=300%22"
                get_ticker(ticker_link)
                calling_websraping()
                retrive_value()
                all_sector+=1
            exit();
        else:
            print("please enter the valid sector.")
        
    program_sequnce()
except Exception as e:
    print(traceback.format_exc())
    print(e)
    print("Ugh!!!Something went wrong!")
