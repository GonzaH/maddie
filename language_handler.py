en = {
  "embed_commands": {
    "mot": "mot",
    "playbooks": "playbooks"
  },
  "plain_commands": {
    "helphere": "helphere",
    "lock": "lock",
    "editlabels": "editlabels",
    "potential": "potential",
    "markcondition": "markcondition",
    "clearcondition": "clearcondition",
    "create": "create",
    "settings": "settings",
    "changesettings": "change_settings",
    "language": "language",
    "teamname": "teamname",
    "updatelang": "update_lang",
    "updategm": "update_gm",
    "updateteamname": "update_teamname",
    "createsettings": "create_settings"
  },
  "dice_rolling": {
    "calculation_title": "Calculation",
    "calculation": lambda result1, result2, mod, calc: f"Dice **{result1}** + **{result2}**, Label{mod} **{calc}**",
    "dice": "Dice",
    "label": "Label",
    "result": "Result"
  },
  "description": "Description",
  "moves": {
    "moves": "moves",
    "adult": "adult",
    "non_existent_playbook_intro": "Sorry, I couldn't find that playbook, the available playbooks are:",
    "non_existent_playbook_end": "\nType an exclamation sign and one of the names in lowercase and without the 'The', moves or adult\ne.g.: !beacon, !moves, !adult",
    "moves_plus": {
      "response_header": "**Name - description, keyword, label**\n"
    }
  },
  "playbook_interactions": {
    "fail_preffix": "Oh no, ",
    "already_locked": lambda label_name: f"Oh no, {label_name} is already locked!",
    "is_locked": lambda label_name: f"Oh no, {label_name} is locked, this one can't change!",
    "labels_base": "Your labels are:\n",
    "up": "up",
    "down": "down",
    "value_is_in_border": lambda value, label_name, direction: f"Oh no, with a value of {value}, your {label_name} can't go {direction}! You get a condition!",
    "locked": "[LOCKED]",
    "condition_not_marked": "You don't have any condition marked",
    "youre": "You are:\n",
    "dont": "don't ",
    "condition_status": lambda status: f"Oh, you {status}have that condition marked.",
    "no_character": "I'm sorry but it appears you have no character created",
    "existing_character": "I'm sorry but it appears you already have character created",
    "invalid_condition": lambda condition_name: f"Oh no, {condition_name} is not a valid condition",
    "different_labels": "The labels must be different",
    "congrats_pending_advancements": lambda adv_count: f"Nice, you can now do {adv_count + 1} advancements",
    "congrats_potential": lambda potential: f"Nice, you have {potential + 1} potential marked",
    "no_template": lambda playbook_name: f"It seems I don't have a template for a playbook called {playbook_name}",
    "congrats_on_creation": lambda char, playbook: f"Congratulations {char}, The {playbook} on joining the team!",
    "potential": lambda potential: f"You have {potential} potential marked",
    "congrats_pending_advancements": lambda adv_count: f"You can do {adv_count + 1} advancements"
  },
  "labels": {
    "danger": "danger",
    "freak": "freak",
    "superior": "superior",
    "savior": "savior",
    "mundane": "mundane"
  },
  "inverted_labels": {
    "danger": "danger",
    "freak": "freak",
    "superior": "superior",
    "savior": "savior",
    "mundane": "mundane"
  },
  "conditions": {
    "afraid": "afraid",
    "angry": "angry",
    "guilty": "guilty",
    "hopeless": "hopeless",
    "insecure": "insecure"
  },
  "inverted_conditions": {
    "afraid": "afraid",
    "angry": "angry",
    "guilty": "guilty",
    "hopeless": "hopeless",
    "insecure": "insecure"
  },
  "playbooks": {
    "the": "The",
    "list": ['beacon', 'bull', 'delinquent', 'doomed', 'janus', 'legacy', 'nova', 'outsider', 'protege', 'transformed'],
    "playbooks": "Playbooks",
    "available": "Available Playbooks are - ",
    "playbook_re": r"!mot ([a-z]+)",
    "moment_of_truth": "MOMENT OF TRUTH",
    "this_is_mot": lambda usr: f"This is {usr}'s moment!"
  },
  "configuration": {
    "settings": "Settings\n",
    "language": "Language",
    "teamname": "Team name",
    "customNames": "Custom names",
    "no_file": "This chat doesn't have a configuration file. To create it write the following command:\n!adventure en\nif you wish for it to be in english.\n",
    "existing_settings": "This chat already has a configuration file.",
    "successfull_update": "The update was successfull",
    "successfull_creation": "The configuration file has been created"
  }
}

