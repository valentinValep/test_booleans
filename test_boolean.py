def test_boolean(arg_num, bool1, bool2):
	success = 1
	translate = "abcdefghijklmnopqrstuvwxyz"

	if arg_num > len(translate):
		print("Too many arguments")
		exit(1)

	for index in range(2**arg_num):
		binary = "0" * (arg_num - len(bin(index)[2:])) + bin(index)[2:]
		for arg_index in range(arg_num):
			exec(f"global {translate[arg_index]}; {translate[arg_index]} = int(binary[arg_index])")
		exec(f"global res1; res1 = ({bool1})")
		exec(f"global res2; res2 = ({bool2})")
		if res1 != res2:
			success = 0
	return (success)

assert(test_boolean(1, "a", "a") == True)
assert(test_boolean(2, "a and b", "b and a") == True)
assert(test_boolean(2, "a and not b", "b and a") == False)
assert(test_boolean(2, "a and b", "b and not a") == False)
assert(test_boolean(2, "not a and b", "b and not a") == True)
assert(test_boolean(5, "not (a and (b or c or d) and (e or c or d))", "a and (b or c or d) and (e or c or d)") == False)
assert(test_boolean(5, "not (a and (b or c or d) and (e or c or d))", "not a or (not b and not c and not d) or (not e and not c and not d)") == True)

print("Success : These two expressions are equals" if test_boolean(5, "a and (b or c or d) and (e or c or d)", "a and ((b and e) or c or d)") else "Failed : These two expressions are inequals")
