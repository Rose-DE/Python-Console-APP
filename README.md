**World Travel News Quiz**

**Description**
The World Travel News Quiz is an interactive Python-based quiz game that immerses users in exploring different countries through trivia and news headlines. This engaging game utilizes REST APIs to fetch random country data from Restcountries API. It displays the top three news headlines using the News API and  presents three questions related to the randomly chosen country and. Users answer the questions and receive scores based on their answers.

**Features**
•	Allows users to choose the difficulty level of the quiz.
•	Selects a random country using the REST countries API.
•	Retrieves the top three headlines from the randomly chosen country using the News API. 
•	Asks three questions related to the country (capital, currency, continent).
•	Scores users based on the correctness of their answers.
•	Provides appropriate badges based on the user's final score.
•	Offers a link to share the game experience on Twitter.

**Installations**
•	Git bash
•	Requests: For making API requests
•	NewsApi-python: For News API integration
•	Blessed: For optional text-based UI enhancements

**Coding Steps**
1.	Imports: Import necessary libraries. Ln 8:13
2.	API Integration: Use API keys to connect with the required APIs.   Ln 16
3.	User Interactions: Define user interactions using print statements and terminal functions.  Ln 20:22
4.	Difficulty Level Selection: Allow users to choose the quiz difficulty level using input function. Ln26
5.	REST API Calls: Fetch a random country's data and select a country using REST APIs.   Ln 29:43
6.	API Integration: Combine data from REST and News APIs.   Ln 47
7.	Top Headlines Display: Show the top three headlines for the chosen country.   Ln 50:57
8.	Question Generation: Create three questions using a dictionary. Ln 59:66
9.	Score Calculation: Evaluate the user's score based on their answers. Ln 70:79
10.	Twitter Sharing Link: Provide a link to share the score on Twitter. Ln 100

**Contributors**
•	Imports: Edith Rosasi and Sandra Abali
•	User Interactions: Lilian Nyabicha
•	Difficulty Level Selection: Amarachi Njoku
•	REST API Calls: Rose Wamaitha, Monsurat Adepoju, and Praise Ajogbor
•	API Integration: Mosunmola Fasasi
•	Top Headlines Display: Edith Rosasi and Sandra Abali
•	Question Generation: Mosunmola Fasasi, Rose Wamaitha, Praise Ajogbor
•	Score Calculation: Lilian Nyabicha and Monsurat Adepoju
•	Twitter Sharing Link: Amarachi Njoku

**Usage**
•	Run the script and follow on-screen instructions.
•	Choose the quiz difficulty level ('easy', 'medium', 'hard').
•	View the top three news headlines of the randomly chosen country.
•	Answer the questions related to the selected country.
•	Receive scores based on your answers.
•	Earn badges based on your final score.
•	Share your score on Twitter using the provided link.

**Support**
Contributions to enhance the quiz game or add new features are welcome! To contribute:
1.	Fork the repository.
2.	Create a new branch (git checkout -b feature/enhancement).
3.	Make your changes and commit them (git commit -am 'Add new feature').
4.	Push to the branch (git push origin feature/enhancement).
5.	Create a new Pull Request.

**Credits**
•	Restcountries API
•	News API

**License**
This project is licensed under the Women Techsters Fellowship 2023/2024/subgroup 10.
