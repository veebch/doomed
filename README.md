[![YouTube Channel Views](https://img.shields.io/youtube/channel/views/UCz5BOU9J9pB_O0B8-rDjCWQ?label=YouTube&style=social)](https://www.youtube.com/channel/UCz5BOU9J9pB_O0B8-rDjCWQ)

# We're all Doomed - A Bitcoin Fear and Greed Index visualiser
A [fear and greed index](https://alternative.me/crypto/fear-and-greed-index/visualiser) visualiser for Bitcoin inspired by the Doom health monitor.

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

# Acknowlegement

The default images are based on the sprite set [shared online](https://spritedatabase.net/display.php?object=549) by FalconDelta.

# Licence

GPL 3.0
