🤖 Multi-Agent AI Pipeline Chatbot
10-Point Practical Assignment | Advanced AI Integration

📌 Project Overview
This project is a sophisticated Multi-Agent System (MAS) that integrates 5 distinct AI Agents into a single, cohesive pipeline. Unlike a standard chatbot, this system uses a sequential workflow where each agent processes the output of the previous one, ensuring a high-quality, critiqued, and polished final response.

🛠️ Tech Stack
Orchestration: CrewAI (or LangChain)

Models: Google Gemini 3 Flash / OpenAI GPT-4o

Frontend: Streamlit

Language: Python 3.12+

🧬 The Agent Pipeline
The system utilizes a 5-stage pipeline to handle user queries:

Researcher: Scours information and provides raw data points.

Coder/Technical Lead: Processes technical logic or code-based solutions.

Logical Critic: Reviews the work of the previous agents for hallucinations or errors.

Creative Stylist: Refines the tone and ensures the output is engaging.

Final Manager: Conducts a final quality check and formats the output for the user.

🚀 Installation & Setup
Clone the repository:

Bash
git clone https://github.com/your-username/5_AI_Agents.git
cd 5_AI_Agents
Install dependencies:

Bash
pip install -r requirements.txt
Set up Environment Variables:
Create a .env file and add your API keys:

Code snippet
GEMINI_API_KEY=your_google_api_key_here
Run the Application:

Bash
streamlit run main.py
📸 UI Features
Unified Chat Interface: Simple, intuitive interaction with the entire AI team.

Pipeline Trace: A transparent view of what each agent contributed to the final answer.

Accountability: Logs indicating which model was used for which task.

