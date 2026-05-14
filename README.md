# 3.2 Seleniumiga Google.com testimine

See projekt kasutab Pythonit ja Seleniumi, et automatiseerida Google'i otsingut Chrome brauseris.

## Projekti eesmärk

Programmi eesmärk on avada Google'i avaleht, sisestada kasutaja antud otsingupäring ja kuvada terminalis kuni 5 esimest otsingutulemust.

## Kasutatud tehnoloogiad

- Python
- Selenium
- Google Chrome
- Selenium WebDriver

## Projekti failid

- `google_search.py` - põhiprogramm Google'i otsingu automatiseerimiseks
- `requirements.txt` - projekti sõltuvused
- `TEST_PLAN.md` - testimisplaan programmi kontrollimiseks
- `README.md` - projekti kirjeldus ja juhised

## Paigaldamine

Python peab olema arvutisse installitud.

Installi vajalik sõltuvus:

```cmd
py -m pip install -r requirements.txt
```

Või installi Selenium eraldi:

```cmd
py -m pip install selenium
```

## Programmi käivitamine

Käivita projektikaustas:

```cmd
py google_search.py
```

Programm küsib otsingupäringut. Pärast päringu sisestamist avab Selenium Chrome brauseri, teeb Google'i otsingu ja kuvab terminalis leitud tulemused.

## Testimine

Testimisplaan asub failis `TEST_PLAN.md`.

Seal on kirjeldatud kontrollid Seleniumi installimise, programmi käivitamise, Google'i avamise, otsingu tegemise, tulemuste kuvamise ja brauseri sulgemise kohta.
