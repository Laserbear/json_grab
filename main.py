import sys
""" Command Line Options should allow for real-time processing and offline processing of detected JSON
	Should also be able to accept a list of endpoints to scrape JSON from
	Perhaps a parameter for maximum storage on the device

"""
#The following function is borrowed without remorse from https://gist.github.com/dideler/2395703#file-pyargs-md
def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

dictofargs = getopts(sys.argv)
print(dictofargs)
if ('-edgy' in dictofargs.keys() and dictofargs['-edgy']): #edgy easteregg
	print("\x1b[1;32;40m"+"\r\n                      ______\r\n                   .-        -.\r\n                  /  get rekt  \\              \r\n                 |              |\r\n                 |,  .-.  .-.  ,|        @laserbear \r\n                 | )(_ /  \\_ )( |\r\n                 |/     /\\     \\|\r\n       (@_       <__    ^^    __>     \r\n  _     ) \\_______\\__|IIIIII|__/_______________________ \r\n (_)@8@8{}<___________________________________________/ \r\n        )_/         \\ IIIIII /           \r\n       (@            --------                    \r\n        "+"\x1b[0m")
url = raw_input("Domain to crawl?\n") #get domain to fire webcrawler at
print("Crawling: " +  url)


