## Description
This script takes a paragraph string and a paragraph width, and returns an array of justified strings without breaking any words.


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


## Testing

Unit tests are included in the `test_justify.py` file. To run the tests, make sure you have `pytest` installed:

bash
pip install pytest


Then run the tests with:

bash
pytest test_justify.py


## Files

- `justify.py`: The main script for text justification.
- `test_justify.py`: Contains unit tests for the `justify_text` function.

## Function Explanation

- `justify_text(paragraph, width)`: This function takes a paragraph string and a width, and returns a list of justified lines.

### How to Run Tests

1. Ensure you have Python installed.
2. Install `pytest` if you haven't already:

    bash
    pip install pytest
    

3. Save the test file `test_justify.py` in the same directory as `justify.py`.

4. Run the tests:

    bash
    pytest test_justify.py