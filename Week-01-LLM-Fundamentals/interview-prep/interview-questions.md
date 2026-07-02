<!-- LLMs -->
Q1. What is an LLM?

Answer: LLM stands for Large Language Model. It is a neural network trained on massive amounts of text data to understand and generate human-like language. Modern LLMs such as GPT, Gemini, Claude, and Llama are based on the Transformer architecture.

Q2. Why are they called Large Language Models?

Answer: Because:
        They are trained on huge datasets.
        They contain billions of parameters.
        They can understand and generate natural language.

Q3. Can an LLM think?

Answer: No.LLMs do not think like humans.They predict the most probable next token based on patterns learned during training.

Q4. Difference between AI, ML, Deep Learning and LLM?

Answer: 

        AI

        ↓

        Machine Learning

        ↓

        Deep Learning

        ↓

        Large Language Models

        LLMs are a subset of Deep Learning.


<!-- Prompts -->
Q5. What is a Prompt?

Answer: A prompt is the instruction or input provided to an LLM.
Example: Explain React Hooks.

Q6. Difference between System Prompt and User Prompt?

Answer: System Prompt defines the behavior of the AI.

Example: 
        You are an expert JavaScript teacher.

        User Prompt is the actual question.

        Example

        Explain closures.

Q7. Can the user override the System Prompt?

Answer: The user can try, but the model generally prioritizes the system prompt. However, prompt injection attacks can sometimes influence behavior, so applications should validate and protect prompts.


<!-- Transformers -->
Q8. What problem did Transformers solve?

Answer: Earlier models like RNNs and LSTMs processed text sequentially and struggled with long-range dependencies.
Transformers introduced self-attention, allowing every token to attend to every other relevant token in parallel.

Q9. What is Self-Attention?

Answer: elf-attention allows every token in a sentence to determine which other tokens are important for understanding its meaning.

Q10. Why are Transformers faster than RNNs?

Answer: Because Transformers process all tokens in parallel instead of one token at a time.


<!-- Tokenization -->
Q11. What is Tokenization?

Answer: Tokenization is the process of converting text into tokens before sending it to the model.

Q12. Is one token equal to one word?

Answer: No.A token can be:
        one character
        part of a word
        one word
        punctuation

Q13. Why do LLMs use tokens instead of words?

Answer: okens allow the model to efficiently represent text across multiple languages, punctuation, symbols, and rare words.


<!-- Context Window -->
Q14. What is Context Window?

Answer: The context window is the maximum number of tokens that an LLM can consider during a single request.
    It includes:

    System Prompt
    User messages
    Assistant messages
    Model response

Q15. What happens if the context window becomes full?

Answer: Older tokens are removed or truncated, causing the model to forget earlier parts of the conversation unless the application manages history.


<!-- Parameters -->
Q16. What are Parameters?

Answer: Parameters are the learned weights inside a neural network.They store the knowledge learned during training.

Q17. Does more parameters always mean a better model?

Answer: No.Performance also depends on:
    training data
    architecture
    fine-tuning
    optimization


<!-- Streaming -->
Q18. What is Streaming?

Answer: Streaming allows the model to return tokens as they are generated instead of waiting for the complete response.

Q19. Why do chatbots use Streaming?

Answer: Because it improves user experience by reducing perceived latency.users see the answer appearing immediately.

Q20. Does Streaming make the model faster?

Answer: No.The model takes almost the same amount of computation time.
        Streaming only lets the user start receiving output earlier.


<!-- API -->
Q21. What determines API Cost?

Answer: API cost is generally based on:
        Input Tokens
        Output Tokens

Q22. What are Frontier Models?

Answer: Frontier Models are the most advanced state-of-the-art language models available at a given time.
Examples:
    GPT
    Gemini
    Claude


<!-- Practical -->
Q23. Why do we send conversation history every time?

Answer: Because LLM APIs are stateless.They do not automatically remember previous conversations.

Q24. How do ChatGPT or Gemini remember previous messages?

Answer: The application stores conversation history and sends it again with each request.

Q25. What is the role of the Tokenizer?

Answer: Tokenizer converts text into tokens before inference and converts generated tokens back into text.