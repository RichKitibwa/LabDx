# LabDx
## Machine learning model for automated laboratory diagnosis

### Getting started

### Setting up the virtual environment

Install pip on your computer.  
Clone the project from Github.  
Go into the project folder and run `python3 -m venv /path/to/new/virtual/environment` in the terminal inorder to create a virtual environment.  
Activate the virtual environment by running `your virtual env name\Scripts\activate` in the terminal in windows or `source your virtual env name/bin/activate` in MAC os and linux.  
Install Flask in the virtual enviromnet using `pip3 install flask` for MAcos or Linux and `pip install flask` for windows      
Run the app using `python3 -m flask run` in the terminal for MACOS or Linux and `python -m flask run` for windows   

### Deploying to heroku
Initialise the repository using `git init` in the terminal.  
Run `heroku login` to login to your heroku account  
Add the requirements file by running `pip freeze > requirements.txt`, Add the Procfile file and add this `web: gunicorn app:app`  
Add runtime.txt file, add this `python-3.7.2`  . 
Then add all changes and commit by running `git add . && git commit -m 'commit message'`  

Finally push to heroku by running `heroku git:remote -a LabDx`
