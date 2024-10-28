<h2>Hello! :wave:</h2>
<h3>Thanks for checking out my project. </h3>

This program aims to predict the language in which a string of text is written using a Multinomial Naive Bayes classifier and language data from Tatoeba. 

## :book: Table of Contents
1. [Project Overview](#computer-project-overview)
2. [Installation](#wrench-installation)
3. [Usage](#man_technologist-usage)

## :computer: Project Overview

This project is a language detection model designed to identify the language of a given text input. It utilizes a Naive Bayes (NB) classifier and various text preprocessing techniques to build a robust model capable of predicting languages accurately. The model can be selected to operate at two levels: a 10-language fast model and a 100-language comprehensive model, allowing flexibility based on performance needs.

## :wrench: Installation

To set up this project on your local machine, follow these steps:

1. <b>Download the Project Files:</b>
   - Ensure you have received the project files. You can download them from the provided link or source.

2. <b>Extract the Files:</b>
   - If the project files are in a zip archive, extract them to your desired directory.

3. <b>Extract NB.zip:</b>
   - The models in this project are stored in the NB.zip file. Extract them in the root project folder before running the program. 

3. <b>Navigate to the Project Directory:</b>
   - Open your terminal or command prompt and navigate to the directory where you extracted the project files.
   ```bash
   cd path/to/NB-Language_Classifier
4. <b>Ensure You have the Necessary Libraries Installed</b>
   - If you are only running main.py, you only need:
      - joblib
   - If you want to train/test the models using the Tatoeba or your own data, you will need:
      - sklearn
      - pandas
      - langcodes
      - joblib
   - Use the following command to install the libraries:
   ```bash
   pip install [library_name]

## :man_technologist: Usage
1. Run the Main Program:
   - Execute the 'main.py' file to begin running the program
   ```bash
   python main.py
2. Select a Mode:
   - The program gives the user 2 models to select from.
   ```bash
   Hello! Which model would you like to use? (1 or 2)
   1. 10-Language Model (Faster)
   2. 100-Language Model (Slower)
   ```
   - The 10-Language Model has training on data containing the top 10 most widely used languages available in the dataset: English, Chinese, Hindu, Spanish, French, Bengali, Portuguese, Russian, Urdu, and Japanese
   - The 100-Language Model was trained on the top 100 languages seen the most in the Tatoeba Dataset. If you want to look at the data here is a download link (WARNING: This file is 663 MB):
      - https://downloads.tatoeba.org/exports/sentences.
   - The model will then ask for an input:
   ```bash
   Okay! Tell me somthing, and I will tell you what language you are speaking! :)
   ```
   - You can then input some phrase in any of the trained languages and it will output what it thinks is the correct answer:
</div>
