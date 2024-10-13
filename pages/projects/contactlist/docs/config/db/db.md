As ContactList makes use of Apache CouchDB, each contact is stored as a document in the database.

## Fields

### Types
So far, these types are defined:

- datetime
- dropdown
- image
- string
- textarea

#### datetime
The "datetime" type is an ISO 8601 timestamp represented by a single string value.

Fields:
- timestamp
  - Rust type: String
  - desc: Timestamp stored as ISO 8601 string

#### dropdown
The "dropdown" type, as described in the name, is shown as a dropdown.

Fields: 
- choice
  - Rust type: String
  - desc: Stored dropdown choice. The stored value uses the internal name.
- choices
  - Rust type: HashMap<String, String>
  - desc: Map of choices available. Keys are the internal name, values are the displayed name
  - Not stored in document

#### image

To-Do: Should images be stored as base64 or in a path?

#### string

Fields:
- content
  - Rust type: String,
  - desc: Stored string value
- maxlength
  - Rust type: u32
  - desc: Maximum length of the input
  - Not stored in document

#### textarea
The difference between textarea and string is that textarea is represented in HTML as <textarea> instead of <input type="text">

Fields:
- content
  - Rust type: String,
  - desc: Stored string value
- maxlength
  - Rust type: u32
  - desc: Maximum length of the input
  - Not stored in document