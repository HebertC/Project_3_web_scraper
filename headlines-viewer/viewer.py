# import required modules
import csv
from flask import Flask, render_template

# path to CSV file with headlines
CSV_FILE_PATH = '/home/hbrtxito/Downloads/Project_3_Web_Scraper/cnn/news.csv'

# create Flask application
app = Flask(__name__)


def get_headlines_from_csv():
    """
    This function returns a list of headlines from CSV files in reversed order.
    If for some case this function will cause an exception, it will be display exception to console
    and will return an empty list
    """
    try:
        # open file for reading
        csvfile = open(CSV_FILE_PATH, 'rb')
        # create CSV file reader
        reader = csv.DictReader(csvfile)
        # create empty list for headlines
        headlines = []
        # for every ron in CSV file
        for row in reader:
            # read headline string, remove spaces (.strip() call) from both sides
            # and insert it to the list
            headlines.append(row['big_headlines'].strip())

        # close the file
        csvfile.close()
        # reverse the list (most fresh headlines will be on the first place)
        headlines.reverse()
        return headlines
    except Exception as e:
        # print exception message to the console
        print e
        # return an empty list
        return []

# set handler on root path
@app.route('/')
def index():
    # get last headlines
    last_headlines = get_headlines_from_csv()
    # render html template with a list of found headlines and return rendered html to browser
    return render_template('index.html', headlines=last_headlines)

# if file was ran by Python
if __name__ == '__main__':
    # start application development server
    app.run()
