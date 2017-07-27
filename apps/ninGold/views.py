from django.shortcuts import render, HttpResponse, redirect
from random import randrange
import datetime
# the index function is called when root is visited
def index(request):
    try:
        request.session['gold'],
        request.session['messages']
    except:
        request.session['gold'] = 0
        request.session['messages'] = []
    return render(request, "ninGold/index.html")

def process(request):
	location = request.POST['building']
	# Refer to the video to see how I refactored this code.
	if location == "farm":
		gold_earned = randrange(10,21)
	elif location == "cave":
		gold_earned = randrange(5,11)
	elif location == "house":
		gold_earned = randrange(2,6)
	elif location == "casino":
		gold_earned = randrange(-50,50)
	# We want to represent the color of the text as a part of the message. Since the message is now something more than the text on the screen, we want a container data structure (list, tuple, object, or dictionary) as the individual item in the session['messages'] list
	request.session['gold'] += gold_earned
	if gold_earned < 0:
		color = "red"
		new_string = "Went to casino and lost "+str(-gold_earned)+" gold. Ouch! "+str(datetime.datetime.now()) # remember to concatenate the numbers to the string after you convert them into strings!
	else:
		color = "green"
		new_string = "Went to "+location+" and got "+str(gold_earned)+" gold. "+str(datetime.datetime.now())
	new_dictionary = {
	"color":color,
	"message":new_string
	}
	request.session['messages'].insert(0,new_dictionary)
        return redirect('/')


