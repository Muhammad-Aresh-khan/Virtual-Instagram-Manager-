
from langchain_core.prompts import ChatPromptTemplate , SystemMessagePromptTemplate ,HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import Runnable

import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))  # goes to insta_agent/
sys.path.insert(0, project_root)
from app.config import API_KEY, MODEL , CAPTION_PROMPT_SYSTEM
# Set up the LLM
llm = ChatGoogleGenerativeAI(
    api_key=API_KEY,
    model=MODEL

)

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(CAPTION_PROMPT_SYSTEM),
    HumanMessagePromptTemplate.from_template("Generate a short, engaging Instagram caption for the topic: {topic}. Make it creative and trendy.IMPORTANT INSTRUCTIONS:DOnt give multiple Captions just one and no extra text and you respone will driectly be posted to instagram so only single caption include hastags for reach")
])

# Output parser
parser = StrOutputParser()

# LangChain pipeline
caption_chain: Runnable = prompt | llm | parser

def generate_caption(topic: str) -> str:
    """Generates an Instagram caption based on the given topic."""
    return caption_chain.invoke({"topic": topic})