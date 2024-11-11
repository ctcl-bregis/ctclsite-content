## Introduction
Like many laptop and Chromebook devices, MediaCow Touch 2 includes an embedded controller; a separate microcontroller/microprocessor that manages various devices.

Originally, there was two microcontrollers named "IOEC" and "PMEC" up to some time in late July 2024 where the functionality of the two were merged into a single microcontroller, named "SMEC". Up to September 11, 2024, the microcontroller used was the STMicroelectronics STM32L496. Starting September 11, 2024, the [Sunplus Technology/Tibbo Technology SP7021](https://www.sunplus.com/products/plus1.asp) is now used for the embedded controller.

I was initially hesitant to switch to the SP7021 as it is immensely more complex to implement than the STM32L496 as I was already nearing the deadline.

### Hardware Introduction
MediaCow Touch 2 is unique in its device class in which it uses a dedicated System on Chip for its embedded controller.

As mentioned before, MediaCow Touch 2 makes use of the SP7021 System in Package. I have had interest in the SP7021 since 2020 and I saw MediaCow Touch 2 as a possible application for it.

## Functions
Note: The term "system" refers to the System on Module and the operating system that runs on it

A quick overview of the functions of SMEC:

- Read battery state and report State of Charge to the system
- Collect data from on-board telemetry; power monitors, PMICs, etc.
- Read button presses and switch states from the side-mounted keypad
- Read and process sensor data
- Drive side-mounted LCD display
- Audio subsystem
  - Processing of audio data from microphones
  - Processing of audio data from the system
  - Audio effects control
  - Audio playback independent of the system; System-independent media player
