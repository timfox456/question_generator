# Data Science Project w/ Linc Global
## Dataset to Use -
The file product_catalog.tsv attached.
# Problem Details -
## Background:
Given a dataset such as a product catalog, we’d like to automatically generate a list of questions with answers. This knowledge can then help the customer success team to understand what questions shoppers might ask about the products during shopping and what questions can be answered by the catalog directly.
## Problems to solve:
1) Design and implement an algorithm to generate questions and answers from the dataset. Multiple questions can have the same answer. The output is a json file where each item has two attributes: questions and answer, where the questions attribute is a list of questions with the given answer. There should be no duplicate answers in the output, and the questions/answers should make common sense and be correct according to the catalog.
 *  Hint: imagine you are trying to buy a product. What kind of questions will you ask regarding the products in the catalog?
2) Design and implement an algorithm to find an answer to an input utterance. It should try to match the utterance to the questions, and return up to 3 answers if there are questions that match well with the utterance. If there is no question that matches well with the utterance, return None.
 *  Average matching time per utterance must be below 80ms on a CPU machine.
 *  You should illustrate the success of your approach by providing 10 examples of good
matching (or no matching) results.
 *  You should explain how you determine if a question is a good match with an utterance.
Please keep in mind that the input utterance can be anything and it’s quite often that there is no good answer that can be provided.

## General Rules 
- You are expected to use Python, but feel free to use any library or reference code. Apply any NLU and/or machine learning techniques you find useful. But please refer to them in your submission.
- Time duration: you are free to spend as much as time as you like. We’d like to receive your submission within 48 hours after you receive this project assignment. If you need more time, please ask for an extension.
- Evaluation criterion:
 *  Code structure, speed, matching accuracy and documentation
 *  Number of columns questions are generated from
 *  Variety of questions generated
 *  Bonus points are given to questions generated from the descriptive columns such as attribute.fittext, attribute.description, etc.
- Please submit your actual code to “join-us@letslinc.com”. Also submit a Readme about your approach(es) and how to run your program, as well as how much time you spend on this project.
- If your program does not run, it will get disqualified.
- Please do not share this question with anyone else. Thank you.
- If you can’t finish the coding but would still like to share your thoughts and general strategy, you can still submit the “Readme” file. It would be great if you can submit working source code to demonstrate your programming skills.
- We’d like you to try your best on this problem, however, if you find this problem too challenging, please move on to an alternative on the next page.

All the Best!!!
Linc Machine Learning Team
