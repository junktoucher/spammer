import requests, os, random, threading, time, colorama
from colorama import Fore
colorama.init()

class Main:
	def __init__(self):

		self.tokens: list = open("tokens.txt", 'r').read().split('\n')
		self.proxies: list = open("proxies.txt", 'r').read().split('\n')
		self.tokenamount: int = len(self.tokens)
		self.style = f'{Fore.RED}[{Fore.WHITE}+{Fore.RED}]{Fore.WHITE}'
		self.red = Fore.RED
		
	def main(self):

		print(f'{self.style} Amount to spam: {self.red}', end='')

		try:
			spam_amount = int(input())
		except:
			print(f'{self.style} Enter a valid number!')
			input()
			quit()

		os.system('cls')
		print(f'{self.style} Channel ID: {self.red}', end='')
		channel_id = input()
		os.system('cls')
		print(f'{self.style} Message: {self.red}', end='')
		message = input()
		os.system('cls')
		print(f'{self.style} Threads: {self.red}', end='')
		try:
			threadamount = int(input())
		except:
			print(f'{self.style} Enter a valid number!')
			input()
			quit()
		os.system('cls')
		for i in range(threadamount):
			threading.Thread(target=Main().spam, args=(spam_amount, channel_id, message)).start()
			time.sleep(.3)
			
	def spam(self, amount: int, channel_id: str, message: str) -> None:

		for i in range(amount):
			for i in range(self.tokenamount):
				headers = {
				"authorization" : self.tokens[i]
				}
				payload = {
				"content" : message
				}
				s = requests.Session()
				s.post('https://discord.com/api/v9/channels/{}/messages'.format(channel_id), headers=headers, json=payload, proxies={"http" : "http://" + random.choice(self.proxies)})

if __name__ == "__main__":

	Main().main()
