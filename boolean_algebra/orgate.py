"""
A OR Gate is a logic gate in boolean algebra which results to true(1)
if any of the input is 1, and false(0) if  both the inputs are 0.
Following is the truth table of a OR Gate:
   | Input 1 | Input 2 |  Output |
   |      0      |     0      |      0      |
   |      0      |     1      |      1      |
   |      1      |     0      |      1      |
   |      1      |     1      |      1      |
Following is the code implementation of the OR Gate
"""

def or_gate(input_1: int, input_2: int) -> int:
    if(input_1 == 0 and input_2 == 0):
        return 0
    else:
        return 1
    
def main() -> None:
    print("Truth Table of OR Gate:")
    print("|   Input 1   |  Input 2  | Output |")
    print(f"|      0      |    0      |  {or_gate(0, 0)}     |")
    print(f"|      0      |    1      |  {or_gate(0, 1)}     |")
    print(f"|      1      |    0      |  {or_gate(1, 0)}     |")
    print(f"|      1      |    1      |  {or_gate(1, 1)}     |")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()

"""
References: 
https://github.com/TheAlgorithms/Python/blob/master/boolean_algebra/norgate.py 
https://www.geeksforgeeks.org/logic-gates-in-python/
"""
