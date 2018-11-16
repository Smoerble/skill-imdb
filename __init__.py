# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import requests
import json

def getRatingFor(title):
    baseURL = "http://www.omdbapi.com/?apikey=7726e540&"
    request = baseURL + "t=" + title
    #print request
    r = requests.get(request)
    imdbinfo = r.json()
    if "Error" in imdbinfo:
        LOG.info(imdbinfo["Error"])
        return "Es tut mir Leid, aber ich kenne %s noch nicht." % title
        #return "I am sorry, I don't know the movie %s" % title
    #		sys.exit()
    imdbrating = imdbinfo["imdbRating"]
    outtext = "%s has a IMDB rating of %s." % (imdbinfo["Title"], imdbrating)
    return outtext

def getActorsFor(title):
    baseURL = "http://www.omdbapi.com/?apikey=7726e540&"
    request = baseURL + "t=" + title
    #print request
    r = requests.get(request)
    imdbinfo = r.json()
    if "Error" in imdbinfo:
        LOG.info(imdbinfo["Error"])
        return "Es tut mir Leid, aber ich kenne %s noch nicht." % title
        #return "I am sorry, I don't know the movie %s" % title
    #		sys.exit()
    actors = imdbinfo["Actors"]
    outtext = "%s has the following actors %s." % (imdbinfo["Title"], actors)
    return outtext

def getMovieFromPhrase(phrase, keyword):
    output = phrase.split(keyword)
    return output[-1].strip()


# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class ImdbSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(ImdbSkill, self).__init__(name="ImdbSkill")

    def initialize(self):
        imdbIntent = IntentBuilder("ImdbIntent").require("Imdb").build()
        self.register_intent(imdbIntent, self.handle_imdb_intent)

        imdbActorsIntent = IntentBuilder("ActorsIntent").require("Actors").build()
        self.register_intent(imdbActorsIntent, self.handle_actors_intent)

        dialogIntent = IntentBuilder("DialogIntent").require("Hello").build()
        self.register_intent(dialogIntent, self.handle_dialog_intent)

    def handle_imdb_intent(self, message):
        movieTitle = getMovieFromPhrase(message.data.get('utterance'), "rating hat")
        LOG.info("Movie Title: " + movieTitle)
        rating = getRatingFor(movieTitle)
        LOG.info("Message: " + rating)
        self.speak_dialog(rating)

    def handle_actors_intent(self, message):
        movieTitle = getMovieFromPhrase(message.data.get('utterance'), "Schauspieler für")
        LOG.info("Movie Title: " + movieTitle)
        actors = getActorsFor(movieTitle)
        LOG.info("Message: " + actors)
        self.speak_dialog(actors)

    # The "handle_xxxx_intent" function is triggered by Mycroft when the
    # skill's intent is matched.  The intent is defined by the IntentBuilder()
    # pieces, and is triggered when the user's utterance matches the pattern
    # defined by the keywords.  In this case, the match occurs when one word
    # is found from each of the files:
    #    vocab/en-us/Hello.voc
    #    vocab/en-us/Imdb.voc
    # In this example that means it would match on utterances like:
    #   'imdb'
    #   'movie database'

    # In this case, respond by simply speaking a canned response.
    # Mycroft will randomly speak one of the lines from the file
    #    dialogs/en-us/imdb.hello.dialog
    def handle_dialog_intent(self, message):
        self.speak_dialog("imdb.hello")

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    def stop(self):
        return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return ImdbSkill()
