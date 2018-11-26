# Learn how to convert string to dictionary using json library.

import json
a_string = "{'ola':'amigo','grazie':'italian','gracias':'spanish','merci':'french','danke':'german'}"
into_a_dict = json.loads(a_string)
print(into_a_dict)

# khong chay duoc