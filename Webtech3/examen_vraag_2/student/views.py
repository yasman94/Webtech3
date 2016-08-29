from django.shortcuts import render
import redis
import urllib2
import json

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def index(request):
    name = request.GET.get('name', '')
    exam = request.GET.get('exam', '')
    date = request.GET.get('date', '')
    reden = request.GET.get('reden', '')
    if name == '' or exam == '' or date == ''or reden == '':
        return index_without_params(request)
    else:
        return index_with_params(request, name.lower(), exam.lower(), date.lower(), reden.lower())

# Slechts een simpele form
def index_without_params(request):
    return render(request, 'student/index_form.html', {})


def index_with_params(request, name, exam, date, reden):

    response_val = json.loads(urllib2.urlopen('http://api.icndb.com/jokes/random?name=Yassine Aarab&exam=Webtech2&date=29/08/2016&reden=Afwezig').read())['value']
    joke = response_val['joke']
    id = response_val['id']
    key = name + ':' + exam + ':' + date + ':' + reden + ':' + str(id)


    if not r.exists(key):
        r.set(key, joke)

    return render(request, 'student/index_joke.html', { 'student' : name.capitalize() + ' ' + exam.capitalize()+ ' ' + date.capitalize()+ ' ' + reden.capitalize(),
                                                             'joke' : joke })
