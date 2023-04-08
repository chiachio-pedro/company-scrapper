# Company-Scrapper

A simple Python program that uses "Selenium" to scrap company data from LinkedIn with the objective to be used as Marketing and Sales Leads.

- v.1.00.00 - Release:
  - Officially released!
  - When executed it will scrap data from the companies that appear at the search results...
  - You must enter 3 basic parameters:
    - LinkedIn e-mail...
    - LinkedIn password...
    - Company search terms you want to use...

## Dependencies?

Google Chrome

## Get Started:

1 - Clone the project to your local machine:

```
git clone https://github.com/chiachio-pedro/company-scrapper.git
```

2 - Create the Python3 Virtual Environment based on the "requirements.txt"

```
python -m venv venv
```
```
venv\Scripts\activate
```
```
pip install -r requirements.txt
```

3 - Run the script!

```
python app.py
```

4 - Wait for Selenium to finish, based on the size of the info you are going to get it can take a while...

5 - After the scrap is done, a ".csv" file called "lead_list.csv" will be available at the folder.

**OBS: Remember to use a fake profile! Never knows if LinkedIn will ban you or not because of auto-scrapping!**
