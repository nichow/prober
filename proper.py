import sys
import time
import requests
from urllib.parse import urlparse

# ERROR HANDLING
# first check if we have the proper number of arguments
if len(sys.argv) != 3:
    print('Invalid number of arguments. Prober must execute with 2 arguments.')
    print('1st Argument: Test site URL, 2nd Argument: file to be written to')
    sys.exit(1)
# parse the url
p = urlparse(sys.argv[1])
if p.scheme != 'http' and p.scheme != 'https':
    print('InvalidArgument: first argument must be a properly formatted URL, should start with "http://" or "https://"')
    sys.exit(1)
if p.port != 80 and p.port is not None:
    print('InvalidPort: Must use default port of 80')
    sys.exit(1)

# assign our variables and create the sample file if it doesn't exist
url = sys.argv[1]
filepath = sys.argv[2]
file = open(filepath, 'w+')
# write the url we're using in the header
file.write('URL=' + url + '\n\n')
while True:
    # record the time just before the request and cast as int
    startTime = round(time.time())
    # GET request to url specified
    try:
        print('making request to ' + url)
        r = requests.get(url, timeout=30.0)
        print("request successful, writing to " + filepath)
        # write truncated UNIX time along with the received status code
        file.write(str(round(time.time())) + ', ' + str(r.status_code) + '\n')
    except requests.exceptions.Timeout:
        # catch timeout exception, write time with -1 code and reattempt
        print('connection timeout')
        file.write(str(round(time.time())) + ', -1\n')
    except requests.exceptions.TooManyRedirects:
        # catch redirect loop, write time with -1 code and reattempt
        print("Max number of redirects reached")
        file.write(str(round(time.time())) + ', -1\n')
    except requests.exceptions.ConnectionError:
        # catch errors such as DNS errors, or any other connection problems, write -1 and reattempt
        print('Failed to connect to server')
        file.write(str(round(time.time())) + ', -1\n')
    except requests.exceptions.RequestException:
        # if request was bad program aborts
        print('Request Exception, likely a bad url')
        file.write(str(round(time.time())) + ', -1\n')
    # record time after request was made
    endTime = round(time.time())
    # sleep for 30 seconds minus the amount of time it took to execute
    time.sleep(30 - (endTime - startTime))
