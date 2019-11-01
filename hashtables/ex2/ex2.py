#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length
    """
    YOUR CODE HERE
    """
    # put all items in hash map
    for ticket in tickets:
        hash_table_insert(ht, ticket.source, ticket.destination)

    # set first item 
    route[0] = hash_table_retrieve(ht, "NONE")
    for i in range(1, length):
        # set current location by finding last source 
        route[i] = hash_table_retrieve(ht, route[i - 1])
    return route



tickets = [
  Ticket( "PIT", "ORD") ,
  Ticket( "XNA", "CID" ),
  Ticket( "SFO", "BHM" ),
  Ticket( "FLG", "XNA" ),
  Ticket( "NONE", "LAX" ),
  Ticket("LAX", "SFO" ),
  Ticket("CID", "SLC"),
  Ticket( "ORD", "NONE"),
  Ticket( "SLC", "PIT" ),
  Ticket( "BHM", "FLG" )
]

# ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]
x = reconstruct_trip(tickets, len(tickets))
print(x)