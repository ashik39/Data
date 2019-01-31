def main():
	w=1
	n=int(input())
	for i in range(1,n):
		w=w*i
	print(w)
try:
	main()
except:
	print('invalid')
