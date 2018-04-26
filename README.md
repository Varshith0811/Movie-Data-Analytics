# Movie-Data-Analytics
###### A tool to predict the IMDB rating of a movie using machine learning

### Features:
* Predict the IMDB rating of any movie
* Calculate error of predictions
* Display Movie data and poster from IMDB
* Interactive GUI

## Setup
### Dependencies
* tkinter (The main Tk software will also be needed if not installed)
* Pillow
* pandas
* scipy
* scikit-learn

### Installation
```sh
git clone https://github.com/robjweiss/Movie-Data-Analytics.git
```

## Instructions
1. Change directories to the `src` folder using `cd src`
2. Launch the program by running the main file using `python main.py`
3. Enter a move title and the year it was made, if known

## Usage
The following example uses a movie where the year is specified and a movie without a year being specified:
![Alt text](/examples/example.gif?raw=true "Example Usage")

Example result using Star Wars (2017):
![Alt text](/examples/StarWarsExample.png?raw=true "Star Wars (2017)")


## Additional Information
* The system implements machine learning using random forests and predicts the rating of a given movie based on data from over 10,000 films
* This program is written in python 3 and uses Tk as a user interface
* The [OMDb API](http://www.omdbapi.com/) was used to obtain the IMDb entries
* The data that the machine learning model is based on was obtained from this [dataset](https://www.kaggle.com/orgesleka/imdbmovies)
