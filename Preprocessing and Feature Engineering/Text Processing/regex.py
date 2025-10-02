import re

input_text = "The rain in Spain stays mainly in the plain. In Hartford, Hereford, and Hampshire, hurricanes hardly ever happen."

output = re.sub(r'[^a-zA-z\s]',"", input_text)


print(output)