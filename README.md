# prober
proper.py -- My dyslexia kicked in and I completely bungled the spelling of prober, 
I thought it was funny so I kept it

the program is run from the command line with two arguments: the url 
formatted properly with the scheme (i.e. http:// or https://) as well as 
the specified file to write to

the program requires the default port of 80. 

The program uses the Requests python library (http://docs.python-requests.org/en/master/)
this library by default resolves internal redirect (307) responses. I kept this behavior in,
so internal redirects will resolve and the program will write a 200 response to the files

included is a samplefile which gives example output for http://playdota.com (which was down when I began running the prober) 
