from bs4 import BeautifulSoup

out = open('out.txt','w',encoding='utf-8')
with open("1.html",encoding='utf-8') as file:
    soup = BeautifulSoup(file.read(),'lxml')
spo_datas = soup.find_all('div',class_='iCQtmPqY0QvkumAOuCjr')
for spo_data in spo_datas:
    str1 = spo_data.find('div',class_='Type__TypeElement-goli3j-0 fCtMzo t_yrXoUO3qGsJS4Y6iXX standalone-ellipsis-one-line').text
    str2 = spo_data.find('a').text
    str3 = str2+' '+str1+'\n'
    out.write(str3)
out.close()
