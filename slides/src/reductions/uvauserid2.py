def check_uva_userid2(what):

	state_table = [ 
		# from each state, where to go on an 'l', 'd', and 'o', respectively
		[], # we numbered our states from 1, so we burn spot 0
		[2,    None, None], # state 1 goes to 2 on a letter
		[3,    None, None], # state 2 goes to 3 on a letter
		[4,    5,    None], # state 3 goes to 4 on a letter and 5 on a digit
		[None, 5,    None], # state 4 goes to 5 on a digit
		[6,    None, None], # state 5 goes to 6 on a letter
		[7,    None, None], # state 6 goes to 7 on a letter
		[8,    None, None], # state 7 goes to 8 on a letter
		[None, None, None], # no transitions out of state 8
	]
	final_states = [3, 4, 6, 7, 8]

	chars = list(what.lower())
	state = 1
	while len(chars) > 0:
		which = 0 if chars[0].isalpha() else 1 if chars[0].isdigit() else 2
		next_state = state_table[state][which]
		if next_state is None: return False
		state = next_state
		chars.pop(0)
	return state in final_states



print(check_uva_userid2(input()))
