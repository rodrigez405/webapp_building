from flask import Flask, url_for
import os
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello():
    # import the magic random picker
    import random, urllib2
    
    # list of things to pick from
    url_for_list = "https://raw.githubusercontent.com/bellcodo/laughing-meme/master/typing_options.lst"
    raw_typing_options = urllib2.urlopen(url_for_list)
    list_of_options = raw_typing_options.read()
    #print "DEBUG - raw typing options is %s, %s" % (raw_typing_options, list_of_options)
    typing_options = list_of_options.split()
    
    # find a way to pick something
    typing_choice = random.choice(typing_options)
    return url_for('static', 'img/typing_choice')

if __name__ == "__main__":
    # go get the PORT from the environment
    port = os.environ.get("PORT")
    # run the app with the port and bind to any ip
    app.run(
      "0.0.0.0"
    , int(port)
    )
