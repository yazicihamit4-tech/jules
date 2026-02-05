import json

# Manually extracted data from index.html (since extracting via python script from HTML text is error prone without soup)
WORD_DATA = {
    1: { "length": 3, "words": ["OBA", "HAN", "OKU", "YAY", "ALP", "BEY", "GÖK", "TÜRK", "ÇER", "GÜÇ", "SOY", "BAŞ", "KAN", "YOL", "ATA", "DAĞ", "GÖL", "BAĞ", "SAÇ", "YAŞ", "GÖZ", "KAŞ", "DİŞ", "EL", "KOL"] },
    2: { "length": 4, "words": ["OTAĞ", "BÖRÜ", "OKÇU", "YURT", "ORDU", "KAYI", "ASYA", "METE", "URAL", "KALE", "ÜLKÜ", "ÇERİ", "OĞUZ", "KUTU", "PAŞA", "EREN", "OZAN", "AŞIK", "KENT", "OBAL", "UÇAK", "TANK", "GEMİ", "MAVİ", "SARI", "KIZIL", "KARA", "AKÇA"] },
    3: { "length": 5, "words": ["TURAN", "VATAN", "KAĞAN", "YAVUZ", "FATİH", "UYGUR", "GİRNE", "SİVAS", "İZMİR", "AYDIN", "BİLGE", "ÇORUH", "DİCLE", "FIRAT", "KARS", "KÖMEN", "ALTAY", "PAMİR", "HAZAR", "KONAK", "SARAY", "DENİZ", "IRMAK", "TOROS", "YÖRÜK", "ZEYBEK", "HORON", "HALAY"] },
    4: { "length": 6, "words": ["SELÇUK", "BOZKIR", "ANKARA", "MANİSA", "MARDİN", "EDİRNE", "SAMSUN", "BAYRAK", "MİLLET", "DEVLET", "MECLİS", "İSTİLA", "DESTAN", "KUDRET", "VİCDAN", "KERKÜK", "MUSUL", "BALKAN", "KAFKAS", "CEPHE", "SİPER", "MEHMET", "ASKER", "SUBAY", "YÜZBAŞI", "BİNBAŞI"] },
    5: { "length": 7, "words": ["SAKARYA", "OSMANLI", "ANADOLU", "AKDENİZ", "ATATÜRK", "TRABZON", "ANTALYA", "MALATYA", "KÜTAHYA", "ISPARTA", "YASEMİN", "ZÜMRÜT", "PIRLANTA", "TÜRKMEN", "KIPÇAK", "KARLUK", "BASMIL", "TÜRKEŞ", "BAŞBUĞ", "ALPEREN", "AKINCILAR", "YENİÇERİ", "LEVENT"] },
    6: { "length": 8, "words": ["TEŞKİLAT", "MEMLEKET", "HÜRRİYET", "İSTİKLAL", "TEKİRDAĞ", "OSMANİYE", "NEVŞEHİR", "KAHRAMAN", "YILDIRIM", "BARBAROS"] },
    7: { "length": 9, "words": ["KASTAMONU", "ZONGULDAK", "GÜMÜŞHANE", "ÇANAKKALE", "BALIKESİR", "GAZİANTEP", "KIRIKKALE", "ADAPAZARI", "EGEMENLİK", "DEMOKRASİ", "ANITKABİR", "ESKİŞEHİR", "ŞANLIURFA", "ALPARSLAN", "MALAZGİRT"] },
    8: { "length": 10, "words": ["BAŞKOMUTAN", "DOLMABAHÇE", "CUMHURİYET", "DİYARBAKIR", "KIRKLARELİ", "BÜYÜKŞEHİR", "FENERBAHÇE", "ÜNİVERSİTE", "TELEVİZYON", "BİLGİSAYAR", "ARKADAŞLIK", "ÖĞRETMENİM", "HASTANELER"] }
}

def validate():
    errors = []
    for level, data in WORD_DATA.items():
        expected_len = data["length"]
        words = data["words"]
        for word in words:
            # Check length (account for Turkish special chars if needed, though len() works in Python 3)
            # Just standard len()
            if len(word) != expected_len:
                errors.append(f"Level {level} Error: Expected {expected_len} chars, found '{word}' ({len(word)} chars)")

    if errors:
        print("❌ DATA ERRORS FOUND:")
        for e in errors:
            print(e)
    else:
        print("✅ All word lengths are correct.")

if __name__ == "__main__":
    validate()
