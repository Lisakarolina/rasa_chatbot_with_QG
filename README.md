## Question-Answering Chatbot
This is a Rasa chatbot that is supposed to answer questions for two different topics. It has a simple design that mainly accepts user questions to give an answer in a single-turn interaction. The course of conversation consists of two parts: the question-asking part and the evaluation part. The evaluation part is there to get a feedback of potential test users. 

### General Information
The file transfer.py brings to bring the question-answer pairs that were produced with automated question generation in yaml-Format and inserts them in the corresponding Rasa file, the questions in the nlu.yml file and the answers in the domain.yml file. 
There are two actions implemented: ActionSubmit makes sure the user feedback is stored into the database at the end of the feedback section. SaveQA stores every question that has been classified by NLU as retrieval intent FAQ. 

### Data for Retrieval Intent
The data for the retrieval intent FAQ were gathered wwith automated question generation, applied to a wikipedia article and a text for gardening advice. The question-answer-pairs that came out of the question generation were cleaned so that pairs not suitable for the purpose were sorted out. The remaining pairs were transferred to the Rasa files (via transfer.py). They were supplemented by additional question examples to have more training data for the response selector.

### Status
This chatbot is experimental. It is about finding out whether automated question generation could go well together with the retrieval approach that is built into the Rasa architecture.
Since many of the automatically generated questions were very specific so that finding enough training data (that is, alternative verbalizations for the questions) were not easy, which affected the accuracy of the response selector noticeably.  
