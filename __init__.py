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

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class ImdbSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(ImdbSkill, self).__init__(name="ImdbSkill")

    def initialize(self):
        intent = IntentBuilder("ImdbIntent").require("Imdb").build()
        self.register_intent(intent, self.handle_imdb_intent)

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
    def handle_imdb_intent(self, message):
        # In this case, respond by simply speaking a canned response.
        # Mycroft will randomly speak one of the lines from the file
        #    dialogs/en-us/imdb.dialog
        self.speak_dialog("imdb")
        LOG.info("**START**")
        LOG.info(message.data)
        LOG.info("****")
        LOG.info(message.data.get('phrase'))
        LOG.info("****")
        LOG.info(message.data.get('utterance'))
        LOG.info("****")
        LOG.info(message.data.get('MovieTitle'))
        LOG.info("**END**")		

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
