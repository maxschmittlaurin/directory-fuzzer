# Author : Maximilien Schmitt-Laurin

# IMPORTANT NOTICE :
# The following source code is meant for educational purposes only and should not be used for malicious activity.

# This script finds resources on a remote host based on a word list provided as input.

import requests
from datetime import datetime



# Ask user for the URL, an extension and a word list.

url = input("\n Enter a URL : ")
ext = input("\n Enter an extension : ")


# This directory fuzzer is basic and doesn't use multithreading so long word lists
# are not advised.

wordList = input("\n Enter a word list (.txt) : ")




# Check if the word list exits.

try:

    # Read the word list.
    
    wordListLines = open(wordList, "r").readlines()

except:

    print("\n\n Can't find the word list. \n")
    exit()




# Check if the given URL is valid

try:
    t = requests.get(url)

except:

    print("\n\n Invalid URL \n")
    exit()




# Print a nice banner with information on which host are we about to scan.

print("")
print("_" * 60)
print(" Please wait, scanning remote host...", url)
print("_" * 60)
print("")



# Check the date and time the scan was started.

scanStartTime = datetime.now()




hasFoundResults = False



try:

    # Looping for each word in our word list.

    for i in range(0, len(wordListLines)):

        word = wordListLines[i].replace("\n", "")


        # Send a GET request to the specified URL.

        r = requests.get(url + "/" + word + ext)


        # If we don't receive a 404 status code...

        if r.status_code != 404:

            if not hasFoundResults:

                hasFoundResults = True

                # We print that the scan found some resources.

                print("\n The scan found the following resources : \n")


            # We print the URL and the status code of the requested resource.

            print(" " + url + "/" + word + ext + " - " + str(r.status_code))

except:

    print("\n The scan was interrupted due to an unexpected error. \n")
    exit()



# If the scan did not find any resources.

if not hasFoundResults:

            # We print that the scan did not find any resources.

            print("\n The scan did not find any resources : \n")



# Check the date and time again.

scanEndTime = datetime.now()


# Calculate the difference in time to know how long the scan took.

totalScanTime = scanEndTime - scanStartTime


# Printing the information on the screen.

print(f"\n Scanning completed in : {totalScanTime} \n")



print("")
