# write your code here


msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
memory = 0.0
msg_index = 0

def isfloat(num):
	try:
		float(num)
		return True
	except ValueError:
		return False


def memcheck(x, y, mem):
	if x == "M":
		x = mem
	if y == "M":
		y = mem
	return x, y


def is_one_digit(v):
	ret = False
	if v > -10 and v < 10 and v.is_integer():
		ret = True
	return ret


def check(v1,v2,v3):
	msg = ""
	if is_one_digit(v1) and is_one_digit(v2):
		msg = msg + msg_6
	if (v1 == 1 or v2 == 1 ) and v3 =="*":
		msg = msg + msg_7
	if (v1 == 0 or v2 ==0) and (v3 =="*" or v3 == "+" or v3 == "-"):
		msg = msg + msg_8
	if msg != "":
		msg = msg_9 + msg
		print(msg)


def flow(m):
	global memory
	memory = m
	print(msg_0)
	a = input().split()
	x, oper, y = a
	x, y = memcheck(x, y, memory)
	result = 0.0
	if isfloat(x) and isfloat(y):
		if oper != "+" and oper != "-" and oper != "*" and oper != "/":
			print(msg_2)
			result = flow(memory)
		else:
			check(float(x),float(y), oper)
			if oper == "+":
				result = float(x) + float(y)
			elif oper == "-":
				result = float(x) - float(y)
			elif oper == "*":
				result = float(x) * float(y)
			elif oper == "/" and float(y) != 0:
				result = float(x) / float(y)
			else:
				print(msg_3)
				result = flow(memory)
	else:
		print(msg_1)
		result = flow(memory)
	print(result)
	newFlow(memory,result)

def innerflow(res):
	global msg_index
	global memory
	if msg_index == 10:
		print(msg_10)
	elif msg_index == 11:
		print(msg_11)
	elif msg_index == 12:
		print(msg_12)
	ans = input()
	if ans == "y":
		if msg_index < 12:
			msg_index += 1
			innerflow(res)
		else:
			memory = res
			finish(memory,res)
	elif ans == "n":
		finish(memory,res)
	else:
		innerflow(res)




def finish(mem, result):
	print(msg_5)
	inp = input()
	if inp == "y":
		flow(mem)
	elif inp =="n":
		exit()
	else:
		finish(mem,result)


def newFlow(mem, result):
	global memory
	print(msg_4)
	inp = input()
	if inp == "y":
		if is_one_digit(result):
			global msg_index
			msg_index = 10
			innerflow(result)
			finish(memory, result)
		else:
			memory = result
			finish(memory,result)
	elif inp == "n":
		finish(memory,result)
	else:
		newFlow(memory,result)



flow(memory)

