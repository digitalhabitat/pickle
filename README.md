# pickle

## An "open-book" python exercise which implements three functions in Python

#### number_to_words()

+ Takes as an **argument a string** representing a US phone number

	+ **outputs a string which** has a transformed part
	+ or all of the phone number
	+ into a single "wordified" phone number that can be typed on a US telephone


+ for example, a valid output of

	+ number_to_words("1-800-724-6837") .... could be

	+ "1-800-PAINTER"


+ If you find it makes things simpler, feel free to constrain this function
to only output "wordifications" in English.

#### words_to_number()

+ Does the reverse of the above function

+ for example, the
output of

	+ words_to_number("1-800-PAINTER") ... should be

	+ "1-800-724-6837"

#### all_wordifications()

+ Outputs all possible combinations of

+  **numbers** and **English
words** in a phone number.