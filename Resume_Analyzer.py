from ollama import chat
import os
from pypdf import PdfReader

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

    def save_report(self, filename="Report.txt", report=""):
        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(report)
        except Exception as e:
            print(f"An error occurred while saving the report: {e}")

    def load_prompt(self,filename):
        prompt = """"""
        extracted_text = self.read_resume(filename)
        context = input("Enter the context for resume analysis : ")
        task = input("Enter the task for resume analysis : ")
        output_format = input("Enter the output format for resume analysis : ")
        example_output = """1. Overall assessment
                - Evaluate the candidate's technical background and relevance to the target role.
        
                2. Strengths
               - Identify demonstrated technical strengths.
        
                3. Weaknesses
                - Identify areas where the candidate may lack experience or skills relevant to the target role.
        
                4. Missing skills
                - Identify any skills or experiences that are missing from the resume that would be beneficial for the target role.
        
                5. Recommended improvements
                - Provide actionable suggestions for improving the resume to better align with the target role.
            """
        constraint = """- Do not invent experience that isn't present in the resume.
            - Only use information explicitly stated in the resume text.
            - If something is unclear, say it is unclear instead of guessing.
            - Keep the analysis concise and practical.
            """
        prompt += "context :\n" + context + "\n"
        prompt += "task :\n" + task + "\n"
        prompt += "constraint :\n" + constraint + "\n"
        prompt += "output_format :\n" + output_format + "\n"
        prompt += "example_output :\n" + example_output + "\n"
        prompt += "Resume Text :\n" + extracted_text
        return self.analyze_resume(prompt)
        
    
    def obtain_file_path(self, filename):
        try:
            pdf_path = os.path.abspath(filename)
            if not os.path.exists(pdf_path):
                raise FileNotFoundError(f"The file '{filename}' does not exist.\n Make sure to provide the correct path or place the file in the same directory as this script.")
            return pdf_path
        except FileNotFoundError as e:
            print(e)
            return None

    def read_resume(self, filename):
        try:
            pdf_path = self.obtain_file_path(filename)
            if pdf_path is None:
                return None
            reader = PdfReader(pdf_path)
            full_text = """"""
            
            for idx , page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    page_formatted = f"\n\n--- Page {idx + 1} ---\n\n{page_text}\n\n"
                    full_text += page_formatted
                else:
                    print(f"Warning: No text found on page {idx + 1}.")
            return full_text
        except Exception as e:
            print(f"An error occurred while reading the resume: {e}")
            return None
def main():
    ResumeAnalyzerInstance = ResumeAnalyzer()
    while True:
        # prompt = """"""
        try:
            filename = input("Enter the filename of the resume : ")
            if filename.strip() == "":
                print("Filename cannot be empty. Please enter a valid filename.")
                continue
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
            report = ResumeAnalyzerInstance.load_prompt(filename)
            if report:
                ResumeAnalyzerInstance.save_report(report=report)
                print("Report saved successfully.")
            else:
                print("No report generated.")


main()
