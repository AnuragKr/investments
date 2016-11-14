import requests
import json
import re
D = {}
d = {}
D_avg = {}
r = requests.get('https://gist.githubusercontent.com/murtuzakz/4bd887712703ff14c9b0f7c18229b332/raw/d0dd1c59016e2488dcbe0c8e710a1c5df9c3672e/season7.json')
data = json.loads(r.text)
regex = re.compile("investors")
regex2 = re.compile("Kevin")
thousand = re.compile("\$((\d+\.\d+)|(\d+))K")
million = re.compile("\$((\d+\.\d+)|(\d+))M")
percentage = re.compile("((\d+)|(\d+\.\d+))%")
for key,val in data.items():
    L = data[key]
    for j in range(len(L)):
        str = ' '
        for k,v in L[j].items():
             match = regex.search(k)
             if(match):
                 if v:
                     li = []
                     temp = v.find("and")
                     if(temp > 0):
                         l = v.replace("and",",")
                         li = l.split(',')
                         li[0]=li[0].replace('\n','')
                         li[1]=li[1].replace('\n','')
                     else:
                        li = v.split(",")
                     #print(li)
                     for i in li:
                             if (len(i)>1):
                                 match = regex2.search(i)
                                 if(match):
                                     lt = i.strip(' ').split(' ')
                                     if (len(lt)>2):
                                         i = lt[0]+" "+ lt[1]+lt[2]
                                     else:
                                         i = lt[0]+" " +lt[1]
                                     #print(i.strip(' '))
                                 s = i.strip(' ')
                                 D[s]=D.setdefault(s,[])
                                 st = L[j]['company']['title']
                                 D[s].append(st.replace('\xa0', ' '))
                                 d[st]=d.setdefault(st,0)
                                 stc = L[j]['kitna']
                                 m = stc.split('for')
                                 #print(m)
                                 match = thousand.search(m[0])
                                 if(match):
                                     invest_amount = float(match.group(1))*1000
                                 match = million.search(m[0])
                                 if(match):
                                     invest_amount = float(match.group(1))*1000000
                                 match = percentage.search(m[1])
                                 if(match):
                                     percent = float(match.group(1))
                                 #print(invest_amount,percent)
                                 final_value = (invest_amount/percent)*100
                                 d[st]=round(final_value)
                                 D_avg[s] = D_avg.setdefault(s,1)
                                 D_avg[s] += invest_amount


# Getting list of all investors in a sorted order who invested in more number of companies
print("A list of all the investors that invested, along with the companies they invested in, sorted by the investor with maximum number of investments")
print("---------------------------------------------------------------------------------------------------")
ranked = sorted(D.items(),key=lambda e:len(e[1]),reverse=True)#Doing Sorting Bases On Number Of Companies
for i in range(len(ranked)):
    print("\n{} : {}".format(ranked[i][0],ranked[i][1]))#Printing As Per Given Format
    #print("\n")
#Representing list of company with their predicted full current value
print("--------------------------------------------------------------------------------------------------")
print("Valuation of the comapny by the Investor")
print("**************************************************************************************************")
ranked = sorted(d.items(),key=lambda e:e[1],reverse=True)
for i in range(len(ranked)):
    print("\n{} : ${}".format(ranked[i][0],ranked[i][1]))
    #print("\n")
print("**************************************************************************************************")
print("Total Amount  and Average Amount Invested By an Investor")
print("--------------------------------------------------------------------------------------------------")
ranked = sorted(D_avg.items(),key=lambda e:e[1],reverse=True)
for i in range(len(ranked)):
    print("\n{} : ${} : average investment ${:.2f}".format(ranked[i][0],ranked[i][1],ranked[i][1]/len(D[ranked[i][0]])))
    #print("\n")
print("--------------------------------------------------------------------------------------------------")
