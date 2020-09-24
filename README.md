# The DGENs Bot Command List and Description

The bot has some basic functions, mostly for entertainment.

The bot was made using the `discord-py`, `csv`, `asyncio`, `random`, and `time` Python libraries.

To use, replace the following:
- `<TOKEN>` with your bot's token.
- `<PREFIX>` with your preferred prefix.
- `<PATH_TO_DIR>` with where your guild.csv file is.

The bot has some features like:
- Guild-specific states for commands like `switch`.
- An actually helpful remindme command that pings the user after X-hours.

## Commands and Features Available

| Command/Feature | Arguments                                   | Description                                   |
| --------------- | ------------------------------------------- | --------------------------------------------- |
|remindme         | \<Hours> \<Text>                            | Reminds the user with a ping after X hours.   |
|switch           | on \| off                                   | Switches `Mama mo mode` on or off.            |
|print            | \<text>                                     | Prints text into an embed title.              |
|ha               | *on mention of "ha"*                        | Prints "hatdog" upon mention of "ha".         |
|impostor         | *on mention of "impostor"*                  | Prints if the user mentioned is an impostor.  |


## To Do

- [x] Remove the need for "" for parsing arguments
- [x] Improved remindme syntax
- [ ] Convert all input to lowercase for parsing
- [x] Add `help` command.
