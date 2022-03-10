import csv
import re

import cleanup
from questiongenerator import QuestionGenerator
from questiongenerator import print_qa




def write_file(my_string ):
    text_file = open("file.txt", "w")
    n = text_file.write(my_string)
    text_file.close()


if __name__ == "__main__":
    qg = QuestionGenerator()
    tsv_file = open('articles/product_catalog.tsv')

    return_array = []
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    header = next(read_tsv)
    for row in read_tsv:
        my_doc = cleanup.cleanup(row)
        print(my_doc)
        qa_list = qg.generate(
           my_doc,
           num_questions=10,
           answer_style="sentences",
           use_evaluator=True
        )
        print(print_qa(qa_list, show_answers=True))
        return_array.append(print_qa(qa_list, show_answers=True))
    print(return_array)




