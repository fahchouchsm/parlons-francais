#!/usr/bin/env python3
"""A small, colourful B2 French conjugation trainer (standard library only)."""
import os, random, shutil

RESET='\033[0m'; BOLD='\033[1m'; DIM='\033[2m'; CYAN='\033[96m'; BLUE='\033[94m'; GREEN='\033[92m'; YELLOW='\033[93m'; RED='\033[91m'; MAGENTA='\033[95m'; WHITE='\033[97m'
TENSES = {
 '1': ('Présent de l’indicatif', 'maintenant, habitudes, vérités générales'),
 '2': ('Passé composé', 'action terminée et datée'),
 '3': ('Imparfait', 'habitude, description ou action en cours'),
 '4': ('Futur simple', 'projet ou prédiction'),
 '5': ('Conditionnel présent', 'hypothèse, souhait ou conseil'),
 '6': ('Mix des temps', 'les cinq temps en alternance'),
}
MIX_TENSE = 'Mix des temps'
DATA = {
 'Présent de l’indicatif': [
  ('prendre', 'nous', 'prenons', 'Chaque matin, nous prenons le temps de vérifier les informations avant de décider.'),
  ('résoudre', 'tu', 'résous', 'Tu résous les problèmes avec méthode, même quand la situation semble urgente.'),
 ('venir', 'ils', 'viennent', 'Ils viennent régulièrement assister aux conférences organisées par la mairie.'),
 ('savoir', 'je', 'sais', 'Je sais que cette décision aura des conséquences importantes pour l’équipe.'),
  ('convaincre', 'elle', 'convainc', 'Elle convainc ses collègues en présentant des faits vérifiables et nuancés.'),
  ('tenir', 'vous', 'tenez', 'Vous tenez compte des contraintes avant de proposer une solution réaliste.'),
  ('atteindre', 'on', 'atteint', 'On atteint plus facilement ses objectifs quand on mesure régulièrement ses progrès.'),
  ('défendre', 'ils', 'défendent', 'Ils défendent leur point de vue tout en restant ouverts au dialogue.'),
  ('obtenir', 'je', 'obtiens', 'J’obtiens de meilleurs résultats lorsque je planifie chaque étape du travail.'),
  ('conduire', 'elle', 'conduit', 'Elle conduit les négociations avec calme et fermeté.'),
  ('répondre', 'vous', 'répondez', 'Vous répondez aux critiques sans perdre de vue l’objectif principal.'),
  ('offrir', 'on', 'offre', 'On offre davantage de possibilités aux étudiants qui s’investissent.'),
  ('suivre', 'nous', 'suivons', 'Nous suivons l’évolution du dossier grâce à un tableau de bord partagé.'),
  ('reconnaître', 'ils', 'reconnaissent', 'Ils reconnaissent volontiers leurs limites et demandent un avis extérieur.'),
  ('soutenir', 'tu', 'soutiens', 'Tu soutiens cette proposition parce qu’elle répond aux besoins du terrain.'),
  ('s’apercevoir', 'je', 'm’aperçois', 'Je m’aperçois que les détails changent souvent le sens d’un argument.'),
 ],
 'Passé composé': [
  ('réussir', 'elle', 'a réussi', 'Elle a réussi à convaincre le comité grâce à des arguments précis.'),
  ('mettre', 'nous', 'avons mis', 'Nous avons mis en place une solution provisoire en attendant les résultats.'),
  ('venir', 'ils', 'sont venus', 'Ils sont venus malgré la pluie pour soutenir leur quartier.'),
 ('écrire', 'j’', 'ai écrit', 'J’ai écrit au responsable afin de demander une explication détaillée.'),
  ('découvrir', 'nous', 'avons découvert', 'Nous avons découvert une erreur dans le rapport après une vérification approfondie.'),
  ('prendre', 'il', 'a pris', 'Il a pris la parole pour rappeler les enjeux essentiels du débat.'),
  ('naître', 'elles', 'sont nées', 'Elles sont nées dans cette région, mais ont vécu à l’étranger pendant plusieurs années.'),
  ('comprendre', 'vous', 'avez compris', 'Vous avez compris la situation dès que les premiers résultats sont arrivés.'),
  ('prendre', 'elle', 'a pris', 'Elle a pris une décision difficile après avoir consulté toute son équipe.'),
  ('ouvrir', 'ils', 'ont ouvert', 'Ils ont ouvert le débat à des participants qui n’étaient pas d’accord.'),
  ('partir', 'nous', 'sommes partis', 'Nous sommes partis avant l’aube afin d’éviter les embouteillages.'),
  ('lire', 'tu', 'as lu', 'Tu as lu les conditions attentivement avant de signer le contrat.'),
  ('perdre', 'il', 'a perdu', 'Il a perdu confiance après plusieurs promesses non tenues.'),
  ('se rendre', 'elles', 'se sont rendues', 'Elles se sont rendues sur place pour évaluer les dégâts.'),
  ('voir', 'j’', 'ai vu', 'J’ai vu à quel point cette expérience avait changé sa manière de travailler.'),
  ('apprendre', 'vous', 'avez appris', 'Vous avez appris la nouvelle par un collègue qui était présent à la réunion.'),
 ],
 'Imparfait': [
  ('lire', 'vous', 'lisiez', 'À cette époque, vous lisiez beaucoup pour préparer votre concours.'),
  ('être', 'il', 'était', 'Le trajet était long, mais la vue sur la côte compensait largement la fatigue.'),
  ('faire', 'nous', 'faisions', 'Nous faisions souvent le point le vendredi pour améliorer notre organisation.'),
 ('pouvoir', 'je', 'pouvais', 'Je pouvais enfin travailler au calme lorsque les enfants dormaient.'),
  ('croire', 'elle', 'croyait', 'Elle croyait que le projet avancerait plus vite avec des moyens supplémentaires.'),
  ('attendre', 'nous', 'attendions', 'Nous attendions une réponse officielle lorsque la nouvelle est tombée.'),
  ('vivre', 'ils', 'vivaient', 'Ils vivaient modestement, mais ils accordaient beaucoup de valeur à leur liberté.'),
  ('devoir', 'tu', 'devais', 'Tu devais souvent adapter ton discours selon les personnes présentes.'),
  ('sembler', 'cela', 'semblait', 'Cela semblait impossible jusqu’à ce qu’une solution simple apparaisse.'),
  ('pleuvoir', 'il', 'pleuvait', 'Il pleuvait depuis des heures quand le train est finalement arrivé.'),
  ('préparer', 'nous', 'préparions', 'Nous préparions une présentation lorsque le directeur nous a interrompus.'),
  ('connaître', 'elle', 'connaissait', 'Elle connaissait déjà les lieux grâce à plusieurs séjours précédents.'),
  ('vouloir', 'ils', 'voulaient', 'Ils voulaient changer de méthode, mais ils manquaient encore de recul.'),
  ('falloir', 'il', 'fallait', 'Il fallait agir rapidement pour limiter les conséquences de la panne.'),
  ('dire', 'je', 'disais', 'Je disais toujours la même chose : la clarté évite bien des malentendus.'),
  ('grandir', 'vous', 'grandissiez', 'Vous grandissiez dans un environnement où l’on valorisait la curiosité.'),
 ],
 'Futur simple': [
  ('voir', 'tu', 'verras', 'Tu verras rapidement les progrès si tu pratiques un peu chaque jour.'),
  ('devoir', 'nous', 'devrons', 'Nous devrons trouver un compromis acceptable pour toutes les parties.'),
  ('être', 'elle', 'sera', 'Elle sera ravie de présenter son projet devant le jury.'),
 ('envoyer', 'ils', 'enverront', 'Ils enverront le dossier complet avant la fin de la semaine.'),
  ('venir', 'je', 'viendrai', 'Je viendrai vous présenter les résultats dès que l’analyse sera terminée.'),
  ('recevoir', 'vous', 'recevrez', 'Vous recevrez une confirmation automatique après l’enregistrement de votre demande.'),
  ('suffire', 'cela', 'suffira', 'Cela suffira pour lancer la première étape du projet dès lundi.'),
  ('devenir', 'ils', 'deviendront', 'Ils deviendront progressivement autonomes grâce à cet accompagnement.'),
  ('pouvoir', 'elle', 'pourra', 'Elle pourra commencer dès que les autorisations nécessaires seront accordées.'),
  ('faire', 'nous', 'ferons', 'Nous ferons le point sur les résultats au début du mois prochain.'),
  ('savoir', 'tu', 'sauras', 'Tu sauras bientôt si ta candidature a été retenue.'),
  ('tenir', 'je', 'tiendrai', 'Je tiendrai compte de vos remarques dans la prochaine version du document.'),
  ('prendre', 'vous', 'prendrez', 'Vous prendrez connaissance du rapport avant la séance de jeudi.'),
  ('falloir', 'il', 'faudra', 'Il faudra prévoir une marge de sécurité en cas de retard.'),
  ('mourir', 'la tradition', 'mourra', 'La tradition ne mourra pas si les nouvelles générations se l’approprient.'),
  ('courir', 'ils', 'courront', 'Ils courront le risque de perdre leur avantage s’ils attendent trop longtemps.'),
 ],
 'Conditionnel présent': [
  ('pouvoir', 'je', 'pourrais', 'Je pourrais vous aider davantage si vous me donniez un peu plus de contexte.'),
  ('falloir', 'il', 'faudrait', 'Il faudrait vérifier les chiffres avant de tirer une conclusion.'),
  ('vouloir', 'nous', 'voudrions', 'Nous voudrions proposer une alternative plus respectueuse de l’environnement.'),
 ('devoir', 'tu', 'devrais', 'Tu devrais relire ton texte pour corriger les nuances de registre.'),
  ('préférer', 'elle', 'préférerait', 'Elle préférerait reporter la réunion afin de réunir des données plus fiables.'),
  ('accepter', 'nous', 'accepterions', 'Nous accepterions cette proposition si les conditions étaient clairement définies.'),
  ('être', 'vous', 'seriez', 'Vous seriez plus convaincant en illustrant votre argument par un exemple concret.'),
  ('dire', 'ils', 'diraient', 'Ils diraient la vérité s’ils se sentaient réellement écoutés.'),
  ('accompagner', 'je', 'accompagnerais', 'J’accompagnerais volontiers ce changement s’il était mieux expliqué.'),
  ('pouvoir', 'vous', 'pourriez', 'Vous pourriez reformuler votre demande pour éviter toute ambiguïté.'),
  ('falloir', 'il', 'faudrait', 'Il faudrait également consulter les personnes directement concernées.'),
  ('avoir', 'nous', 'aurions', 'Nous aurions davantage de choix si le budget était plus flexible.'),
  ('venir', 'elle', 'viendrait', 'Elle viendrait avec plaisir si son emploi du temps le permettait.'),
  ('prendre', 'tu', 'prendrais', 'Tu prendrais moins de risques en vérifiant cette information à la source.'),
  ('savoir', 'ils', 'sauraient', 'Ils sauraient comment réagir s’ils avaient reçu une formation adaptée.'),
  ('vivre', 'on', 'vivrait', 'On vivrait mieux avec des horaires plus compatibles avec les transports.'),
 ],
}
DATA[MIX_TENSE] = [item for tense, items in DATA.items() if tense != MIX_TENSE for item in items]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def read_input(prompt=''):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        clear()
        print(f'{GREEN}À bientôt — bon courage pour le français !{RESET}')
        raise SystemExit
