
As stated in the [Week 48, 2024 blog post](/blog/wk48_2024), I have started to do a major refactoring of MediaCow Touch 2. 

## Refactoring
On November 27, 2024, I started the refactoring of the project. On both the GitHub repository and on the website, I moved everything into a directory named "old" and started fresh.

### Overcomplication and SMEC
MediaCow Touch 2 started with two compute elements: The LattePanda Mu and a low-power STMicroelectronics STM32 microcontroller. Over the several months of what could be considered development, it turned into the LattePanda Mu and the Sunplus/Tibbo SP7021.

At some point in development, I had the idea to add a small display mounted to the side of the case. While at first, the idea was to use a small, low-resolution OLED display, I knew at the time that this would complicate the project. Later on, I wanted to use a higher-resolution display. I found the [240x960 display offered by Adafruit](https://www.adafruit.com/product/5799) and noticed it required an RGB interface. At this point, the idea of using the SP7021 appeared.

I want to have MediaCow Touch 2 be unique instead of having it yet another DIY tablet that consists of a touchscreen on a 3D printed box. Though, I do agree that using a quad-core, Linux-capable SoC as an embedded controller is excessive, it would set MediaCow Touch 2 apart from any other tablet computer. SMEC, the embedded controller, is practically a project on its own with its customized Linux kernel, assets and software.

To make this possible, I must come up with a solid project and task management system, preferably one where I do not have to write any code.

## Current Status
I have came up with new deadlines for the project. The first deadline is March 27, 2025; GalaxyCon Richmond. The second deadline is June 20, 2025; the summer solstice.

With college starting on January 13, 2025 and other projects, I may not have as much time to work on MediaCow Touch 2.

### Process
I have been coming up with some sort of plan to complete this project successfully.

An idea I had was to design and 3D print the case before I start circuit design. I would, however, need to determine things like connectors, placement of the side-mounted display and vent placement before I can design and print the case.

### Steam Deck
The Steam Deck OLED that I have received on January 3, 2025 already has made an impact over the design of MediaCow Touch 2.

I have decided to have all of the connectors and the side-mounted display on the top side (screen facing POV) as I have realised that the connectors would be in the way if the device was held on the left and right sides. Having the connectors on the bottom would not work as the device would not be able to be stood up if anything is connected. Also, the top side is one of the long sides of the device which give more space for the connectors and display. This, however, would bring fundamental changes to the design of the case and carrier board that would have been needed to be done anyway.

I have noticed that the Steam Deck can charge off from USB PD voltages lower than the rated 15 volts though at a slower rate. This is a feature I almost left out of MediaCow Touch 2 as it would have required a couple extra buck-boost power regulators, adding up to US$10 to the BOM. I plan on having this feature available.

### Software Usage
I recently have started to use QCAD for detailed drawings, starting with the case design. It did not take long to figure out how to use it.

### BIOS and firmware
The option to have BIOS and embedded controller firmware loaded from an external device would remain.

### Type-C Controller
The TPS65988 continues to leave me hopelessly confused every time I read its datasheet.

When looking through the old version of the schematic, I have noticed that I had the TPS65988DK part, not the TPS65988(DH). I may reference what I had in the schematic and the TI evaluation module schematic for figuring out how to use the IC.

## Resale
I originally did not plan on building MediaCow Touch 2 units for resale. This is because that I believed that the design was not unique to existing devices. This was prior to the addition of SMEC, wireless and storage devices being on M.2 modules and the loading of device firmware and BIOS from an external flash. I figured that MediaCow Touch 2 could be considered a security-oriented device with features that have not been seen before in tablets and even laptops. Due to the now uniqueness of the device, I have been considering building them for resale when the time comes.

During development in the June-August 2024 period, I have been asked if I would sell MediaCow Touch 2 devices.

If I were to build MediaCow Touch 2 units for resale, I do not expect it to be inexpensive. MediaCow Touch 2 would be relatively difficult to manufacture with its high component count.
