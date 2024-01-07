#Created the environment using Gitbash to install the required libraries
#pip install requests #for making API requests
#pip install googlemaps #for Googlemaps integration
#pip install newsapi-python #for News API
#pip install blessed --for optional text based ui elements

# import the necessary libraries
import requests
import googlemaps
from newsapi import NewsApiClient
from blessed import Terminal
import random
from pprint import pprint as pp

#API keys
newsapi = NewsApiClient(api_key="86a9177772fd4216a64a3089ee4e0dd6") 
gmaps = googlemaps.Client(key="AIzaSyCf9T5oHNKjPyl_TRDM4ec5u3Z3SBaxNWU")  #get your API key from Google Cloud Console

# user interaction
term = Terminal()
print(term.clear) #to clear the terminal
print(term.center("Welcome to the World Travel News Quiz!")) #user welcoming statement
print(term.center("Explore the world through trivia and news!"))

 
# #user chooses their difficulty level
difficulty_level = input(term.center("Choose your difficulty level (easy, medium, hard): ")) 

#selecting a random country using Rest country API
response = requests.get("https://restcountries.com/v3.1/all?random=true")
print(response.status_code)
country_data_list = response.json()
random_country_index = random.randint(0, len(country_data_list) - 1)
country_data = country_data_list[random_country_index]

# pp(country_data)-- to inspect how the data from the API looks

country_name = country_data["name"]
country_code = country_data["cca2"]

#Extracting the questions answers
capital_city = country_data["capital"] 
currency= country_data["currencies"]
continent= country_data["continents"]

# # #getting the top news of a the random country(from the rest API) from the News API

top_headlines = newsapi.get_top_headlines(country_code)
#pp(top_headlines)-- checking if the news api is working 

if 'articles' in top_headlines:
    top_articles = top_headlines['articles'][:3]  # Selecting the first 3 articles
    for index, article in enumerate(top_articles, start=1):
        print(f"Headline {index}: {article['title']}")
        print(f"   Link: {article['url']}")
        print("------") # helps seperate and distinguish between the different articles
else:
    print("No articles found.")

question_1 = f"What is the capital of {country_name}?"
question_2 = f"What is the currency of {country_name}?"
question_3 = f"In which continent is {country_name} located?"
questions = [
    {"question": question_1, "correct_answer": capital_city},
    {"question": question_2, "correct_answer": currency},
    {"question": question_3, "correct_answer": continent}
]


#start score  
score = 0

#looping through the questions

for question in questions:
    term.clear()  # Clear the terminal
    print(question["question"])

    # added to display the user's answer
    user_answer = input("Your answer: ")

    # Check for the correct answer and update score
    if user_answer.lower() == str(question["correct_answer"]).lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {question['correct_answer']}")

# Display the final score
print(f"Your final score: {score}/{len(questions)}")




