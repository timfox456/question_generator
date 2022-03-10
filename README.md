# question_generator


This repo is forked from https://github.com/AMontgomerie/question_generator


## Requirements

[Requirements](./requirments.md)


## How to run

```bash
python main.py
```



## How to run original question answerer

```bash
python run_qg.py --text_file articles/product.txt
```


## Approach

We are using the `iarfmoose/t5-base-question-generator` model from huggingface.  We will be 
using a cleanup routine to format the text and then using the model to generate questions.
