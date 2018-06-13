Pinky's CSV Cleanser
===
To get started, you'll need to have Python 3.6.5 installed to ensure this script runs correctly. It may work on lower or higher versions, but it has not been fully tested.

You'll need to pull the entire repository as the CSV files are currently hardcoded. 

Once you pull the repo, simply navigate to the directory and run `python cleanse-csv.py`

Assumptions Made
===
Generally, it's a bad idea to make assumptions, especially when creating software for client. However, sometimes time constraints sometimes dictate that you, as a developer, make some assumptions about implementation, requirements interpretations, and other such decisions in order to show progress. Normally, I would run these by a product owner, a BA, or another developer. Given the circumstances of this assignment, I opted to go with making assumptions over creating churn in discussing implementation.

Here is a list of assumptions that are made in the implementation:

* The CSV file always has 8 columns, they are the same format (bad unicode notwithstanding), and they are in the same order
* Huge files aren't an issue since there is no UI to block and no additional requirements were given around performance
* The CSV is available (and new one would be generated) in the same location as the script. In other words, the file won't be downloaded from a server (at this point).
* The header does not have UTF-8 encoding issues

Future Enhancements:
===

* Completing the business logic on "happy path" (e.g. good unicode in the CSV)
* Completing creation of a cleansed CSV file output
* Testing on a wider variety of files
* Turning the script into an app by adding "main" defintions