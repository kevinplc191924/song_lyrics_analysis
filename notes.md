# Code notes

## Get method of dictionaries
```python
# Get method
song = {
    'name': 'A song',
    'stats': {
        'views': 100,
        'downloads': 120,
        'comments': None
    },
    'date_info': None
}

# dict.get(key, default)
# 'default' applies if the key doesn't exist
# If 'default' not defined, None is returned

# My own advice, when dealing with nested dicts: set an empty dict as 'default' and use 'or'
# Deals with an non-existing key -> dict.get(key, {})
# Deals with an existing key storing a None -> or {}
# (dict.get(key, {}) or {})

# Useful for upper-level keys storing other dicts
# Expecting: {'date_info': {'day': 12, 'month': 4, 'year': 2005}}
# Since 'date_info' actually stores a None, a further access will cause an AttributeError
# None.get() doesn't exist. The result of 'None or {}' returns {}, and 'get' can run normally
print((song.get('date_info', {}) or {}).get('day', 'Non-existing info'))

# Existing key, retrives its value
print(song.get('name'))
# Nested dictionaries
print(song.get('stats').get('views'))
# Non-existing keys, returning and empty dict
print(song.get('album', {}))
# Non-existing nested keys, returning and empty dict
print(song.get('stats').get('likes', {}))
# A key storing a None: handle it with 'or'
# Two versions, but the first handles Nones better
print((song.get('stats', {}) or {}).get('comments', 'No comments') or 'No comments')
print(song.get('stats', {}).get('comments') or 'No comments')

# Non-existing info
# A song
# 100
# {}
# {}
# No comments
# No comments
```
---
## Json files manipulation
### Save the dictionary to a json file
```python
import json
d = {'a': 1, 'b': 2} # dictionary object
with open('data.json', 'w') as f:
    json.dump(d, f)
```
### Load the dictionary from a json file
```python
with open('data.json', 'r') as f:
    d = json.load(f)
```