# Projekt Zpracování Objednávek

Jednoduchý skript v Pythonu pro zpracování dat o objednávkách z CSV souboru.

## Fáze projektu

### 1. Analýza

Cílem je vytvořit nástroj, který dokáže načíst data z `orders.csv` a provádět nad nimi základní operace.

**Požadavky:**
- Načtení dat ze souboru.
- Sumarizace dat - sečtení celkového počtu kusů pro každý produkt.

### 2. Návrh

Projekt je rozdělen do dvou hlavních souborů:
- `main.py`: Hlavní spouštěcí skript, který se stará o interakci s uživatelem (zobrazení výsledků).
- `data_processor.py`: Modul obsahující logiku pro zpracování dat (načítání, sumarizace).

### Jak spustit

Spusťte soubor `main.py`: `python main.py`