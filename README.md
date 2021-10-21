[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)

# We're all Doomed - A Bitcoin Fear and Greed Index visualiser
A [fear and greed index](https://alternative.me/crypto/fear-and-greed-index/visualiser) visualiser for Bitcoin inspired by the Doom health monitor. The Fear and Greed Index is a multifactorial Bitcoin market sentiment analysis. This code is just a simple tool that pulls that index and visualises it in a window inspired by the health status graphic from Doom. 

- Low health images used for Fear
- High health images used for Greed 

> "Everyone has a plan until they get punched in the mouth".

# Hardware

Uses a Waveshare 1.5 inch RGB OLED, 128 x 128 pixels. Tested with Raspberry Pi Zero. **TO DO: Pico or STM32 Version**

# Installation

Follow the [setup instructions](https://www.waveshare.com/wiki/File:1.5inch_OLED_Module_User_Manual_EN.pdf) for the OLED screen. 

Then clone this repository:

    git clone https://github.com/llvllch/doomed.git
    cd doomed

Install the required Python3 modules
```
python3 -m pip install -r requirements.txt
```

# Running

To start the code running, issue the command: 

    python3 main.py

# Acknowlegements

- The default images are based on the sprite set [shared online](https://spritedatabase.net/display.php?object=549) by FalconDelta.
- Doom - https://en.wikipedia.org/wiki/Doom_(1993_video_game)

# Licence

GPL 3.0
