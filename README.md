
## Introduction

Notes2Anki is your way to **write** your flashcards. Goodnotes 5 released a gamechanger in my opinion. You just write your flashcards,and you can study with them.
However, I don't like the idea of only learning in Goodnotes and their algorithm needs some work imo.
So I decided to create a way to make flashcards in Goodnotes (Or any other notes app) and export them to Anki!

Added image hosting service to reduce the Anki DB size.



## About Anki
Source: https://apps.ankiweb.net/

 Anki is a program which makes remembering things easy. Because it's a lot more efficient than traditional study methods, you can either greatly decrease your time spent studying, or greatly increase the amount you learn.

Anyone who needs to remember things in their daily life can benefit from Anki. Since it is content-agnostic and supports images, audio, videos and scientific markup (via LaTeX), the possibilities are endless.
For example:

    Learning a language
    Studying for medical and law exams
    Memorizing people's names and faces
    Brushing up on geography
    Mastering long poems
    Even practicing guitar chords!

### Anki Software

Check out the Anki website for download links: https://apps.ankiweb.net/#download

## How to create flashcards

It's just as simple as writing!
You just write on each page your Question on the top half of the page
and the answer on the bottom part.
Then you just need to export your document as a pdf.
So each of your page should look like this:

![](https://i.imgur.com/KZjVKMa.png)

You can also add field

1. code: To integrate mnemonics to code the card
2. reference: To add additional information besides the answer
3. Examples: Applications and real life examples to further understanding.
4. Reverse:  Add any character to create an reversed card. Leave blank to cancel the reversed card.

## Requirements

- Make sure you have **python3** installed.
- Run `pip install -r requirements.txt`
   to install the packages required to run the script.

## Usage

This script is run within the terminal.
### Windows
For Windows type _cmd_ in the search bar and then just follow the steps.
### Linux
You should know what the terminal is.

### MacOS
Open spotlight and search there for Terminal and then just follow the steps.

### Use

1. Create a Goodnotes Notebook with template FlashCard

2. Export the Notebook as pdf version and store in the library folder

3. Register at [Cloudinary](https://cloudinary.com)

4. Copy Cloud Name, API Key, and API Secret from the dashboard 

   and paste into the following string in the file notes2anki.py

   ![](https://i.imgur.com/WWNMrhP.png)

   ![](https://i.imgur.com/f9lmFPQ.png)

1. Run `python ./library/paper2anki.py YOURFILE.PDF NAME`
   So you give the program 2 Arguments:
   
   1. The PDF file which contains the flash cards
   2. The name you wish the deck to have.
   
6. Import the .apkg file into Anki

3. Study

## Credits:

- genanki (library to create anki cards in python): https://github.com/kerrickstaley/genanki
- pdfrw great pdf library: https://pypi.org/project/pdfrw/
