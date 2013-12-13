import twitter

# create twitter API object
api = twitter.Api()

# perform a basic search
# twitter API docs: https://dev.twitter.com/docs/api/1/get/search
query = api.search(q = "lazy dog")

# print how quickly the search completed
print "Search complete (%f seconds)" % (query["completed_in"])

# loop through each of my statuses, and print its content
for result in query["results"]:
	print "(%s) @%s %s" % (result["created_at"], result["from_user"], result["text"])