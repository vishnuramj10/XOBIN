# -*- coding: cp1252 -*-
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import re

scrap=Flask(__name__)

@scrap.route("/",methods =['GET','POST'])


def display():
    mov=[]
    if request.method == 'POST':
        gen=request.form['genre']
        if gen=='action':
            url = 'https://www.imdb.com/list/ls069349708/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
        elif gen=='comedy':
            url ='https://www.imdb.com/list/ls076233821/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
        elif gen=='horror':
            url='https://www.imdb.com/list/ls070259906/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
        elif gen=='romance':
            url='https://www.imdb.com/list/ls063141206/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
        elif gen=='thriller':
            url='https://www.imdb.com/list/ls051523000/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
        elif gen=='sci-fi':
            url='https://www.imdb.com/list/ls009668082/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
        elif gen=='animation':
            url='https://www.imdb.com/list/ls027345371/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
        elif gen=='mystery':
            url='https://www.imdb.com/list/ls000070494/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
        elif gen=='psy-thriller':
            url='https://www.imdb.com/list/ls053925669/?sort=user_rating,desc&st_dt=&mode=detail&page=1'

        response = requests.get(url)
        soup = BeautifulSoup(response.text,features="html.parser")
        movList= soup.find_all('h3',{'class':'lister-item-header'})
        movList=movList[:5]
        for i in movList:
            for j in i.find_all('a'):
                mov.append(j.text)
            

    return render_template('scrapping.html',mov=mov) 

                   
   


if __name__ == "__main__":
    scrap.run(debug=True)
