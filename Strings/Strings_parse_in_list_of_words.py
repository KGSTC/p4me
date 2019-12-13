#This code parses text/strings in list of words (where seperators)
## This code works on python IDE or after running python IDE from Cmd window
### Outputs: ['10', ' ', 'green', ' ', 'bottles', '!']
import re
[w for w in re.split('([^0-9A-Za-z])', '10 green bottles!') if w]
