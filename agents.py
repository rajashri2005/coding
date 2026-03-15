import os
from crewai import Agent, LLM

# Initialize Gemini LLM using LiteLLM syntax
gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

# Researcher
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments and comprehensive information about the provided topic',
    backstory='You are an expert researcher with years of experience uncovering the latest trends and data. You leave no stone unturned and provide accurate, well-sourced information.',
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm
)

# Analyst
analyst = Agent(
    role='Data & Trend Analyst',
    goal='Analyze the findings from the researcher and extract actionable insights, patterns, and crucial implications',
    backstory='You have a sharp mind for data and patterns. You can take raw information from researchers and find the deeper meaning, structure it logically, and highlight what truly matters.',
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm
)

# Writer
writer = Agent(
    role="Senior Content Writer",
    goal="Write a compelling, engaging, and highly readable article or report based on the analyst's insights",
    backstory="You are a skilled storyteller and writer. You know how to captivate an audience, making complex topics accessible and interesting without losing factual accuracy.",
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm
)

# Editor
editor = Agent(
    role='Managing Editor',
    goal='Review and refine the drafted content to ensure high quality, grammatical accuracy, perfect flow, and correct formatting.',
    backstory='You have an eagle eye for detail and a deep understanding of good writing. You rigorously check facts, improve phrasing, and ensure every piece meets the highest editorial standards.',
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm
)

# Manager
manager = Agent(
    role='Project Manager',
    goal='Oversee the entire process, ensure the final output is cohesive, meets the original objective, and assemble the final deliverable.',
    backstory='You are an experienced manager who knows how to coordinate a team of experts (researcher, analyst, writer, editor) to deliver a top-notch final product smoothly and efficiently.',
    verbose=True,
    allow_delegation=True,
    llm=gemini_llm
)