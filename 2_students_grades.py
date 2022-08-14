import statistics

n = int(input())
names_dict = {}
for i in range(n):
    name, assessment = input().split(' ')
    assessment = float(assessment)
    if name not in names_dict:
        names_dict[name] = []
    names_dict[name].append(assessment)
for name,assessments in names_dict.items():
    average_assessment = sum(assessments) / len(assessments)

    print(f"{name} -> {' '.join(f'{assessment:.2f}' for assessment in assessments )} (avg: {average_assessment:.2f})")
