R, P, S = 0, 1, 2
combos, WIN, score_p1, score_p2 = [R, P, S, R, P, S], [(R, P), (P, S), (S, R)], 0, 0
with open("input","r") as f :
    for d in f.read().split('\n')[:-1] :
        fight_p1 = ord(d[0]) - ord('A'), combos[ord(d[2]) - ord('X')]
        fight_p2 = ord(d[0]) - ord('A'), combos[ord(d[0]) - ord('A') + ord(d[2]) - ord('Y')]
        score_p1 += 6 * (fight_p1 in WIN) + 3 * (fight_p1[0] == fight_p1[1]) + fight_p1[1] + 1
        score_p2 += 6 * (fight_p2 in WIN) + 3 * (fight_p2[0] == fight_p2[1]) + fight_p2[1] + 1
print(f"{score_p1 = }\n{score_p2 = }")