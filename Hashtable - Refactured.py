# A shorter version of the Hashtable.py code that came before it.
# Based on following instrucitons:

# Whenever we have duplicate code like the loop that finds the entry in
# hashtable_update and hashtable_lookup, we should think if there is a better way
# to write this that would avoid the duplication. We should be able to rewrite
# these procedures to be shorter by defining a new procedure and rewriting both
# hashtable_update and hashtable_lookup to use that procedure.

# Modify the code for both hashtable_update and hashtable_lookup to have the same
# behavior they have now, but using fewer lines of code in each procedure.  You
# should define a new procedure to help with this. Your new version should have
# approximately the same running time as the original version, but neither
# hashtable_update or hashtable_lookup should include any for or while loop, and
# the block of each procedure should be no more than 6 lines long.

def hashtable_update(htable, key, value):
    bucket = hashtable_get_bucket(htable, key)     #find the bucket
    entry = bucket_find(bucket, key)               #looking for the key within the bucket
    if entry:                                      #if find the entry, update the value
        entry[1] = value
    else:                                          #otherway append the key and its value, to the end of the bucket
        bucket.append([key,value])
    return htable

def hashtable_lookup(htable, key):
    entry = bucket_find(hashtable_get_bucket(htable, key), key)   #find the bucket and search for the entry within the bucket
    if entry:                                                     #if entry is not None (empty), return the second value                                            
            return entry[1]
    return None                                                   #otherway return None

def bucket_find(bucket, key):
    for entry in bucket:      #go through all elements in bucket, if you find the key in an element, return that element
        if entry[0] == key:
            return entry
    return None

def make_hashtable(size):        #create a list with size number of sublists
    table = []
    for unused in range(0, size):
        table.append([])
    return table

def hash_string(s, size):
    h = 0
    for c in s:
         h = h + ord(c)
    return h % size

def hashtable_get_bucket(htable, key):       #find a specific bucket in the htable
    return htable[hash_string(key, len(htable))]


table = make_hashtable(10)
hashtable_update(table, 'Python', 'Monty')
hashtable_update(table, 'CLU', 'Barbara Liskov')
hashtable_update(table, 'JavaScript', 'Brendan Eich')
hashtable_update(table, 'Python', 'Guido van Rossum')
print hashtable_lookup(table, 'Python')
print table
