# **Desafio de Projeto: Chatbot de Assistência Técnica**

Objetivo: Desenvolver um chatbot de assistência técnica utilizando modelos de linguagem. O chatbot deve ser capaz de compreender perguntas relacionadas a um determinado domínio técnico (por exemplo, programação, tecnologia da informação, etc.) e fornecer respostas relevantes.

Etapas sugeridas:

1. **Definição do Domínio:**
     \- Escolha um domínio específico para o chatbot (por exemplo, suporte técnico para programadores).
     \- Identifique os principais tópicos e perguntas que o chatbot deve ser capaz de lidar.
2. **Seleção do Modelo de Linguagem:**
     \- Escolha um modelo de linguagem pré-treinado que seja adequado para a tarefa. Pode ser GPT-3, GPT-4, BERT, ou outro modelo relevante.
3. **Desenvolvimento de Funcionalidades:**
     \- Implemente funcionalidades que permitam ao chatbot compreender e responder a perguntas relacionadas ao domínio escolhido.
4. **Testes de Software:**
     \- Desenvolva casos de teste para garantir a robustez e confiabilidade do chatbot.
     \- Realize testes abrangentes, considerando cenários diversos e potenciais situações de erro.
5. **Avaliação da Performance:**
     \- Teste o chatbot com uma variedade de perguntas e avalie sua capacidade de compreensão e resposta.
     \- Considere métricas como precisão, recall e F1-score.
6. **Documentação:**
     \- Prepare documentação clara que explique como o chatbot foi desenvolvido, como ele pode ser utilizado e quais são suas limitações.

Este desafio permitirá avaliar várias habilidades, incluindo compreensão de modelos de linguagem, desenvolvimento de funcionalidades, habilidades de teste de software e documentação. A implementação de uma interface não é obrigatória, mas pode ser considerada para melhorar a experiência do usuário.



#  Sobre o python-documentation-assistant

Foi selecionado o domínio do assistente como sendo os Pacotes Python, suportado pelo modelo de linguagem da Google Gemini. Como funcionalidades, o assistente consegue ler a documentação oficial da Python.org por meio da biblioteca Python BeautifulSoup e assistir o usuário com quaisquer dúvidas que tanjam o escopo da documentação. Para os testes, veja alguns a seguir:

![image-20240224195421479](assets/image-20240224195421479.png)

![image-20240224195506611](assets/image-20240224195506611.png)

![image-20240224195610867](assets/image-20240224195610867.png)

![image-20240224200708511](assets/image-20240224200708511.png)

![image-20240224200730412](assets/image-20240224200730412.png)

![image-20240224200749156](assets/image-20240224200749156.png)

Devido à sua limitação de escopo, o sistema somente responde, satisfatoriamente, assuntos sobre Pacotes Python, como visto acima



# Documentação

Para instalar o projeto em um ambiente Windows, basta seguir o passo-a-passo a seguir em seu ambiente de desenvolvimento:

- git clone https://github.com/Ninniet5670/python-documentation-assistant.git
- python -m venv venv
- ./venv/Scripts/activate.ps1
- pip install -r requirements.txt
- streamlit run main.py

Ou acesse o link a seguir para seu uso online: https://python-documentation-assistant.streamlit.app

