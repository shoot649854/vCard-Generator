class format:
    def __init__(self) -> None:
        pass

    def format_name(self, name_details):
        """
        Modified to accept a dictionary of name details.
        """
        prefix = name_details.get("prefix", "")
        first_name = name_details.get("first_name", "")
        middle_name = name_details.get("middle_name", "")
        last_name = name_details.get("last_name", "")
        suffix = name_details.get("suffix", "")
        nickname = name_details.get("nickname", None)
        
        components = [last_name, first_name, middle_name, prefix, suffix]
        name_components = ';'.join(filter(None, components))
        vcard_name_field = f"N:{name_components}"
        vcard_nickname_field = f"NICKNAME:{nickname}" if nickname else ""
        return vcard_name_field + ('\n' + vcard_nickname_field if nickname else '')
    
    def format_work(self, work_details):
        """
        Formats work details into a vCard-compatible string.
        """
        formatted_work = ''
        for key, value in work_details.items():
            if value:
                formatted_work += f"{key}:{value}\n"
        return formatted_work

    def format_email(self, email_details):
        """
        Formats email details into a vCard-compatible string.
        """
        formatted_email = ''
        for key, value in email_details.items():
            if value:
                formatted_email += f"EMAIL;TYPE={key.upper()}:{value}\n"
        return formatted_email

    def format_address(self, address_details):
        """
        Formats address details into a vCard-compatible string.
        """
        formatted_address = ''
        for key, value in address_details.items():
            if value:
                formatted_address += f"ADR;TYPE=HOME;{key.upper()}:{value}\n"
        return formatted_address

    def format_gender(self, gender):
        """
        Formats gender details into a vCard-compatible string.
        """
        if gender:
            return f"GENDER:{gender.capitalize()}\n"
        return ''

    def format_image(self, image_path):
        """
        Formats image details into a vCard-compatible string.
        """
        if image_path:
            return f"PHOTO;TYPE=JPEG;ENCODING=BASE64:{image_path}\n"
        return ''