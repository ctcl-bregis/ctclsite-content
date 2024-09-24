## Overview
Development on MediaCow Touch 2 has been slow since I have started the college semester and I have gained significant burnout from the project. This was my concern with not getting the project done by August 26, 2024. 

## Challenges
Many parts of the project remain unfinished.

### 12-20v to 3.3v 
A challenge that I have been facing is finding a switching buck converter that can step down the 12-20v VSYS voltage to 3.3v that is used by a variety of devices. Cutting costs is important especially due to the amount of these regulators expected to be used in the design. 

The main concerns were:
- Efficiency at low currents (1-200mA)
- Implementation cost
- Voltage input support

Up to August 30, 2024, I have had the plans to use Silergy SY21019 regulators extensively for most components that require 3.3v until I found out about the Diodes AP63203. On Mouser, as of August 30, 2024, the AP63203 is US$0.715 per unit with a quanity of 10 while the SY21019 is US$0.551/unit with a quanity of 10. I determined that the implementation cost of the AP63203 would be less due to the regulator having a fixed output of 3.3v; does not require a resistor divider on the output to set the voltage. As result, the AP63203 would have a lower implementation cost while being more simple to use. 

The AP63203 seems to have good efficiency all around with the efficiency remaining above 70% from 1mA to 2A [according to the datasheet](https://www.diodes.com/assets/Datasheets/AP63200-AP63201-AP63203-AP63205.pdf). The SY21019 has similar performance with an inductor value of 22uH [as seen in its datasheet](https://us1.silergy.com/download/downloadFile?id=2877&type=product&ftype=note). The AP63203 uses a realitively small inductor value of around 3.3-3.9uH, I felt that I had to verify to this by using the formula in the datasheet.

After following the recommended layouts in the datasheets for both the AP63203 and SY21029. The AP63203 appears to use half the amount of external components.

An SY21019 may continue to be used for the 12v input to the OLED display on the side of the case. Another SY21019 is used to step VSYS down to 3.5v in a pre-regulator configuation for SMEC and sensors. 

### System Management Embedded Controller: The switch to SP7021
By September 11, 2024, I have started to go with the idea of using the Sunplus/Tibbo SP7021 SiP (System in Package) in place of the STMicroelectronics STM32L496 for SMEC (System Management Embedded Controller).

The idea to use the SP7021 arised when I was looking for other options for the side-mounted display. Specifically, I was looking at the [HD371001C40](https://www.adafruit.com/product/5799) and [TL032FWV01-I1440A](https://www.adafruit.com/product/5828) where I noticed that in the description for both that it mentions "The TFT driver is ST7701S and uses both SPI and TTL RGB 'dot clock' data. The SPI is only for configuring the display - you cannot draw pixels over SPI!". The STM32L496 may have been able to drive the display though by then, there would not be enough RAM or CPU cycles left to do anything else.

On September 15, 2024, I have made a fork of the 'SP7021' repository provided by Sunplus on GitHub along with some of its submodules. I threw together some sort of logo for the repository, which is just the "MediaCow Touch 2" logo from the mct2 repository with the text "System Management Embedded Controller" in the Terminus font. The use of Terminus was inspired by the font's use in the game OneShot. The font may be used for UI elements on the side-mounted display along with the [Pixel](/projects/pixel_fonts/) font series I have created.

Switching from a common microcontroller to a Linux-capable quad-core ARM SoC so close to the deadline may seem like a terrible idea but using the SP7021 may bring many benefits along with making MediaCow Touch 2 even more unique. I wanted to use the SP7021 for a few years now. MediaCow Touch 2 may be a good reason to finally start development with the SP7021.

### Side Display
As mentioned in the section above, I have planned to switch out the 128x32 OLED display for a much higher resolution LCD display.

The display chosen was the [TL032FWV01-I1440A](https://www.adafruit.com/product/5828) from Adafruit. The display has a resolution of 320x820 and supports 262K colors. According to its datasheet, the response time is 30-35ms which corresponds to a maximum theoretical frame rate of 28 to 33 FPS. 

The resolution, color support and framerate of the display makes the possibilities of what could be done near endless. 

#### RGB666 from RGB888
I have been looking at the SP7021 documentation provided by Sunplus. [It seems to be possible to use an RGB666 format display with the SP7021's TTL display interface](https://sunplus.atlassian.net/wiki/spaces/doc/pages/1758101595/How+to+setup+and+use+LVDS+Type+TFT-LCD+on+SP7021+EV+Board?focusedCommentId=2270134273).


