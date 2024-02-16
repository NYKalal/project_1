from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback

import os
import json
import pandas as pd
from dotenv import load_dotenv
import PyPDF2
import traceback


load_dotenv()

KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key = key, model = 'gpt-3.5-turbo', temperature=0.7)

# i need to read the response.json file , reading the json file is simple through file handling

with open("D:/project_1/response.json","r") as f:
    response_json = json.load(f)


# this is the template in i need to pass in PromptTemplate class
TEMPLATE1="""
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz  of {number} multiple choice questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like  RESPONSE_JSON below  and use it as a guide. \
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}

"""

#defining the prompt template class
quiz_generation_prompt = PromptTemplate(
    input_variables=["text","number", "subject","tone","response_json"],
    template = TEMPLATE1
)


# incorporating the llm-model and prompttemplate in ll-chain class 
quiz_chain = LLMChain(llm=llm, 
                    prompt=quiz_generation_prompt, 
                    output_key="quiz",
                    verbose = True)



# again making the model to check whether the quiz questions created is right or not instead of making human to check

TEMPLATE2="""
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""

# retaining the same model for evaluation
# llm = ChatOpenAI(openai_api_key = key, model = 'gpt-3.5-turbo', temperature=0.7)

#defing the PromptTemplate for evaluation
quiz_evaluation_prompt = PromptTemplate(
    input_variables=["subject","quiz"],
    template = TEMPLATE2
)

# defining the chain
review_chain = LLMChain(llm=llm, 
                        prompt=quiz_evaluation_prompt, 
                        output_key="review",
                        verbose = True)


# threading the chains using SequentialChain class
generate_evaluation_chain = SequentialChain(chains=
    [quiz_chain, review_chain], 
    input_variables=["text","number", "subject","tone","response_json"],
    output_variables=["quiz","review"],
    verbose= True 
            )


