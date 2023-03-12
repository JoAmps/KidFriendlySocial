# Project Name
### KidFriendlySocial: Making social media safe and fun for kids!
![logo](https://github.com/JoAmps/KidFriendlySocial/blob/main/src/images/logo.png)
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
Firstly, wanted to see the most common unique words(unigram) that appeared in tweets that contain bad language:
![common words](https://github.com/JoAmps/KidFriendlySocial/blob/main/src/images/Common%20words.png)
As an be seen there are some words that are more general such as want, human etc, these are included here because they were used in contexts of tweets that are not kid appropriate but the words themselves are appropriate but the words that are strictly for bad language can be seen in there such as fuck, stupid, niggers etc.

Also, it was ideal to visualize a word cloud of tweet that contain good language and ones that contain bad language, to see how different they are:
![word cloud](https://github.com/JoAmps/KidFriendlySocial/blob/main/src/images/Word%20cloud.png)
As can be seen above, there is a clear difference in the good and bad language tweets, which is useful for us to differentiate and build a model to try and classify tweets according to this.


## Model building and Evaluation
### Predictive Model
The distil Roberta model which has been pretrained on a huge corpus of tweets(model name: vinai/bertweet-base) was used as the base model of choice for training, because the model already understands how tweets are constructed so it can easily generalize to our tweets, and also since its a distil roberta model, its a smaller model that still has excellent accuracy, and most importantly, its smaller in size, so it trains faster and the inference speed(latency speed) is smaller. 4 metrics were used ( accuracy, recall, precision and f1), but the most important metric here is precision, as the key is to minimize false positives(the situation where the tweet contains bad language but the model predicts it to contain good language). Its okay to allow flag some good language as negative, but its not good to allow bad language to get out there, so reducing this situation(higher precision) is the most important here. Below are the metrics obtained:

#### accuracy: 0.949936717761215 
#### precision: 0.9477199286616215 
#### recall: 0.9464880338247377 
#### f1: 0.9470952154920613

The performance seems good, with the precision being almost 95%, which suggests the model does well in catching bad language tweets. To visualize all these metrics, the confusion matrix was used, the result is below here:
![confusion matrix](https://github.com/JoAmps/KidFriendlySocial/blob/main/src/images/confusion_matrix.png)
As can be seen, a lot of bad language tweets were correctly predicted with only 376 out of 5483(false positives) incorrectly predicted, also for good language tweets, only 336 were wrongly predicted as being bad language tweets. This shows the model would be robust in predicting if a tweet contains bad language or good language

### Generative Model
GPT3 was used for generating the recommendations when bad language is detected, the temperature(how random the generations should be) was set to 0.8, the max length to 256, to allow users to express themselves more, text davicni 003 which was the most advanced model at the time of building was used, and an excellent prompt written to generate the recommendations. The GPT3 was finetuned using 150 tweets of bad language-good language pairs to enable the model to understand the context a little better to generate relevant recommendations

