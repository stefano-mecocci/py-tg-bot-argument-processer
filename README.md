# ArgumentProcesser
An arguments validator and parser to use together with
[python-telegram-bot](https://github.com/pyrogram/python-telegram-bot)

# Requirements

Just copy-paste the file

# How to use

1. create a list of options (see below)
    ```
    options = [...]
    ```
2. add these lines of code
    ```
    ap = ArgumentProcesser(update.message.text, update, context)
    is_valid = ap.try_matches_execute(options)
    ```

### List of options
A non empty list of n tuples, where n are the number of possible
formats of the command
```
[ 
    (types string, filters list, handler function),
    ...
]
```

### Types string
A string of `n` types separated by spaces where `n` >= 0

Examples:
- `""`
- `"str int"`

### Filters list
A list of `n` dicts, where `n` is the number of types in types string \
If you don't want a filter for a type, in place of a dict you must use `None`

Examples:
```python
[]
[{'val': 3}, None]
[None, {'range': (0, 4)}]
```

### Filter
A filter is a dict where the key can be one of:
- `val` to match exact value
- `range` for type int, where value = `(min, max)` (min and max included)
- `regex` for types str, subcmd, user

Examples:
```python
{'val': 3} # it matches the value AFTER the parsing
{'range': (0, 5)}
{'regex': "myregex"}
```

### Handler function
A function with 3 parameters wich returns none:
```python
def fn(update, context, args):
```
where `args` is the list of arguments **after** the command

### Types
There are five possible types:
- `str`    -> a string between double quotes (e.g. "hello world")
- `int`    -> an integer
- `bool`   -> a value among these: true, false, on, off
- `user`   -> a value consisting of a telegram user (e.g. @pippo)
- `subcmd` -> a value with only lowercase letters (e.g. add)
