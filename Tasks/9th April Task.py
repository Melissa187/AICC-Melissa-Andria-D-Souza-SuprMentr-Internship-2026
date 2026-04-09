#Task:
#convert the project into:
#hat based MAS, add roles: reseacher, writer, reviewer.
class Researcher:
    """Replaces the data collection part of ExecutorAgent"""
    def handle_message(self, task):
        print(f"🔍 [Researcher]: Finding data for: '{task}'...")
        # Logic adapted from Executor's 'collect data' 
        return f"Research results for {task}: Found relevant facts and figures."

class Writer:
    """Replaces the report generation part of ExecutorAgent"""
    def handle_message(self, research_data):
        print(f"✍️ [Writer]: Writing report based on research...")
        # Logic adapted from Executor's 'generate report' 
        return f"FINAL REPORT\n---\nContext: {research_data}\nSummary: This is a detailed analysis."

class Reviewer:
    """Replaces the ValidatorAgent"""
    def handle_message(self, draft):
        print(f"🛡️ [Reviewer]: Checking draft quality...")
        # Logic adapted from Validator's validation check [cite: 2]
        if draft and len(draft) > 20:
            return "PASSED: The report is comprehensive."
        else:
            return "FAILED: The report is too short."

class ChatMAS:
    """The Controller that manages the conversation flow"""
    def __init__(self):
        self.researcher = Researcher()
        self.writer = Writer()
        self.reviewer = Reviewer()

    def run_chat(self, initial_task):
        print(f"🚀 SYSTEM STARTING: {initial_task}")
        print("-" * 30)

        # 1. Researcher takes the initial task
        research_output = self.researcher.handle_message(initial_task)
        print(f"Message from Researcher: {research_output}\n")

        # 2. Writer takes the researcher's output
        draft_output = self.writer.handle_message(research_output)
        print(f"Message from Writer:\n{draft_output}\n")

        # 3. Reviewer takes the writer's output
        final_verdict = self.reviewer.handle_message(draft_output)
        print(f"Message from Reviewer: {final_verdict}")
        
        print("-" * 30)
        print("SYSTEM COMPLETE.")

if __name__ == "__main__":
    # Example usage from your main.py logic 
    mas = ChatMAS()
    mas.run_chat("Global Warming Trends 2024")