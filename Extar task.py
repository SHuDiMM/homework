grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
def average_grades(i) : return (sum(i)/len(i))
result = (map(average_grades, grades))
av_grades = []
for n in result: av_grades.append(n)
st_names = list(students)
st_names.sort()
def comb_list(a) : return ([a,av_grades[st_names.index(a)]])
result = (map(comb_list, st_names))
name_grade = []
for n in result: name_grade.append(n)
final_dict = dict(name_grade)
print(final_dict)