from pocketsphinx import LiveSpeech, get_model_path
import os

def voice_command(user_speech ,maschine_command, model_lang='en-us', model_dict_lang='cmudict-en-us.dict'):
    model_path = get_model_path()
    speech = LiveSpeech(
        verbose=False,
        sampling_rate=16000,
        buffer_size=2048,
        no_search=False,
        full_utt=False,
        hmm=os.path.join(model_path, model_lang),
        lm=os.path.join(model_path, model_dict_lang)
    )
    for phrase in speech:
        print(phrase)
        if str(phrase) == user_speech:
            maschine_command
        else:
            print("Couldn't catch the phrase!")

