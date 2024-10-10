This document covers the how I style code, writing and other media. This document contains personal opinions.

Some inspiration for this document is taken from the style guides from [suckless](https://suckless.org/coding_style/) and [Google](https://google.github.io/styleguide/).

## Common Code Guidelines
This section covers conventions used across most programming languages. See the pages linked at the top of the page for styling for specific programming languages.

### Indentation
When possible, indentation shall be done with **four spaces**.

Many IDEs have the feature where the "Tab" key inserts four spaces. 

### Comments
In recent times, I have been trying to have comments more useful.

Like what is stated in [Google's style guide for Python](https://google.github.io/styleguide/), comments shall not describe the code; assume however is reading the code has extensive experience with the programming language. Comments are to be used to explain why a certain thing is done in a certain way. 

## UI and Messages
Messages from the software to the user shall get to the point and be descriptive.

### Addressing the user
The software shall not use first person terms or act as if it were to be sentient.

UI elements, log messages and code should generally avoid these terms:
- I
- I am
- I'm
- Me
- Myself
- Please
- Sorry

Gender-neutral pronouns are to be used when referring to the user or someone else. 

### Error Messages
Error messages should describe the error clearly while giving sufficient information to resolve the error.

## Terminology
Following 2020, many organizations started to change terminology in documentation and software. 

The changes done to documents have been horribly inconsistent from one vendor to another. In some recent document revisions, especially those from Texas Instruments (see SLVSDV5B Revision B, August 2021), the terminology is inconsistent throughout the document with "Slave", "Peripheral", and "Secondary" being used to refer to the same thing.  

### Slave/Master
I believe that the terms "Slave/Master" did not really make that much sense to begin with. It was never a US-specific issue. USB seemed to have used Host/Device well before the 2020s and that seems to be most suitable option though it only properly fits electronics engineering. Some cases, "device" is already used to describe a different part. 

Master/Slave may continue to be used where it is to be consistent with existing documents. This includes the use of MISO/MOSI for SPI signal names.

### Whitelist/Blacklist
Projects will continue to use the terminology "Whitelist/Blacklist".

