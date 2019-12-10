from django.shortcuts import render
from django.http import HttpResponse
import requests
import bs4
# Create your views here.
page=requests.get('https://fabpedigree.com/james/mathmen.htm')

soup=bs4.BeautifulSoup(page.content, 'html.parser')

print("The list of 100 great mathematicians of all time:")
lists=soup.findAll('li')
x=[]
for list in lists:
   x.append(list.find('a').string)

def home(request):
    # return HttpResponse('Hello from home')


        d={
            'name': x,
            'college':'SXC'
        }
        return render(request,'home.html',d)




def bootcamp(boot):
    return HttpResponse("<h1>Hello from bootcamp</h1>")
