# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 17:56:17 2016

@author: EnriqueAldana
"""

import webbrowser
topicList = ['nano', 'wire', 'photon']
for topic in topicList:
    webbrowser.open('http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&f=S&l=50&d=PTXT&RS=SPEC%2F%22graph%22&Refine=Refine+Search&Query=SPEC%2F%22'+topic+'%22')



