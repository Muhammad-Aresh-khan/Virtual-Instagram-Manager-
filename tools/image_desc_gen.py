
from langchain_core.prompts import ChatPromptTemplate , SystemMessagePromptTemplate ,HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import Runnable

import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))  # goes to insta_agent/
sys.path.insert(0, project_root)
from app.config import API_KEY, MODEL
# Set up the LLM
llm = ChatGoogleGenerativeAI(
    api_key=API_KEY,
    model=MODEL

)

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are here to generate the visual description for image using the provided caption "),
    HumanMessagePromptTemplate.from_template("Turn this caption into a detailed visual scene prompt: {caption}. Make it creative and trendy also include company logo in text company name Wenawa  .")
])

# Output parser
parser = StrOutputParser()

# LangChain pipeline
visual_desc_chain: Runnable = prompt | llm | parser

def generate_Visual_desc(topic: str) -> str:
    """Generates an Instagram image descriptionc based on the given caption."""
    return visual_desc_chain.invoke({"caption":topic})

