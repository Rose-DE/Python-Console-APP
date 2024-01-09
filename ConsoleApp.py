#Created the environment using Gitbash to install the required libraries
#pip install requests #for making API requests
#pip install newsapi-python #for News API
#pip install blessed --for optional text based ui elements
# used if and else statements alongside dictionaries to define the game

# import the necessary libraries
import requests
from newsapi import NewsApiClient
from blessed import Terminal
import random
import time
import urllib.parse
import webbrowser
from pprint import pprint as pp

#API keys
newsapi = NewsApiClient(api_key="86a9177772fd4216a64a3089ee4e0dd6") 

# user interaction
term = Terminal()
print(term.clear) #to clear the terminal
print(term.center("Welcome to the World Travel News Quiz!")) #user welcoming statement
print(term.center("Explore the world through trivia and news!"))

 
# #user chooses their difficulty level
while True:
    difficulty_level = input(term.center("Choose your difficulty level (easy, medium, hard): ").lower())
   if difficulty_level.lower() in ['easy', 'medium', 'hard']:
        break
    else:
        print("Invalid difficulty level. Please choose from 'easy', 'medium', or 'hard'.")

# Display a message based on the selected difficulty level
if difficulty_level == 'easy':
    print("Great choice! Get ready for some easy questions.")
elif difficulty_level == 'medium':
    print("You're up for a challenge! Medium difficulty it is.")
else:
    print("Brace yourself! Hard difficulty awaits.")

# Confirm the chosen difficulty level
print(f"You chose the difficulty level: {difficulty_level}")

#selecting a random country using Rest country API
response = requests.get("https://restcountries.com/v3.1/all?random=true")
#print(response.status_code)
country_data_list = response.json()
random_country_index = random.randint(0, len(country_data_list) - 1)
country_data = country_data_list[random_country_index]

# pp(country_data)-- to inspect how the data from the API looks

country_name = str(country_data["name"]["common"])
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
    if any(user_answer.lower() in str(answer).lower() for answer in question["correct_answer"]):
        print("Correct!")
        score += 1
    else:
        correct_answers_str = ', '.join(map(str, question['correct_answer']))
        print(f"Wrong! The correct answer is {correct_answers_str}")
# Display the final score
print(f"Your final score: {score}/{len(questions)}")

#final message to the user
if score == 3:
   print("Congratulations, you've earned the 'Travel Expert' badge!")
elif score == 0:
  print ("oops!! get back on the road")
else:
    print("Congratulations, you've earned the 'Travel' badge!")

# delay final score output by 3 seconds
time.sleep(3)

#link to share the game on socials
tweet_text = "I just scored " + str(score) + " on the World Travel News Quiz! #wtf #group10 #travelquiz"
encoded_text = urllib.parse.quote(tweet_text)
url = f"https://twitter.com/intent/tweet?text={encoded_text}"
webbrowser.open(url)





