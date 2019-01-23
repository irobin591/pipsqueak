class Language:
    """Static class to hold some functions for handling languages"""
    @staticmethod
    def name(code: str, raise_error: bool=True, return_all: bool=False) -> str or tuple or None:
        """
        Get language name corresponding to provided ISO 639-1 code
        :param code: ISO 639-1 code
        :param raise_error: Raise error if language not found (rather than return None)
        :param return_all: If False, and the language has multiple names, only return the first
        :return: Language name
        """
        try:
            result = languages[code]
            if isinstance(result, str):
                return result
            else:
                return result if return_all else result[0]

        except KeyError as error:
            if raise_error:
                raise error
            else:
                return None

    @staticmethod
    def code(name: str or tuple, raise_error: bool=True) -> str or None:
        """
        Get ISO 639-1 code corresponding to language name
        """
        try:
            if isinstance(name, str):
                return [key for key, value in languages.items()
                        if isinstance(value, str) and value == name or isinstance(value, tuple) and name in value][0]
            else:
                return [key for key, value in languages.items()
                        if isinstance(value, tuple) and value == name][0]

        except IndexError:
            if raise_error:
                raise KeyError(name)
            else:
                return None


class Country:
    """Static class to hold some functions for handling countries"""
    @staticmethod
    def name(code: str, raise_error: bool=True, return_all: bool=False) -> str or tuple or None:
        """
        Get country name corresponding to provided ISO 3166-1 alpha-2 code
        """
        try:
            result = countries[code]
            if isinstance(result, str):
                return result
            else:
                return result if return_all else result[0]
        except KeyError as error:
            if raise_error:
                raise error
            else:
                return None

    @staticmethod
    def code(name: str, raise_error: bool=True) -> str or None:
        """
        Get ISO 3166-1 alpha-2 code corresponding to country name
        """
        try:
            if isinstance(name, str):
                return [key for key, value in countries.items()
                        if isinstance(value, str) and value == name or isinstance(value, tuple) and name in value][0]
            else:
                return [key for key, value in countries.items()
                        if isinstance(value, tuple) and value == name][0]

        except IndexError:
            if raise_error:
                raise KeyError(name)
            else:
                return None


