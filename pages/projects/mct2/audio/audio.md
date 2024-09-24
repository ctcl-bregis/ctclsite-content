## Audio
As the MediaCow series altogether was originally audio-oriented, audio quality still remains as a priority in device design.

### Headphone Jack
Even though in recent times, I rarely use the headphone jack on any devices as my headphones (Sennheiser Momentum 3) have an integrated USB codec that I connect to a PC or laptop through a USB cable and has Bluetooth that I use with my phone (despite the phone having a headphone jack which is why I even picked it out in the first place), the device will have a headphone jack as I believe most computers, including smartphones, should have one unless it absolutely cannot be included in the design.

MediaCow Touch 2 will include a standard 3.5mm audio jack that likely supports an extra connection for a microphone (TRRS connector) which many phones and laptops have support for. 

### CODEC
With the switch to the SP7021 as SMEC, HD Audio is no longer used as the SP7021 would be used for audio processing, which does not support HD Audio. I2S would be used instead. 

#### CODEC Selection
The Analog Devices ADAU1372 may be used as it has multiple digital microphone inputs, high sample rate support (192KHz), integrated headphone amplifiers and low power usage.

#### I2S Source
There may be a multiplexer IC on board to switch the source signal from SMEC to the System on Module. This is mainly for debugging and development purposes to test the audio CODEC independent of SMEC.