import os
import sys
import threading
import time
from urllib.parse import urljoin
import urllib.request
import requests
from bs4 import BeautifulSoup

def extractor(sites):
    '''Extract pdfs from a single or a list of urls or html filenames passed.'''
    if_file=os.getcwd()
    os.makedirs('DownloadedPdfs', exist_ok=True)
    os.chdir('DownloadedPdfs')
    return_dir= os.getcwd()
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
      "X-Requested-With": "XMLHttpRequest"}

    for i in range(len(sites)):
        site = sites[i].strip()
        isAFile=False

        if (len(site.split('.'))==2) and ('.html' in site):
            isAFile=True
            os.chdir(if_file)
            try:
                with open(site, 'r', encoding='utf8') as f:
                    content= f.read()
            except Exception as e:
                print(e)
                print('Place file: ' + site + ' in ' + os.getcwd())
        
        if len(site.split('//'))>1:
            fname = site.split('//')[1]
        else:
            fname = site
            site = 'http://'+site
        
        print('Extracting pdfs from: ' + site)
        
        try:
            if isAFile==False:
                req=urllib.request.Request(site, headers=header)
                content = urllib.request.urlopen(req).read()
                soup = BeautifulSoup(content, 'html.parser')
            else:
                soup = BeautifulSoup(content, 'html.parser')
        except Exception as e:
            print(e)

        os.chdir(return_dir)
        os.makedirs(fname, exist_ok=True)
        os.chdir(fname)

    links = soup.find_all('a')
    pdflist=[]

    for link in links:
        z= link.get('href')
        if '.pdf' in z:
            pdflist.append(urljoin(site,z))
    total_files=len(pdflist)
    
    print(str(total_files) + ' pdf files are available in ' + site)
    print('')
    j=0
    fourlists=[[],[],[],[]]
    
    for k in range(len(pdflist)):
        rem=k%4
        fourlists[rem].append(pdflist[k])

    fourthreads=[]
 
    for m in range(4):
        arg=fourlists[m]
        if len(arg)!=0:
            threadname='athread'+str(m)
            threadname =threading.Thread(target= downloader, args=[arg])
            fourthreads.append(threadname)

    for thread in fourthreads:
        thread.start()

    for thread in fourthreads:
       thread.join()

    print('')   
    print(str(total_files) + ' pdf files extraced from ' + site+ ' at '+ os.getcwd())

def downloader(threadlist):
    for j in range(len(threadlist)):
        filename= threadlist[j].split('/')[-1]
        try:
            response =requests.get(threadlist[j])
            print('Downloading... ' + filename)
            with open(filename, 'wb') as file:
                file.write(response.content)
                print('Downloaded ' + filename)
                print('')
        except:
            print('Failed to download ' +filename )
    

if len(sys.argv)>1:
    sites = sys.argv[1:]
else:
    print('Enter URL (you can also pass list of urls using comma as seperator) OR You can also give filename of htmlfile: ' )
    sites=input()
    sites= sites.split(',')

    
starttime=time.time()

if __name__ == '__main__':
    extractor(sites)

endtime= time.time()
print('Total time taken by download is', endtime-starttime)
