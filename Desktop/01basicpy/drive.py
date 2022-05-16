driving = input('请问你有没有开过车：')

if driving != '有' and driving != '没有':

	print('只能输入有或者没有')

	raise SystemExit 
#raise 触发错误，系统离开

# 如果想要不停的问他，直到他回答有或者没有怎么办 while回圈

age = input('你的年龄：')

age = int(age)

#先处理开车部分 一块一块处理

if driving == '有':

	if age >= 18:

		print('你通过了测验')

	else:

		print('奇怪你怎么会开车')

elif driving == '没有':

	if age >= 18:

		print('你可以考驾照了，怎么没有考')

	else:

		print('很好，再过几年就可以考驾照了')