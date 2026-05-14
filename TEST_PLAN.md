# Testimisplaan

## Test 1: Seleniumi installimise kontroll

**Eesmärk:** Kontrollida, kas Selenium on arvutisse installitud.

**Sammud:**

1. Ava terminal projekti kaustas.
2. Käivita käsk:

```cmd
py -m pip show selenium
```

**Oodatav tulemus:**
Terminal kuvab Seleniumi versiooni ja paketi info.

## Test 2: Programmi käivitamine

**Eesmärk:** Kontrollida, kas Python fail käivitub ilma vigadeta.

**Sammud:**

1. Ava terminal projekti kaustas.
2. Käivita käsk:

```cmd
py google_search.py
```

**Oodatav tulemus:**
Programm küsib kasutajalt otsingupäringut.

## Test 3: Google'i avamine

**Eesmärk:** Kontrollida, kas Selenium avab Google'i veebilehe Chrome brauseris.

**Sammud:**

1. Käivita programm.
2. Sisesta otsingupäring, näiteks:

```text
Python Selenium
```

**Oodatav tulemus:**
Chrome brauser avaneb ja Google'i veebileht laaditakse.

## Test 4: Otsingupäringu sisestamine

**Eesmärk:** Kontrollida, kas programm leiab Google'i otsingukasti ja sisestab sinna teksti.

**Sammud:**

1. Käivita programm.
2. Sisesta otsingupäring:

```text
Selenium WebDriver
```

**Oodatav tulemus:**
Programm sisestab otsingupäringu Google'i otsingukasti.

## Test 5: Otsingu tegemine

**Eesmärk:** Kontrollida, kas Google'i otsing käivitatakse.

**Sammud:**

1. Käivita programm.
2. Sisesta otsingupäring.
3. Oota tulemuste lehe laadimist.

**Oodatav tulemus:**
Google kuvab otsingutulemuste lehe.

## Test 6: Otsingutulemuste kuvamine terminalis

**Eesmärk:** Kontrollida, kas programm kuvab terminalis esimesed otsingutulemused.

**Sammud:**

1. Käivita programm.
2. Sisesta otsingupäring.
3. Vaata terminali väljundit.

**Oodatav tulemus:**
Terminalis kuvatakse kuni 5 esimest otsingutulemust.

## Test 7: Brauseri sulgemine

**Eesmärk:** Kontrollida, kas brauser sulgub programmi lõpus korrektselt.

**Sammud:**

1. Käivita programm.
2. Tee otsing.
3. Kui terminalis kuvatakse tekst `Vajuta Enter, et brauser sulgeda...`, vajuta Enter.

**Oodatav tulemus:**
Chrome brauser sulgub.

Pärast seda peaks projekti kaustas olema:

```text
google_search.py
README.md
requirements.txt
TEST_PLAN.md
```
