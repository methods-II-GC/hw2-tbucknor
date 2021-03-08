#!/usr/bin/env python3
"""HW2"""

#with open("conll2000.tag.txt") as garnaches:
    #for beans in garnaches:
       # print(beans)
       
import argparse
import random
from typing import Iterator, List

#read tags line by line    
def read_tags(path: str) -> Iterator[List[List[str]]]:
    with open(path, "r") as source:
        lines = []
        for line in source:
            line = line.rstrip()
            if line:  # Line is contentful.
                lines.append(line.split())
            else:  # Line is blank.
                yield lines.copy()
                lines.clear()
    # Just in case someone forgets to put a blank line at the end...
    if lines:
        yield lines
            
tags = list(read_tags(args.input)) 
    
def main(args.input: argparse.Namespace) -> None:
    with open(args.input, "w") as sink:
        for tags in sink
            print(tags)
            
        if __name__ == "__main__":
#declare arguments.
    parser = argparse.ArgumentParser(tags)
    parser.add_argument('--output-file', type=str, help="File path.")
    parser.add_argument('--testRatio', type=float, default=0.10,
                        help="Test to training ratio.")
    parser.add_argument('--devRatio', type=float, default=0.10,
                        help="Development to training ratio.")  
                      
#pass to main.
    main(parser.parse_args())

#Split train, dev and test.
def TrainDevTestSplit(path, train, dev, test):
    with open(args.train, "w") as sink:
        for tags in sink:
            print(tags)
            
    with open(args.dev, "w") as sink:
        for tags in sink:
            print(tags)
            
    with open(args.dev, "w") as sink:
        for tags in sink:
            print(tags)            
            
            
            


        
