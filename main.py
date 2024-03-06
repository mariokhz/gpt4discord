import botgpt4 as gpt4

modelo = "gpt-4-turbo-preview"
system = "You are a helpful assistant"
dtoken = '' # Discord Bot Token
openaitoken = '' # OpenAI Api Key


gpt4.main(system, modelo,dtoken,openaitoken)
