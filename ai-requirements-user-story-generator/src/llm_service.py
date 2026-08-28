import ollama


class OllamaService:
    """
    Service layer responsible for communicating with the
    locally running Ollama LLM.
    """

    def __init__(self, model: str = "llama3.2"):
        self.model = model

    def generate(self, prompt: str) -> str:
        """
        Send a prompt to Ollama and return the generated response.
        """

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]