a=input("Enter the Student's name:")
all={
    "Chandu":26,
    "Akhil":24,
    "Ramesh":30
}
if a in all:
    print(a + "'s marks:", all[a])
else:
    print("Student Not found")
