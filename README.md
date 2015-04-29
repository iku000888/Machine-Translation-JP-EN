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

## Random streams of consciousness
- Maybe things would work better if there is a "fragment" entities between sentences and words.
- English grammer forces words to be separated by spaces. Japanese does not. Trim spaces from EN, or add spaces between JP words?
- Words between different languages are many to many mapping due to synonyms. Perhaps include frequence information or some contextual key(seems complicated)
