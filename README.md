This is a math quiz that I created as my 1st personal project using Python. Please point out what I can do better please! Details about the code here: 



Libraties used: random, time, threading ("import {insert libraty_name})


Main function (line 45):
Inputs: users' name
Established vars: 'questions', 'questions_count', 'score', 'three_words'

This function gets the users' name and is where other functions like "questions_generator()", "timer()",  "answers()". Basically this function serves the purpose of allowing the program itself to function through calling these functions whilist using features of lists, for-loops, error-handling, if-else statements, sleep, and varaibles.


def timer(): 

Purpose: Used to as it is countdown from 30 (or any other whole number) to 0. Which once it reaches 0 or all the questions are answered, the program ends. Where the score of the user is said in both instances.

Features: while-loops, sleee(time library) and if-statements


def answers():

Purpose: Serves for the program to 'know' the answer before the user answers their questions. In other words, the numbers and operators generated from "def question_generator" function, and is used so the program 'knows' the answer before the user puts in their input.

Features: if-else statements, return


def question_generator():

Purpose: Basically two randomly generated numbers are picked from 1-20. The operators from '+', '-', '/', and  '*'; are also randomly choosen. Which it calls the "answers()" function so the algotithm itself knows the answer so it can check if the users' answer is correct or not. Lastly, it returns an f-string that is basically the question itself (eg: "What is 5 + 5 = ")

Features: f-strings, global vars, if-else statements, return.

