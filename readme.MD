# Project Name
### KidFriendlySocial: Making social media safe amd fun for kids

# Project Intro/Objective
With the rise of social media use among younger generations, it is important to ensure that the content they are exposed to is appropriate and free from harmful language.

KidFriendlySocial is a web application designed to promote safe online social interactions for children. With the increasing use of social media by children, it is essential to provide a platform that can filter out inappropriate language in their tweets, thereby promoting a healthy online environment.

KidFriendlySocial addresses this need by utilizing a predictive model and a generative model built using machine learning techniques to identify tweets that contain bad language content. The app flags these tweets, alerting the user of the potentially harmful content, and then offers recommendations on how to rephrase their tweets that are more kid-friendly or appropriate for children. This feature helps children become more aware of what is acceptable and unacceptable online behavior, making them better digital citizens.

Moreover, the recommendations aspect is particularly useful, as it helps children learn how to express themselves appropriately while still being creative with their language. This feature will help build their writing skills and promote a positive online environment for children.


# Technologies used

* Backend development : Python for building the whole backend application
* Frontend development : HTML and CSS for the frontend
* Machine learning models: Distil-Roberta for bad language detection and GPT-3 for generating recommendations
* Deep learning : Pytorch framework for building the NLP deep learning model
* Web framework: Flask for building the web application
* APIs : Twitter api to obtain real time data 
* Containerization: Docker for packaging the application and dependencies
* Container orchestration: Kubernetes for deploying and managing containers
* Cloud hosting: Digital Ocean for hosting the application in the cloud
* CI/CD : Github actions for continous integration and continous delivery
* Database: MYSQL as the database
* Version Control: Git for code version control and DVC for data and model version control
* Testing: Pytest for unit and integration testing
* Monitoring: Prometheus for monitoring metrics and Grafana for visualizing them

# Project Description(Technical)
The model was built using the state-of-the-art natural language processing algorithm, DistilRoberta, to detect and classify bad language content. The app also leverages OpenAI's GPT-3 to generate recommendations for users to improve their tweets when bad language is detected.

The application was built using Flask, a lightweight Python web framework, and containerized using Docker to ensure that it can be deployed easily on any infrastructure. The app is hosted on DigitalOcean Kubernetes, a highly scalable and efficient platform that can handle a large volume of traffic. The application is also monitored using Prometheus and Grafana to ensure optimal performance, and all data is stored and managed in a MYSQL database also hosted on digital ocean

KidFriendlySocial also incorporates several MLOps best practices, including version control of models and data, continuous integration and continuous deployment (CI/CD), and automated testing. The project follows the agile methodology, allowing for continuous feedback and improvement.

Overall, KidFriendlySocial provides a valuable service to users who want to ensure that their tweets are appropriate for children, by leveraging cutting-edge machine learning algorithms and best practices in software engineering, the application is highly scalable, efficient, and reliable.

# Results
## Analytics
Firstly, wanted to see the most common unique words that appeared in tweets that contain bad language:
