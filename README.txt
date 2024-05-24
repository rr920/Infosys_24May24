# Left Align Text Script

## Description
This script takes a paragraph string and a paragraph width, and returns an array of left and right justified strings without breaking any words.


## How to Run
To run the script, use the following command:

bash
python3 ./justify.py --paragraph-string "Your paragraph here" --paragraph-width 20 #15, 25, 30 etc.


## Sample Output
For example:

bash
python3 ./justify.py --paragraph-string "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works." --paragraph-width 20


Output:

Array [1] = "This  is  a   sample"
Array [2] = "text      but      a"
Array [3] = "complicated  problem"
Array [4] = "to be solved, so  we"
Array [5] = "are adding more text"
Array [6] = "to   see   that   it"
Array [7] = "actually      works."



## Assumptions
- Words will not be broken across lines.


## Unit Tests
To add unit tests, you can use the `unittest` framework in Python. Create a `test_justify.py` file with tests for various cases.