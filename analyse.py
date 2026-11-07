import os
from google import genai

# =========================================================================
# CLÉ API : Récupérée automatiquement depuis les secrets GitHub
# =========================================================================
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("Erreur : La clé GEMINI_API_KEY est manquante dans les secrets GitHub !")
    exit(1)

# Initialisation de l'IA Google Gemini
ai_client = genai.Client(api_key=GEMINI_API_KEY)

# Vos données de jeu (Vous pouvez modifier ces chiffres directement ici sur GitHub)
donnees_jeu = "1.25x, 4.80x, 1.05x, 2.10x, 1.35x"

# Consigne stricte pour l'IA
SYSTEM_PROMPT = """
Tu es un expert en probabilités et théorie des jeux. 
Fais une analyse statistique des résultats de jeu fournis. 
Rappelle toujours de manière neutre que chaque tirage est indépendant et que le hasard pur reste imprévisible.
"""

print("Analyse en cours via Gemini...")

try:
    response = ai_client.models.generate_content(
        model='gemini-2.5-flash',
        contents=f"{SYSTEM_PROMPT}\n\nVoici les données à analyser : {donnees_jeu}"
    )
    print("\n=== RAPPORT D'ANALYSE ===")
    print(response.text)
except Exception as e:
    print(f"Une erreur est survenue : {str(e)}")
    
