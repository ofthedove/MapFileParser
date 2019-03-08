# MapFileParser
Python Script to Parse GCC Map Files

Very simple at the moment. Just turns the .text. sections into a csv so you can play with it in Excel. Doesn't even do a very good job of that.

To use it, create a file called `inputMap.txt`. Copy the section of the map file that shows the size of all the compiled code into it. Only include sections that start with `.text.`. Run the program with `python3 MapParser.py`. Output will be generated and stored in files `outputMap.csv` and `outputSummary.csv`. Output is delimited with tabs. 

