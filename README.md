# pickle

## Python phone number exercise

### Quick Start

The file that defines the functions also contains testing examples

To demonstrate examples enter `./thrice` into terminal

***Output:***

Testing words_to_numbers

1-800-PAINTERS
1-800-72468377
1-800-FLOWERS
1-800-3569377
1-800-INSURANCE
1-800-467872623
1-800-GARBAGE
1-800-4272243

Testing numbers_to_words

1-800-72468377
1-800-PAINTERS
1-800-3569377
1-800-FLOWERS
1-800-467872623
1-800-INSURANCE
1-800-4272243
1-800-GARBAGE

Testing all_wordfications of 72468377

724-68377
724-MT-377
724-MU-377
724-MUD-77
724-MUDS-7
724-NT-377
724-NU-377
724-NV-377
724-OT-377
724-OTES-7
724-OVER-7
724-OVERS
PA-468377
PAIN-8377
PAINT-377
PAINTER-7
PAINTERS
PB-468377
PC-468377
QA-468377
QB-468377
QC-468377
RA-468377
RAG-68377
RAH-68377
RAIN-8377
RB-468377
RBI-68377
RC-468377
SA-468377
SAG-68377
SAGO-8377
SAINT-377
SB-468377
SC-468377
SCH-68377
SCI-68377

### Credit and Caveats

Regular Expressions are used to match for 1-800-XXXXXXX number format

**num_to_alphanum()** Cycles the phone number through all possible alphanumeric combinations. The following link below was used as a guide.

+ https://www.geeksforgeeks.org/find-possible-words-phone-digits/

**numbers_to_words()** will only test for a single English word.
 It uses the follow library to determine if a string is English
+ https://github.com/rfk/pyenchant/

**all_wordifications()** can take a long time if the passed argument is greater than around 7 characters. It use the following library to find compond english words.
+ https://pypi.org/project/compound-word-splitter/

**Additional Source** i wished i looked at earlier

+ https://automatetheboringstuff.com/chapter7/


### Functions

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
