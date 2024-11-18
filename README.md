## `aire`

Tired of wrestling with regex every once in a while? `aire` is an AI-powered `re` module.

It exposes one primitive `compile` which is equivalent to `re.compile` but you describe what the regex should be in 
natural language so you don't have to remember and relearn the rules. 

### 🚀 Quick Example

```
import aire

p = aire.compile("number indicating line item followed by a dot, space, and then the name of the section. Example is: 1. Introduction")

print(p.search("2. Related Materials"))
# <re.Match object; span=(0, 20), match='2. Related Materials'>
```

### 🛠️ Installation

Install from PyPI:

```
pip install aire
```

For local development, it's recommended to use [`poetry`](https://python-poetry.org/docs/):

```
poetry install 
poetry shell 
```

### 🤖 Which AI?

Currently it only works with OpenAI. Add your API_KEY as environment variable `export OPENAI_API_KEY=...` and `aire` will configure the client. 
