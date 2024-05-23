# AudioWiz Documentation

Well it's not much right now, but it is what it is!
#
## 1.audiowiz
### audiowiz contains these functions:

1. `speak(text)` This will say 'text'

2. `translate(text, text_language, language_to_translate_to)` This will translate text from it's default language to the intended language and then speak it out loud. Be sure to use the short form(e.g: english -> en) or else it won't work!
3. `read_pdf_out(path_to_pdf)` This will read out the pdf.
Please make sure to remove all non-text elements(e.g: images) out of the PDF and insure it really is a PDF.
4. `save_audio(text, language, output_path, file_name)` This will save the text you put in it as a MP3.
5. `def summarize_and_read_out(text_to_summarize)` This will take a long text, summarize it and then read it out for you!(This is just a random function I made for fun 😊)
#
## voicewiz
### voicewiz contains these functions:
1. `def voice_command(user_speech ,maschine_command, model_lang, model_dict_lang)` This takes in what the user says and executes the command you provided. `model_lang` and `model_dict_lang` are modifiable, but you don't need to do that if you are giving it input in English. But if you are giving inputs in another language, you might want to refer to the `pocketsphinx` documentation

Thats actually all from the current version 0.0.1. 

Happy Coding!
