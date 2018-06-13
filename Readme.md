# Pinky's CSV Cleanser
Welcome to the repository where all of your CSV cleansing dreams come true. Well, maybe not all of them. But this repository contains a script that:

* reads a CSV file 
* attempts to repair any UTF-8 encoding issues by replacing with the simple Unknown Unicode character
* formats the known columns according to the [requirements](requirements.md) (partially complete)
* generates a cleansed CSV file (not started)

## Setup
To get started, you'll need to have Python 3.6.5 installed in a macOS 10.13 environment to ensure this script runs correctly. It may work on lower or higher versions, but it has not been tested. In that case, YMMV.

## Run the Script
You'll need to pull the entire repository as the CSV files are currently hardcoded to those included in the directory. To use different CSV, simply replace the CSV content in the `sample-with-broken-utf8.csv` file. 

Once you pull the repo, simply navigate to the directory and run `python cleanse-csv.py`

## Assumptions Made
Generally, it's a bad idea to make assumptions in a vaccuum, especially when creating software for client. However, sometimes time constraints dictate that you, as a developer, make some assumptions about implementation, requirements interpretations, and other such decisions in order to show progress. Normally, I would run these by a product owner, a BA, or another developer. Given the circumstances of this assignment, I opted to go with making assumptions over creating churn in discussing implementation details.

Here is a list of assumptions that are made in the implementation:

* The CSV file always has 8 columns, they are the same format (bad unicode notwithstanding), and they are in the same order.
* Huge files aren't an issue since there is no UI to block and no additional requirements were given around performance.
* The CSV is available (and new one would be generated) in the same directory as the script. In other words, the file won't be downloaded from a URL.
* The header does not have UTF-8 encoding issues

# Future Enhancements
* Completing the business logic to normalize the CSV (e.g. good unicode in the CSV)
* Completing creation of a normalized CSV file output
* Testing on a wider variety of files and scenarios
* Refactoring the code to make better use of Python collection features and proper code structure to support running from a wider variety of scenarios

# Lessons (Re)Learned
Here is a summary of a few things I learned on this journey.

* Picking a language you're not intimately familiar with isn't the best option when there are time constraints. I should know this by now, but I really enjoyed digging into some meaty Python concepts.
* Don't dive so deep on the trickier problems that you ignore the obvious ones. I spent so much time on the bad unicode CSV, I completely neglected the good unicode CSV scenario. 