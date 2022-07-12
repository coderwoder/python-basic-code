list = ['start - start the car',
        'stop - stop the car',
        'quit - exit the portal']
cmds = ['start', 'stop', 'quit']
input_user = ''
started = True
while input_user != 'quit':
    input_user = input('>>>').lower()
    if input_user == 'help':
        print(*list, sep='\n')
    elif input_user in cmds:
        if input_user == cmds[0]:
            if started:
                print("Starting the car... woroommmmmmmmmmmmmmmm")
                started = False
            else:
                print("Car already started...")
        elif input_user == cmds[1]:
            if not started:
                print("Stoping the car...creeeekkkkk")
                started = True
            else:
                print("Your Car Needs to be started to stop it")
    elif input_user not in list:
        print("Not a valid input....")
