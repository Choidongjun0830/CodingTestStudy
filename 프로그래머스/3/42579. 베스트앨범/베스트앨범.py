def solution(genres, plays):
    answer = []
    songs = {}
    total_plays = {}
    for i in range(len(genres)):
        if genres[i] in total_plays:
            total_plays[genres[i]] += plays[i]
        else:
            total_plays[genres[i]] = plays[i]
            
        if genres[i] not in songs:
            songs[genres[i]] = [(plays[i],i)]
        else:
            songs[genres[i]].append((plays[i],i))
    rank = sorted(total_plays, key=total_plays.get, reverse=True) #가장 많이 재생된 장르 순 정렬
    
    for i in rank:
        temp = sorted(songs[i], key=lambda x: (-x[0], x[1])) #장르 내에서 많이 재생되고, 재생 횟수가 같으면 고유 번호가 낮은거
        if len(temp) == 1:
            answer.append(temp[0][1])
        else:
            for i in range(2):
                answer.append(temp[i][1])
    return answer