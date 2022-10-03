#Name: Erik Wright
from __future__ import division
from array import array
from ast import Num, operator
from cmath import inf
from inspect import stack
from queue import Empty
from operator import add, sub, mul, truediv
import sys

class Caculator:

    def __init__(self):
        self.stack = []
             
    def isempty(self):
        if self.stack == []:
            return True
        else:
            return False

    def convert(self, infix):
        # use a stack to covert infix to postfix
        self.stack.clear()
        pos = ''
        count = 0
        par = 0
        print(infix)

        for i in infix:
            count += 1
            if i == '(':
                par += 1
            elif i == ')':
                par -= 1    
       
        if count == 0:
            sys.exit("You didn't enter anything.")

        if par != 0:
            sys.exit("Wrong parenthses format")

        for i in range(0, len(infix)):
            if i == (len(infix)-1):
                end = str(infix[i])
                if end == '+' or end == '-' or end == '/' or end == '*' or end == '^' or end == ' ':
                    sys.exit("Can't end with an operand or space")
        
        for i in infix:
            if i in ['*', '/']:
                while self.stack and self.stack[-1] in ['*', '/']:
                    pos += self.stack.pop()
                self.stack.append(i)
            elif i in ['^']:
                while self.stack and self.stack[-1] in ['^']:
                    pos += self.stack.pop()
                self.stack.append(i)
            elif i in ['+', '-']:
                while self.stack and self.stack[-1] != '(':
                    pos += self.stack.pop()
                self.stack.append(i)
            elif i == '(':
                self.stack.append(i)
            elif i == ')':
                while self.stack[-1] != '(':
                    pos += self.stack.pop()
                self.stack.pop()
            else:
                pos += i
        while self.stack:
            pos += self.stack.pop()
            
        postfix = pos
        return postfix

    def evaluate(self, postfix):
        self.stack.clear()
        result = 0
        
        for i in postfix:
            if i.isdigit():
                self.stack.append(float(i))
            elif i.isalpha():
                sys.exit("Sorry I can't compute letters")
            else:
                numA = self.stack.pop()
                numB = self.stack.pop()
                if i == '+':
                    out = add(numA, numB)
                    self.stack.append(out)
                elif i == '-':
                    out = sub(numB, numA)
                    self.stack.append(out)
                elif i == '/':
                    out = numB / numA 
                    self.stack.append(out)
                elif i == '*':
                    out = numA * numB     
                    self.stack.append(out)
                elif i == '^':
                    out = pow(numB, numA)
                    self.stack.append(out)
        result = self.stack.pop()
        return result

if __name__ == '__main__':
    ## instantiating the linked list
    cal = Caculator()

    print("Instruction: When passing argument please do not put a space between each element. do: 1+2 not 1 + 2")
    input = input('Enter in argument: ')

    postfix = cal.convert(input)
    print(postfix)

    result = cal.evaluate(postfix)
    print(result)