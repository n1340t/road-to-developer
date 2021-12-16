skills = [3, 4, 3, 1, 6, 5]
teamSize = 3
maxSkills = 2

for i, _ in enumerate(skills):
    a = skills[i: i + teamSize]
    if len(a) < teamSize:
        break
    if max(a) - min(a) <= maxSkills:
      print(a)