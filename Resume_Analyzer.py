from ollama import chat

class ResumeAnalyzer:
    def __init__(self, model_name="llama3.2"):
        self.model_name = model_name

    def analyze_resume(self, prompt):
        messages = [
            {
                "role": "user",
                "content": f"Analyze the following resume using the following prompt:\n{prompt}"
            }
        ]
        response = chat(model=self.model_name, messages=messages)
        return response["message"]["content"]

def main():
    ResumeAnalyzerInstance = ResumeAnalyzer()

    example_output = """1. Overall assessment
        evaluate the candidates overall resume according to given context and constraints in a short paragraph

        2. Strengths
        - list the strengths by analysing the resume and list it in a bulletin form

        3. Weaknesses
        - list the weaknesses by analysing the resume and list it in a bulletin form

        4. Missing skills
        -Identify skills that would strengthen the candidate for the target role.

        5. Recommended improvements
        -Give specific improvements based only on the resume.
    """
    constraint = """- Do not invent experience that isn't present in the resume.
    - Only use information explicitly stated in the resume text.
    - If something is unclear, say it is unclear instead of guessing.
    - Keep the analysis concise and practical.
    """
    while True:
        prompt = ""
        try:
            choice = input("Do you want to enter a prompt for resume analysis? (y/n): ")
            if choice.lower() == 'n':
                break
            elif choice.lower() != 'y':
                print("Invalid choice. Please enter 'y' or 'n'.")
                continue
        except KeyboardInterrupt:
            print("\nExiting the program.")
            return
        else:
            context = input("Enter the context for resume analysis : ")
            prompt += context + "\n"
            task = input("Enter the task for resume analysis : ")
            prompt += task + "\n"
            prompt += constraint + "\n"
            output_format = input("Enter the output format for resume analysis : ")
            prompt += output_format + "\n" 
            if prompt.strip() == "":
                print("Prompt cannot be empty. Please enter a valid prompt.")
                continue
            with open("sample_resume.txt", "r", encoding="utf-8") as file:
                resume_text = file.read()
                prompt += example_output + "\n" + "Resume Text:\n" + resume_text
                result = ResumeAnalyzerInstance.analyze_resume(prompt)
                with open("Report.txt", "w", encoding="utf-8") as file:
                    file.write(result)

main()
