class String_class:
	def get_string():
		s=input("Enter a string")
		return s
	def print_string(s):
		print(s.upper())
ob=String_class
def test():
	s1=ob.get_string()
	ob.print_string(s1)
test()
