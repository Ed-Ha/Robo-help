# Robo-help
This is a Python Flask web application that allows users to chat with different virtual assistants based on their profession.
 
try me: https://robot-help.ew.r.appspot.com/

The project is hosted on a Google Cloud server to ensure that it's accessible online.       
The server is responsible for handling incoming requests from users, processing them, and returning the appropriate responses to the users.

The main functionality of the app is the chat feature, which is implemented using HTML templates and JavaScript to enable communication between the user and the virtual assistant. The app has two versions, one in English and the other in Hebrew.
The application also includes a search feature that filters categories of professions based on user input.

The chat functionality is powered by the OpenAI API.               
The virtual assistants in the app communicate with users by sending API requests to the GPT model, which generates text responses based on the user's input. This allows for a dynamic and natural conversation experience that's tailored to each user's needs.

The virtual assistants in the app provide profession-specific assistance by answering user queries and providing relevant information. Users can select a profession from a list of available options and start a conversation with the respective virtual assistant. The conversation history is saved, and the user can clear the conversation and start afresh.

As there is no database, the application only allows one session at a time, meaning that users cannot engage in simultaneous conversations with specific professional.    
