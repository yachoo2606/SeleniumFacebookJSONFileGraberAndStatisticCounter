# SeleniumFacebookJSONFileGraberAndStatisticCounter
 
## Set up

first of all you need to install requirements libraries via:
```
pip install -r requirements.txt
```

Next step is to create .env file in main directory
the structure of ./env file should be as follows (without quotes):

```dotenv
FBLOGIN='your faceebook email'
FBPASSWD='yout facebook password'
```

## Usage

First run the downloadFile.py and when downloading starts change the zoom of the window 
to fit list with files.

Next run the processFiles.py file to delete unnecessary zip files and show the statistics.
