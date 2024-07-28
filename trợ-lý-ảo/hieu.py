you = input("Say something: ")

if you == "":
    robot_brain = "I can't hear you, try again"
elif you == "Hello":
    robot_brain = "xin chào"
elif you == "Today":
    robot_brain = "Thu 6"
else:
    robot_brain = "I'm fine thank you and you"

print(robot_brain)
