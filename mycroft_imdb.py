import sys
import requests
import json
import urllib
import pyttsx
from gtts import gTTS
import os

baseURL = "http://www.omdbapi.com/?apikey=7726e540&"

def getRatingFor(title):
	request = baseURL + "t=" + title 
	print request
	r = requests.get(request)
	imdbinfo = r.json()
	if "Error" in imdbinfo:
		print (imdbinfo["Error"])
#		sys.exit()
	imdbrating = imdbinfo["imdbRating"]
	outtext = "%s has a i.m.d.b. rating of %s." % (imdbinfo["Title"], imdbrating)
	return outtext

def tts(imdbinfo):
	speak = "osx"
	imdbrating = imdbinfo["imdbRating"]
	if (speak == "osx"):
		outtext = "%s hat ein i.m.d.b. rating von %s.\n" %(imdbinfo["Title"], imdbrating)
		print (outtext)
		os.system("say \"%s\"" %outtext)
	elif (speak == "gtts"):
#	print json.dumps(imdbinfo, indent=2)
		outtext = "%s hat ein iemdehbeh rating von %s.\n" %(imdbinfo["Title"], imdbrating)
		tts = gTTS(text=outtext, lang='de')
		tts.save("good.mp3")
		os.system("play -q good.mp3")
	elif (speak == "pyttsx"):
		engine = pyttsx.init()
		outtext = "%s hat ein i.m.d.b rating von %s.\n" %(imdbinfo["Title"], imdbrating)
		print (outtext)
#		engine.say(outtext)
		engine.say('Hallo text.')
		engine.runAndWait()
	else:
		print ("%s has a imdb rating of %s" %(imdbinfo["Title"],imdbrating))		

def getMovieFromPhrase(phrase):
	output = phrase.split("rating for")
	return output[-1]

def main():
    while True:
		statement = raw_input("> ")
		if statement == "quit":
			break
		movie = getMovieFromPhrase(statement).strip()
		print ("found Movie: %s" %movie)
		info = getRatingFor(movie)
		print (json.dumps(info, indent=2))
		tts(info)
 
 

if __name__ == "__main__":
    main() 
