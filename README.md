# File Organization Script for Legal Estate Planning Documents

## Project Overview
In this project, I developed a Python-based script to automate the sorting of estate planning documents into predefined categories. The goal was to help organize large sets of documents like wills, deeds, and financial records. The script identifies keywords in file contents and uses those to categorize the files into Real Estate, Financial, and Personal Property folders.

## Tools & Technologies Used
- Python 3
- Libraries: `os`, `shutil`
- Future Enhancements: Use of regex for more advanced keyword matching

## Key Features
- Scans files in a source folder
- Reads file contents and identifies keywords
- Sorts files into folders based on keyword matches
- Preserves original files using a copy method

## Workflow
1. Read file contents
2. Match keywords to a predefined category
3. Copy file to appropriate category folder
4. Print summary and status to terminal

## Sample Results
Example input files:
- `John_House_Will.txt` -> Real Estate
- `Robert_IRA_Plan.txt` -> Financial
- `David_Jewelry_Collection.txt` -> Personal Property

Terminal output shows each step, including matches and any issues accessing files.

## Future Enhancements
- Use regex for smarter keyword matching
- Add new categories (e.g., Health Records, Tax Documents)
- Create a simple GUI for non-technical users
- Add more robust error handling for file access and IO issues

## Conclusion
This script demonstrates practical legal tech problem-solving using Python. It’s adaptable to legal environments where large volumes of documents need to be accurately and securely organized.
