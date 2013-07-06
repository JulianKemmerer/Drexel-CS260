#!/usr/bin/env python


from array import *
from list_array import *


def makeTrie():
	allWords = []
	f = open("AliceInWonderland.txt","r");
	lines = f.readlines();
	for i in lines:
		thisline = i.split(" ");	
		for j in thisline:
			if j!="":
				allWords.append(j.strip())
	x=ListArray()
	for word in allWords:
		for letter in word:
			if (word!=""):
				x.insert(letter,x.end())
		x.insert("$",x.end())
	count=0
	counter=0
	while(x.retrieve(counter)!=None):
		if x.retrieve(counter)=="$":
			count=count+1
		counter=counter+1
	return count


print "The purpose of this program is to create a trie of all the words appearing in AliceInWonderland.txt, and to find the size of that trie."
print "The program does this by creating an array list containing all the words that are in Alice in Wonderland."
print "It then iterates through each word, and adds the corresponding letters in order to the list_array implementation. The letters following each letter are stored in a list. At the end of each word, a '$' character is added to indicate the end of a unique word. The method then counts the number of occurences of the '$' character, and returns that number as the size of the trie." 

print "The size of the trie of AliceInWonderland.txt is:",makeTrie(),"."


