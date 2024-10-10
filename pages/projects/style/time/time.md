When possible, [ISO standard 8601](https://www.iso.org/iso-8601-date-and-time-format.html) is used.

## Weeks
Unlike many software set to a US locale, **weeks must start on Monday**. The standard ISO 8601 has weeks start on Monday.

I believe any software dealing with time and date must have the option to set the start of the week to any day of the week. 

## Formats

### Shorthand - Month name, day, year
Since 2022, I commonly used this format for dates in directory names: `<three letter month><day><year>`

For example:
- backup_may262024
- photos_feb222022

However, starting July 31, 2024, I would start using the numbers-only format described in the following section for this purpose.

### Shorthand - numbers only
This date format is used in any instance that it is beneficial. This format would be used in file names, directory names, software builds and anywhere a shorthand date is needed. It replaces the format that I commonly used.

The format used is `YYYYMMDD` where:
- YYYY - Year, four-number representation, values less than four digits are to have leading zero(es)
- MM - Month, two-number representation, single-digit values are to have a leading zero
- DD - Day, two-number representation, single-digit values are to have a leading zero

For example, in file and directory names:
- backup_20240526
- photos_20220222

For date formats including the time, this format shall be used:

The format used is `YYYYMMDD_HHMMSSZZZ` where:
- YYYY - Year, four-number representation
- MM - Month, two-number representation, single-digit values are to have a leading zero
- DD - Day, two-number representation, single-digit values are to have a leading zero
- HH - Hour, two-number representation in 24-hour format, single-digit values are to have a leading zero
- MM - Minute, two-number representation, single-digit values are to have a leading zero
- SS - Second, two-number representation, single-digit values are to have a leading zero
- ZZZZZ - Time zone, in this format:
  - First character is to determine a negative or positive offset that uses p and n to represent + and - respectively
  - Second to fifth is the UTC offset. Written as described in ISO 8601.

For example:
- September 22, 2024, 12:58 PM EDT: 202409221258n0400
- February 22, 2022, 10:22 PM EST: 202202222222n0500
- June 7, 2004, 2:47 AM EDT: 200406070247n0400
- April 1, 2008, 12:00 PM CEST: 200804011200p0200

### Long form
In text such as documents and general communications, this format is preferred:

Day, month and year known:
- `<month name> <day>, <year>`

Month and year known:
- `<month name> <year>`

Examples:
- "Server backups would commence on August 11, 2024"
- "Planning started in March 2021"

## Project Year Ranges
Sometimes, a project contains the text "CTCL" then the year range of the project. Another example of the use of a year range is describing when I worked on a project under the "Projects" page of this website.

### Sub-projects
With projects under a general project series, the starting year depends on the type of project.

#### Software
With software, the starting year is when the development of the original idea has started. For example "ctclsite-rust" having the year range 2019-2024 despite the Rust version not existing prior to 2022. 

This means that cbtssite (HTML/CSS-only versions from 2019-2022), ctclsite-python and ctclsite-rust would all share the year range 2019-<present year>.

#### Hardware projects
Hardware projects under a general series would have their own starting year ranges.

For example, MediaCow Touch 2 would have the starting year as 2021 while the MediaCow project series altogether started in 2018.

Hardware platforms created for a larger project would also have their own starting years.

This also applies to software created solely for a hardware project. For example, firmware used on hardware in MediaCow Touch 2 would have the starting year 2021.

#### Hardware projects split into phases
Hardware projects that are split into phases would have the year range of the project as a whole. 

For example: NetKart Phase 1, NetKart Phase 2, NetKart Phase 3 and NetKart Phase 4 would have the starting year as 2019 when I acquired the base go-kart. However, hardware created for a larger project, such as the theoretical "NetKart-ECU" would have its own starting year. 