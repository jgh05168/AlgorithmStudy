def solution(papers):

    papers.sort()
    ans = 0
    other_papers = []
    for idx in range(len(papers)):
        if papers[idx] >= len(papers) - idx:
            ans = len(papers) - len(other_papers)
            break
        other_papers.append(papers[idx])

    return ans

