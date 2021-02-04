# CandyKeys Notifications in Telegram

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

Background: I was tired of checking the [Zealios V2 storepage on CandyKeys](https://candykeys.com/product/zealios-switches-v2) every day for that sweet tactile feel. To save time, I coded a small script to notify me on Telegram if any Zealios V2 switch is in stock.

**Important note: This service was quickly hacked together.** It might be unstable and unreliable.

I might refactor the service to be configurable and more stable if I have enough motivation and time in the future.

### Built With

* BeautifulSoup for website parsing

* [Python Telegram Bot Library](https://github.com/python-telegram-bot/python-telegram-bot) for telegram notifications

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Working installation of Python 3.

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/tanikai/candykeys-notification.git
   ```

2. Install Python packages with pip

   ```sh
   pip install -f requirements.txt
   ```

3. Configure Telegram Bot API Key

### Usage

Run service.py file with Python 3.

## License

Distributed under the GPLv3 License. See `LICENSE` for more information.

## Contact

Kai Anter - [@tanikai29](https://twitter.com/tanikai29) - kai.anter@web.de

Project Link: [https://github.com/tanikai/candykeys-notification](https://github.com/tanikai/candykeys-notification)
