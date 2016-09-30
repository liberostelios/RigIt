from enum import Enum


class GameDataEnum(Enum):
    def __init__(self, menuId, gameId=None, description=None, data=None):
        self.menuId = menuId
        if (gameId != None):
            self.gameId = gameId
        else:
            self.gameId = menuId
        if (description != None):
            self.description = description
        else:
            self.description = self.name
        self.data = data #TODO: consider allowing multiple data arguments

    def __str__(self):
        return self.description

    def __ge__(self, other):
        if self.__class__ is other.__class__:
            return self.menuId >= other.menuId
        return NotImplemented

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.menuId > other.menuId
        return NotImplemented

    def __le__(self, other):
        if self.__class__ is other.__class__:
            return self.menuId <= other.menuId
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.menuId < other.menuId
        return NotImplemented

    @classmethod
    def stringList(cls):
        strings = []
        for _, member in cls.__members__.items():
            strings.append(str(member))
        return strings

    @classmethod
    def _fromAttribute(cls, name, value):
        for member in cls.__members__:
            if (getattr(cls.__members__[member], name) == value):
                return cls.__members__[member]
        raise ValueError('%r is not a valid %s' % (value, cls.__name__))

    @classmethod
    def fromMenuId(cls, menuId):
        return cls._fromAttribute('menuId', menuId)

    @classmethod
    def fromGameId(cls, gameId):
        return cls._fromAttribute('gameId', gameId)

    @classmethod
    def fromDescription(cls, description):
        return cls._fromAttribute('description', description)

    @classmethod
    def fromData(cls, data):
        return cls._fromAttribute('data', data)


class RegisteredPosition(GameDataEnum):
    CF = (0, 12, 'Centre Forward')
    SS = (1, 11, 'Second Striker')
    LFW = (2, 9, 'Left Wing Forward')
    RWF = (3, 10, 'Right Wing Forward')
    AMF = (4, 8, 'Attacking Midfielder')
    LMF = (5, 6, 'Left Midfielder')
    RMF = (6, 7, 'Right Midfielder')
    CMF = (7, 5, 'Centre Midfielder')
    DMF = (8, 4, 'Defensive Midfielder')
    LB = (9, 2, 'Left Back')
    RB = (10, 3, 'Right Back')
    CB = (11, 1, 'Centre Back')
    GK = (12, 0, 'Goalkeeper')


class PlayablePosition(GameDataEnum):
    C = (0,)
    B = (1,)
    A = (2,)
    #S = (3,) #TODO: not sure if supported


class PlayingStyle(GameDataEnum):
    NONE = (0, 0, 'None')
    GOAL_POACHER = (1, 1, 'Goal Poacher')
    DUMMY_RUNNER = (2, 2, 'Dummy Runner')
    FOX_IN_THE_BOX = (3, 3, 'Fox in the Box')
    TARGET_MAN = (4, 13, 'Target Man')
    CREATIVE_PLAYMAKER = (5, 14, 'Creative Playmaker')
    PROFILIC_WINGER = (6, 4, 'Prolific Winger')
    CLASSIC_NO_TEN = (7, 5, 'Classic No. 10')
    HOLE_PLAYER = (8, 6, 'Hole Player')
    BOX_TO_BOX = (9, 7, 'Box to Box')
    THE_DESTROYER = (10, 9, 'The Destroyer')
    ANCHOR_MAN = (11, 8, 'Anchor Man')
    BUILD_UP = (12, 15, 'Build Up')
    EXTRA_FRONTMAN = (13, 10, 'Extra Frontman')
    OFFENSIVE_FULLBACK = (14, 11, 'Offensive Fullback')
    DEFENSIVE_FULLBACK = (15, 12, 'Defensive Fullback')
    OFFENSIVE_GOALKEEPER = (16, 16, 'Offensive Goalkeeper')
    DEFENSIVE_GOALKEEPER = (17, 17, 'Defensive Goalkeeper')
    # UNKNOWN = (18, 16, 'Unknown') #TODO: not sure if supported


class StrongerFoot(GameDataEnum):
    RIGHT_FOOT = (0, 0, 'Right foot')
    LEFT_FOOT = (1, 1, 'Left foot')


class SkinColor(GameDataEnum):
    LIGHT = (0, 1, 'Light', 0xFFD1B3)
    FAIR = (1, 2, 'Fair', 0xDFB391)
    MEDIUM = (2, 3, 'Medium', 0xC19572)
    OLIVE = (3, 4, 'Olive', 0xA37658)
    BROWN = (4, 5, 'Brown', 0x845C40)
    BLACK = (5, 6, 'Black', 0x64442C)
    TRANSPARENT = (6, 0, 'Transparent', 0xCC00FF)
    CUSTOM = (7, 7, 'Custom', 0xFFFFFF)


