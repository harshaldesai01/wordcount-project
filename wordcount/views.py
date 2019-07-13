from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request,'home.html')

def count(request):
	fulltext = request.GET['fulltext']

	words = fulltext.split()
	words = [word.lower() for word in words]
	table = str.maketrans('', '', string.punctuation)
	stripped = [w.translate(table) for w in words]
	clean_word_list = [word for word in stripped if word not in stopwords_list]

	sortedwords = sorted(clean_word_list.items(), key=operator.itemgetter(1), reverse=True )

	return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})


def about(request):
	return render(request,'about.html')
