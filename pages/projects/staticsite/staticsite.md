StaticSite is a static site generator that takes in a configuration directory made up of JSON configuration files and Markdown files. It replaces the "ctclsite" dynamic webpage backends.

Currently, it makes use of the [Lysine](/projects/lysine) templating engine for both HTML and CSS, though CSS generation may be handled by [Serine](/projects/serine/) once it is in a useable state.

It may find use outside of the website, such as in documentation for other projects.

## Development
The project was started on December 16, 2024 and it was first used on December 31, 2024 for generating this website.

As of January 1, 2025, the project consists of a single Python file, build.py that is 296 lines including comments and empty lines, which I plan to decrease. At this time, it is unoptimized and the code is hard to read; there is a lot of room for improvement. It is however much faster, more maintainable and more useful than previous website "backends" that used Actix-Web, Django and Flask that dynamically generated what was essentially static content.

The project was partially inspired by suckless [swerc](https://git.suckless.org/swerc/log.html) which in itself is a fork of [werc](https://werc.cat-v.org). It is not planned to have StaticSite as simple and fast as either swerc or werc.








