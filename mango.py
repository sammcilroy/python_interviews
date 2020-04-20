def person_is_seller(name):
    return name[-1] == 'm' # mango sellers have names ending in m

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "johnny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johnny"] = []

from collections import deque
search_queue = deque() # create a new queue
search_queue += graph["you"] # add all of my neighbours to the queue

while search_queue: # while the queue is not empty
    person = search_queue.popleft() # take the first person from the queue
    if person_is_seller(person): # check whether the person is a mango seller
        print(person + " is a mango seller!")
        break
    else:
        search_queue += graph[person] # not a seller, add all of their neighbours the queue
