# AudioWiz-v.1
AudioWiz is a python library that uses popular text-to-speech, voice and audio libraries to let developers work with it in a easy way. You are viewing the v.1 repository of it.
## Installation:
Command: `pip install audiowiz`

Alternatively if that doesn't work for you, you can go ahead and download the files you need or download the whole repository.
After that you can use the requirements.txt to download the necessary packages. Just copy the pip line and paste it into your terminal. This will download all the necessary packages!

Note the there is one branch for each version, so be sure to download it from the version branch you actually need.

> I have only tested it on windows, since it is the only computer I have. But I would appreciate any Linux, MacOS or Unix user giving me feedback, if it works fine on your OS!
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


voice_command("opengithub", open_github()) 
'''
Remember to type the user command together, or else the function will be outputed as soon as the user says the first word!
'''
```
#
## Licence:
It is a standard MIT License(https://github.com/PrathamGhaywat/AudioWiz-v.1/blob/main/LICENSE)

*For more information, contact me through my email Pratham.Ghaywat@outlook.com*

#
## Documentation
You can view the documentation here:
https://github.com/PrathamGhaywat/AudioWiz-v.1/blob/main/Documentation.md

I am planning on creating a website that will display the documentation, but that is for later!
#
## Roadmap
I am currently planning on what are the next steps of the project, but here is high level overview of functions that I want to implement:
- `record(channel, output_path)` somehow it doesn't work on my computer so I want to insure it is working, before I publish it!
- `voice_recognize(sample_voice)` This will recognize the voice and provide if the voices match or not
- `convert_stt(channel, output_path)` This will convert speech to text(stt) and output it in a .txt file.
- There are more functions, but I put the most important ones I want to create.

Well that's it!
