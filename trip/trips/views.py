from django.http import HttpResponse
from pymongo.connection import Connection
import json
from django.shortcuts import render_to_response
from bson import json_util
from bson.json_util import default



connection = Connection('localhost', 27017)
db = connection.tripedia


def productids(request):
    #return HttpResponse((db['tripcollection'].find()))
    entity = db['tripcollection'].find()
    if not entity:
        return HttpResponse("Error! Please try again later.")
    return HttpResponse(entity)

def search_form(request):
    return render_to_response('trips/search_form.html')

def search(request):
    if 'from' in request.GET and 'time' in request.GET:
        json_docs = []
        entity = db['tripcollection'].find({"name": request.GET['from'],"time":{'$lt':int(request.GET['time'])*3600}})
        json_docs = json.dumps(list(entity), default=json_util.default, sort_keys=True, indent=3)
        message = json_docs
        variables = {"members": json.loads(message,object_hook=json_util.object_hook ),"from":request.GET['from'],"time":request.GET['time']}
        return render_to_response('trips/display.html',variables)
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


   