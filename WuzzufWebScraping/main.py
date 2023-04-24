import requests
from bs4 import BeautifulSoup as bs
import  pandas as pd

search = input("Enter the query: ")

t=0
h = 0

diction = {"title": [], "location": [], "types": [], "fields": [], "technos": []}

df = pd.DataFrame(diction)

print("loading",end=".")
while t!=-1 :
    print(".",end="")
    link = "https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=" + search.replace(' ', "%20")+"&start="+str(t)
    t+=1


    response = requests.get(link)

    soup = bs(response.content, "lxml")

    data=soup.findAll("div",{"class":"css-1gatmva e1v1l3u10"})

    if len(data)==0:
        break
    if len(data)<15:
        t=-1



    for i in data:
        title=i.find("a",{"class":"css-o171kl"})
        location = i.find("span", {"class": "css-5wys0k"})
        types = i.findAll("span", {"class": "css-1ve4b75 eoyjyou0"})


        typesText=""
        fieldsText = ""
        technosText = ""


        fields = i.findAll("a", {"class": "css-o171kl"})
        technologies = i.findAll("a", {"class": "css-5x9pm1"})
        # print(f"title: {title.text}",end="\t\t")
        # print(f"location: {location.text}",end="\n")
        # print("job type: " ,end="")
        for  i in types:
            # print(i.text,end=" ")
            typesText+=(i.text+" ")
        # print("\n",end="")
        # print("fields: ",end="")
        for i in fields:
            # print(i.text,end= " ")
            fieldsText+=(i.text)
        # print("\n", end="")

        # print("technologies needed: ",end=" ")

        for i in technologies:
            # print(i.text, end=" ")
            technosText+=(i.text)

        df.loc[h]=[title.text,location.text,typesText,fieldsText,technosText]
        h+=1
        # print("\n", "")
        # print("----------------------------------------------------------------",end="\n\n")


print("")
print("do you want to show data or load it to your device")
respnse=int(input("1-show \t\t 2-load\n"))
if respnse==1:
    print(df)
else:
    s=input("enter the fileName you want data to be loaded to ")
    df.to_csv(s+".csv",index=False)
    print("Scraping done successfully")










