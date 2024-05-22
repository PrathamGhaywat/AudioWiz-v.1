# AudioWiz-v.1
AudioWiz is a python library that uses popular text-to-speech, voice and audio libraries to let developers work with it in a easy way. You are viewing the v.1 repository of it.
## Types:
AudioWiz v.1 has currently two types: 
- audiowiz
- voicewiz
### audiowiz:
- audiowiz let's you work with text-to-speech and speech libraries in an easy way.
- Example: audiowiz has a function called read_pdf_out(path_to_pdf). The function let's you put in the path to your pdf and then the function will narrate it to you

```python
from Audiowiz.audiowiz import read_out_pdf

read_pdf_out(path_to_pdf) 
#Once the code is run, your computer will start reading out the code
#Note that the pdf file can't have any non-text elements(e.g images) in it!
```
#

### voicewiz
- voicewiz let's you work with voices and voice input.
- Example: voicewiz has a function called voice_command(user_speech ,maschine_command, model_lang, model_dict_lang). This function let's you put what the user should say and what the maschine should say.

```python
from Audiowiz.voicewiz import voice_command
import webbrowser

def open_github():
          webbrowser.open("https://www.github.com")


voice_command("opengithub", open_github()) #Remember to type the user command together, or else the function will be outputed as soon as the user says the first word!
```
#
## Licence:
It is a standard MIT License()

