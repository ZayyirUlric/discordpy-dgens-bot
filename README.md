# The DGENs Bot Command List and Description

The bot has some basic functions, mostly for entertainment.

The bot was made using the `discord-py`, `csv`, `asyncio`, and `time` Python libraries.

To use, replace the following:
- \<TOKEN> with your bot's token.
- \<PREFIX> with your preferred prefix.
- \<PATH_TO_DIR> with where your python script is.

## Commands Available

1. remindme
   - tags user after X hours
     - MMremindme "\<hours>\/\<message>\"
2. switch        
   - switches "Mama mo mode" on and off. Guild specific.
     - MMswitch on|off 
3. print         
   - prints a message in an embed
     - MMprint \<message>


## Remindme Syntax

MMremindme    -> command
"0.1/mama mo" -> argument 
""            -> container of the whole argument
0.1           -> number, in hours
/             -> delimiter for splitting time from message 
mama mo       -> string to be printed after X hours

## To Do

- [ ] Remove the need for "" for parsing arguments
