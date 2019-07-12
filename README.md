# pickle

## An "open-book" python exercise which implements three functions in Python

#### number_to_words()

+ Takes a **string argument** representing a US phone number

+ 	**outputs a string** which has
 + a transformed part of phone number
 + or all of the phone number into
 + a single "wordified" phone number that can be typed on a US telephone


+ for example

	+ `number_to_words("1-800-724-6837")` ---outputs---> "1-800-PAINTER"


+ this function is constrained to only output "wordifications" in English.

#### words_to_number()

+ Does the reverse of the above function

+ for example

	+ `words_to_number("1-800-PAINTER")` --outputs--> "1-800-724-6837"

#### all_wordifications()

+ Outputs all possible combinations of

+  **numbers** and **English
words** in a phone number.
