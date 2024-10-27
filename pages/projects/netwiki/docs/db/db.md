
## Overview
NetWiki currently uses SQLite3.

Pages are stored in a database.

## Schema
This section is structured like the database. Any sections under this section represent tables.

The schema is defined in a JSON file as "src/data/tables.json". This file is only used during compilation.

Each field's name is prefixed the name of the table it belongs to. 

### page
"page" is the table that stores information about each page.

#### "page_id"
"page_id" is the numerical ID of the page.

#### "page_name"
"page_name" is the internal name of the page. It is the representation of the page title with spaces replaced with underscores
