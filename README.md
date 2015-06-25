# Machine-Translation-JP-EN
Attempt implementing the concept of "tranlsation by analogy".
Comments, feedbacks and pointers are always welcome.
This is a WIP.
## Design Goals:
- No awareness of grammer
- Symmetry in the logic used; avoid leveraging on things specific to a language, such as English words are separated by spaces while Japanese is not.
- Build a relational mapping of sentence(J)-word(J)-word(E)-sentence(E)
- Avoid Machine Learning for the time being. First focus on the 'simple' logics.
- Aimed accuracy level -> better than nothing

## External Dependencies
- Accessible MySql instance that can create tables
- Python-MySql.connector: https://packages.debian.org/sid/all/python-mysql.connector/download

## Planned Usage:
Deployable data exchange via JSON/SOAP in the future.
i.e. Receive sentence to be translated and send back translated sentence.

## Random streams of consciousness
- Maybe things would work better if there is a "fragment" entities between sentences and words.
- English grammer forces words to be separated by spaces. Japanese does not. Trim spaces from EN, or add spaces between JP words?
- Words between different languages are many to many mapping due to synonyms. Perhaps include frequence information or some contextual key(seems complicated)
- Idea from Betsuyaku: List words by frequency within a document, and type in translation one by one
- Replace parametrically. (No wild card)
