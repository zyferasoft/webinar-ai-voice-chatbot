from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain import OpenAI, LLMChain, PromptTemplate


class ChatBot:
    def __init__(self):
        # Initialize the chatbot, setting up API keys or configurations
        self.client = OpenAI()
        self.template = """Imagine you are a teacher in mathematics. 
You will test the user with short mathematics questions. 
In the first coming input do not forget to introduce yourself. 
After getting the users' answer, tell them whether it is correct or not. 
If it is not correct, give them the right answer and ask another question. 
Do not forget to ask a new question for each time. 
Do not write any answer for "Human:"

{chat_history}

Human: {user_message}
AI:"""
        self.prompt_template = PromptTemplate(input_variables=["chat_history","user_message"], template=self.template)
        self.memory = ConversationBufferMemory(memory_key="chat_history")

        self.llm_chain = LLMChain(
            llm=self.client,
            prompt=self.prompt_template,
            verbose=True,
            memory=self.memory,
        )


    def interact_with_chatgpt(self, user_input):
        # Take user input and interact with ChatGPT
        # Return the response generated by ChatGPT
        print(f"user_input: {user_input}")
        response = self.llm_chain.predict(user_message=user_input)
        return response

