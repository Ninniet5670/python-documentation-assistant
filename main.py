import os
import time
from dotenv import load_dotenv

import requests
from bs4 import BeautifulSoup
import streamlit as st
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

SITE_URL = 'https://packaging.python.org/en/latest/tutorials/packaging-projects/#choosing-build-backend'
response = requests.get(SITE_URL)
soup = BeautifulSoup(response.content, 'html.parser')

st.title('Guia de Usário para Pacotes Python no que tange o guia no link a seguir:')
st.text('https://packaging.python.org/en/latest/tutorials/packaging-projects/#choosing-build-backend')
question = st.text_input("O que deseja saber?", "Do que se trata essa documentação?")

if st.button("Enviar"):        
    with st.spinner('Carregando'):
        response = model.generate_content(f'''Você é um especialista em Python, mais especificamente sobre criação de pacotes,
                                          que sabe responder perguntas com base na documentação oficial da Python.org. 
                                          Responda à pergunta do usuário em português no contexto desta documentação a seguir: "{soup}".
                                          Qualquer outro tipo de pergunta que saia deste escopo deve ser desconsiderada, sendo explicado
                                          que não se respondem perguntas fora do escopo supracitado. 
                                          {question}''')

    st.markdown("## Sua resposta")
    st.markdown("---")
    t = st.empty()
    for i in range(len(response.text) + 1):
        t.markdown("## %s" % response.text[0:i])
        time.sleep(0.04)
