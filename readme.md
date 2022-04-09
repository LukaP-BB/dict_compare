![example workflow](https://github.com/github/docs/actions/workflows/python-app.yml/badge.svg)
# Nested objects deep comparison

This script contains a single function aiming to compare deeply 2 objects.
The function will return a dictionnary of the differences between the 2 objects. 

If you are looking for exhaustive deep diff, you are probably looking for the [deepdiff](https://github.com/seperman/deepdiff) library. 
This function covers my use cases but is far from exhaustive, and was just an excuse to reinvent the wheel on a bored saturday. 

## What can this do ?
This function compares recursively 2 given objects. They can be nested dictionaries, lists etc... It will return a dictionary of all differences between the 2 objects. 

It's a useful function to compare 2 big data dumps where few differences are expected.

## How to use it ?

Either copy the function in one of your script or download `dict_diff.py` next to your script and `from dict_diff import diff` to use it.
