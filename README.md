# fun_project_1_abizar
This is the first fun project from the Complete AI Python Bootcamp by Skill Academy Pro.


# Mini Quiz App: Indonesian

# Facts and Myths with Streamlit

## Table of Contents

```
● Project Overview
```
```
● Installation Instructions
```
```
● Running the Application
```
```
● Quiz Content Overview
```
```
● Scoring System
```
```
● Profession Suggestions
```
```
● Requirements and Dependencies
```
```
● Contributing and Adding New Questions
```
## Project Overview

Welcome to the **Mini Quiz App: Indonesian Facts and Myths** , an
engaging and interactive quiz application built using Streamlit. This app
is designed to test and expand your knowledge about Indonesia’s rich
cultural heritage, fascinating facts, and popular myths. Whether you are
a curious learner, a student, or just someone who loves trivia, this quiz
offers a fun and educational experience.

The quiz presents a series of multiple-choice questions where users
select whether a statement is a fact or a myth. After completing the quiz,
users receive a detailed score report, personalized feedback, and even a
profession suggestion based on their performance. The app combines
educational content with an intuitive user interface, making learning
enjoyable and accessible.

This project showcases how Streamlit can be used to create dynamic,
stateful web applications with minimal code, emphasizing simplicity,
clarity, and user engagement.

## Installation Instructions


To get started with the Mini Quiz App, you need to have Python installed
on your system. The app relies on the Streamlit library, which can be
easily installed via pip. Follow these steps to set up the environment:

1. **Install Python**
Ensure you have Python 3.7 or higher installed. You can download it from
the official website: https://www.python.org/downloads/.
2. **Create a Virtual Environment (Optional but Recommended)**
Creating a virtual environment helps manage dependencies and avoid
conflicts with other projects.

python -m venv quiz-env source quiz-env/bin/activate # On Windows:
quiz-env\Scripts\activate

3. **Install Streamlit**
Use pip to install Streamlit, the core dependency for running the app.

pip install streamlit

