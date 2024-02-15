from peopleScrapper import PeopleScrapper

data = [
    {
        'companies': ['eiffage'],
        'keywords': ['technicien', 'responsable achat'],
        'locations': ['Paris'],
        'person_limit': 5
    },
    {
        'companies': ['groupe snef'],
        'keywords': ['responsable achat'],
        'locations': ['Marseille'],
        'person_limit': 5
    }
]

scrapper = PeopleScrapper(data)