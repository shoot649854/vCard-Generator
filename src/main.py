from Format import format

ft = format()


def create_apple_contact_file(
    name_details,
    work_details,
    email_details,
    address_details,
    phone,
    image_path=None,
    gender=None,
    birthday=None,
    note=None,
):
    # Build vCard string
    vcard = "BEGIN:VCARD\nVERSION:3.0\n"
    vcard += ft.format_name(name_details)
    vcard += ft.format_work(work_details)
    vcard += ft.format_email(email_details)
    vcard += ft.format_address(address_details)
    vcard += ft.format_gender(gender)
    vcard += ft.format_image(image_path)
    vcard += f"TEL;TYPE=CELL:{phone}\n"
    if birthday:
        vcard += f"BDAY:{birthday}\n"
    if note:
        vcard += f"NOTE:{note}\n"
    vcard += "END:VCARD\n"

    # Write vCard to file
    full_name = (
        name_details.get("First Name", "") + " " + name_details.get("Last Name", "")
    )
    if not full_name.strip():
        full_name = "Contact"
    with open(f"{full_name}.vcf", "w") as file:
        file.write(vcard)


# Example usage:
name_details = {
    "prefix": "Dr.",
    "first_name": "John",
    "middle_name": "H.",
    "last_name": "Doe",
    "suffix": "III",
    "nickname": "Johnny",
}

work_details = {
    "Organization": "XYZ Corp",
    "Title": "Software Engineer",
    "Role": "Developer",
    "Work URL": "http://www.xyzcorp.com",
}

email_details = {
    "Work Email": "john.doe@xyzcorp.com",
    "Email": "john.doe@example.com",
    "Emails": "john.doe@personal.com;john.doe2@personal.com",
}

address_details = {
    "Label": "Home Address",
    "Street": "123 Main St",
    "City": "City",
    "State / Province": "State",
    "Postal Code": "12345",
    "Country": "Country",
}

create_apple_contact_file(
    name_details=name_details,
    work_details=work_details,
    email_details=email_details,
    address_details=address_details,
    phone="+123456789",
    image_path="path/to/image.jpg",
    gender="Male",
    birthday="1990-01-01",
    note="Friend from college",
)
