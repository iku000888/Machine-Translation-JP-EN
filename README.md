# Machine-Translation-JP-EN
Attempt implementing the concept of "tranlsation by analogy".

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
