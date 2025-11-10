# guide_data.py
guide_data = {
    "Sprains and Strains": {
        "images": [f"images/sprain{str(i).zfill(2)}.jpg" for i in range(1, 7)],
        "screen": "sprain_guide",
        "key": "Sprains and Strains",
        "question_bg": "images/sprainQuestions.jpg",
        "questions": [
            "Did you hear a “pop” or feel a snap when the injury happened?",
            "Is the area swollen, bruised, or painful to move?",
            "Is the person unable to move the area at all?"
        ],
        "severe_bg": "images/sprainSevere.jpg"
    },
    "Laceration (Cut)": {
        "images": [f"images/laceration{str(i).zfill(2)}.jpg" for i in range(1, 10)],
        "screen": "laceration_guide",
        "key": "Laceration (Cut)",
        "question_bg": "images/lacerationQuestions.jpg",
        "questions": [
            "Is the wound bleeding heavily and not stopping?",
            "Is something stuck in the wound (glass, metal)?",
            "Is the cut deep or very large?"
        ],
        "severe_bg": "images/lacerationSevere.jpg"
    },
    "Bruise / Contusion": {
        "images": [f"images/bruise{str(i).zfill(2)}.jpg" for i in range(1, 7)],
        "screen": "bruise_guide",
        "key": "Bruise / Contusion",
        "question_bg": "images/bruiseQuestions.jpg",
        "questions": [
            "Is there severe pain or swelling in the injured area?",
            "Was the bruise caused by a strong impact to the head, chest, or back?",
            "Does the skin look very dark, purple, or oddly shaped?"
        ],
        "severe_bg": "images/bruiseSevere.jpg"
    },
    "Nosebleeds": {
        "images": [f"images/nosebleed{str(i).zfill(2)}.jpg" for i in range(1, 8)],
        "screen": "nosebleed_guide",
        "key": "Nosebleeds",
        "question_bg": "images/nosebleedQuestions.jpg",
        "questions": [
            "Has the nosebleed lasted more than 20 minutes?",
            "Was the nosebleed caused by a head injury or trauma?",
            "Is the person feeling faint, dizzy, or very weak?"
        ],
        "severe_bg": "images/nosebleedSevere.jpg"
    },
    "Insect Bites": {
        "images": [f"images/insectbite{str(i).zfill(2)}.jpg" for i in range(1, 8)],
        "screen": "insect_bite_guide",
        "key": "Insect Bites or Minor Allergic Reactions",
        "question_bg": "images/insectbiteQuestions.jpg",
        "questions": [
            "Is the person having trouble breathing or swallowing?",
            "Is there swelling on the face, lips, or throat?",
            "Is the person dizzy, confused, or showing signs of fainting?"
        ],
        "severe_bg": "images/insectbiteSevere.jpg"
    },
    "Burns (1st or 2nd)": {
        "images": [f"images/burns{str(i).zfill(2)}.jpg" for i in range(1, 8)],
        "screen": "burns_guide",
        "key": "Burns (1st or 2nd)",
        "question_bg": "images/burnsQuestions.jpg",
        "questions": [
            "Is the burn larger than the size of the person's hand?",
            "Are there open blisters or raw, peeling skin?",
            "Was the burn caused by chemicals or electricity?"
        ],
        "severe_bg": "images/burnsSevere.jpg"
    },
    "Fainting": {
        "images": [f"images/fainting{str(i).zfill(2)}.jpg" for i in range(1, 6)],
        "screen": "fainting_guide",
        "key": "Fainting",
        "question_bg": "images/faintingQuestions.jpg",
        "questions": [
            "Did the person lose consciousness for more than a minute?",
            "Are they breathing abnormally or not at all?",
            "Is there a head injury associated with the faint?"
        ],
        "severe_bg": "images/faintingSevere.jpg"
    },
    "Choking (Partial)": {
        "images": [f"images/choking{str(i).zfill(2)}.jpg" for i in range(1, 6)],
        "screen": "choking_guide",
        "key": "Choking (Partial)",
        "question_bg": "images/chokingQuestions.jpg",
        "questions": [
            "Is the person unable to breathe or speak clearly?",
            "Is their face turning blue or lips discolored?",
            "Is the person becoming unconscious?"
        ],
        "severe_bg": "images/chokingSevere.jpg"
    },
}
