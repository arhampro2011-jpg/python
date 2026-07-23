
def friend_out(friends):
    print('an operation is done')
    for i in range (len(friends)):
        print(friends[i],end=' ')
    print()


friends=['kanav','nirav','raghav','ayaan','daksh','aarav']
print(friends)
friend_out(friends)
print(friends[2:5])
print(friends[-2])

friends.append("pratyush")
friend_out(friends)

friends.pop(2)
friend_out(friends)

friends.remove("daksh")
friend_out(friends)

friends.sort()
friend_out(friends)

friends.reverse()
friend_out(friends)

student={
    'name':'arham',
    'age':15,
    'roll_no':4,
    'marks':95.3,


}
print(student)
print(student.get('age'))
student['name']='ayaan'
print(student)
student.pop('marks')
print(student)

roll_no=[1,2,3,4,5]
students=dict(zip(roll_no,friends))
print(students)