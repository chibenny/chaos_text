## Chaos Text
A rage text generator with some extra sauce.

### Cool, but why?
The missus asked for it about 5 years ago. I finally got around to it.  
I might add a mobile version at some point (We can't stop now. This is alpha country.)

The default (no checkboxes checked) makes rEgUlAr RaGe TeXt, with a 30% chance that the first letter's capitalization is inverted.  
**Extra Rage**: screws things up.  
**Chaos Mode**: makes it worse.

Enjoy.

### Installation

**Requires Python 3.9 or newer**

1. Old School:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. Don't forget to:
    ```sh
    pip install -r requirements.txt
    ```

3. Run [uvicorn](https://www.uvicorn.org/):
    ```sh
    uvicorn main:app --reload
    ```
