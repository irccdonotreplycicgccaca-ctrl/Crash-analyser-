import os
from google import genai

# Récupération de la clé secrète Google AI Studio
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("Erreur : La clé GEMINI_API_KEY est manquante dans les secrets GitHub !")
    exit(1)

# Initialisation de l'IA Gemini
ai_client = genai.Client(api_key=GEMINI_API_KEY)

# Échantillon de données de test (multiplicateurs d'un jeu de Crash)
# Vous pourrez modifier ces chiffres directement ici selon vos sessions de jeu
donnees_jeu = "1.25x, 1.05x, 4.80x, 1.10x, 2.15x, 1.00x, 1.35x, 12.50x, 1.02x, 1.40x"

# Consigne stricte intégrant les mathématiques du Crash et l'analyse statistique
SYSTEM_PROMPT = """
Agis comme un expert en mathématiques appliquées, probabilités et théorie des jeux spécialisé dans l'analyse des jeux de type "Crash".
Analyse rigoureusement l'échantillon de multiplicateurs fourni :
1. Calcule la moyenne et observe la fréquence des "Instant Crashes" (proches de 1.00x).
2. Rappelle l'absence de mémoire du jeu (indépendance des tours, illusion des séries et sophisme du joueur).
3. Précise de manière neutre que l'espérance mathématique reste négative à cause de l'avantage de la maison et que les stratégies de type martingale mènent au risque de ruine.
"""

print("Analyse statistique du jeu de Crash en cours via Gemini...")

try:
    response = ai_client.models.generate_content(
        model='gemini-2.5-flash',
        contents=f"{SYSTEM_PROMPT}\n\nVoici les données de jeu à analyser : {donnees_jeu}"
    )
    print("\n=== RAPPORT D'ANALYSE MATHÉMATIQUE ===")
    print(response.text)
except Exception as e:
    print(f"Une erreur est survenue : {str(e)}")
  
