# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:56:11 2019

-|---|-----------------|---|-
-|   |                 |   |-
-|   |my text goes here|   |-
-|   |                 |   |-
-|---|-----------------|---|-

@author: dahaynes
"""

userSentence = input("Please enter some text: ")

testSentence = "David Haynes"

borderChar = "*"
whiteSpace = " "
margin = 4

len(testSentence)+ (margin*2)
line1 = borderChar * (margin + len(testSentence) + margin + 2 )
line2 = borderChar + (whiteSpace * (margin + len(testSentence) + margin )) + borderChar
line3 = borderChar + (whiteSpace * margin) + testSentence + (whiteSpace * margin) + borderChar