def pause(): read_input(f'\n{DIM}Entrée : continuer  ·  Ctrl+C : quitter{RESET}')
def normalize_answer(answer):
    return ' '.join(answer.lower().replace('’', "'").split())
def answer_hint(answer):
    words = answer.split()
    return ' '.join(word[0] + '·' * max(1, len(word) - 1) for word in words)
def title(sub=''): 
    clear(); w=min(shutil.get_terminal_size((80,20)).columns, 92); line='━'*w
    print(f'{CYAN}{line}{RESET}\n{BOLD}{YELLOW}   PARLONS FRANÇAIS{RESET}  {DIM}│ Atelier de conjugaison · niveau B2{RESET}')
    if sub: print(f'{DIM}   {sub}{RESET}')
    print(f'{CYAN}{line}{RESET}\n')
def choose_tense():
    print(f'{BOLD}{WHITE}Choisis un temps :{RESET}')
    for k,(name, use) in TENSES.items(): print(f'  {YELLOW}{k}{RESET}  {name:<25} {DIM}{use}{RESET}')
    while True:
        x=read_input(f'\n{CYAN}› {RESET}').strip()
        if x in TENSES: return TENSES[x][0]
        if x.lower() in ('q','0'): return None
        print(f'{RED}Choix invalide. Entre 1 et 6.{RESET}')
