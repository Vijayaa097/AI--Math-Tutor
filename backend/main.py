
import sympy as sp
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline  # Hugging Face for NLP
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Load Hugging Face model for text generation
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B") 

class MathProblem(BaseModel):
    problem: str

@app.post("/solve")
def solve_math_problem(math_problem: MathProblem):
    """
    Solve a mathematical expression using SymPy and provide an explanation using an open-source NLP model.
    """
    try:
        logger.info(f"Received problem: {math_problem.problem}")
        
        # Parse and solve the math expression
        expr = sp.sympify(math_problem.problem)
        solution = sp.simplify(expr)
        
        logger.info(f"Computed solution: {solution}")
        
        # Generate explanation using Hugging Face model
        explanation = generate_explanation(math_problem.problem, solution)
        logger.info("Generated explanation from open-source NLP model")

        return {"problem": math_problem.problem, "solution": str(solution), "explanation": explanation}
    
    except Exception as e:
        logger.error(f"Error solving problem: {e}")
        return {"error": str(e), "solution": "Error", "explanation": "Error"}

def generate_explanation(problem, solution):
    """
    Generate a step-by-step explanation using Hugging Face NLP model.
    """
    prompt = (
        f"The following is a math problem and its correct solution.\n"
        f"Provide a step-by-step explanation suitable for a beginner.\n\n"
        f"Problem: {problem}\n"
        f"Solution: {solution}\n"
        f"Step-by-step explanation:"
    )

    generated_text = generator(
        prompt,
        max_length=1500,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.9,
        truncation=True,
        pad_token_id=50256
    )[0]['generated_text']
    print(generated_text)
    return clean_explanation(generated_text)
def clean_explanation(text):
    """
    Post-process generated text to remove irrelevant or extra content.
    """
    explanation = text.split("Step-by-step explanation:")[-1].strip()
    
    # Remove any unrelated text after an abrupt sentence end.
    explanation = explanation.split("\n\n")[0].strip()

    return explanation

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)