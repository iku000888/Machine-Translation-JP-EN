# Machine-Translation-JP-EN
Attempt implementing the concept of "tranlsation by analogy".
Comments, feedbacks and pointers are always welcome.

## Design Goals:
- No awareness of grammer
- Symmetry 
- Build a relational mapping of sentence(J)-word(J)-word(E)-sentence(E)
- Aimed accuracy level -> better than nothing

## Functionalities to support
- Teach sentence pair
- Teach word pair
- Import/export accumulated JP-EN mapping
- Edit JP-EN mapping to manually filter incorrect knowledge.
- Translate sentence
- Train translate -> Attempt translation, receive human feedback, and learn something from it.

## Usage
On the terminal:
- python main.py learn-word <English Word> <Japanese Word>
- python main.py learn-sentence <English Sentence> <Japanese Sentence>
- python main.py import-words <CSV with word pairs>
- python main.py import-sentences <Text file with sentence pairs>
- python main.py translate-word <direction> <word>
- python main.py export-words <csv destination>
- python main.py export-sentences <txt file destination>
- python main.py build-sentence-word-mp
  

## Random streams of consciousness
- Maybe things would work better if there is a "fragment" entities between sentences and words.
- English grammer forces words to be separated by spaces. Japanese does not. Trim spaces from EN, or add spaces between JP words?
- Words between different languages are many to many mapping due to synonyms. Perhaps include frequence information or some contextual key(seems complicated)
- Idea from Betsuyaku: List words by frequency within a document, and type in translation one by one
- Replace parametrically. (No wild card)
