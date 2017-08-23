# Your First Python Web App: Conor McGregor vs. Floyd Mayweather Flask Voting App + Heroku

### Here are your instructions
1. download the latest version of python from https://www.python.org/downloads/ and then install it. Also, make sure to check the **ADD TO PATH** box when going through the installation wizard.

2. Create an account on Heroku.com

3. MAC USERS ONLY: Install `homebrew` if you don't have it already with `sudo /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

4. MAC USERS ONLY: Open up your terminal with cmd + space then type in `terminal` and then Install the heroku CLI client with `brew install heroku` and press **enter** in the terminal

5. WINDOWS USERS ONLY: To install Heroku CLI Client on windows just go to `https://devcenter.heroku.com/articles/heroku-cli#windows` and click the `64-bit` or `32-bit` link to download and install

6. WINDOWS USERS ONLY: Open your command line by hitting the windows key and typing in `cmd` or `powershell`.

7. Type in `git` in your command line either on mac or windows and see if you get an error. If you do get an error, go online and type in `install git`. Then get `git` either for windows or mac by clicking one of the search results that pop up.

8. At this point, **Git and Heroku should be working**!

9. Now in your terminal or command prompt, enter the command `git clone https://github.com/CleverProgrammer/flask_vote_app`

10. Now navigate to the project folder using `cd flask_vote_app`

11. Enter the command: `heroku login` and provide your heroku login details. Note: When you type in password the cursor in the command line doesn't move. Don't freak out lol just type in your password for Heroku anyway.

12. Now after you are logged in, use `heroku create` to create a new heroku application for you.

13. push the code to heroku using `git push heroku master`

14. Now make your own database where the votes will be stored with `heroku addons:create heroku-postgresql`

15. Now launch the web app online: `heroku ps:scale web=1`

16. Here is a little tricky and advanced part but don't worry so much about understanding it yet... Then in your terminal, you’ll need to run migrations for your db schema, to do this simply type `heroku run bash` on your terminal

17. Once the terminal loads enter the command `python init_db.py`

18. Now press `ctrl + d` to exit out of the heroku bash thing.

19. BOOOOOOM! Your site is now on Heroku. Type in `heroku open` to go check it out online woohoo!!
