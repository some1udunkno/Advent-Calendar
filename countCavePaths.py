'''

Advent of Code - 2021

--- Day 12: Passage Pathing ---
With your submarine's subterranean subsystems subsisting suboptimally, the only way you're getting out of this cave anytime soon is by finding a path yourself. Not just a path - the only way to know if you've found the best path is to find all of them.

Fortunately, the sensors are still mostly working, and so you build a rough map of the remaining caves (your puzzle input). For example:

start-A
start-b
A-c
A-b
b-d
A-end
b-end
This is a list of how all of the caves are connected. You start in the cave named start, and your destination is the cave named end. An entry like b-d means that cave b is connected to cave d - that is, you can move between them.

So, the above cave system looks roughly like this:

    start
    /   \
c--A-----b--d
    \   /
     end
Your goal is to find the number of distinct paths that start at start, end at end, and don't visit small caves more than once. There are two types of caves: big caves (written in uppercase, like A) and small caves (written in lowercase, like b). It would be a waste of time to visit any small cave more than once, but big caves are large enough that it might be worth visiting them multiple times. So, all paths you find should visit small caves at most once, and can visit big caves any number of times.

--- Part Two ---
After reviewing the available paths, you realize you might have time to visit a single small cave twice. Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small caves can be visited at most once. However, the caves named start and end can only be visited exactly once each: once you leave the start cave, you may not return to it, and once you reach the end cave, the path must end immediately.

'''

def countPaths(connections, allowRevisit=False):
    map = {}
    for c in connections:
        a, b = c.split("-")
        if a not in map.keys():
            map[a] = [b]
        else:
            map[a].append(b)
            
        if b not in map.keys():
            map[b] = [a]
        else:
            map[b].append(a)
            
    paths = [[['start'], [], False]] # initialize paths and the explored tokens associated with this path (none)
    numPaths = 0
    while len(paths) > 0:
        path, explored, revisit = paths.pop()
        for c in map[path[-1]]:
            if allowRevisit:
                if (c in explored and not c.isupper() and revisit) or c == 'start':
                    continue
                elif (c in explored and not c.isupper() and not revisit):
                    newPath = path[:]
                    newExplored = explored[:]
                    newPath.append(c)
                    newExplored.append(c)
                    paths.append([newPath[:], newExplored[:], True])
                elif c == 'end':
                    numPaths += 1
                    continue
                else:
                    newPath = path[:]
                    newExplored = explored[:]
                    newPath.append(c)
                    newExplored.append(c)
                    paths.append([newPath[:], newExplored[:], revisit])
            else:
                if (c in explored and not c.isupper()) or c == 'start':
                    continue
                elif c == 'end':
                    numPaths += 1
                    continue
                else:
                    newPath = path[:]
                    newExplored = explored[:]
                    newPath.append(c)
                    newExplored.append(c)
                    paths.append([newPath[:], newExplored[:], False])
                
    return numPaths

paths = ['nu-start',
'rt-start',
'db-qh',
'PE-end',
'sl-rt',
'qh-end',
'ZH-rt',
'nu-rt',
'PE-db',
'db-sl',
'nu-ZH',
'nu-qh',
'PE-qh',
'ZH-db',
'ne-end',
'ne-ZH',
'QG-db',
'qh-sl',
'ZH-qh',
'start-ZH',
'nu-PE',
'uf-db',
'ne-sl',]
'''
paths = ['start-A',
'start-b',
'A-c',
'A-b',
'b-d',
'A-end',
'b-end',]
'''
print(countPaths(paths))
print(countPaths(paths, True))