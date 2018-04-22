#!/usr/bin/envpython3
# coding: utf-8

import re
import os
import csv
from textract import process

class Proc(object):
    def __init__(self, file):
        self.filename = file

    def convertPDF(self):
        cwd = os.path.dirname(__file__) # get current location of script

        text = process(os.path.join('pdfbooks', self.filename)).decode('utf8')

        if not os.path.exists('txtbooks'):
            os.makedirs('txtbooks')

        self.filename = re.sub(r'\.pdf$', '.txt', self.filename)
        target = open(os.path.join(cwd,'txtbooks', self.filename), 'w')

        target.write(text)

        print(os.path.join(cwd,'txtbooks', self.filename))
        with open(os.path.join(cwd,'txtbooks', self.filename), 'r') as myfile:
            text=myfile.read()

        self.text = str(text)

    def get_text(self):
        return self.text

    def fname(self, txt, name1, name2, classification):
        #r = re.compile('%s((.*)?)%s'%(name1,name2),re.DOTALL)
        r = re.compile('%s(\s[\w]+(\.|\,|\!|\?|\-)?\s?){5,150}?%s|%s(\s[\w]+(\.|\,|\!|\?|\-)?\s?){5,150}?%s'%(name1,name2,name2,name1),re.DOTALL)
        csvfile = open('base11.csv', 'w')

        for m in r.finditer(txt):
            print(m.group(0))
            print('\n\n------------------------\n\n')


            w = csv.writer(csvfile, delimiter=',')
            w.writerow([str(m.group(0))])