class PlayerGlovesColor(GameDataEnum):
    WHITE = (0, 0, 'White', 0xFFFFFF)
    BLACK = (1, 1, 'Black', 0x262626)
    RED = (2, 2, 'Red', 0xA92024)
    BLUE = (3, 3, 'Blue', 0x004CFF)
    YELLOW = (4, 4, 'Yellow', 0xFFD300)
    GREEN = (5, 5, 'Green', 0x285E30)
    PINK = (6, 6, 'Pink', 0xd3448B)
    TURQUOISE = (7, 7, 'Turquoise', 0x5CBBD1)


class Spectacles(GameDataEnum):
    NONE = (0, 0, 'None')
    RECTANGLE_RIMLESS = (1, 1, 'Rectangle (rimless)')
    RECTANGLE_HALF_FRAME = (2, 2, 'Rectangle (half frame)')
    RECTANGLE_FULL_FRAME = (3, 3, 'Rectangle (full frame)')
    OVAL_RIMLESS = (4, 4, 'Oval (rimless)')
    OVAL_HALF_FRAME = (5, 5, 'Oval (half frame)')
    OVAL_FULL_FRAME = (6, 6, 'Oval (full frame)')
    ROUND_FULL_FRAME = (7, 7, 'Round (full frame)')


class SpectaclesFrameColor(GameDataEnum): # Apparently identical to GlovesColor
    WHITE = (0, 0, 'White', 0xFFFFFF)
    BLACK = (1, 1, 'Black', 0x262626)
    RED = (2, 2, 'Red', 0xA92024)
    BLUE = (3, 3, 'Blue', 0x004CFF)
    YELLOW = (4, 4, 'Yellow', 0xFFD300)
    GREEN = (5, 5, 'Green', 0x285E30)
    PINK = (6, 6, 'Pink', 0xd3448B)
    TURQUOISE = (7, 7, 'Turquoise', 0x5CBBD1)


class IrisColor(GameDataEnum):
    BLACK = (0, 0, 'Black', 0x120600)
    DARK_BROWN = (1, 1, 'Dark brown', 0x361000)
    BROWN = (2, 2, 'Brown', 0x723C12)
    SADDLE_BROWN = (3, 3, 'Saddle brown', 0xA14800)
    MIDNIGHT_BLUE = (4, 4, 'Midnight blue', 0x121C2A) #TODO: proper name
    CHARCOAL = (5, 5, 'Charcoal', 0x2E3C40)
    GRAY = (6, 6, 'Gray', 0x788084)
    BLUE = (7, 7, 'Blue', 0x3E7899)
    SIENNA  = (8, 8, 'Sienna', 0xAF5A18)
    GREEN = (9, 9, 'Green', 0x5C8436)
    PURPLE = (10, 10, 'Purple', 0x9378AB)
    #TODO: not sure if more colors are supported

