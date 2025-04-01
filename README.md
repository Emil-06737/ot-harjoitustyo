# Ristinolla

Pelin voittaa se pelaaja, jonka tarpeeksi monesta merkistä muodostuu katkeamaton suora, kun pelaajat vuorotellen laittavat merkkejänsä ruudukkoon.

## Dokumentaatio

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Asennusohjeet

1. Aja Asennuskomento:

```bash
poetry install
```

2. Aja käynnistämiskomento:

```bash
poetry run invoke start
```

## Komentorivikomentoja

Käynnistämiskomento:

```bash
poetry run invoke start
```

Testauskomento:

```bash
poetry run invoke test
```

Testikattavuuskomento:

```bash
poetry run invoke coverage-report
```