languages = dict([
    ("aa", "Afar"),
    ("ab", "Abkhazian"),
    ("af", "Afrikaans"),
    ("ak", "Akan"),
    ("am", "Amharic"),
    ("ar", "Arabic"),
    ("an", "Aragonese"),
    ("as", "Assamese"),
    ("av", "Avaric"),
    ("ae", "Avestan"),
    ("ay", "Aymara"),
    ("az", "Azerbaijani"),
    ("ba", "Bashkir"),
    ("bm", "Bambara"),
    ("be", "Belarusian"),
    ("bn", "Bengali"),
    ("bh", "Bihari"),
    ("bi", "Bislama"),
    ("bs", "Bosnian"),
    ("br", "Breton"),
    ("bg", "Bulgarian"),
    ("ca", ("Catalan", "Valencian")),
    ("ch", "Chamorro"),
    ("ce", "Chechen"),
    ("cu", ("Church Slavic", "Old Slavonic", "Church Slavonic", "Old Bulgarian", "Old Church Slavonic")),
    ("cv", "Chuvash"),
    ("kw", "Cornish"),
    ("co", "Corsican"),
    ("cr", "Cree"),
    ("cs", "Czech"),
    ("da", "Danish"),
    ("dv", ("Divehi", "Dhivehi", "Maldivian")),
    ("dz", "Dzongkha"),
    ("en", "English"),
    ("eo", "Esperanto"),
    ("et", "Estonian"),
    ("eu", "Basque"),
    ("ee", "Ewe"),
    ("fo", "Faroese"),
    ("fj", "Fijian"),
    ("fi", "Finnish"),
    ("fr", "French"),
    ("fy", "Western Frisian"),
    ("ff", "Fulah"),
    ("Ga", "Georgian"),
    ("de", "German"),
    ("gd", ("Gaelic", "Scottish Gaelic")),
    ("ga", "Irish"),
    ("gl", "Galician"),
    ("gv", "Manx"),
    ("el", "Modern Greek"),
    ("gn", "Guarani"),
    ("gu", "Gujarati"),
    ("ht", ("Haitian", "Haitian Creole")),
    ("ha", "Hausa"),
    ("he", "Hebrew"),
    ("hz", "Herero"),
    ("hi", "Hindi"),
    ("ho", "Hiri Motu"),
    ("hr", "Croatian"),
    ("hu", "Hungarian"),
    ("hy", "Armenian"),
    ("ig", "Igbo"),
    ("io", "Ido"),
    ("ii", ("Sichuan Yi", "Nuosu")),
    ("iu", "Inuktitut"),
    ("ie", ("Interlingue", "Occidental")),
    ("ia", "Interlingua"),
    ("id", "Indonesian"),
    ("ik", "Inupiaq"),
    ("is", "Icelandic"),
    ("it", "Italian"),
    ("jv", "Javanese"),
    ("ja", "Japanese"),
    ("kl", ("Kalaallisut", "Greenlandic")),
    ("kn", "Kannada"),
    ("ks", "Kashmiri"),
    ("ka", "Georgian"),
    ("kr", "Kanuri"),
    ("kk", "Kazakh"),
    ("km", "Central Khmer"),
    ("ki", ("Kikuyu", "Gikuyu")),
    ("rw", "Kinyarwanda"),
    ("ky", ("Kirghiz", "Kyrgyz")),
    ("kv", "Komi"),
    ("kg", "Kongo"),
    ("ko", "Korean"),
    ("kj", ("Kuanyama", "Kwanyama")),
    ("ku", "Kurdish"),
    ("lo", "Lao"),
    ("la", "Latin"),
    ("lv", "Latvian"),
    ("li", ("Limburgan", "Limburger", "Limburgish")),
    ("ln", "Lingala"),
    ("lt", "Lithuanian"),
    ("lb", ("Luxembourgish", "Letzeburgesch")),
    ("lu", "Luba-Katanga"),
    ("lg", "Ganda"),
    ("mh", "Marshallese"),
    ("ml", "Malayalam"),
    ("mr", "Marathi"),
    ("Mi", "Micmac"),
    ("mk", "Macedonian"),
    ("mg", "Malagasy"),
    ("mt", "Maltese"),
    ("mn", "Mongolian"),
    ("mi", "Maori"),
    ("ms", "Malay"),
    ("my", "Burmese"),
    ("na", "Nauru"),
    ("nv", ("Navajo", "Navaho")),
    ("nr", "South Ndebele"),
    ("nd", "North Ndebele"),
    ("ng", "Ndonga"),
    ("ne", "Nepali"),
    ("nl", ("Dutch", "Flemish")),
    ("nn", "Norwegian Nynorsk"),
    ("nb", "Norwegian Bokmål"),
    ("no", "Norwegian"),
    ("oc", "Occitan"),
    ("oj", "Ojibwa"),
    ("or", "Oriya"),
    ("om", "Oromo"),
    ("os", ("Ossetian", "Ossetic")),
    ("pa", ("Panjabi", "Punjabi")),
    ("fa", "Persian"),
    ("pi", "Pali"),
    ("pl", "Polish"),
    ("pt", "Portuguese"),
    ("ps", ("Pushto", "Pashto")),
    ("qu", "Quechua"),
    ("rm", "Romansh"),
    ("ro", ("Romanian", "Moldavian", "Moldovan")),
    ("rn", "Rundi"),
    ("ru", "Russian"),
    ("sg", "Sango"),
    ("sa", "Sanskrit"),
    ("si", ("Sinhala", "Sinhalese")),
    ("sk", "Slovak"),
    ("sl", "Slovenian"),
    ("se", "Northern Sami"),
    ("sm", "Samoan"),
    ("sn", "Shona"),
    ("sd", "Sindhi"),
    ("so", "Somali"),
    ("st", "Southern Sotho"),
    ("es", ("Spanish", "Castilian")),
    ("sq", "Albanian"),
    ("sc", "Sardinian"),
    ("sr", "Serbian"),
    ("ss", "Swati"),
    ("su", "Sundanese"),
    ("sw", "Swahili"),
    ("sv", "Swedish"),
    ("ty", "Tahitian"),
    ("ta", "Tamil"),
    ("tt", "Tatar"),
    ("te", "Telugu"),
    ("tg", "Tajik"),
    ("tl", "Tagalog"),
    ("th", "Thai"),
    ("bo", "Tibetan"),
    ("ti", "Tigrinya"),
    ("to", "Tonga"),
    ("tn", "Tswana"),
    ("ts", "Tsonga"),
    ("tk", "Turkmen"),
    ("tr", "Turkish"),
    ("tw", "Twi"),
    ("ug", ("Uighur", "Uyghur")),
    ("uk", "Ukrainian"),
    ("ur", "Urdu"),
    ("uz", "Uzbek"),
    ("ve", "Venda"),
    ("vi", "Vietnamese"),
    ("vo", "Volapük"),
    ("cy", "Welsh"),
    ("wa", "Walloon"),
    ("wo", "Wolof"),
    ("xh", "Xhosa"),
    ("yi", "Yiddish"),
    ("yo", "Yoruba"),
    ("za", ("Zhuang", "Chuang")),
    ("zh", "Chinese"),
    ("zu", "Zulu")
])

