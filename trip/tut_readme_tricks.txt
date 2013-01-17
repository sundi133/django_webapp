	
While @ErenGüven shows you a nice manual approach to solving this json serializing issue, pymongo comes with a utility to accomplish this for you. I use this in my own django mongodb project:

import json
from bson import json_util

json_docs = []
for doc in cursor:
    json_doc = json.dumps(doc, default=json_util.default)
    json_docs.append(json_doc)
Or simply:

json_docs = [json.dumps(doc, default=json_util.default) for doc in cursor]
And to get them back from json again:

docs = [json.loads(j_doc, object_hook=json_util.object_hook) for j_doc in json_docs]



if doc.find({"cost":{'$gt':request.GET['time']})