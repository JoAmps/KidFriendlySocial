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
* Microservices: Used to separate the functionality of the application into smaller, more modular components, improving scalability and maintainability.
* Frontend development : HTML and CSS for the frontend
* NLP models: Distil-Roberta for bad language detection and GPT-3 for generating recommendations
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

# Data
The data for this project was obtained from two dictinct sources, firstly from available datasets on the internet, and from data extracted from the twitter api. The data available on the internet was cleaned and put into a format that is usable, and it was already labelled, whiles i used doccana, an opne source data labelling platform to label all the data extracted from the twitter api.

## Model building and Evaluation
### Predictive Model
The distil Roberta model which has been pretrained on a huge corpus of tweets(model name: vinai/bertweet-base) was used as the base model of choice for training, because the model already understands how tweets are constructed so it can easily generalize to our tweets, and also since its a distil roberta model, its a smaller model that still has excellent accuracy, and most importantly, its smaller in size, so it trains faster and the inference speed(latency speed) is smaller. 4 metrics were used ( accuracy, recall, precision and f1), but the most important metric here is precision, as the key is to minimize false positives(the situation where the tweet contains bad language but the model predicts it to contain good language). Its okay to allow flag some good language as negative, but its not good to allow bad language to get out there, so reducing this situation(higher precision) is the most important here. Below are the metrics obtained:

#### accuracy: 0.949936717761215 
#### precision: 0.9477199286616215 
#### recall: 0.9464880338247377 
#### f1: 0.9470952154920613

The performance seems good, with the precision being almost 95%, which suggests the model does well in catching bad language tweets. To visualize all these metrics, the confusion matrix was used, the result is below here:
![confusion matrix](https://github.com/JoAmps/KidFriendlySocial/blob/main/src/images/confusion_matrix.png)
As can be seen, a lot of bad language tweets were correctly predicted with only 376 out of 5483(false positives) incorrectly predicted, also for good language tweets, only 336 were wrongly predicted as being bad language tweets. This shows the model would be robust in predicting if a tweet contains bad language or good language. They key here is to try to reduce the 376 false positives to capture more bad language tweets, as thats the one we are most interested in predicting.

### Generative Model
GPT3 was used for generating the recommendations when bad language is detected, the temperature(how random the generations should be) was set to 0.8, the max length to 256, to allow users to express themselves more, text davicni 003 which was the most advanced model at the time of building was used, and an excellent prompt written to generate the recommendations. The GPT3 was finetuned using 150 tweets of bad language-good language pairs to enable the model to understand the context a little better to generate relevant recommendations.


# Model in Production
### Deployment
The model was deployed using docker and kubernetes and hosted on digital ocean. The authentications(signup, login) was written using flask, and jwt authentication used to authenticate users to use the app and all the passwords hashed using bcrypt to protect user privacy.  The app was made available to 20 diverse users for a week, to interact with the app, in order to get feedback on how to improve the app, and also to use their feedback to score the performance of the model and improve the model.

### WebApp Demo
Below is a demo of how the app works. PS: i had to take the app down, since it costs money to host the app on digital ocean(the docker containers, the kubernetes clusters and the mysql database).
Demo of model predicting good language:
![good language](https://github.com/JoAmps/KidFriendlySocial/blob/main/src/images/good_language_demo.gif)
Demo of model predicting bad language:
![bad language](https://github.com/JoAmps/KidFriendlySocial/blob/main/src/images/Bad_language_demo.gif)
As can be seen in the demos, the good language prediction is straight forward, the focus is on detecting the bad language, the model correctly detects that the tweet contains bad language that is not useful for kids, and generates appropriates recommendations for them to use to improve their tweets, so in the demo, the actual tweet was : 
* "piss off, you f**king b***ch, get the hell of here", 
#### and the generated recommendations were : 
* "Go away, you awful person, get out of here"
* "Go away, you meanie, scram!"
* "Beat it, you nasty individual, leave now!"
#### As can be seen the recommendations contain the same meaning and context as the original tweet, but it is a more kidfriendly version and contains no bad language, which is what we seek to accomplish.


### Monitoring


# Conclusion


# Future Work

#### Browser Extension
One potential avenue for future development is to incorporate KidFriendlySocial as a browser extension. This would allow users to easily flag inappropriate language and receive recommendations for kid-friendly alternatives while browsing Twitter or other social media platforms. By integrating KidFriendlySocial directly into the user's browser, we can provide a more seamless and user-friendly experience.

#### Integration with Twitter
Another possible direction for future work is to integrate KidFriendlySocial directly into Twitter. This could take the form of a built-in language filter, which would automatically flag tweets containing inappropriate language and offer users suggestions for rephrasing their tweets. By partnering with Twitter, we can potentially reach a much larger audience and make a greater impact in promoting online safety for kids.

#### Refinement of Data and Machine Learning Models 
As with any machine learning model, there is always room for improvement. In future iterations of KidFriendlySocial, we would gather a lot of more diverse data that captures a lot of bad language and even in other languages in order to detect bad language no matter how its put out. One way is to keep rolling out the app to differnet and more diverse users and capturing their feedback and using it to add to training data.
We may also explore different models or fine-tune our existing models to improve their accuracy and reliability. This could involve experimenting with different transformer models. Also, reducing the inference and latency speed of the predictions by employing techniques such as quantization and weight pruning to deliver quick results to users

#### Integration with Other Social Media Platforms
Finally, we may consider integrating KidFriendlySocial with other social media platforms beyond Twitter. This could include popular platforms such as Facebook, Instagram, or TikTok, allowing us to expand our reach and provide even more comprehensive language filtering and recommendation services.
#### and many more that cannot be said here(for obvious reasons)
#### These are just a few examples of the potential future directions for KidFriendlySocial. By continuing to develop and improve this tool, we can work towards a safer and more positive online environment for kids and young people. 

# Conclusion
KidFriendlySocial is a web application that aims to make social media safer and more child-friendly. By using machine learning models(NLP), web technologies, container technologies and cloud hosting, we were able to create an application that can detect and flag bad languagest and provide recommendations to improve the language used in social media posts.

In the future, we plan to expand KidFriendlySocial by incorporating it as a browser extension and integrating it into popular social media platforms. We also plan to enhance the application by reducing latency speed and inference speed, obtaining and improving the dataset and adding a few more very useful features.

We hope that KidFriendlySocial can help parents and guardians feel more at ease with their children's social media usage and contribute to a safer and more positive online community.