countries = dict([
    ("AF", u"Afghanistan"),
    ("AX", u"\xc5land Islands"),
    ("AL", u"Albania"),
    ("DZ", u"Algeria"),
    ("AS", u"American Samoa"),
    ("AD", u"Andorra"),
    ("AO", u"Angola"),
    ("AI", u"Anguilla"),
    ("AQ", u"Antarctica"),
    ("AG", u"Antigua and Barbuda"),
    ("AR", u"Argentina"),
    ("AM", u"Armenia"),
    ("AW", u"Aruba"),
    ("AU", u"Australia"),
    ("AT", u"Austria"),
    ("AZ", u"Azerbaijan"),
    ("BS", u"Bahamas"),
    ("BH", u"Bahrain"),
    ("BD", u"Bangladesh"),
    ("BB", u"Barbados"),
    ("BY", u"Belarus"),
    ("BE", u"Belgium"),
    ("BZ", u"Belize"),
    ("BJ", u"Benin"),
    ("BM", u"Bermuda"),
    ("BT", u"Bhutan"),
    ("BO", (u"Bolivia", "Plurinational State of Bolivia")),
    ("BQ", (u"Bonaire, Sint Eustatius and Saba", "Caribbean Netherlands")),
    ("BA", u"Bosnia and Herzegovina"),
    ("BW", u"Botswana"),
    ("BV", u"Bouvet Island"),
    ("BR", u"Brazil"),
    ("IO", u"British Indian Ocean Territory"),
    ("BN", u"Brunei Darussalam"),
    ("BG", u"Bulgaria"),
    ("BF", u"Burkina Faso"),
    ("BI", u"Burundi"),
    ("KH", u"Cambodia"),
    ("CM", u"Cameroon"),
    ("CA", u"Canada"),
    ("CV", u"Cape Verde"),
    ("KY", u"Cayman Islands"),
    ("CF", u"Central African Republic"),
    ("TD", u"Chad"),
    ("CL", u"Chile"),
    ("CN", u"China"),
    ("CX", u"Christmas Island"),
    ("CC", u"Cocos (Keeling Islands)"),
    ("CO", u"Colombia"),
    ("KM", u"Comoros"),
    ("CG", u"Congo"),
    ("CD", ("DR Congo", u"The Democratic Republic of the Congo")),
    ("CK", u"Cook Islands"),
    ("CR", u"Costa Rica"),
    ("CI", u"C\xf4te D'ivoire"),
    ("HR", u"Croatia"),
    ("CU", u"Cuba"),
    ("CW", u"Cura\xe7ao"),
    ("CY", u"Cyprus"),
    ("CZ", u"Czech Republic"),
    ("DK", u"Denmark"),
    ("DJ", u"Djibouti"),
    ("DM", u"Dominica"),
    ("DO", u"Dominican Republic"),
    ("EC", u"Ecuador"),
    ("EG", u"Egypt"),
    ("SV", u"El Salvador"),
    ("GQ", u"Equatorial Guinea"),
    ("ER", u"Eritrea"),
    ("EE", u"Estonia"),
    ("ET", u"Ethiopia"),
    ("FK", (u"Falkland Islands", "Malvinas")),
    ("FO", u"Faroe Islands"),
    ("FJ", u"Fiji"),
    ("FI", u"Finland"),
    ("FR", u"France"),
    ("GF", u"French Guiana"),
    ("PF", u"French Polynesia"),
    ("TF", u"French Southern Territories"),
    ("GA", u"Gabon"),
    ("GM", u"Gambia"),
    ("GE", u"Georgia"),
    ("DE", u"Germany"),
    ("GH", u"Ghana"),
    ("GI", u"Gibraltar"),
    ("GR", u"Greece"),
    ("GL", u"Greenland"),
    ("GD", u"Grenada"),
    ("GP", u"Guadeloupe"),
    ("GU", u"Guam"),
    ("GT", u"Guatemala"),
    ("GG", u"Guernsey"),
    ("GN", u"Guinea"),
    ("GW", u"Guinea-bissau"),
    ("GY", u"Guyana"),
    ("HT", u"Haiti"),
    ("HM", u"Heard Island and McDonald Islands"),
    ("VA", (u"Holy See", "Vatican", "Vatican City State")),
    ("HN", u"Honduras"),
    ("HK", u"Hong Kong"),
    ("HU", u"Hungary"),
    ("IS", u"Iceland"),
    ("IN", u"India"),
    ("ID", u"Indonesia"),
    ("IR", (u"Iran", "Islamic Republic of Iran")),
    ("IQ", u"Iraq"),
    ("IE", u"Ireland"),
    ("IM", u"Isle of Man"),
    ("IL", u"Israel"),
    ("IT", u"Italy"),
    ("JM", u"Jamaica"),
    ("JP", u"Japan"),
    ("JE", u"Jersey"),
    ("JO", u"Jordan"),
    ("KZ", u"Kazakhstan"),
    ("KE", u"Kenya"),
    ("KI", u"Kiribati"),
    ("KP", (u"North Korea", "DPR Korea", "Democratic People's Republic of Korea")),
    ("KR", ("South Korea", "Republic of Korea")),
    ("KW", u"Kuwait"),
    ("KG", u"Kyrgyzstan"),
    ("LA", u"Lao People's Democratic Republic"),
    ("LV", u"Latvia"),
    ("LB", u"Lebanon"),
    ("LS", u"Lesotho"),
    ("LR", u"Liberia"),
    ("LY", u"Libya"),
    ("LI", u"Liechtenstein"),
    ("LT", u"Lithuania"),
    ("LU", u"Luxembourg"),
    ("MO", u"Macao"),
    ("MK", (u"Macedonia", "The Former Yugoslav Republic of Macedonia")),
    ("MG", u"Madagascar"),
    ("MW", u"Malawi"),
    ("MY", u"Malaysia"),
    ("MV", u"Maldives"),
    ("ML", u"Mali"),
    ("MT", u"Malta"),
    ("MH", u"Marshall Islands"),
    ("MQ", u"Martinique"),
    ("MR", u"Mauritania"),
    ("MU", u"Mauritius"),
    ("YT", u"Mayotte"),
    ("MX", u"Mexico"),
    ("FM", (u"Micronesia", "Federated States of Micronesia")),
    ("MD", (u"Moldova", "Republic of Moldova")),
    ("MC", u"Monaco"),
    ("MN", u"Mongolia"),
    ("ME", u"Montenegro"),
    ("MS", u"Montserrat"),
    ("MA", u"Morocco"),
    ("MZ", u"Mozambique"),
    ("MM", u"Myanmar"),
    ("NA", u"Namibia"),
    ("NR", u"Nauru"),
    ("NP", u"Nepal"),
    ("NL", u"Netherlands"),
    ("NC", u"New Caledonia"),
    ("NZ", u"New Zealand"),
    ("NI", u"Nicaragua"),
    ("NE", u"Niger"),
    ("NG", u"Nigeria"),
    ("NU", u"Niue"),
    ("NF", u"Norfolk Island"),
    ("MP", u"Northern Mariana Islands"),
    ("NO", u"Norway"),
    ("OM", u"Oman"),
    ("PK", u"Pakistan"),
    ("PW", u"Palau"),
    ("PS", ("Palestinia", u"Occupied Palestinian Territory")),
    ("PA", u"Panama"),
    ("PG", u"Papua New Guinea"),
    ("PY", u"Paraguay"),
    ("PE", u"Peru"),
    ("PH", u"Philippines"),
    ("PN", u"Pitcairn"),
    ("PL", u"Poland"),
    ("PT", u"Portugal"),
    ("PR", u"Puerto Rico"),
    ("QA", u"Qatar"),
    ("RE", u"R\xe9union"),
    ("RO", u"Romania"),
    ("RU", u"Russian Federation"),
    ("RW", u"Rwanda"),
    ("BL", u"Saint Barth\xe9lemy"),
    ("SH", u'Saint Helena, Ascension and Tristan Da Cunha'),
    ("KN", u"Saint Kitts and Nevis"),
    ("LC", u"Saint Lucia"),
    ("MF", u"Saint Martin (French Part)"),
    ("PM", u"Saint Pierre and Miquelon"),
    ("VC", u"Saint Vincent and the Grenadines"),
    ("WS", u"Samoa"),
    ("SM", u"San Marino"),
    ("ST", u"Sao Tome and Principe"),
    ("SA", u"Saudi Arabia"),
    ("SN", u"Senegal"),
    ("RS", u"Serbia"),
    ("SC", u"Seychelles"),
    ("SL", u"Sierra Leone"),
    ("SG", u"Singapore"),
    ("SX", u"Sint Maarten (Dutch Part)"),
    ("SK", u"Slovakia"),
    ("SI", u"Slovenia"),
    ("SB", u"Solomon Islands"),
    ("SO", u"Somalia"),
    ("ZA", u"South Africa"),
    ("GS", u"South Georgia and the South Sandwich Islands"),
    ("SS", u"South Sudan"),
    ("ES", u"Spain"),
    ("LK", u"Sri Lanka"),
    ("SD", u"Sudan"),
    ("SR", u"Suriname"),
    ("SJ", u"Svalbard and Jan Mayen"),
    ("SZ", u"Swaziland"),
    ("SE", u"Sweden"),
    ("CH", u"Switzerland"),
    ("SY", (u"Syria", "Syrian Arab Republic")),
    ("TW", u"Taiwan"),
    ("TJ", u"Tajikistan"),
    ("TZ", (u"Tanzania", "United Republic of Tanzania")),
    ("TH", u"Thailand"),
    ("TL", u"Timor-leste"),
    ("TG", u"Togo"),
    ("TK", u"Tokelau"),
    ("TO", u"Tonga"),
    ("TT", u"Trinidad and Tobago"),
    ("TN", u"Tunisia"),
    ("TR", u"Turkey"),
    ("TM", u"Turkmenistan"),
    ("TC", u"Turks and Caicos Islands"),
    ("TV", u"Tuvalu"),
    ("UG", u"Uganda"),
    ("UA", u"Ukraine"),
    ("AE", u"United Arab Emirates"),
    ("GB", u"United Kingdom"),
    ("US", u"United States"),
    ("UM", u"United States Minor Outlying Islands"),
    ("UY", u"Uruguay"),
    ("UZ", u"Uzbekistan"),
    ("VU", u"Vanuatu"),
    ("VE", (u"Venezuela", "Bolivarian Republic of Venezuela")),
    ("VN", u"Viet Nam"),
    ("VG", u"British Virgin Islands"),
    ("VI", u"U.S. Virgin Islands"),
    ("WF", u"Wallis and Futuna"),
    ("EH", u"Western Sahara"),
    ("YE", u"Yemen"),
    ("ZM", u"Zambia"),
    ("ZW", u"Zimbabwe")
])


# For testing purposes
if __name__ == "__main__":
    for key, value in languages.items():
        print("{} corresponds to {}".format(Language.code(value), Language.name(key)))

    print("Code for Language Divehi is " + Language.code("Divehi"))

    for key, value in countries.items():
        print("{} corresponds to {}".format(Country.code(value), Country.name(key)))