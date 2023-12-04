from typing import Callable, Optional

def inputFile(fname: str, type: bool):

    with open (fname, mode = 'r') as f:
        if type == True:
            return f.read()
        else: 
            lines = []
            for line in f:
                lines.append(line.strip("\n"))
            return lines
                
    
    