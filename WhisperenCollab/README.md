# Transcripción de audio del SCEWC 

Usado whisper de openai 

Modelo usado: `large-v2`

Siguiendo el workflow de: https://ai.plainenglish.io/convert-speech-to-text-for-free-with-openai-whisper-6fae9aba1f49

## 1 - GPU

At first glance, it might look a little bit intimidating. But trust me, you won’t need more than 10 lines of code.

Next, click on the menu titled Runtime, and right here, there’s the option for Change Runtime Type.

Click on that, and that opens up this dialog where you can choose the hardware accelerator.

Be sure to select GPU or a graphics card. It turns out that graphics cards run these models extremely well. Next, click on Save.

![image](https://github.com/Aleixbs/Python_bases/assets/84009394/5bd0a84b-9758-4707-b3ff-569d0b016cf0)

## 2 - Installing OpenAI Whisper and Dependencies
Next, we need to install OpenAI’s Whisper model.

In the first Google Colab cell, enter:
```python
!pip install git+https://github.com/openai/whisper.git
```
This will install Whisper from GitHub.

After, we’re going to install ffmpeg, which will allow us to work with audio and video files.

Again, we’re not installing anything on your computer since we are in a Google Colab Notebook.

```python
!sudo apt update && sudo apt install ffmpeg
```

## 3 - From Speech to Text with OpenAI Whisper
Next click on the Folder icon in the left hand side of the Google Colab notebook.

Once the file has been successfully uploaded, we are now ready to extract text from this audio file.

Copy this code:

```python
!whisper "Sample.mp4" --model medium.en
```

Once you finish entering the code, run it!

After a little bit of wait time, you should see the results. 
