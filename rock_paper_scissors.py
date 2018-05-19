import random
def game():
	start = 'start'
	stop = 'stop'
	rock = 'rock'
	paper = 'paper'
	scissors = 'scissors'
	user_choice = raw_input('type "start" to start the game : ')
	robot_choice = ['paper','rock','scissors']

	if user_choice == start:
		user_choice = raw_input("type your choice rock or paper or scissors /n OR type stop to stop the game : ")
		if user_choice == stop:
			print "Bye Bye"
			exit()
		else:
			while user_choice != stop:    
			    if user_choice == rock:
				    if random.choice(robot_choice) == 'rock':
					    print 'you got the same choice!'
					    user_choice = raw_input("type your choice rock or paper or scissors /n OR type stop to stop the game : ")
				    if random.choice(robot_choice) == 'paper':
					    print 'robot Wins!'
					    user_choice = raw_input("type your choice rock or paper or scissors /n OR type stop to stop the game : ")
				    if random.choice(robot_choice) == 'scissors':
					    print 'You Win!'
					    user_choice = raw_input("type your choice rock or paper or scissors /n OR type stop to stop the game : ")

			    if user_choice == paper:
				    if random.choice(robot_choice) == 'rock':
					    print 'You Win!'
					    user_choice = raw_input("type your choice rock or paper or scissors /n OR type stop to stop the game : ")
				    if random.choice(robot_choice) == 'paper':
					    print 'Yout got the same choice!'
					    user_choice = raw_input("type your choice rock or paper or scissors /n OR type stop to stop the game : ")
				    if random.choice(robot_choice) == 'scissors':
					    print 'Robot Wins!'
					    user_choice = raw_input("type your choice rock or paper or scissors /n OR type stop to stop the game : ")

			    if user_choice == scissors:
				    if random.choice(robot_choice) == 'rock':
					    print 'Robot Wins!!'
					    user_choice = raw_input("type your choice rock or paper or scissors /n OR type stop to stop the game : ")
				    if random.choice(robot_choice) == 'paper':
					    print 'You win !'
					    user_choice = raw_input("type your choice rock or paper or scissors /n OR type stop to stop the game : ")
				    if random.choice(robot_choice) == 'scissors':
					    print 'You got the same choice'
					    user_choice = raw_input("type your choice rock or paper or scissors /n OR type stop to stop the game : ")
			    if user_choice == stop:
				    print "Bye Bye"
				    exit()
			    if user_choice != stop and user_choice!= rock and user_choice!= paper and user_choice!= scissors and user_choice!= start:
				    print "please try again mayber you write the word wrong"
				    user_choice = raw_input("type your choice rock or paper or scissors /n OR type stop to stop the game : ")

	else:
		if user_choice != stop:
		    print "please try again mayber you write the word wrong"
		    game()
		else:
			exit()

game()