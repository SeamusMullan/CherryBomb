import datetime
import os

# Things like text colors, etc.
class C:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK  = '\33[30m'
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'

# Functions for dealing with error formatting

def returnError(error):
    print(C.FAIL + "ERROR: " + C.ENDC + "\n" + C.WARNING + error + C.ENDC)

def returnWarning(warning):
    print(C.WARNING + "WARNING: " + C.ENDC + "\n" + C.WARNING + warning + C.ENDC)

def returnInfo(info):
    print(C.OKBLUE + "INFO: " + C.ENDC + "\n" + C.OKBLUE + info + C.ENDC)

def saveErrorLog(error):
    if not os.path.exists("Error Logs\\"):
        os.makedirs("Error Logs\\")

    with open(f"Error Logs\\Log-{datetime.datetime}-CherryBomb.txt", "w") as errorLog:
        errorLog.write(error + "\n")
        errorLog.close()


# BIG PARAGRAPH OF TEXT
def returnTwintInfo():
    print(f"""
    {C.OKBLUE}Here is how to format your variables for the twitter modules.{C.ENDC}

    {C.OKCYAN}    Variable             Type       Description{C.OKGREEN}
    --------------------------------------------
    Username             (string) - Twitter user's username
    User_id              (string) - Twitter user's user_id
    Search               (string) - Search terms
    Geo                  (string) - Geo coordinates (lat,lon,km/mi.)
    Location             (bool)   - Set to True to attempt to grab a Twitter user's location (slow).
    Near                 (string) - Near a certain City (Example: london)
    Lang                 (string) - Compatible language codes: https://github.com/twintproject/twint/wiki/Langauge-codes
    Output               (string) - Name of the output file.
    Elasticsearch        (string) - Elasticsearch instance
    Year                 (string) - Filter Tweets before the specified year.
    Since                (string) - Filter Tweets sent since date, works only with twint.run.Search (Example: 2017-12-27).
    Until                (string) - Filter Tweets sent until date, works only with twint.run.Search (Example: 2017-12-27).
    Email                (bool)   - Set to True to show Tweets that _might_ contain emails.
    Phone                (bool)   - Set to True to show Tweets that _might_ contain phone numbers.
    Verified             (bool)   - Set to True to only show Tweets by _verified_ users
    Store_csv            (bool)   - Set to True to write as a csv file.
    Store_json           (bool)   - Set to True to write as a json file.
    Custom               (dict)   - Custom csv/json formatting (see below).
    Show_hashtags        (bool)   - Set to True to show hashtags in the terminal output.
    Limit                (int)    - Number of Tweets to pull (Increments of 20).
    Count                (bool)   - Count the total number of Tweets fetched.
    Stats                (bool)   - Set to True to show Tweet stats in the terminal output.
    Database             (string) - Store Tweets in a sqlite3 database.
    To                   (string) - Display Tweets tweeted _to_ the specified user.
    All                  (string) - Display all Tweets associated with the mentioned user.
    Debug                (bool)   - Store information in debug logs.
    Format               (string) - Custom terminal output formatting.
    Essid                (string) - Elasticsearch session ID.
    User_full            (bool)   - Set to True to display full user information. By default, only usernames are shown.
    Profile_full         (bool)   - Set to True to use a slow, but effective method to enumerate a user's Timeline.
    Store_object         (bool)   - Store tweets/user infos/usernames in JSON objects.
    Store_pandas         (bool)   - Save Tweets in a DataFrame (Pandas) file.
    Pandas_type          (string) - Specify HDF5 or Pickle (HDF5 as default).
    Pandas               (bool)   - Enable Pandas integration.
    Index_tweets         (string) - Custom Elasticsearch Index name for Tweets (default: twinttweets).
    Index_follow         (string) - Custom Elasticsearch Index name for Follows (default: twintgraph).
    Index_users          (string) - Custom Elasticsearch Index name for Users (default: twintuser).
    Retries_count        (int)    - Number of retries of requests (default: 10).
    Resume               (string) - Resume from the latest scroll ID, specify the filename that contains the ID.
    Images               (bool)   - Display only Tweets with images.
    Videos               (bool)   - Display only Tweets with videos.
    Media                (bool)   - Display Tweets with only images or videos.
    Pandas_clean         (bool)   - Automatically clean Pandas dataframe at every scrape.
    Lowercase            (bool)   - Automatically convert uppercases in lowercases.
    Pandas_au            (bool)   - Automatically update the Pandas dataframe at every scrape.
    Proxy_host           (string) - Proxy hostname or IP.
    Proxy_port           (int)    - Proxy port.
    Proxy_type           (string) - Proxy type.
    Tor_control_port     (int)    - Tor control port.
    Tor_control_password (string) - Tor control password (not hashed).
    Retweets             (bool)   - Get retweets done by the user.
    Hide_output          (bool)   - Hide output.
    Popular_tweets       (bool)   - Scrape popular tweets, not most recent (default: False).
    Skip_certs           (bool)   - Skip certs verification for Elasticsearch, useful for SSC (default: False).
    Native_retweets      (bool)   - Filter the results for retweets only (warning: a few tweets will be returned!).
    Min_likes            (int)    - Filter the tweets by minimum number of likes.
    Min_retweets         (int)    - Filter the tweets by minimum number of retweets.
    Min_replies          (int)    - Filter the tweets by minimum number of replies.
    Links                (string) - Include or exclude tweets containing one or more links. If not specified you will get both tweets that might contain links or not. (please specify `include` or `exclude`)
    Source               (string) - Filter the tweets for specific source client. (example: `--source "Twitter Web Client"`)
    Members_list         (string) - Filter the tweets sent by users in a given list.
    Filter_retweets      (bool)   - Exclude retweets from the results.
    {C.ENDC}
    """)




