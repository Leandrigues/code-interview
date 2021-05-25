# iGotAnOffer
from collections import defaultdict

def findCoursePath(preRequisites, numCourses):
    # preReqMap = defaultdict(list)
    preReqMap = { subject: [] for subject in range(numCourses) }
    inverse = { subject: -1 for subject in range(numCourses) }
    for preReq in preRequisites:
        preReqMap[preReq[1]].append(preReq[0])
        inverse[preReq[0]] = preReq[1]
    print("inverse", inverse)
    visited = {k: False for k in range(numCourses)}
    # print(preReqMap)
    def BFS(start):
        queue = [start]
        done = 1
        while queue:
            s = queue.pop(0)
            print(f'{s}->', end='')
            # print("s: ", s)
            for i in preReqMap[s]:
                queue.append(i)
                done += 1
                visited[i] = True

    for key in inverse:
        if inverse[key] == -1:
            first = key
            BFS(first)

preReqs = [(4,0), (5,0), (3,5), (1,5)]
findCoursePath(preReqs, 6)
# {
#     4: [3],
#     3: [2],
#     2: [1]
#     1: []
# }


# 1 -> 2 -> 3 -> 4