#!/usr/bin/env python3
"""

    Ensk.is - Free and open English-Icelandic dictionary

    Copyright (c) 2023, Sveinbjorn Thordarson <sveinbjorn@sveinbjorn.org>
    All rights reserved.

    Redistribution and use in source and binary forms, with or without modification,
    are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, this
    list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright notice, this
    list of conditions and the following disclaimer in the documentation and/or other
    materials provided with the distribution.

    3. Neither the name of the copyright holder nor the names of its contributors may
    be used to endorse or promote products derived from this software without specific
    prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
    IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
    INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
    NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
    PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
    WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGE.


    Find phonetic IPA spelling for words in the dictionary that don't have any.


"""

import subprocess

from db import EnskDatabase
from util import is_ascii

SKIP = frozenset(
    (
        "barcode",
        "box-office",
        "roleplay",
        "anarcho-capitalism",
        "anarcho-capitalist",
        "animalistic",
        "Aruba",
        "bibliographer",
        "biodome",
        "bioengineer",
        "blowjob",
        "coedit",
        "cretinism",
        "cromulent",
        "encave",
        "endogamous",
        "gangbang",
        "geoheliocentrism",
        "Guadeloupe",
        "Guam",
        "guestbook",
        "hagiographer",
        "hagiographical",
        "haitch",
        "hierophantic",
        "honkey",
        "honkie",
        "immunocompromisation",
        "immunodeficient",
        "inswathe",
        "isomorphism",
        "katana",
        "Martinique",
        "Mayotte",
        "mediascape",
        "megacorporation",
        "neo-nazi",
        "neo-nazism",
        "neurochemical",
        "neurodegeneration",
        "newswire",
        "newswoman",
        "paleolithic",
        "querulant",
        "seeress",
        "seneschal",
        "sociobiology",
        "spectrography",
        "starship",
        "Svalbard",
        "telepath",
        "tergum",
        "thermophile",
        "thermophilic",
        "timbal",
        "Timor-Leste",
        "Tokelau",
        "volcanological",
        "wishlist",
        "wyvern",
        "xenolith",
        "zombify",
        "zoophilia",
        "facticity",
        "fibrillate",
        "monotonal",
        "sado-masochism",
        "tesseract",
        "Gaea",
        "Gaia",
        "gyrocopter",
        "Babylon",
        "vice-regent",
        "xenomorph",
        "gladius",
        "jotun",
        "kobold",
        "longsword",
        "metaphilosophy",
        "spadroon",
        "theogony",
        "Aristotelian",
        "Aristotelianism",
        "auxesis",
        "Beelzebub",
        "Czechoslovakia",
        "sociopathy",
        "Yugoslavic",
        "cozener",
        "disjection",
        "thorough-paced",
        "white-ear",
        "gnoll",
        "synonymicon",
        "ghast",
        "Pegasus",
        "teleprocessing",
        "treant",
        "lich",
        "xeno-",
        "arquebus",
        "IRC",
        "prementioned",
        "boobie",
        "criminological",
        "Kiev",
        "Lombardy",
        "Oceanian",
        "phonographer",
        "praeter-",
        "preter-",
        "pilum",
        "calisthenic",
        "civilizational",
        "doobie",
        "pedophile",
        "pedophilia",
        "colotomy",
        "scientism",
        "scientistic",
        "Babylonian",
        "config",
        "California",
        "Kyiv",
        "battlecruiser",
        "postcolonialism",
        "APC",
        "Canaan",
        "man-o'-war",
        "quadrireme",
        "quinquereme",
        "handjob",
        "nunchucks",
        "Siam",
        "paleontological",
        "paleontologist",
        "paleontology",
        "lictor",
        "sarabande",
        "chitinous",
        "asthenia",
        "phthalimide",
        "piezo",
        "trichromatic",
        "voidability",
        "allergenicity",
        "biophysicist",
        "deckhouse",
        "overdosage",
        "recursiveness",
        "toxicodynamics",
        "Copt",
        "neurochemistry",
        "nonracial",
        "otoscopy",
        "recyclability",
        "redesignate",
        "toxigenic",
        "taxidermic",
        "anhedonic",
        "dysphoric",
        "megacorp",
        "epistemologically",
        "Cartesianism",
        "unsystematic",
        "homebrew",
        "phenomenological",
        "relativistic",
        "weltanschauung",
        "weltschmerz",
        "well-known",
        "angst-ridden",
        "biometry",
        "biostatistics",
        "kilocalorie",
        "militarize",
        "remilitarize",
        "self-hatred",
        "afterword",
        "all-powerful",
        "biostatistical",
        "felicific",
        "law-giver",
        "malform",
        "monarchism",
        "theocrat",
        "unenlightening",
        "left-wing",
        "right-wing",
        "obstipation",
        "monoglot",
        "monist",
        "pacifistic",
        "epicurism",
        "remilitarization",
        "vampiric",
        "vampirish",
        "Prussia",
        "pseudocrater",
        "Shetlands",
        "Valhalla",
        "circumlunar",
        "nonreligious",
        "suburbanization",
        "neuropsychological",
        "neuropsychologist",
        "lightbulb",
        "footsoldier",
        "goldworker",
        "graverobber",
        "horsemeat",
        "uncorrupt",
        "unsayable",
        "crossbowman",
        "anti-democratic",
        "counter-offensive",
        "retroactivity",
        "slaveholder",
        "Rhodesia",
        "Esperantism",
        "Esperantist",
        "parentless",
        "railcar",
        "bason",
        "Carthage",
        "Crete",
        "Danube",
        "provisionary",
        "pseudoscientific",
        "Sicily",
        "cellphone",
        "homeownership",
        "neuroanatomy",
        "neurobiological",
        "neurobiologist",
        "neurobiology",
        "shieldbearer",
        "Abyssinia",
        "Abyssinian",
        "businesspeople",
        "Homeric",
        "orthopedia",
        "Vulgate",
        "patricidal",
        "bicameralism",
        "gynecocracy",
        "sociobiological",
        "sociobiologist",
        "tug-of-war",
        "ultranationalism",
        "ultranationalist",
        "diabolist",
        "latinize",
        "multinationalism",
        "Trinitarian",
        "Trinitarianism",
        "autocratism",
        "appeasable",
        "evangelizer",
        "extralegal",
        "lobbyism",
        "obsequiously",
        "polyphonous",
        "taxonomist",
        "teaset",
        "unappeasable",
        "Achilles",
        "cryptonym",
        "co-founder",
        "Stalinism",
        "thanatology",
        "unideological",
        "gynocentric",
        "autophagia",
        "necropsy",
        "nectarivore",
        "maximizer",
        "game-theoretic",
        "pseudoscientist",
        "unheroically",
        "uninterpretable",
        "overgeneralization",
        "prenup",
        "ultraviolent",
        "belltower",
        "euphoniousness",
        "sellsword",
        "grandkid",
        "gynocracy",
        "matronym",
        "patronym",
        "gerontocracy",
        "artilleryman",
        "earmuff",
        "impecuniosity",
        "knightliness",
        "multilingualism",
        "sunbeaten",
        "cataphract",
        "meagerness",
        "Platonist",
        "frugivore",
        "frugivorous",
        "piscivore",
        "trapezoidal",
        "nectarivorous",
        "microstate",
        "patriarchical",
        "cordwood",
        "kilotonne",
        "multistory",
        "Eurasia",
        "Sinophone",
        "unfalsifiable",
        "unembarrassed",
        "untruthfulness",
        "Byzantium",
        "Manchuria",
        "Manchurian",
        "graphemic",
        "Europeanization",
        "Europeanize",
        "czarism",
        "somnambulator",
        "tsarism",
        "hornlike",
        "Newfoundland",
        "optometer",
        "self-governance",
        "glassmaker",
        "glassmaking",
        "bunkmate",
        "ever-growing",
        "goldsmithery",
        "goldsmithing",
        "reformism",
        "suburbanize",
        "Nile",
        "Egyptology",
        "oceanographical",
        "oceanographically",
        "phrenological",
        "unpretentiousness",
        "denigratory",
        "geothermally",
        "brutishness",
        "polyarchy",
        "polycracy",
        "Nubian",
        "presuppositional",
        "asphyxiant",
        "dehumanization",
        "Hegelian",
        "ratfish",
        "tarasque",
        "experimentee",
        "demersal",
        "filicide",
        "adsorber",
        "agronomic",
        "agronomics",
        "ahistorical",
        "Anglophobe",
        "Anglophobia",
        "Anglophobic",
        "Anglosphere",
        "antialiasing",
        "autodidacticism",
        "bacalao",
        "Bayesian",
        "binational",
        "bioinformatics",
        "bloodlust",
        "candlefish",
        "Canterbury",
        "cenobite",
        "cenobitism",
        "cisalpine",
        "consequentialism",
        "consequentialist",
        "counter-example",
        "cropland",
        "decolonialization",
        "decolonialize",
        "deistic",
        "Deuteronomy",
        "documentarian",
        "eschatological",
        "financialization",
        "fluorosis",
        "Francophile",
        "Gallophile",
        "geoheliocentric",
        "gravesite",
        "leatherwork",
        "leatherworker",
        "leatherworking",
        "maneuverability",
        "megajoule",
        "melioidosis",
        "monophonic",
        "morphogenesis",
        "nazification",
        "neofascism",
        "neofascist",
        "nonhereditary",
        "pathogenicity",
        "phlogiston",
        "physiocrat",
        "postmodernistic",
        "power-hungry",
        "professoriate",
        "pseudorandom",
        "pseudoscalar",
        "quasiparticle",
        "realtime",
        "renascence",
        "smegma",
        "subdiscipline",
        "superconductive",
        "syncratic",
        "tech-savvy",
        "unorthodoxy",
        "uploadable",
        "weaponization",
        "automatable",
        "dreadlock",
        "Anglophilia",
        "pneumonitis",
        "subdermal",
        "Neoplatonic",
        "Neoplatonism",
        "Neoplatonist",
        "ouroboros",
        "ouroborosian",
        "Plato",
        "Helios",
        "geoposition",
        "self-examination",
        "unpersuasive",
    )
)


entries = EnskDatabase().read_all_additions()

no_ipa = [e["word"] for e in entries if e["ipa_uk"] == ""]
not_ascii = [e for e in no_ipa if not is_ascii(e)]
with_whitespace = [e for e in no_ipa if " " in e]
not_ignored = [
    e
    for e in no_ipa
    if e not in SKIP and e not in not_ascii and e not in with_whitespace
]

print(f"Num w. no IPA: {len(no_ipa)}")
print(f"Ignoring {len(not_ascii)} non-ASCII words")
print(f"Ignoring {len(SKIP)} whitelisted words")
print(f"Ignoring {len(with_whitespace)} words with whitespace")
print(f"Fetching IPA for {not_ignored}")

for e in no_ipa:
    if " " in e or e in SKIP or not is_ascii(e):
        continue

    # print(f"Checking {e}")
    try:
        out = subprocess.check_output(["ruby", "ipa-cambridge.rb", e])
        out = out.decode().strip()
    except Exception:
        continue

    if not out:
        print(f'SKIP: "{e}",')
        continue
    comp = out.split("\n")
    c = comp[0]

    s = c.split(" ")
    if len(s) > 1:
        c = s[-1]

    print(f'"{e}": "{str(c)}",')
