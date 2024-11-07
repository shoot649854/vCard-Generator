import argparse

from src.Format import format


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
    ft = format()
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
        name_details.get("first_name", "") + " " + name_details.get("last_name", "")
    )
    if not full_name.strip():
        full_name = "Contact"
    with open(f"{full_name}.vcf", "w") as file:
        file.write(vcard)


def main():
    parser = argparse.ArgumentParser(
        description="Create an Apple contact file (vCard)."
    )

    parser.add_argument("--prefix", type=str, help="Prefix for the name")
    parser.add_argument("--first_name", type=str, required=True, help="First name")
    parser.add_argument("--middle_name", type=str, help="Middle name")
    parser.add_argument("--last_name", type=str, required=True, help="Last name")
    parser.add_argument("--suffix", type=str, help="Suffix for the name")
    parser.add_argument("--nickname", type=str, help="Nickname")

    parser.add_argument("--organization", type=str, help="Organization")
    parser.add_argument("--title", type=str, help="Title")
    parser.add_argument("--role", type=str, help="Role")
    parser.add_argument("--work_url", type=str, help="Work URL")

    parser.add_argument("--work_email", type=str, help="Work Email")
    parser.add_argument("--email", type=str, help="Email")
    parser.add_argument("--emails", type=str, help="Additional Emails (separated by ;)")

    parser.add_argument("--label", type=str, help="Address Label")
    parser.add_argument("--street", type=str, help="Street")
    parser.add_argument("--city", type=str, help="City")
    parser.add_argument("--state", type=str, help="State / Province")
    parser.add_argument("--postal_code", type=str, help="Postal Code")
    parser.add_argument("--country", type=str, help="Country")

    parser.add_argument("--phone", type=str, required=True, help="Phone number")
    parser.add_argument("--image_path", type=str, help="Path to the image")
    parser.add_argument("--gender", type=str, help="Gender")
    parser.add_argument("--birthday", type=str, help="Birthday (YYYY-MM-DD)")
    parser.add_argument("--note", type=str, help="Note")

    args = parser.parse_args()

    name_details = {
        "prefix": args.prefix,
        "first_name": args.first_name,
        "middle_name": args.middle_name,
        "last_name": args.last_name,
        "suffix": args.suffix,
        "nickname": args.nickname,
    }

    work_details = {
        "Organization": args.organization,
        "Title": args.title,
        "Role": args.role,
        "Work URL": args.work_url,
    }

    email_details = {
        "Work Email": args.work_email,
        "Email": args.email,
        "Emails": args.emails,
    }

    address_details = {
        "Label": args.label,
        "Street": args.street,
        "City": args.city,
        "State / Province": args.state,
        "Postal Code": args.postal_code,
        "Country": args.country,
    }

    create_apple_contact_file(
        name_details=name_details,
        work_details=work_details,
        email_details=email_details,
        address_details=address_details,
        phone=args.phone,
        image_path=args.image_path,
        gender=args.gender,
        birthday=args.birthday,
        note=args.note,
    )


if __name__ == "__main__":
    main()