es = {
  "embed_commands": {
    "mdlv": "mot",
    "libretos": "playbooks"
  },
  "plain_commands": {
    "ayudaaqui": "helphere",
    "bloquear": "lock",
    "editaretiquetas": "editlabels",
    "potencial": "potential",
    "marcarpotencial": "markcondition",
    "borrarcondicion": "clearcondition",
    "crear": "create",
    "config": "settings",
    "cambiarconfig": "change_settings",
    "lenguaje": "language",
    "nombreequipo": "teamname",
    "editarleng": "update_lang",
    "editargm": "update_gm",
    "editarnombre": "update_teamname",
    "crearconfig": "create_settings"
  },
  "dice_rolling": {
    "calculation_title": "Cálculo",
    "calculation": lambda result1, result2, mod, calc: f"Dados **{result1}** + **{result2}**, Etiqueta{mod} **{calc}**",
    "result": "Resultado"
  },
  "description": "Descripción",
  "moves": {
    "moves": "movimientos",
    "movimientos": "moves",
    "adult": "adultos",
    "non_existent_playbook_intro": "Perdón, no pude encontrar ese libreto, los libretos disponibles son:",
    "non_existent_playbook_end": "\nEscribí un signo de exclamación y uno de los libretos en minúscula y sin el 'El', movimientos o adultos\np.ej.: !beacon, !movimientos, !adultos",
    "moves_plus": {
      "response_header": "**Nombre - descripción, accesor, etiqueta**\n"
    }
  },
  "playbook_interactions": {
    "fail_preffix": "Oh no, ",
    "already_locked": lambda label_name: f"Oh no, {label_name} ya está bloqueada!",
    "is_locked": lambda label_name: f"Oh no, {label_name} está bloqueada, no puede ser alterada!",
    "labels_base": "Tus etiquetas son:\n",
    "up": "subir",
    "down": "bajar",
    "value_is_in_border": lambda value, label_name, direction: f"Oh no, con un valor de {value}, tu {label_name} no puede {direction}! Marcá una condición!",
    "locked": "[BLOQUEADA]",
    "condition_not_marked": "Esa condición no está marcada",
    "youre": "Estás:\n",
    "dont": " no",
    "condition_status": lambda status: f"Oh,{status} tenés have that condition marked.",
    "no_character": "Lo siento, pero parece que no tenés ningún personaje creado",
    "existing_character": "Lo siento, pero parece que ya tenés ningún personaje creado",
    "invalid_condition": lambda condition_name: f"Oh no, {condition_name} no es una condición válida",
    "different_labels": "Las etiquedas deben ser diferentes",
    "congrats_pending_advancements": lambda adv_count: f"Genial, ahora podés hacer {adv_count + 1} avances",
    "congrats_potential": lambda potential: f"Genial, tenés {potential + 1} potencial marcado",
    "no_template": lambda playbook_name: f"Parece ser que no tengo una plantilla para un libreto llamado {playbook_name}",
    "congrats_on_creation": lambda char, playbook: f"Felicidades {char}, {playbook} por unirte al equipo!",
    "potential": lambda potential: f"Tenés {potential} potencial marcado",
    "pending_advancements": lambda adv_count: f"Podés hacer {adv_count} avances"
  },
  "labels": {
    "danger": "peligro",
    "freak": "fenómeno",
    "superior": "superior",
    "savior": "salvador",
    "mundane": "mundano"
  },
  "inverted_labels": {
    "peligro": "danger",
    "fenomeno": "freak",
    "superior": "superior",
    "salvador": "savior",
    "mundano": "mundane"
  },
  "conditions": {
    "afraid": "asustado",
    "angry": "enojado",
    "guilty": "culpable",
    "hopeless": "desesperanzado",
    "insecure": "inseguro"
  },
  "inverted_conditions": {
    "asustado": "afraid",
    "enojado": "angry",
    "culpable": "guilty",
    "desesperanzado": "hopeless",
    "inseguro": "insecure"
  },
  "playbooks": {
    "the": "",
    "list": ['emblema', 'toro', 'delincuente', 'condenado', 'jano', 'legado', 'nova', 'extranjero', 'protegido', 'transformado'],
    "playbooks": "Libretos",
    "available": "Los Libretos disponibles son - ",
    "playbook_re": r"!mdlv ([a-z]+)",
    "moment_of_truth": "MOMENTO DE LA VERDAD",
    "this_is_mot": lambda usr: f"Este es el momento de la verdad de {usr}!"
  },
  "configuration": {
    "settings": "Configuración\n",
    "language": "Lenguaje",
    "teamname": "Nombre de equipo",
    "customNames": "Nombres customizados",
    "no_file": "Este chat no tiene archivo de configuración. Para crearlo escribí el siguiente comando:\n!aventura es\nsi querés que esté en español.\n",
    "existing_settings": "Este chat ya tiene archivo de configuración.",
    "successfull_update": "El cambio se hizo con éxito",
    "successfull_creation": "El archivo de configuración ha sido creado"
  }
}


lang_dicts = {
  "en": en,
  "es": es
}


def get_for_all_langs(accessor):
    response = ''

    for lang in lang_dicts:
        response = response + get_translation(lang, accessor)

    return response


def get_translation(lang, accessor):
    key_list = accessor.split('.')
    partial_result = lang_dicts[lang]

    for key in key_list:
        if key not in partial_result:
            return None

        partial_result = partial_result[key]

    return partial_result