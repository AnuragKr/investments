import requests,json,re
#---------------------------------

#Initialising Dictionary
D_invest = {} #Dictionary which will container Investor:[List of Company He/She Invested]
D_value = {} #Dictionary which will contain Comany:Valuation By Investor
D_avg = {} #Dictionary which will contain Investor:Toatl Amount invested
def extractInfo(url):
    if(len(url)>0):
         #----------------------------
         #Getting JSON Data From URL Using Requests Module
         r = requests.get(url)
         data = json.loads(r.text)#Loading JSON Data

         #-------------------------------
         #Regular Expression Used For Searching Particular Pattern Or Extracting Out Particular String
         investor = re.compile("investors")
         name = re.compile("Kevin")
         thousand = re.compile("\$((\d+\.\d+)|(\d+))K")
         million = re.compile("\$((\d+\.\d+)|(\d+))M")
         percentage = re.compile("((\d+)|(\d+\.\d+))%")

         #---------------------------------
         #Analysing JSON Data as Dictionary
         for key,val in data.items():
             L = data[key] #Getting a value of every key which denotes episode as List
             #-------------------------------------------
             #Now we have lists regarding one episode contain all info as dictionary 
             for j in range(len(L)):
                 for k,v in L[j].items():#Going one by one attributes of Dictionary
                     match = investor .search(k)#Finding a key investors
                     if(match):
                         if v:#Accepting those investors who funded
                              li = []#List of name of investor
                              temp = v.find("and")#Case where name contains "and" just separating them
                              if(temp > 0):
                                  l = v.replace("and",",")
                                  li = l.split(',')
                                  li[0]=li[0].replace('\n','')
                                  li[1]=li[1].replace('\n','')
                              else:
                                  li = v.split(",")
                              for i in li:
                                  if (len(i)>1):
                                      match = name.search(i)
                                      if(match):
                                          lt = i.strip(' ').split(' ')
                                          if (len(lt)>2):
                                              i = lt[0]+" "+ lt[1]+lt[2]
                                          else:
                                              i = lt[0]+" " +lt[1]
                                      inv_name = i.strip(' ')
                                      D_invest[inv_name]=D_invest.setdefault(inv_name,[])#Creating new key(name of investors) with empty list of companies
                                      comp_name = L[j]['company']['title']#Taking out Company Name
                                      D_invest[inv_name].append(comp_name.replace('\xa0', ' '))
                                      D_value[comp_name]=D_value.setdefault(comp_name,1)#Creating new key(name of company) with value(valuation amount)
                                      inv_amount = L[j]['kitna']
                                      m = inv_amount.split('for')#Spliting a string of investing amount
                                      match = thousand.search(m[0])
                                      if(match):
                                          invest_amount = float(match.group(1))*1000#For investment in K
                                      match = million.search(m[0])
                                      if(match):
                                          invest_amount = float(match.group(1))*1000000#For investment in M
                                      match = percentage.search(m[1])
                                      if(match):
                                          percent = float(match.group(1))#For Percentage
                                      final_value = (invest_amount/percent)*100 #Calculating Valuation By Investor of company
                                      D_value[comp_name]=round(final_value)
                                      D_avg[inv_name] = D_avg.setdefault(inv_name,1)#Creating new key(name of investors) with value(Invested Amount)
                                      D_avg[inv_name] += invest_amount
    else:
        print("Empty String Given")


# Getting list of all investors in a sorted order who invested in more number of companies

def invComp():
    print("A list of all the investors that invested, along with the companies they invested in, sorted by the investor with maximum number of investments")
    print("---------------------------------------------------------------------------------------------------")
    ranked = sorted(D_invest.items(),key=lambda e:len(e[1]),reverse=True)#Doing Sorting Bases On Number Of Companies
    for i in range(len(ranked)):
        print("\n{} : {}".format(ranked[i][0],ranked[i][1]))#Printing As Per Given Format

#Representing list of company with their predicted full current value
        
def compValue():
    print("\nValuation of the comapny by the Investor")
    print("--------------------------------------------------------------------------------------------------")
    ranked = sorted(D_value.items(),key=lambda e:e[1],reverse=True)
    for i in range(len(ranked)):
        print("\n{} : ${}".format(ranked[i][0],ranked[i][1]))
#Representing Total Amount And Average Amount invested by an Investor

def invAvg():
    print("\nTotal Amount  and Average Amount Invested By an Investor")
    print("--------------------------------------------------------------------------------------------------")
    ranked = sorted(D_avg.items(),key=lambda e:e[1],reverse=True)
    for i in range(len(ranked)):
        print("\n{} : Total Investment ${} : average investment ${:.2f}".format(ranked[i][0],ranked[i][1],ranked[i][1]/len(D_invest[ranked[i][0]])))

#-----------------------------------------------
#Main Function
extractInfo('https://gist.githubusercontent.com/murtuzakz/4bd887712703ff14c9b0f7c18229b332/raw/d0dd1c59016e2488dcbe0c8e710a1c5df9c3672e/season7.json')
invComp()
compValue()
invAvg()

    

        
