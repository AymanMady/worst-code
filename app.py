from flask import Flask, render_template, request,render_template_string
import numpy as np
import time
import threading

app = Flask(__name__)

# La fonction taille_de_stache que vous souhaitez tester
def q14(matroustache_reelle):
    matroustache = matroustache_reelle[:]
    for i in range(len(matroustache)):
        max_length = 0
        for j in range(len(matroustache[i])):
            if matroustache[i][j] > max_length:
                max_length = matroustache[i][j]
            if matroustache[i][j] < max_length:
                max_length = max_length
            if matroustache[i][j] == 10:
                max_length += 1
        for j in range(len(matroustache[i])):
            matroustache[i][j] = max_length
        for k in range(100000):
            pass  # Boucle vide pour augmenter la complexité
    return matroustache

@app.route("/q14", methods=["GET", "POST"])
def q14():
    if request.method == "POST":
        # Récupérer la matrice envoyée par le formulaire
        matroustache_reelle = []
        for i in range(6):
            row = [int(request.form[f"poil_{i}_{j}"]) for j in range(10)]
            matroustache_reelle.append(row)
        
        # Appliquer la fonction sur la matrice
        matroustache_taille = taille_de_stache(matroustache_reelle)
        
        # Renvoyer la matrice taillée au template
        return render_template("index.html", matroustache=matroustache_taille, input_matrix=matroustache_reelle)
    
    return render_template("index.html", matroustache=None)
def wait13():
    start_time = time.time()
    
    def countdown():
        countdown_time = 13
        while countdown_time > 0:
            print(f"{countdown_time} secondes restantes...")
            countdown_time -= 1
            time.sleep(1)
        print("Attente terminée !")

    thread = threading.Thread(target=countdown)
    thread.start()

    while time.time() - start_time < 13:
        for _ in range(10000000):  # Boucle inutile
            pass  # Rien à faire ici

    time.sleep(0.0001)  # Petit délai pour être vraiment sûr
    print("Fini!")

@app.route('/q13')
def q13():
    wait13()
    return render_template('ep13.html', message="13 secondes d'attente sont écoulées !")
def compteur_de_mails_prioritaires(prioritaires, expediteurs):
    compteur = 0
    for prioritaire in prioritaires:
        for expediteur in expediteurs:
            if prioritaire[::-1][::-1] == expediteur[::-1][::-1]:
                compteur += len(prioritaire) % len(expediteur) or 1
                break
    return compteur


@app.route('/q12', methods=['GET', 'POST'])
def q12():
    if request.method == 'POST':
        prioritaires = request.form['prioritaires'].split('\n')
        expediteurs = request.form['expediteurs'].split('\n')
        resultat = compteur_de_mails_prioritaires(prioritaires, expediteurs)
        return render_template('q12.html', resultat=resultat)
    return render_template('q12.html')
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MOVAI CODE</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Faire monter Tom Cruise avec Flask & Bootstrap</h1>
        <form method="POST" action="/q11" class="mt-4">
            <div class="mb-3">
                <label for="phrase" class="form-label">Entrez votre phrase :</label>
                <input type="text" name="phrase" class="form-control" id="phrase" placeholder="Exemple: Tom Cruise marche marche marche">
            </div>
            <button type="submit" class="btn btn-primary">Déplacer Tom Cruise</button>
        </form>
        {% if result %}
        <div class="alert alert-success mt-4">
            <strong>Résultat :</strong> {{ result }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

def deplacer_premier_mot(phrase):
    """Déplace le premier mot au bout de la phrase, en mode over-engineered."""
    if not phrase or len(phrase.split()) < 2:
        return phrase  # On ne fait rien, c'est trop simple
    mots = phrase.split()
    # Processus inutilement complexe
    premier_mot = mots.pop(0)  # On retire le premier mot
    mots.append(premier_mot)  # On le remet à la fin
    # On ajoute un traitement ridicule
    return " ".join(mots) + " 🚀"

@app.route("/q11", methods=["GET", "POST"])
def q11():
    result = None
    if request.method == "POST":
        phrase = request.form.get("phrase", "")
        result = deplacer_premier_mot(phrase)
    return render_template_string(TEMPLATE, result=result)
TEMPLATE15 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>La fête à Sylvestre</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">MOVAI CODE : La fête à Sylvestre</h1>
        <p class="text-center">Donnez un texte, et Sylvestre s'occupera de distribuer des coups de poing !</p>
        <form method="POST" action="/q15" class="mt-4">
            <div class="mb-3">
                <label for="texte" class="form-label">Texte :</label>
                <textarea name="texte" class="form-control" id="texte" rows="5" placeholder="Entrez votre texte ici..."></textarea>
            </div>
            <button type="submit" class="btn btn-danger">Envoyer les coups de poing 🥊</button>
        </form>
        {% if result %}
        <div class="alert alert-success mt-4">
            <h2>Résultat :</h2>
            <p>{{ result }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

def distribuer_des_coups_de_poing(texte):
    """
    Transforme le texte en remplaçant certains caractères par des expressions.
    """
    # Une approche inutilement complexe avec une table de correspondance
    mapping = {
        'p': 'poing',
        '.': 'deuxpoings',
        ';': 'poingvirgule',
        ':': 'deuxpoings'
    }

    # Initialisation inutilement complexe
    resultat = ""
    
    # On parcourt caractère par caractère
    for char in texte:
        if char in mapping:
            resultat += mapping[char]
        else:
            resultat += char  # On ajoute les caractères sans remplacement
    
    return resultat  # Retourne le texte modifié

@app.route("/q15", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        # On récupère le texte depuis le formulaire
        texte = request.form.get("texte", "")
        # On applique la fonction inutilement complexe
        result = distribuer_des_coups_de_poing(texte)
    return render_template_string(TEMPLATE15, result=result)
if __name__ == "__main__":
    app.run(debug=True)
