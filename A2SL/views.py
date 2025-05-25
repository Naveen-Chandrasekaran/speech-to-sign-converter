import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from django.contrib.staticfiles import finders
from django.contrib.auth.decorators import login_required




def home_view(request):
	return render(request,'home.html')


def about_view(request):
	return render(request,'about.html')


def contact_view(request):
	return render(request,'contact.html')

@login_required(login_url="login")
def animation_view(request):
    if request.method == 'POST':
        text = request.POST.get('sen')
        # Lowercasing and cleaning the sentence
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)

        # Tokenizing the sentence
        words = word_tokenize(text)
        tagged = nltk.pos_tag(words)

        # Tense detection
        tense = {
            "future": len([word for word in tagged if word[1] == "MD"]),
            "present": len([word for word in tagged if word[1] in ["VBP", "VBZ", "VBG"]]),
            "past": len([word for word in tagged if word[1] in ["VBD", "VBN"]]),
            "present_continuous": len([word for word in tagged if word[1] == "VBG"]),
        }

        # Stop words
        stop_words = set([
            "mightn't", 're', 'wasn', 'wouldn', 'be', 'has', 'that', 'does', 'shouldn', 'do',
            "you've", 'off', 'for', "didn't", 'm', 'ain', 'haven', "weren't", 'are', "she's",
            "wasn't", 'its', "haven't", "wouldn't", 'don', 'weren', 's', "you'd", "don't", 'doesn',
            "hadn't", 'is', 'was', "that'll", "should've", 'a', 'then', 'the', 'mustn', 'i', 'nor',
            'as', "it's", "needn't", 'd', 'am', 'have', 'hasn', 'o', "aren't", "you'll", "couldn't",
            "you're", "mustn't", 'didn', "doesn't", 'll', 'an', 'hadn', 'whom', 'y', "hasn't", 
            'itself', 'couldn', 'needn', "shan't", 'isn', 'been', 'such', 'shan', "shouldn't",
            'aren', 'being', 'were', 'did', 'ma', 't', 'having', 'mightn', 've', "isn't", "won't"
        ])

        # Lemmatizing and filtering stopwords
        lr = WordNetLemmatizer()
        filtered_text = []
        for w, p in zip(words, tagged):
            if w not in stop_words:
                if p[1] in ['VBG', 'VBD', 'VBZ', 'VBN', 'NN']:
                    filtered_text.append(lr.lemmatize(w, pos='v'))
                elif p[1] in ['JJ', 'JJR', 'JJS', 'RBR', 'RBS']:
                    filtered_text.append(lr.lemmatize(w, pos='a'))
                else:
                    filtered_text.append(lr.lemmatize(w))

        # Replace "I" with "Me" for consistency
        words = ['Me' if w == 'I' else w for w in filtered_text]

        # Adding tense indicators
        if max(tense.values()) > 0:
            probable_tense = max(tense, key=tense.get)
            if probable_tense == "past" and tense["past"] >= 1:
                words = ["Before"] + words
            elif probable_tense == "future" and tense["future"] >= 1:
                if "Will" not in words:
                    words = ["Will"] + words
            elif probable_tense == "present" and tense["present_continuous"] >= 1:
                words = ["Now"] + words

        # Matching animation videos or splitting into characters
        filtered_text = []
        for w in words:
            path = w + ".mp4"
            f = finders.find(path)
            if not f:
                filtered_text.extend(list(w))
            else:
                filtered_text.append(w)

        words = filtered_text

        return render(request, 'animation.html', {'words': words, 'text': text})
    else:
        return render(request, 'animation.html')





import os
import subprocess
from django.http import HttpResponseRedirect

def launch_translate_frontend(request):

    return HttpResponseRedirect('http://localhost:4200')




def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			# log the user in
			return redirect('animation')
	else:
		form = UserCreationForm()
	return render(request,'signup.html',{'form':form})



def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#log in user
			user = form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('animation')
	else:
		form = AuthenticationForm()
	return render(request,'login.html',{'form':form})


def logout_view(request):
	logout(request)
	return redirect("home")
