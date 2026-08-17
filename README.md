# Pingvin-dataanalys

Ett litet projekt för att lära mig git och GitHub genom att analysera öppen data.

## Data
Palmer Penguins-datasetet (CC0-licens), insamlat av Palmer Station LTER, Antarktis.
Källa: https://github.com/allisonhorst/palmerpenguins

## Vad skriptet gör
`src/analyze.py` läser in datan och skapar:
- en statistisk sammanfattning i terminalen
- ett stapeldiagram över medelvikt per art
- ett spridningsdiagram över näbblängd vs vikt per art

## Kör själv
\`\`\`
pip install -r requirements.txt
python src/analyze.py
\`\`\`
