import requests
import json

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


def getMovieFromPhrase(phrase):
    output = phrase.split("rating for")
    return output[-1]


def main():
    while True:
        statement = raw_input("> ")
        if statement == "quit":
            break
        movie = getMovieFromPhrase(statement).strip()
        print ("found Movie: %s" % movie)
        info = getRatingFor(movie)
        print (json.dumps(info, indent=2))
        tts(info)


if __name__ == "__main__":
    main()
