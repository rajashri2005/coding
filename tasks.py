from crewai import Task

def create_tasks(topic, researcher, analyst, writer, editor, manager):
    t_research = Task(
        description=f'Conduct comprehensive research on the topic: "{topic}". Gather relevant facts, data, recent developments, and varied perspectives.',
        expected_output='A detailed research report summarizing the key findings, data points, and context regarding the topic.',
        agent=researcher
    )
    
    t_analyze = Task(
        description=f'Review the research report on "{topic}". Identify the most significant trends, core insights, and implications. Structure these findings logically.',
        expected_output='A structured analysis document highlighting the core insights, trends, and actionable takeaways from the research.',
        agent=analyst
    )
    
    t_write = Task(
        description=f'Draft a comprehensive, engaging, and well-structured article/report about "{topic}" based strictly on the analytical insights provided.',
        expected_output='A high-quality draft article or report that effectively communicates the findings to a general audience.',
        agent=writer
    )
    
    t_edit = Task(
        description='Review the drafted article for clarity, accuracy, engagement, and grammatical correctness. Polish the writing and ensure excellent flow.',
        expected_output='A final, highly polished version of the article ready for publication, with no errors.',
        agent=editor
    )
    
    t_manage = Task(
        description='Review the final polished article to ensure all initial requirements regarding the topic were met. Provide a final executive wrapper or summary.',
        expected_output='The final approved article along with a brief executive summary of the project.',
        agent=manager
    )
    
    return [t_research, t_analyze, t_write, t_edit, t_manage]