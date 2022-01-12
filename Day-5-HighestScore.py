#HeightScore
team_scores = input("Input a list of team scores ").split()
for n in range(0, len(team_scores)):
  team_scores[n] = int(team_scores[n])
print(team_scores)

highest_score = 0
for score in team_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score by the team is : {highest_score}")