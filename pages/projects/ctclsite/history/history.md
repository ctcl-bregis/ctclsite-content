## Development History
From 2020 to 2021, my website was made up of just HTML and CSS that I wrote by hand. The webpages were hosted on GitHub Pages initially then was moved to DigitalOcean some time in 2021 when I got a domain name. It was not until December 2021-January 2022 that I wrote a version of the website that has backend code. 

The switch to a version that uses backend code to generate content was mainly due to the former RAMList pages that had amounts of tabular data that was too large to be managed by hand. RAMList was the main reason why I switched to using Rust for the website in November 2022 which turned out to compensate for the highly inefficient method of retrieving and processing data. [RAMList was discontinued in August 2023](/blog/10/) for multiple reasons.

It is possible for me to just make something that generates static HTML pages to served by the webserver. However, there has been plans for features that would not be possible with just HTML and JS such as improved logging, view counters and dynamically generated embeds for other websites.

In February 2024, I have decided to switch to Rust for server and web software development.

Starting July 10, 2024, CSS is now generated with Tera as with HTML. On September 28, 2024, Tera was replaced by a fork of Tera, called [Lysine](/projects/lysine/) that is better suited for CSS generation along with HTML.


### Version Overview
The current version of the website is **LiteFolio**.


| Website Version                        | Programming Language | Web Framework | Development Started | Released           | Development System(s)                                                                                                                                                  |
| -------------------------------------- | -------------------- | ------------- | ------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ctclsite-python v1                     | Python               | Flask         | December 2021       | January 7, 2022    | [Polyethylene Terephthalate](/projects/wbpc/#pc_pet)                                                                                                                          |
| ctclsite-python v2                     | Python               | Flask         | 2022                | 2022               | [Polyethylene Terephthalate](/projects/wbpc/#pc_pet)                                                                                                                          |
| ctclsite-rust v0                       | Rust                 | Actix Web     | November 2022       | January 2023       | "Dichlorofluoromethane" (ThinkPad X240), [Polyethylene Terephthalate](/projects/wbpc/#pc_pet)                                                                                 |
| ctclsite-python v3                     | Python               | Flask         | May 15, 2023        | May 20, 2023       | [Polybutylene Terephthalate](/projects/wbpc/#pc_pbt)                                                                                                                          |
| ctclsite-python v4                     | Python               | Django        | August 26, 2023     | October 20, 2023   | [Polybutylene Terephthalate](/projects/wbpc/#pc_pbt)                                                                                                                          |
| ctclsite-python v5                     | Python, JavaScript   | Django        | November 21, 2023   | December 22, 2023  | [Polybutylene Terephthalate](/projects/wbpc/#pc_pbt)                                                                                                                          |
| ctclsite-rust v1                       | Rust, JavaScript     | Actix Web     | February 18, 2024   | March 3, 2024      | [Polybutylene Terephthalate](/projects/wbpc/#pc_pbt), [Polymethylmethacrylate](/projecdts/wbpc/#pc_pmma)                                                                              |
| LiteFolio (formerly ctclsite-rust v2)  | Rust, JavaScript     | Actix Web     | September 5, 2024   | September 23, 2024 | [Polybutylene Terephthalate](/projects/wbpc/#pc_pbt), [Polymethylmethacrylate](/projects/wbpc/#pc_pmma), [Tetrahydrocannabinol](/projects/wpbc/#pc_thc), Chlorofluoroethane (ThinkPad T450s)|

