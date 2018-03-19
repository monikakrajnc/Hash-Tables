# hashtable_update(htable,key,value) updates the value associated with key. If key is already in the
# table, change the value to the new value. Otherwise, add a new entry
# for the key and value.

def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:  #look if key exist in table
        if entry[0] == key:
            entry[1] = value  #if key is in table, change its value
            return htable
    bucket.append([key, value])     #add a new entry, for the key and value
    return htable

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:    #if key is in table/bucket, print its value
        if entry[0] == key:
            return entry[1]
    return None

def hashtable_add(htable,key,value): #append new sublist, with key and its value, to the existing table
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])


def hashtable_get_bucket(htable,keyword):    #find a sublist with a keyword and print it
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):      #create a list (table) with sublists
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table


table = [[['Francis', 13], ['Ellis', 11]], [['Andy', 5]], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]


#hashtable_update(table, 'Bill', 42)
#hashtable_update(table, 'Rochelle', 94)
#hashtable_update(table, 'Zed', 68)
print(hashtable_update(table, 'Luke', 7))
print(table)
