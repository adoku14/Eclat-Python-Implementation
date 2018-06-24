# Eclat-Python-Implementation
Here is a fast implementation of Pattern mining algorithm for finding frequent itemsets in a transactional database named Eclat
 Moreover, extraction association rules has been implemented. 

The example of running the Algorithms is :

python3 eclat.py input.txt support confidence output_FreqItems Output_Rules.txt 

Example: python3 eclat.py input.txt 3 0.4 items.txt rules.txt

Requirements:
Python >=3.n

If you provide your input file, you should take care about the delimiter. You could change it in the code at read_Data function call.

