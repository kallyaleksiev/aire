## `aire`

`aire` is an ai-powered `re` module.  It uses AI to figure out what the correct regex pattern is so you don't have to remember and relearn the rules. 

It exposes one primitive `compile` which is equivalent to `re.compile` but you describe what the regex should be in 
natural language.

### Example

```
import aire

p = aire.compile("number indicating line item followed by a dot, space, and then the name of the section. Example is: 1. Introduction")

print(p.search("2. Related Materials"))
# <re.Match object; span=(0, 20), match='2. Related Materials'>
```

### Installation

It's recommended to use [`poetry`](https://python-poetry.org/docs/) for now:

```
poetry install 
poetry shell 
```
