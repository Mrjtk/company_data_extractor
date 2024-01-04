import requests
from bs4 import BeautifulSoup
import time 
from time import sleep

import csv
f=open("Companydata.csv",'w+')
writer=csv.writer(f)
writer.writerow(["Company Name","Status","Slug","About","Facebook Link","X Link","Instagram Link","Linkedin Link","Pinterest Link","Youtube","Address1","Address2","Pincode","Location name /Lat,Long",'Country',"State",'City','Category','Sub Category','Class of Company',"CIN",'ROC','Registration Number','Employment Details','Number of Employees','Authorized Capital',"Paid up Capital",'Email Address','Phone Number',"Website Link"])

f=open('compny.txt','r+')
asdf=f.readlines()
for companyname in asdf:
                
                b=companyname.upper()
                propername=b.replace(" ","-")
                def find_cin(companyname):
                                url2=f"https://www.zaubacorp.com/companysearchresults/{companyname}"
                                headers = {
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                                    }

                                page2=requests.get(url2,headers=headers)
                                soup2=BeautifulSoup(page2.content,'html')
                                company_data2=(soup2.get_text())
                                f=open("search.txt",'w')
                                f.write(company_data2)
                                f.close()
                                f=open("search.txt",'r')
                                a=f.readlines()
                                longest_word = max(a, key=len)

                                a=''
                                cin=''
                                for i in longest_word:
                                    a+=i
                                    if "CINNameAddress" in a:
                                        cin+=i
                                        if len(cin)<=21:
                                            pass
                                        else:
                                            break
                                    else:
                                        pass
                                cin=cin[1:]
                                return cin




                cin=find_cin(companyname)


                def compydata(a,b):
                    compy_name=a
                    cia_no=b
                    
                    
                    url2="https://www.zaubacorp.com/company/{}/{}".format(compy_name,cia_no)
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                    }

                    page2=requests.get(url2,headers=headers)
                    soup2=BeautifulSoup(page2.content,'html')
                    company_data2=(soup2.get_text())
                    j=open("company_data2.txt",'w')
                    j.write(company_data2)
                    j.close()

                compydata(propername,cin)

                lencomp = b.split()
                lenword=len(lencomp)

                f=open('company_data2.txt','r+')
                data1=f.read()
                data = data1.split()
                companyname=''
                for i in data:
                    
                    companyname+=i    
                    companyname+=' '
                    if i =="Company,":
                            break
                    else:
                        pass
                companyname=companyname[:-11]
                print(companyname)

                cin=''

                for i in data:
                    if i =="(CIN)":
                            ciapo=data.index("(CIN)")
                            no=data[ciapo+1]
                            cin+=no
                            break
                    else:
                        pass
                print(cin)
                authrisedcaptial=''
                paidcapital=''
                for i in data:
                    if i =="authorized":
                            authcap=data.index("authorized")
                            athcap=data[authcap+5]
                            authrisedcaptial+=athcap
                            break
                    else:
                        pass


                for i in data:
                    if i =="paid":
                            paidcap=data.index("paid")
                            pdcap=data[paidcap+5]
                            paidcapital+=pdcap
                            break
                    else:
                        pass
                

                company_status=""
                
                
                px=lenword+4
                for i in data:
                    if i =="status":
                            st=data.index("status")
                            sts=data[st+px]
                            company_status+=sts
                            break
                    else:
                        pass
                print(company_status)







                slug=''
                about=''
                Facebook=''
                xlink=''
                insta=''
                linkd=''
                pinterest=''
                youtube=''
                Address1=''
                address2=''
                pincode=''
                location=''
                Country="India"
                state=''
                city=""
                catagory=''
                subcatagory=''
                classofcompy=''
                roc=""
                Registrationno=''
                employmentdetails=''
                noemployes=''
                email=''
                phoneno=''
                Website=''

                writer.writerow([propername,company_status,slug,about,Facebook,xlink,insta,linkd,pinterest,youtube,Address1,address2,pincode,location,Country,state,city,catagory,subcatagory,classofcompy,cin,roc,Registrationno,employmentdetails,noemployes,authrisedcaptial,paidcapital,email,phoneno,Website])
                sleep(0.3)
































