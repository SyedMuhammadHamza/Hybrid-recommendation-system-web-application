# Hybrid Recommendation System
<img alt="Website" src="https://img.shields.io/website?url=https%3A%2F%2Fsmhxrecommendersystemapp.herokuapp.com%2F">
<img alt="GitHub" src="https://img.shields.io/github/license/SyedMuhammadHamza/Hybrid-recommendation-system-web-application">
<img alt="GitHub" src="https://img.shields.io/badge/contributions-welcome-brightgreen">


The Regression-based Movie Recommender system that's a hybrid of content-based and collaborative filtering approaches. Simply rate some movies and get immediate recommendations tailored for you


## Table of contents

* [About](##About)
* [Table of contents]()
* [Articles]()
* [Kaggle competition]()
* [Courses & Certificates]()
* [Projects]()
* [Contact]()


## Prerequisites
The following open source packages are used in this project:
* Numpy
* Pandas
* Matplotlib
* Flask
* IMDbPY API

## Project Structure 
```
project
│   README.md
│    
└───Data
│   │   Data_README.txt
│
└───Images
|   |   img1.png
|   |   img1.png
|   |   ...
|
└───Model
│   │   Exploratory data analysis with PostgreSQL.ipynb
│   │   Hybrid recommendation algorithm.ipynb
│   │   PostgreSQL_Database_wrapper.py
│   │   Movies_Datase.pkl
│   │   Movies_Learned_Features.pkl
│   │
│   └───images
│       │   img1.png
│       │   img2.png
│       │   ...
│   
└───Server
      │   README.txt
      └───templates
      │     │    home.html
      │     │    layout.html
      │     │    result.html
      └───app.py
      └───Movies_Datase.pkl
      └───Movies_Learned_Features.pkl
      └───requirements.txt
      └───templates
```
## Dataset 
The dataset is provided by GroupLens and can be downloaded from here it contains the following files(links.csv, movies.csv, ratings.csv, and tags.csv)

> "This dataset (ml-latest-small) describes 5-star rating and free-text tagging activity from MovieLens, a movie recommendation service. It contains 100836 ratings and      3683 tag applications across 9742 movies. These data were created by 610 users between March 29, 1996, and September 24, 2018. This dataset was generated on September    26, 2018."
This [Dataset](https://files.grouplens.org/datasets/movielens/ml-latest-small.zip) of 1 MB is the one used in all Notebooks 
This [Dataset](https://files.grouplens.org/datasets/movielens/ml-latest.zip) of 265 MB is the one used for training deployed model. 

## Roadmap
This Image sums it All up.
<img src="https://github.com/SyedMuhammadHamza/Hybrid-recommendation-system-web-application/blob/main/Images/roadmap.jpeg"/>

## Exploratory Data Analysis(EDA) with PostgreSQ
In this part of the project, I've performed Exploratory data analysis with PostgreSQL.The idea to use PostgreSQL for EDA gives you a sense of how the relational database works, how data in it is stored, and more importantly how to get data out of the database. SQL is a very flexible declarative language and can be used to pose a rich set of queries to get data out of the database even tho it's not Turing complete but its ability to perform data manipulation is exceptional and makes it a great companion to have during EDA I'm going to use SQL queries for data manipulation for almost every single graphical EDA technique today along with some other python libraries mainly for visualization
[NOTEBOOK](https://github.com/SyedMuhammadHamza/Hybrid-recommendation-system-web-application/blob/main/Model/Exploratory%20data%20analysis%20with%20PostgreSQL.ipynb)

## About Hybrid Algorithm 
The hybrid recommendation system consists of the following sequence of steps [NOTEBOOK](https://github.com/SyedMuhammadHamza/Hybrid-recommendation-system-web-application/blob/main/Model/Hybrid%20recommendation%20algorithm.ipynb)
### Step 1. Collaborative filtering
The main objective of collaborative filtering at this step is to learn features for different movies. The implementation of Collaborative filtering here performs "Feature learning" Using a variation of multivariate regression with gradient descent as an optimization algorithm, it takes as input user-item interaction matrix and simultaneously learns both the parameters for different users and features for different movies I'm only going to use Features for different movie in the next step but this technique of using both the parameters for users and feature for movies to learn both simultaneously works beautifully for a problem like recommender systems because this approach unlike content-based filtering doesn't require features for different movies to learn parameters for users or parameters for users to learn features for different movies all you need is a user-item interaction matrix and this algorithm will learn a reasonably good set of both the parameters for users and features for movies because it's a modification of multivariate regression whose optimization objective is a concave cost function that always converges towards global minima regardless of your initial values for both the parameters of users and features for different movies. Once features for movies have been learned by collaborative filtering I'm going to save them in python's [.PKL] file that serializes objects to files on disk and deserialized back into the program at runtime when needed

### Step 2. Content-based filtering
The content-based filtering here again is going to be an extension of multivariate regression but unlike collaborative filtering here I'm going to use the features for movies learned using collaborative filtering now to learn online web-application user parameter using content-based filtering thats unique to the user based on his/her web application movie ratings.This content-based filtering algorithm will run and learn online the parameters unique to each web-application user but this algorithm by no means a type of Online learning algorithm because that definition strictly includes the ability of algorithm to use sequential data coming as input online and use it to update the best predictor for future data at each step

### Step 3. Prediction
Prediction (uses both the Features for movies learned using collaborative filtering and the Parameters unique to user learned using content-based filtering to recommend top-N recommendation) The prediction uses both the vectors for movies learned using collaborative filtering and the parameter unique to user learned using content-based filtering to recommend top-N recommendation
The prediction logic for my web application user is pretty straightforward I'm going to predict the score for all 9742 movies, where each prediction is a linear combination of Movie feature vector (x) learned using Collaborative filtering and Feature vector for web-application user θ learned using content-based filtering

## Model Evaluation
For the evaluation, I've used MSE for learning curve analysis on test and train sets
[NOTEBOOK](https://github.com/SyedMuhammadHamza/Hybrid-recommendation-system-web-application/blob/main/Model/Hybrid%20recommendation%20algorithm.ipynb)

## Usage
Setup to run on localhost<br/>
1.Clone the repository
```
git clone https://github.com/SyedMuhammadHamza/Hybrid-recommendation-system-web-application.git
cd ~/Hybrid-recommendation-system-web-application
```
2. Create a Python 3.7 environment.
```
  virtualenv .
```
      Activate Your Virtual Environment<br/>
      for Linux
      ```
      source bin/activate
      ```
      for Windows
      ```
      cd Scripts
      then
      activate
      ```
3. Install dependencies.
```
   pip install -r requirements.txt
```
4. Run following command from the directory you have stored the file
```
python app.py
```
## Notebooks and Files
* [Exploratory data analysis with PostgreSQ](https://github.com/SyedMuhammadHamza/Hybrid-recommendation-system-web-application/blob/main/Model/Exploratory%20data%20analysis%20with%20PostgreSQL.ipynb)
* [Hybrid recommendation algorithm and evaluation](https://github.com/SyedMuhammadHamza/Hybrid-recommendation-system-web-application/blob/main/Model/Hybrid%20recommendation%20algorithm.ipynb)
* [PostgreSQL_Database_wrapper](https://github.com/SyedMuhammadHamza/Hybrid-recommendation-system-web-application/blob/main/Model/PostgreSQL_Database_wrapper.py)
* [Flask server files](https://github.com/SyedMuhammadHamza/Hybrid-recommendation-system-web-application/tree/main/Server)

## References 
updting soon

## Contributing
Contribute by opening an [issue]() or a [pull request](https://github.com/SyedMuhammadHamza/Hybrid-recommendation-system-web-application). [Guide](https://github.com/firstcontributions/first-contributions) for beginners to make their first contribution.

## Authors
[SYED MUHAMMAD HAMZA](https://syedmuhammadhamza.github.io/Hamza_Portfolio/)

©SyedMuhammadHamza Licensed under [MIT License]()
