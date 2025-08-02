## 1. Introduction 
-> Scrappy is a very simple web scraper that fetches news head lines along with their visit links from Hacker news and mails them to a specified email.

## 2. What are the files?
-> **bot.py** - The actual bot, 
   **cred.py** - Hold the credentials the bot.py uses.
	- FEA: Sending gmail address
	- FEA_PASS: Sending gmail address' app password, **not** the regular login one
	- TEA: The recieving email address
	- SS: Google's SMTP server
	- SP: Which port to connect to on the server
   **requirements.txt** - Holds the bot's dependencies that pip will install 

##3. How to use?
-> Step 1: Ensure you have firefox, python, and pip installed. Also, have a gmail account with app password ready. It will be 12 digit Alphabetic password given to you so that you can log into the FEA account. You CANNOT use your daily password here. 

   Step 2: Download Scrappy-V2, and run the following commands. [Note: Use powershell on windows]
		i. Go into Scrappy-V2 directory
		$ cd Scrappy-V2
		
		ii. Create and activate the python virtual environment in the directory
		-If in Windows:
			$ python -m venv venv
			$ venv\Scripts\Activate.ps1
		-If in Linux:
			$ python -m venv .venv
			$ source .venv/bin/activate

		iii. Get the required dependencies with pip
		$ pip install -r requirements.txt

   Step 3: Edit the cred.py file. Input your sending gmail address in FEA, its 12 digit Alphabetic password into FEA_PASS, and the receiving email address in TEA. 

   Step 4:  Run the bot.py



		
		
	
		