def lesson():
    title('Fiches mémo · observe les terminaisons et le contexte')
    tense=choose_tense()
    if not tense:return
    title(tense)
    examples=DATA[tense]
    for verb, pron, form, phrase in examples:
        print(f'{MAGENTA}{verb}{RESET}  ·  {pron} → {BOLD}{GREEN}{form}{RESET}')
        print(f'  {DIM}{phrase}{RESET}\n')
    print(f'{YELLOW}Astuce B2 :{RESET} repère les marqueurs temporels et le registre de la phrase.')
    pause()
def quiz():
    title('Exercices contextualisés · aucune phrase répétée')
    tense=choose_tense()
    if not tense:return
    if tense == MIX_TENSE:
        mixed_pool = [item for name, items in DATA.items()
                      if name != MIX_TENSE for item in items]
        questions = random.sample(mixed_pool, 12)
    else:
        questions = list(DATA[tense])
    random.shuffle(questions); score=0; streak=0; mistakes=[]
    total_questions = len(questions)
    for i,(verb, pron, answer, phrase) in enumerate(questions,1):
        title(f'Exercice  ·  question {i}/{total_questions}  ·  score {score}  ·  série {streak}')
        print(f'{WHITE}Verbe à conjuguer : {BOLD}{verb}{RESET}')
        print(f'{WHITE}Phrase : {phrase.replace(answer, "_____")}{RESET}\n')
        got=read_input(f'{CYAN}› Ta réponse (? : indice · q : quitter) : {RESET}').strip()
        if got == '?':
            print(f'{YELLOW}Indice : {answer_hint(answer)}{RESET}')
            got=read_input(f'{CYAN}› Ta réponse : {RESET}').strip()
        if got.lower() == 'q': return
        if normalize_answer(got) == normalize_answer(answer):
            print(f'{GREEN}✓ Excellent !{RESET}'); score+=1; streak+=1
        else:
            print(f'{RED}✗ Réponse attendue : {BOLD}{answer}{RESET}')
            mistakes.append((verb, phrase, answer)); streak=0
        read_input(f'{DIM}Entrée : question suivante  ·  Ctrl+C : quitter{RESET}')
    title('Résultat')
    pct=score/total_questions
    color=GREEN if pct>=.75 else YELLOW if pct>=.5 else RED
    print(f'{color}{BOLD}   {score}/{total_questions}  ·  {int(pct*100)} %{RESET}')
    print(f'\n{DIM}{"Très solide ! Continue à varier les contextes." if pct>=.75 else "Relis les fiches puis retente le défi : la répétition paie."}{RESET}')
    if mistakes:
        print(f'\n{YELLOW}{BOLD}À revoir ({len(mistakes)}){RESET}')
        for verb, phrase, answer in mistakes:
            print(f'{DIM}• {verb} : {phrase.replace(answer, BOLD + GREEN + answer + RESET)}{RESET}')
    pause()
def phrases():
    title('Banque de phrases · lis à voix haute')
    all_items=[(t,*item) for t,items in DATA.items() if t != MIX_TENSE for item in items]
    random.shuffle(all_items)
    for t,verb,pron,form,phrase in all_items:
        print(f'{YELLOW}{t}{RESET}  {DIM}({verb} · {pron}){RESET}\n  {phrase}\n')
    pause()
def main():
    while True:
        title('Choisis une activité pour progresser')
        print(f'{BOLD}{WHITE}  1  {CYAN}Fiches mémo{RESET}       revoir les formes et les usages')
        print(f'{BOLD}{WHITE}  2  {CYAN}Défi express{RESET}      répondre et recevoir une correction')
        print(f'{BOLD}{WHITE}  3  {CYAN}Banque de phrases{RESET} lire des exemples B2 naturels')
        print(f'{BOLD}{WHITE}  q  {DIM}Quitter{RESET}')
        x=read_input(f'\n{CYAN}› {RESET}').strip().lower()
        if x=='1': lesson()
        elif x=='2': quiz()
        elif x=='3': phrases()
        elif x in ('q','quit','exit'): clear(); print(f'{GREEN}À bientôt — bon courage pour le français !{RESET}'); return
if __name__=='__main__': main()
