# Bot do Discord

Bot para servidor de Discord

## Gerar conta de bot no discord
<sub>Passo a passo de [freecodecamp](https://www.freecodecamp.org/portuguese/news/tutorial-de-criacao-de-bot-para-o-discord-em-python/)</sub>


1. Esteja logado na [plataforma](https://discord.com/);
2. Acesse a [página de desenvolvedores](https://discord.com/developers/applications);
3. Clique no botão de "Nova Aplicação" no canto superior direito:<br>
![img.png](new_application_img.png)
4.  Vá até a aba “Bot” e clique em “Add Bot”;
>Mantenha as configurações padrão para Public Bot (marcado) e Require OAuth2 Code Grant (desmarcado).
5. Copie o Token, ele será utilizado para a autenticação do seu bot.<br>

# Setup & Launch

1. Clone esse repositório:<br>
```terminal
git clone git@github.com:Robso-creator/discord_bot.git
```

2. `cd` para o novo repositório: <br>
```terminal
cd discord_bot
```

3. Crie um novo ambiente virtual: <br>
```terminal
python -m venv venv
```
4. Ative o novo ambiente virtual: <br>
```terminal
.\venv\Scripts\Activate
```
5. Instale as dependências: <br>
```terminal
pip install -r requirements.txt
```
6. Crie um arquivo `.env` na sua pasta na pasta `root` do projeto: <br>
```terminal
DISCORD_TOKEN=
NASA_TOKEN=DEMO_KEY
```