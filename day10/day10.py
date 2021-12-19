from functools import reduce

stack = []
open_brackets = "([{<"
close_brackets = ")]}>"
points = (3,57,1197,25137)
syntax_error_score = 0
autocomplete_scores = []

with open('day10-input.txt') as f:
    for line in f:
        stack = []
        for bracket in line.strip():
            if bracket in open_brackets:
                stack.append(bracket)
            elif bracket != close_brackets[open_brackets.index(stack.pop())]:
                syntax_error_score+=points[close_brackets.index(bracket)]
                break
        else: 
            autocomplete_scores.append(reduce(lambda x,y: x*5+open_brackets.index(y)+1, stack[::-1],0))


print(syntax_error_score)
print(sorted(autocomplete_scores)[len(autocomplete_scores)>>1])

