# World Travel News Quiz

## Description

The World Travel News Quiz is an interactive Python-based quiz game that immerses users in exploring different countries through trivia and news headlines. This engaging game utilizes REST APIs to fetch random country data from Restcountries API. It displays the top three news headlines using the News API and presents three questions related to the randomly chosen country. Users answer the questions and receive scores based on their answers.

## Features

- **Difficulty Levels**: Allows users to choose the difficulty level of the quiz.
- **Random Country Selection**: Selects a random country using the REST countries API.
- **News Headlines Retrieval**: Retrieves the top three headlines from the randomly chosen country using the News API.
- **Interactive Questions**: Asks three questions related to the country (capital, currency, continent).
- **Scoring System**: Scores users based on the correctness of their answers.
- **Badges**: Provides appropriate badges based on the user's final score.
- **Twitter Integration**: Offers a link to share the game experience on Twitter.

## Installations

Ensure you have the following installed:

- [Git Bash](https://gitforwindows.org/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [NewsApi-python](https://github.com/mattlisiv/newsapi-python)
- [Blessed](https://github.com/jquast/blessed) (optional text-based UI enhancements)

## Coding Steps

1. **Imports**: Import necessary libraries. (Lines 8-13)
2. **API Integration**: Use API keys to connect with the required APIs. (Line 16)
3. **User Interactions**: Define user interactions using print statements and terminal functions. (Lines 20-22)
4. **Difficulty Level Selection**: Allow users to choose the quiz difficulty level using the input function. (Line 26)
5. **REST API Calls**: Fetch a random country's data and select a country using REST APIs. (Lines 29-43)
6. **API Integration**: Combine data from REST and News APIs. (Line 47)
7. **Top Headlines Display**: Show the top three headlines for the chosen country. (Lines 50-57)
8. **Question Generation**: Create three questions using a dictionary. (Lines 59-66)
9. **Score Calculation**: Evaluate the user's score based on their answers. (Lines 70-79)
10. **Twitter Sharing Link**: Provide a link to share the score on Twitter. (Line 100)

## Contributors

- **Imports**: Edith Rosasi and Sandra Abali
- **User Interactions**: Lilian Nyabicha
- **Difficulty Level Selection**: Amarachi Njoku
- **REST API Calls**: Rose Wamaitha, Monsurat Adepoju, and Praise Ajogbor
- **API Integration**: Mosunmola Fasasi
- **Top Headlines Display**: Edith Rosasi and Sandra Abali
- **Question Generation**: Mosunmola Fasasi, Rose Wamaitha, Praise Ajogbor
- **Score Calculation**: Lilian Nyabicha and Monsurat Adepoju
- **Twitter Sharing Link**: Amarachi Njoku

## Usage

1. Run the script and follow on-screen instructions.
2. Choose the quiz difficulty level ('easy', 'medium', 'hard').
3. View the top three news headlines of the randomly chosen country.
4. Answer the questions related to the selected country.
5. Receive scores based on your answers.
6. Earn badges based on your final score.
7. Share your score on Twitter using the provided link.

## Support

Contributions to enhance the quiz game or add new features are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/enhancement`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/enhancement`).
5. Create a new Pull Request.

## Credits

- [Restcountries API](https://restcountries.com/)
- [News API](https://newsapi.org/)

## License

This project is licensed under the Women Techsters Fellowship 2023/2024/subgroup 10.
