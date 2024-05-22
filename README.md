# forFunBot

## Description

forFunBot is a versatile Discord bot created in 2021. It offers a variety of features, from fun games to practical tools, enhancing your Discord experience. Whether you're looking to play a guessing game, check the weather, or get the latest stock prices, forFunBot has you covered. It is now hopefully up and running on fly.io server.

## Features

- **1A2B**: classic guessing game where you guess four digits randomly generated.
- **Weather**: Get the current weather in Taiwan.
- **xkcd**: View the latest comics from the xkcd website.
- **Yahoo**: Check out stock prices using the Yahoo API.
- **Todo List**: Manage your to-do list with recording and updating capabilities.
- **Picture**: Upload pictures directly to Discord.
- **Currency**: See the latest currency exchange rates.
- **Covid**: Access the latest Covid-19 statistics in Taiwan.
- **Cup**: Simulate the classic three cups problem.

## Installation

1. Clone the repository:
    ```bash
    git clone git@github.com:DiegoWu/forFunBot.git
    ```
2. Navigate to the project directory:
    ```bash
    cd forFunBot
    ```
3. Install the necessary dependencies:
    ```bash
    npm install
    ```

## Usage

1. Configure your Discord bot token:
    - Create a `.env` file in the root directory.
    - Add your Discord bot token to the `.env` file:
        ```
        DISCORD_TOKEN=your_token_here
        ```

2. Start the bot:
    ```bash
    cd src
    python3 main.py
    ```

## Commands

- **help**: `$help`
    - * always use help before using a commmand
    - Example: `$help guess`
- **1A2B**: `$guess`
    - Example: `$guess`
- **Weather**: `$weather`
    - Example: `$weather`
- **xkcd**: `$xkcd`
    - Example: `$xkcd`
- **Yahoo**: `$stonk <stock_symbol>`
    - Example: `$yahoo AAPL`
- **Todo List**: `$todo <action> <item>`
    - Example: `$todo add Buy milk`
- **Picture**: `$picture <upload>`
    - Example: `$picture upload path/to/picture.jpg`
- **Currency**: `$currency <currency_code>`
    - Example: `$currency USD`
- **Covid**: `$covid`
    - Example: `$covid`
- **Cup**: `$cup`
    - Example: `$cup`

## Contributing

We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) for more details.


## Contact

For any questions or feedback, please reach out to me at 930404d@gmail.com.
