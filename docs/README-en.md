[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
![makefile](https://img.shields.io/badge/makefile-enabled-brightgreen?logo=gmail&logoColor=blue)
[![pytest](https://img.shields.io/badge/pytest-enabled-brightgreen?logo=pytest&logoColor=#0A9EDC)](https://docs.pytest.org/en/7.4.x/)

# Discord Bot

<sub>Don't speak Portuguese? [Click here](https://github.com/Robso-creator/discord_bot/blob/main/README-en.md) to view
this page in English</sub>

This is a Discord bot project developed in Python that offers a variety of features to enhance the user experience on
Discord servers. The bot was created to be flexible, user-friendly, and expandable, allowing customization of commands
and integration with other services.

Documentation of commands is available [here](https://robso-creator.github.io/discord_bot/commands/)

# Summary

* [Creating Necessary Tokens](#creating-necessary-tokens)
    * [Generate bot account on Discord](#generate-bot-account-on-discord)
    * [Generate NASA API authentication token](#generate-nasa-api-authentication-token)
* [Setup & Launch](#setup-&-launch)

# Creating Necessary Tokens

For the bot to function properly, some tokens need to be provided. Below you can understand how to generate them.

## Generate bot account on Discord

<sub>Step by step guide
from [freecodecamp](https://www.freecodecamp.org/portuguese/news/tutorial-de-criacao-de-bot-para-o-discord-em-python/)</sub>

1. Be logged into the [platform](https://discord.com/);
2. Access the [developer page](https://discord.com/developers/applications);
3. Click on the "New Application" button in the top right corner:<br>
   ![img.png](../static/new_application_img.png)
4. Go to the "Bot" tab and click "Add Bot";

> Keep the default settings for Public Bot (checked) and Require OAuth2 Code Grant (unchecked).

5. Copy the Token, it will be used for authenticating your bot.<br>
6. While you're at it, on the same page, click "OAuth2" and select "bot"

> In this step, we're going to add the bot to your server.

7. Then choose the permissions you want to give to your bot, for the default of this repository only text message
   permissions are sufficient.
8. Click the 'copy' button above the permissions and paste it into your browser, select the server you want to add the
   bot to and then click "Authorize"

## Generate NASA API authentication token

<sub>This token is not mandatory, for testing purposes only the DEMO_KEY is sufficient.</sub>
<sub>With authentication, the hit limit on the API increases dramatically</sub>

1. The first thing to do is to request the [generation of your token](https://api.nasa.gov/) for access to the space
   agency's API;
2. After filling in the form fields with your first name, last name, and email address, your token will be sent to the
   provided email address;
3. Copy the Token, it will be used to authenticate the NASA API.

> Your token is for personal use and should not be shared.

# Setup & Launch

1. Clone this repository:<br>

```terminal
git clone git@github.com:Robso-creator/discord_bot.git
```

2. `cd` into the new repository: <br>

```terminal
cd discord_bot
```

3. Create a new virtual environment: <br>

```terminal
python -m venv venv
```

4. Activate the new virtual environment: <br>

```terminal
.\venv\Scripts\Activate
```

5. Install the dependencies: <br>

```terminal
pip install -r requirements.txt
```

6. Create a `.env` file in the root project folder: <br>

```terminal
DISCORD_TOKEN=
DISCORD_SERVER_ID=
NASA_TOKEN=DEMO_KEY
```

7. Run the .py file: <br>

```terminal
python -m main
```
