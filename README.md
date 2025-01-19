<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a id="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url] [![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url] [![Issues][issues-shield]][issues-url] [![Unlicense License][license-shield]][license-url] [![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<!-- <br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    &middot;
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div> -->

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents**

- [About The Project](#about-the-project)
- [Roadmap](#roadmap)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Quickstart](#quickstart)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

<!-- ABOUT THE PROJECT -->

## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This project explores the concept of digital mimicry—an audacious experiment to clone and automate the essence of online presence. The goal is to dissect, reconstruct, and fully automate how individuals interact on social platforms, bringing to light the fascinating nuances of digital personas. It’s not just a technical proof-of-concept; it’s a playful manifesto for the age of algorithms, where authenticity and automation often collide.

At its core, this project is about:

- Understanding Online Identity: By analyzing how people communicate, post, and interact, this project aims to simulate their unique digital behaviors, creating lifelike yet automated “clones.”
- Automating Social Interaction: From casual chats to posting updates, the system strives to emulate human-like engagement across platforms, blurring the line between human presence and machine-driven conversation.
- Exploring the Ethical Edges: As both a prank and a thought-provoking experiment, this project probes the implications of impersonation and automation, encouraging reflection on trust, identity, and authenticity in the digital age.

This repository is not just a tool—it’s a creative statement about the potential and perils of technological mimicry. Whether used to entertain friends, explore the limits of AI, or spark debates about the future of online interaction, the project is a testament to the increasingly blurred boundaries of human and machine in the social media sphere.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

## Roadmap

This project offers the following functionalities:

- [x] **Integrated Discord Direct Message Auto-Response**
  - Automates responses to incoming direct messages on Discord.
- [x] **Conversation Agent**
  - Powered by GPT-4o Leverages OpenAI’s GPT-4o model (by default) or integrates with XAI Grok for lifelike and engaging conversations.
- [x] **Human Conversation Framework**
  - Implements a modular framework capturing key elements of human dialogue (e.g., tone, context, intent) for detailed and dynamic prompting.
- [ ] **Twitter Integration**
  - Extends the project to Twitter, enabling automated posting and interaction.
- [ ] **Discord Voice Call Automation**
  - Impersonate human voice call through Discord client.

These features make the project a robust tool for experimenting with automated online interactions, from casual conversations to advanced social networking tasks.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This section provides instructions for setting up and running the project locally. Follow the steps below to get started.

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.11+
- Poetry for dependency management: Install Poetry
- Docker for containerization: Install Docker

### Installation

1. Clone the Repository

   ```sh
   git clone https://github.com/neo-lky/impersonation.git
   cd impersonation
   ```

2. Install Dependencies

   Use Poetry to install all required dependencies:

   ```sh
   poetry install
   ```

3. Set Up Environment Variables

   Copy the sample `.env.sample` file and configure it with your API keys:

   ```sh
   cp .env.sample .env
   ```

4. Configure the Discord Token

   Obtain a Discord token for user login by following the instructions at [DiscordPy Self Authenticating][discord.py-self-authenticatin-url].

   Important: Be aware that using self-bots violates Discord’s Terms of Service.

5. Run the Application

   The entry point of the application is main.py. You can run it with:

   ```sh
   poetry run python main.py
   ```

6. Optional: Run with Docker

   Build and run the Docker container:

   ```sh
   docker build -t impersonation .
   docker run --env-file .env impersonation
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Quickstart

```py
from src.agent import ConversationAgent
from src.discord_client import DiscordClient

agent = ConversationAgent("agent-name", "openai-api-key")
client = DiscordClient(agent, "discord-token")
client.start_client()
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- ### Top contributors:

<a href="https://github.com/othneildrew/Best-README-Template/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=othneildrew/Best-README-Template" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Neo Lee - [@neo_lky](https://twitter.com/neo_lky) - neo.lky852@gmail.com

Project Link: [https://github.com/neo-lky/impersonation](https://github.com/neo-lky/impersonation)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [discord.py-self](https://github.com/dolfies/discord.py-self)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/neo-lky/impersonation/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/neo-lky/impersonation/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/neo-lky/impersonation/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/neo-lky/impersonation/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/neo-lky/impersonation/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/neo-lee-71b4a1222/
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[discord.py-self-authenticatin-url]: https://discordpy-self.readthedocs.io/en/latest/authenticating.html