class NationalityRegion(GameDataEnum):
    NONE = (0, 0, 'None')
    AFGHANISTAN = (1, 1, 'Afghanistan')
    BAHRAIN = (2, 2, 'Bahrain')
    BANGLADESH = (3, 3, 'Bangladesh')
    CHINA = (4, 7, 'China')
    HONGKONG = (5, 8, 'Hong Kong')
    INDIA = (6, 9, 'India')
    INDONESIA = (7, 10, 'Indonesia')
    IRAN = (8, 11, 'Iran')
    IRAQ = (9, 12, 'Iraq')
    JAPAN = (10, 13, 'Japan')
    JORDAN = (11, 14, 'Jordan')
    NORTHKOREA = (12, 15, 'North Korea')
    SOUTHKOREA = (13, 16, 'South Korea')
    KUWAIT = (14, 17, 'Kuwait')
    LAOS = (15, 18, 'Laos')
    LEBANON = (16, 19, 'Lebanon')
    MALAYSIA = (17, 21, 'Malaysia')
    MALDIVES = (18, 22, 'Maldives')
    OMAN = (19, 26, 'Oman')
    PAKISTAN = (20, 27, 'Pakistan')
    PALESTINE = (21, 28, 'Palestine')
    PHILIPPINES = (22, 29, 'Philippines')
    QATAR = (23, 30, 'Qatar')
    SAUDIARABIA = (24, 31, 'Saudi Arabia')
    SINGAPORE = (25, 32, 'Singapore')
    SRILANKA = (26, 33, 'Sri Lanka')
    SYRIA = (27, 34, 'Syria')
    THAILAND = (28, 36, 'Thailand')
    UAE = (29, 37, 'UAE')
    VIETNAM = (30, 38, 'Vietnam')
    YEMEN = (31, 39, 'Yemen')
    KYRGYZREPUBLIC = (32, 40, 'Kyrgyz Republic')
    TAJIKISTAN = (33, 41, 'Tajikistan')
    TURKMENISTAN = (34, 42, 'Turkmenistan')
    ALGERIA = (35, 44, 'Algeria')
    ANGOLA = (36, 45, 'Angola')
    BENIN = (37, 46, 'Benin')
    BOTSWANA = (38, 47, 'Botswana')
    BURKINAFASO = (39, 48, 'Burkina Faso')
    BURUNDI = (40, 49, 'Burundi')
    CAMEROON = (41, 50, 'Cameroon')
    CAPEVERDE = (42, 51, 'Cape Verde')
    CENTRALAFRICANREP = (43, 52, 'Central African Republic')
    CHAD = (44, 53, 'Chad')
    THECOMOROS = (45, 54, 'The Comoros')
    CONGODR = (46, 55, 'Congo DR')
    COTEDIVOIRE = (47, 56, 'Côte d Ivoire')
    EGYPT = (48, 58, 'Egypt')
    EQUATORIALGUINEA = (49, 59, 'Equatorial Guinea')
    ERITREA = (50, 60, 'Eritrea')
    ETHIOPIA = (51, 61, 'Ethiopia')
    GABON = (52, 62, 'Gabon')
    REPUBLICOFTHEGAMBIA = (53, 63, 'Republic of the Gambia')
    GHANA = (54, 64, 'Ghana')
    GUINEA = (55, 65, 'Guinea')
    GUINEABISSAU = (56, 66, 'Guinea Bissau')
    KENYA = (57, 67, 'Kenya')
    LIBERIA = (58, 69, 'Liberia')
    LIBYA = (59, 70, 'Libya')
    MADAGASCAR = (60, 71, 'Madagascar')
    MALAWI = (61, 72, 'Malawi')
    MALI = (62, 73, 'Mali')
    MAURITANIA = (63, 74, 'Mauritania')
    MAURITIUS = (64, 75, 'Mauritius')
    MOROCCO = (65, 76, 'Morocco')
    MOZAMBIQUE = (66, 77, 'Mozambique')
    NAMIBIA = (67, 78, 'Namibia')
    NIGER = (68, 79, 'Niger')
    NIGERIA = (69, 80, 'Nigeria')
    RWANDA = (70, 81, 'Rwanda')
    SENEGAL = (71, 83, 'Senegal')
    SIERRALEONE = (72, 85, 'Sierra Leone')
    SOMALIA = (73, 86, 'Somalia')
    SOUTHAFRICA = (74, 87, 'South Africa')
    SUDAN = (75, 88, 'Sudan')
    TOGO = (76, 91, 'Togo')
    TUNISIA = (77, 92, 'Tunisia')
    UGANDA = (78, 93, 'Uganda')
    ZAMBIA = (79, 94, 'Zambia')
    ZIMBABWE = (80, 95, 'Zimbabwe')
    CONGO = (81, 98, 'Congo')
    REUNION = (82, 100, 'Réunion')
    ANTIGUAANDBARBUDA = (83, 104, 'Antigua and Barbuda')
    ARUBA = (84, 105, 'Aruba')
    BARBADOS = (85, 107, 'Barbados')
    BERMUDA = (86, 109, 'Bermuda')
    CANADA = (87, 110, 'Canada')
    COSTARICA = (88, 112, 'Costa Rica')
    CUBA = (89, 113, 'Cuba')
    DOMINICANREPUBLIC = (90, 115, 'Dominican Republic')
    ELSALVADOR = (91, 116, 'El Salvador')
    GRENADA = (92, 117, 'Grenada')
    GUADELOUPE = (93, 118, 'Guadeloupe')
    GUATEMALA = (94, 119, 'Guatemala')
    HAITI = (95, 120, 'Haiti')
    HONDURAS = (96, 121, 'Honduras')
    JAMAICA = (97, 122, 'Jamaica')
    MARTINIQUE = (98, 123, 'Martinique')
    MEXICO = (99, 124, 'Mexico')
    MONTSERRAT = (100, 125, 'Montserrat')
    NETHERLANDSANTILLES = (101, 126, 'Netherlands\' Antilles')
    PANAMA = (102, 128, 'Panama')
    PUERTORICO = (103, 129, 'Puerto Rico')
    TRINIDADANDTOBAGO = (104, 133, 'Trinidad and Tobago')
    TURKSANDCAICOSIS = (105, 134, 'Turks and Caicosis')
    UNITEDSTATES = (106, 135, 'United States')
    FRENCHGUIANA = (107, 138, 'French Guiana')
    SURINAME = (108, 139, 'Suriname')
    CURACAO = (109, 140, 'Curaçao')
    ARGENTINA = (110, 144, 'Argentina')
    BOLIVIA = (111, 145, 'Bolivia')
    BRAZIL = (112, 146, 'Brazil')
    CHILE = (113, 147, 'Chile')
    COLOMBIA = (114, 148, 'Colombia')
    ECUADOR = (115, 149, 'Ecuador')
    PARAGUAY = (116, 150, 'Paraguay')
    PERU = (117, 151, 'Peru')
    URUGUAY = (118, 152, 'Uruguay')
    VENEZUELA = (119, 153, 'Venezuela')
    GUYANA = (120, 159, 'Guyana')
    AUSTRALIA = (121, 162, 'Australia')
    FIJI = (122, 164, 'Fiji')
    NEWCALEDONIA = (123, 165, 'New Caledonia')
    NEWZEALAND = (124, 166, 'New Zealand')
    PAPUANEWGUINEA = (125, 167, 'Papua New Guinea')
    SAMOA = (126, 168, 'Samoa')
    SOLOMONISLANDS = (127, 169, 'Solomon Islands')
    TAHITI = (128, 170, 'Tahiti')
    ISRAEL = (129, 189, 'Israel')
    TURKEY = (130, 190, 'Turkey')
    ALBANIA = (131, 191, 'Albania')
    ANDORRA = (132, 192, 'Andorra')
    ARMENIA = (133, 193, 'Armenia')
    AUSTRIA = (134, 194, 'Austria')
    AZERBAIJAN = (135, 195, 'Azerbaijan')
    BELARUS = (136, 196, 'Belarus')
    BELGIUM = (137, 197, 'Belgium')
    BOSNIAANDHERZEGOVINA = (138, 198, 'Bosnia and Herzegovina')
    BULGARIA = (139, 199, 'Bulgaria')
    CROATIA = (140, 200, 'Croatia')
    CYPRUS = (141, 201, 'Cyprus')
    CZECHREPUBLIC = (142, 202, 'Czech Republic')
    DENMARK = (143, 203, 'Denmark')
    ENGLAND = (144, 204, 'England')
    ESTONIA = (145, 205, 'Estonia')
    FAROEISLANDS = (146, 206, 'Faroe Islands')
    FINLAND = (147, 207, 'Finland')
    FRANCE = (148, 208, 'France')
    GEORGIA = (149, 209, 'Georgia')
    GERMANY = (150, 210, 'Germany')
    GREECE = (151, 211, 'Greece')
    HUNGARY = (152, 212, 'Hungary')
    ICELAND = (153, 213, 'Iceland')
    IRELAND = (154, 214, 'Ireland')
    ITALY = (155, 215, 'Italy')
    KAZAKHSTAN = (156, 216, 'Kazakhstan')
    LATVIA = (157, 217, 'Latvia')
    LIECHTENSTEIN = (158, 218, 'Liechtenstein')
    LITHUANIA = (159, 219, 'Lithuania')
    LUXEMBOURG = (160, 220, 'Luxembourg')
    MACEDONIA = (161, 221, 'Macedonia')
    MALTA = (162, 222, 'Malta')
    MOLDOVA = (163, 223, 'Moldova')
    NETHERLANDS = (164, 224, 'Netherlands')
    NORTHERNIRELAND = (165, 225, 'Northern Ireland')
    NORWAY = (166, 226, 'Norway')
    POLAND = (167, 227, 'Poland')
    PORTUGAL = (168, 228, 'Portugal')
    ROMANIA = (169, 229, 'Romania')
    RUSSIA = (170, 230, 'Russia')
    SANMARINO = (171, 231, 'San Marino')
    SCOTLAND = (172, 232, 'Scotland')
    SLOVAKIA = (173, 234, 'Slovakia')
    SLOVENIA = (174, 235, 'Slovenia')
    SPAIN = (175, 236, 'Spain')
    SWEDEN = (176, 237, 'Sweden')
    SWITZERLAND = (177, 238, 'Switzerland')
    UKRAINE = (178, 239, 'Ukraine')
    UZBEKISTAN = (179, 240, 'Uzbekistan')
    WALES = (180, 241, 'Wales')
    GIBRALTAR = (181, 245, 'Gibraltar')
    MONACO = (182, 250, 'Monaco')
    Others = (183, 260, 'Others')
    TAIWAN = (184, 298, 'Taiwan')
    SERBIA = (185, 303, 'Serbia')
    MONTENEGRO = (186, 304, 'Montenegro')
    SINTMAARTEN = (187, 310, 'Sint Maarten')
    KOSOVO = (188, 311, 'Kosovo')
    SOUTHSUDAN = (189, 312, 'South Sudan')

if (__name__ == '__main__'):
    pass
