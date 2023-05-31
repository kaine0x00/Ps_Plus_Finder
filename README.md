# Playstation Plus Finder

Long time members of the PS Plus service know the pain of *the monthly essential releases being amongst your physical library of games*. The intent behind this script is to **find out all of those physical games that are safe to be disposed of** (sold, traded, gifted etc.) because they're essentially duped on your library.

## Input

For this script to work, you must first **create a text file containing all your physical games** (or those you suspect are duped) separated by newlines, with the following format:
```
Mortal Kombat X
Titanfall 2
Fallout 4
```

It is important to note, you must be **precise with the naming** (punctuation, spaces etc) but *capitalisation is not necessary*

## Scrape and Result

**Two files will be created** with this script:

-  a *scrape file* (is non important for the user, since it contains css and all the text from the reference page), this file is necessary for the program to run but may be deleted later.
-  **Result file**: It will contain the **matches between your library and the source** in an easily readable format.

> The **path for these two files must be inputted as text** in the terminal upon running the script with the format: `$YOUR_PATH/$FILE_NAME.txt` (*use \ in Windows*)

## Dependencies

For the script to function, **you must have installed the scrapy library**, you may install it with `pip install scrapy` or *use the bash script included*. Also, you may know that this script depends on the following source: https://www.finder.com.au/playstation-plus-free-games, if this website were to dissapear or get too out of date **you may replace it in the script with another website** with a listing of ps plus titles.
