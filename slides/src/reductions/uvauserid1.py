def check_uva_userid1(what):
	chars = list(what.lower())
	# check first character (must be a letter)
	if len(chars) == 0: return False
	if not chars[0].isalpha(): return False
	chars.pop(0)
	# check second character (must be a letter)
	if len(chars) == 0: return False
	if not chars[0].isalpha(): return False
	chars.pop(0)
	# return true if of the form ll
	if len(chars) == 0: return True
	# check optional 3rd letter
	if chars[0].isalpha():
		chars.pop(0)
		# return true if of the form lll
		if len(chars) == 0: return True
	# check digit
	if len(chars) == 0: return False
	if not chars[0].isdigit(): return False
	chars.pop(0)
	# check first letter after the digit
	if len(chars) == 0: return False
	if not chars[0].isalpha(): return False
	chars.pop(0)
	# return true if of the form lldl or llldl
	if len(chars) == 0: return True
	# check second letter after the digit
	if not chars[0].isalpha(): return False
	chars.pop(0)
	# return true if of the form lldll or llldll
	if len(chars) == 0: return True
	# check third letter after the digit
	if not chars[0].isalpha(): return False
	chars.pop(0)
	# return true if of the form lldlll or llldlll
	if len(chars) == 0: return True
	return False


print(check_uva_userid1(input()))