4. **Download the Application Code**
Save the Python script containing the quiz app code (e.g.,
fun_project_1.py to your local machine.

By following these steps, you will have a ready environment to run the
quiz app smoothly.

## Running the Application

Once the installation is complete, running the Mini Quiz App is
straightforward. Open your terminal or command prompt, navigate to the
directory containing the app script, and execute the following command:

streamlit run fun_project_1.py

This command launches the Streamlit server and automatically opens the
app in your default web browser. The interface is user-friendly, with
clear instructions and interactive elements such as radio buttons for
answer selection and buttons to submit your responses.

You can retake the quiz as many times as you like, and the app will
maintain your session state to keep track of your answers and scores
during each attempt.

## Quiz Content Overview

The quiz consists of a carefully curated set of questions focusing on
Indonesian facts and myths. Each question presents a statement, and the


user must decide whether it is a Fakta (Fact) or Mitos (Myth). The
questions cover a variety of topics, including:

```
● Historical landmarks and their origins (e.g., Candi Borobudur)
```
```
● Unique flora and fauna native to Indonesia (e.g., Rafflesia arnoldii)
```
```
● Natural disasters and their historical impact (e.g., Gunung
Krakatau eruption)
```
```
● Cultural practices and traditions (e.g., eating habits)
```
```
● Traditional arts and performances (e.g., Wayang kulit)
```
Each question is accompanied by two answer choices, and after
submission, the app provides immediate feedback explaining why the
answer is correct or incorrect. This educational approach helps users
learn interesting facts while dispelling common myths.

## Scoring System

The scoring mechanism is designed to be simple yet effective in
evaluating the user's knowledge. Here’s how it works:

```
● Each correct answer awards one point.
```
```
● Incorrect answers do not penalize the user but do not add to the
score.
```
```
● The total score is the sum of all correct answers out of the total
number of questions.
```
After submitting the quiz, users receive a detailed breakdown of their
performance, including:

```
● Total score displayed as “X out of Y” where X is the number of
correct answers and Y is the total questions.
```
```
● Individual feedback for each question, highlighting the correct
answer and providing informative messages to reinforce learning.
```
This scoring system encourages users to aim for accuracy while
providing constructive feedback to improve their understanding.

## Profession Suggestions

To add a fun and personalized touch, the app suggests a profession or
role based on the user’s quiz score. This feature is designed to motivate


users and give them a playful insight into how their knowledge might
align with certain cultural or academic interests.

The profession suggestions are categorized as follows:

```
● Perfect Score (All Correct Answers):
Ahli Budaya Indonesia (Indonesian Culture Expert) — You have an
excellent grasp of Indonesian facts and myths, making you a great
candidate for cultural research or education.
```
```
● High Score (70% or More Correct):
Peneliti Sejarah (History Researcher) — Your knowledge is strong,
and you have the potential to delve deeper into historical studies.
```
```
● Moderate Score (40% to 69% Correct):
Penggemar Budaya (Culture Enthusiast) — You have a good
foundation and a keen interest in Indonesian culture.
```
```
● Low Score (Below 40%):
Pemula yang Ingin Belajar (Beginner Eager to Learn) — Everyone
starts somewhere! Keep exploring and learning more about
Indonesia.
```
This feature not only adds an element of gamification but also
encourages continuous learning and curiosity.

## Requirements and Dependencies

The Mini Quiz App is built with simplicity and accessibility in mind. The
primary requirements and dependencies include:

```
● Python 3.7+ : The programming language used for the app.
```
```
● Streamlit : The web framework that powers the interactive UI and
session management.
```
Additional dependencies are minimal, making the app lightweight and
easy to deploy on various platforms, including local machines, cloud
servers, or containerized environments.

To ensure compatibility and smooth operation, it is recommended to keep
Streamlit updated to the latest stable version.

## Contributing and Adding New Questions

This project is designed to be easily extendable and customizable. If you
want to contribute or add new questions to the quiz, follow these
guidelines:


5. **Fork or Clone the Repository**
Obtain a local copy of the project files.
6. **Locate the Questions Dictionary**
In the main Python script (fun_project_1.py, find the dictionary named
questions. This dictionary holds all quiz questions as keys, with their
corresponding answer choices, correct answers, and feedback messages
as values.
7. **Add New Questions**
To add a new question, insert a new key-value pair in the dictionary
following the existing format. For example:

"New question statement here.": { "choices": ["Fakta", "Mitos"],
"correct": "Fakta", "correct_msg": "Correct answer explanation.",
"incorrect_msg": "Incorrect answer explanation." }

8. **Maintain Consistency**
Ensure that each question has exactly two choices: "Fakta" and "Mitos".
Provide clear and informative feedback messages to enhance the
learning experience.
9. **Test Your Changes**
Run the app locally to verify that the new questions appear correctly and
that scoring and feedback work as expected.
10. **Submit a Pull Request (If Applicable)**
If contributing to a shared repository, submit your changes for review
and inclusion.

By following these steps, you can help grow the quiz content, making it
richer and more diverse for all users.

Thank you for exploring the Mini Quiz App! We hope this tool inspires
you to learn more about Indonesia’s incredible culture and history while
having fun along the way. Happy quizzing! 🎉## Additional Tips and Best
Practices

To maximize your experience with the Mini Quiz App and ensure smooth
operation, consider the following tips and best practices:

### Enhancing User Experience

```
● Clear Instructions: Always read the instructions carefully before
starting the quiz to understand how to select answers and submit
your responses.
```
```
● Take Your Time: There is no time limit, so take your time to think
about each question and learn from the feedback.
```

```
● Retake the Quiz: Feel free to retake the quiz multiple times to
improve your score and reinforce your knowledge.
```
### Customizing the Quiz

```
● Adding Multimedia: Although the current version focuses on text-
based questions, you can enhance the quiz by adding images or
audio clips related to Indonesian culture to make it more engaging.
```
```
● Styling the Interface: Streamlit allows customization of the UI
with themes and CSS-like styling. Experiment with colors, fonts,
and layouts to create a unique look.
```
```
● Localization: The quiz is currently in Indonesian language, but
you can adapt it to other languages or dialects to reach a broader
audience.
```
### Deployment Suggestions

```
● Local Deployment: Ideal for personal use or small groups,
running the app locally is simple and requires minimal setup.
```
```
● Cloud Deployment: For wider accessibility, consider deploying
the app on cloud platforms such as Heroku, AWS, or Streamlit
Cloud. This allows users to access the quiz from anywhere.
```
```
● Containerization: Use Docker to containerize the app for
consistent deployment across different environments.
```
## Frequently Asked Questions (FAQs)

### Can I add more than two answer choices per question?

Currently, the quiz is designed with two choices: "Fakta" and "Mitos" to
keep it straightforward. However, you can modify the code to support
more options if desired, but this will require adjusting the scoring and UI
logic.

### How does the app maintain my answers during the quiz?

The app uses Streamlit’s session state to store your selections and
scores, ensuring that your progress is saved as you navigate through the
quiz.

### Is the quiz suitable for all age groups?


Yes! The quiz content is educational and appropriate for learners of all
ages interested in Indonesian culture and history.

### Can I use this app for educational purposes?

Absolutely! The app is a great tool for teachers, students, and cultural
enthusiasts to learn and test knowledge interactively.

## Contact and Support

If you encounter any issues, have suggestions for improvements, or want
to contribute to the project, please feel free to reach out. Collaboration
and feedback are highly appreciated to make this quiz app better for
everyone.

```
● GitHub Repository: [Link to repository if available]
```
```
● Email: abigivan99@gmail.com
```
```
● Community Forum: Join discussions and share your experiences
with other users.
```
## Acknowledgments

Special thanks to the Indonesian cultural experts and educators who
inspired the content of this quiz. Their dedication to preserving and
sharing Indonesia’s rich heritage makes projects like this possible.

## License

This project is open-source and available under the MIT License. Feel
free to use, modify, and distribute the code with proper attribution.

Thank you for your interest in the Mini Quiz App: Indonesian Facts and
Myths. We hope it brings you joy, knowledge, and a deeper appreciation
for Indonesia’s vibrant culture and history. Selamat belajar dan semoga
sukses! 🎉## Detailed Explanation of the Application Structure

Understanding the internal structure of the Mini Quiz App can help you
customize and extend it effectively. Below is a breakdown of the key
components and how they interact within the Streamlit framework.


### 1. Questions Dictionary

At the heart of the app lies a Python dictionary named questions. This
dictionary organizes all quiz content in a structured manner. Each key is
a string representing a quiz question, and its value is another dictionary
containing:

```
● choices : A list of possible answers, typically ["Fakta", "Mitos"].
```
```
● correct : The correct answer string.
```
```
● correct_msg : A message displayed when the user selects the
correct answer, providing additional context or explanation.
```
```
● incorrect_msg : A message shown when the user selects an
incorrect answer, clarifying the misconception.
```
This design allows for easy addition, removal, or modification of
questions without altering the core logic of the app.

### 2. User Interface Components

The app leverages Streamlit’s interactive widgets to create a seamless
user experience:

```
● Radio Buttons : For each question, radio buttons allow users to
select one answer from the provided choices. Each radio button
group is assigned a unique key to maintain state across
interactions.
```
```
● Buttons : A "Lihat Hasil" (View Results) button triggers the
evaluation of answers and displays the results.
```
```
● Text and Headers : Clear headings and descriptive text guide
users through the quiz process.
```
Streamlit’s session state is used extensively to store user selections and
scores, ensuring that data persists as users interact with the app.

### 3. Scoring and Feedback Logic

When the user submits their answers, the app compares each selected
answer against the correct one stored in the questions dictionary. The
scoring logic is straightforward:

```
● Increment the score by one for each correct answer.
```
```
● No penalty for incorrect answers.
```
After scoring, the app displays:

```
● The total score.
```

```
● Detailed feedback for each question, highlighting correct and
incorrect responses with appropriate messages.
```
```
● A profession suggestion based on the score.
```
This immediate feedback loop enhances learning by reinforcing correct
knowledge and correcting misunderstandings.

### 4. Profession Suggestion Mechanism

The profession suggestion is a creative feature that maps the user’s quiz
performance to a hypothetical role or title. This mapping is based on
score thresholds and is designed to motivate users by associating their
knowledge level with culturally relevant professions.

The logic is simple but effective:

```
● Perfect scores receive the highest accolade.
```
```
● High scores suggest research-oriented roles.
```
```
● Moderate scores indicate enthusiasm and interest.
```
```
● Lower scores encourage continued learning.
```
This gamification element adds personality and engagement to the quiz
experience.

## Troubleshooting and Common Issues

While the Mini Quiz App is designed to be robust and user-friendly, you
may encounter some common issues during installation or usage. Here
are some troubleshooting tips:

### Installation Problems

```
● Streamlit Not Found : Ensure that Streamlit is installed in the
active Python environment. Use pip show streamlit to verify
installation.
```
```
● Python Version Issues : The app requires Python 3.7 or higher.
Check your Python version with python --version.
```
```
● Virtual Environment Activation : If using a virtual environment,
make sure it is activated before installing dependencies or running
the app.
```
### Running the App


```
● Port Conflicts : If Streamlit fails to start due to port conflicts,
specify a different port using:
```
streamlit run fun_project_1.py --server.port 8502

```
● Browser Not Opening : If the app does not open automatically,
copy the local URL displayed in the terminal and paste it into your
browser manually.
```
### Quiz Functionality

```
● Answers Not Saving : Ensure that your browser allows cookies
and local storage, as Streamlit uses these for session state.
```
```
● UI Not Updating : Refresh the browser or restart the Streamlit
server if the interface becomes unresponsive.
```
## Advanced Customization Ideas

For developers and enthusiasts looking to enhance the Mini Quiz App
beyond its current capabilities, here are some advanced ideas:

### Adding Multimedia Content

Incorporate images, audio, or video clips related to each question to
create a richer learning environment. Streamlit supports media
embedding with simple commands like st.image() and st.audio().

### Dynamic Question Loading

Instead of hardcoding questions, load them from external files such as
JSON or CSV. This approach facilitates easier content management and
updates without modifying the source code.

### User Authentication and Progress Tracking

Integrate user login features to track individual progress over time. This
can be achieved by connecting the app to a backend database or using
third-party authentication services.

### Leaderboards and Social Sharing

Add competitive elements by displaying leaderboards or enabling users
to share their results on social media platforms, encouraging community
engagement.

### Localization and Language Support


Expand the app’s reach by supporting multiple languages. Use
translation files or libraries to switch quiz content dynamically based on
user preferences.

## Example Code Snippet for Adding a New Question

To illustrate how to add a new question, here is a sample snippet you can
insert into the questions dictionary:

"Pulau Komodo adalah habitat asli dari komodo, kadal terbesar di
dunia.": { "choices": ["Fakta", "Mitos"], "correct": "Fakta",
"correct_msg": "Benar! Pulau Komodo memang merupakan habitat asli
komodo.", "incorrect_msg": "Salah! Komodo terbesar di dunia hidup di
Pulau Komodo." }

This snippet adds a question about Komodo Island and its famous
inhabitants, complete with answer choices and feedback messages.

## Best Practices for Maintaining the Quiz Content

Maintaining a high-quality quiz requires regular updates and careful
content management. Here are some best practices:

```
● Verify Facts : Ensure all quiz statements are accurate and up-to-
date by consulting reliable sources.
```
```
● Balance Difficulty : Mix easy, moderate, and challenging
questions to cater to a wide audience.
```
```
● Cultural Sensitivity : Be respectful and considerate of cultural
nuances and avoid controversial or sensitive topics.
```
```
● User Feedback : Collect feedback from users to identify confusing
questions or errors.
```
```
● Version Control : Use Git or other version control systems to track
changes and collaborate effectively.
```
## Visual Overview of the App Interface


The app features a clean and intuitive interface with:

```
● A prominent title and description.
```
```
● Sequentially numbered questions with radio button choices.
```
```
● A submission button to view results.
```
```
● Color-coded feedback messages for correct and incorrect answers.
```
```
● Profession suggestions and a reward image to celebrate user
achievements.
```
This design ensures users remain engaged and motivated throughout the
quiz.

## Summary

The Mini Quiz App: Indonesian Facts and Myths is a thoughtfully crafted
educational tool that combines interactive technology with cultural
learning. Its modular design, clear user interface, and engaging feedback
mechanisms make it an excellent example of how simple web
applications can deliver meaningful experiences.

Whether you are a developer looking to customize the app or a user
eager to test your knowledge, this project offers a solid foundation and
plenty of opportunities for growth and enjoyment.

Happy coding and selamat belajar! 🎉



