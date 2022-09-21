import platform,os,time
os.system('git pull')
os.system('clear')


arc = str(platform.uname().machine)
if 'arm' in arc:
	print('Join Our Facebook Group');time.sleep(2)
	os.system("xdg-open https://www.facebook.com/luki.kece.79")
	__import__("mrrayancrack").login()
elif 'aarch' in arc:
	print('Join Our Facebook Group');time.sleep(2)
	os.system("xdg-open https://www.facebook.com/luki.kece.79")
	__import__("crackmrrayan").login()
else:
	print('Join Our Facebook Group');time.sleep(2)
	os.system("xdg-open https://www.facebook.com/luki.kece.79")
	print('Your Device is not supported')