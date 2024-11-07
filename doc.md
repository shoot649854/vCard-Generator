This Python script is designed to generate a vCard file, which is a standardized format for electronic business cards, commonly used by Apple Contacts and other applications. Here’s a breakdown of its components and functionality:

### 1. Imports and Dependencies

-   **`argparse`**: Used to parse command-line arguments. This lets users specify details for creating the contact file directly from the command line.
-   **`format`** (from `Format`): An imported class (or module) that presumably contains methods to format various parts of the vCard. Each formatting method (`format_name`, `format_work`, etc.) is likely responsible for formatting a particular section of the vCard.

### 2. `create_apple_contact_file` Function

This function builds and writes a vCard file based on provided contact details.

-   **Parameters**:
    -   `name_details`, `work_details`, `email_details`, `address_details`: Dictionaries containing details for each respective part of the contact.
    -   `phone`, `image_path`, `gender`, `birthday`, `note`: Other details of the contact.
-   **vCard Creation**:
    -   The function initializes a vCard string (`vcard`) and sets the version to 3.0, which is widely supported.
    -   It then formats each component of the vCard by calling formatting functions from the `ft` instance (`ft.format_name(name_details)`, etc.), which likely apply the correct vCard field labels and format.
    -   **Phone Number**: Directly added to the vCard with `TYPE=CELL`.
    -   **Optional Details**: If `birthday` and `note` are provided, they are added to the vCard as well.
    -   The vCard ends with `END:VCARD`.
-   **File Writing**:
    -   The function attempts to generate the contact’s full name from `first_name` and `last_name`. If these are empty, it defaults to “Contact.”
    -   The generated vCard string is written to a file named `{full_name}.vcf`.

```bash
poetry run python src/cli.py  \
  --first_name "" \
  --last_name "" \
  --phone " \
  --email "" \
  --organization "" \
  --title "" \
  --work_url "" \
  --street "" \
  --city "" \
  --state "" \
  --postal_code "" \
  --country "" \
  --note "" \
  --image_path "" \
  --gender ""
```

---

Based on the previous info, create a command to create a vCard file for following information:
