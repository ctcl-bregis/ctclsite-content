SMEC, System Management Embedded Controller, is a dedicated microprocessor that handles various system management tasks.

## Overview

### History

#### Previous Designs
An embedded controller was expected to be present in the design since the beginning of the project in 2021. The original MediaCow Touch from 2020 had something that could be considered an embedded controller: a Teensy LC board that made use of a NXP/Freescale Kinetis MKL26Z64VFT4 microcontroller though its only purpose was to control the button board on the side of the case.

Photos from 2021 show that the embedded controller consisted of a Microchip PIC32MX MIPS microcontroller.

#### Current
The initial block diagram sent to LattePanda at the beginning of the current project in June 2024 showed that the design did not have an embedded controller. The team suggested that I should add one.

I started out with an STMicroelectronics STM32L-series microcontroller though this changed later on.

With the introduction of the side-mounted display, this changed. On September 11, 2024, I officially switched to the Sunplus/Tibbo SP7021 System in Package. 
There are several reasons why I went with a System in Package over a common, low-power, microcontroller. The use of a dedicated processor as the embedded controller would have the device unique to other tablet designs.

SMEC ended up being a project on its own with its own embedded Linux distribution, assets and software.

## Features

### Power Management
SMEC controls various power regulators on board.

### Display
SMEC controls the dedicated side-mounted display. 

As of December 27, 2024, the display is to be determined.

### Audio
SMEC acts as a DSP for audio input and output.

SMEC can possibly playback audio on its own.

### Firmware Management
A unique feature of MediaCow Touch 2 is that SMEC is capable of emulating an SPI flash device where the system on module (LattePanda Mu) can read directly from for loading the BIOS image.

