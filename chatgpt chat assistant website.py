import openai
#pip install openai if it doesn't work use pip install openai==0.28
import gradio
#pip install gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a chatbot which is made by shreyash and yaksh"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Personalised chatbot")

demo.launch(share=True)
#code is not for commertial use