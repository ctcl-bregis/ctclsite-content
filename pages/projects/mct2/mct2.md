MediaCow Touch 2 is a project pertaining to the design and assembly of a mobile tablet device.

**Disclaimer**: Anything on this page and other pages related to this project is preliminary data and may change at any moment.


### Name
MediaCow Touch 2 is part of the MediaCow series, the history behind the name is covered in the [MediaCow page](/projects/mc/).

## Overview
The design of MediaCow Touch 2 tries to be unique from existing tablet devices.

Unlike some of the devices that it takes inspiration from, MediaCow Touch 2 is not gaming-oriented and is instead for general-purpose use.

### Security and Privacy Features
MediaCow Touch 2 provides hardware-level security features that are often not seen in devices of its class.

#### Audio and Microphones
Audio signals to and from the integrated audio CODEC can be disconnected by onboard switches.

Speakers are to be connected to the carrier board through JST-style connectors instead of being soldered directly.

#### TPM
The carrier board has a TPM header for the option of a TPM module.

#### State
MediaCow Touch 2 follows the principles of the document titled ["State Considered Harmful"](https://blog.invisiblethings.org/papers/2015/state_harmful.pdf).

User storage is to be provided by an SSD connected to the carrier board's M.2 slot. The SPI flash memory IC used for BIOS is socketed on the carrier board and can be removed when the device is disassembled. 

By default, the LattePanda Mu contains an 64GB eMMC for user-accessible storage and an SPI flash for BIOS. It may be possible to remove these devices from the module or be provided a LattePanda Mu that does not have these devices populated.

This also applies to the embedded controller, SMEC, where its storage is provided by an eMMC module that plugs into the carrier board. It may be possible for the embedded controller to emulate an SPI flash device for the LattePanda Mu to read from. 

#### BIOS
The BIOS to be used is coreboot, an open source firmware.

#### Ports
Power to USB ports can be disabled by the embedded controller. This can help prevent damage from devices such as USB Killer or Bad USB.
