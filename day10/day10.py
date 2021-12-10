from functools import reduce

stack = []
o = ('(','[','{','<')
c = (')',']','}','>')
p = (3,57,1197,25137)
syntax_error_score = 0
autocomplete_scores = []

with open('day10-input.txt') as f:
    for line in f:
        stack.clear()
        for b in line.strip():
            if b in o:
                stack.append(b)
            elif b != c[o.index(stack.pop())]:
                syntax_error_score+=p[c.index(b)]
                break
        else: 
            if len(stack)!=0:
                autocomplete_scores.append(reduce(lambda x,y: x*5+o.index(y)+1, reversed(stack),0))


print(syntax_error_score)

print(sorted(autocomplete_scores)[len(autocomplete_scores)>>1])

