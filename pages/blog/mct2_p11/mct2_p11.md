
As stated in the [Week 48 2024 blog post](/blog/wk48_2024), I have started to do a major refactoring of MediaCow Touch 2. 

## Refactoring
On November 27, 2024, I started the refactoring of the project. On both the GitHub repository and on the website, I moved everything into a directory named "old" and started fresh.

### Overcomplication and SMEC
MediaCow Touch 2 started with two compute elements: The LattePanda Mu and a low-power STMicroelectronics STM32 microcontroller. Over the several months of what could be considered development, it turned into the LattePanda Mu and the Sunplus/Tibbo SP7021.

At some point in development, I had the idea to add a small display mounted to the side of the case. While at first, the idea was to use a small, low-resolution OLED display, I knew at the time that this would complicate the project. Later on, I wanted to use a higher-resolution display. I found the [240x960 display offered by Adafruit](https://www.adafruit.com/product/5799) and noticed it required an RGB interface. At this point, the idea of using the SP7021 appeared.

I want to have MediaCow Touch 2 be unique instead of having it yet another DIY tablet that consists of a touchscreen on a 3D printed box. Though, I do agree that using a quad-core, Linux-capable SoC as an embedded controller is excessive, it would set MediaCow Touch 2 apart from any other tablet computer. SMEC, the embedded controller, is practically a project on its own with its customized Linux kernel, assets and software.

To make this possible, I must come up with a solid project and task management system, preferably one where I do not have to write any code.

## Current Progress
As mentioned before, I basically started fresh, with the existing progress available for reference.

Some parts may be copied from the former design, such as the USB Type-C controller.

### SMEC Video on Main Display 
I put down some ideas for a PCB that switches video from the LattePanda Mu and the HDMI display interface of SMEC; the SP7021.

It turns out that video bridge ICs are quite difficult to source, especially those for DisplayPort and MIPI DSI. This feature is likely not going to be needed or practical as configuration can be done from the side-mounted display. For debugging purposes, I may leave the HDMI interface exposed through an FPC connector.

### SMEC Side Display
I recently came across the [Tailorpixels TTH318BVE-01C 288x960 LCD](https://tailorpixels.com/product/3-18-inch-ips-tft-bar-lcd-mipi-288x960/). It is larger while having a capacitive touchscreen. The catch is that it has a MIPI DSI interface. The only RGB-MIPI bridge that I could find that is currently in stock appears to be the Toshiba TC358778XBG. Publicly available information for this IC is limited, sourcing has historically been difficult and it uses a BGA package though it may be possible to make use of it in this project. If this bridge IC is used, it may be the only BGA package IC used on the carrier PCB.