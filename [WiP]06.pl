member(X,[X|_]).
member(X,[_|T]):- member(X,T).

contains_duplicates2([]):- false.
contains_duplicates2([X|T]):- member(X,T); contains_duplicates2(T).

has_4unique_characters([X1,X2,X3,X4|_],_):- not(contains_duplicates2([X1,X2,X3,X4])), ! .
has_4unique_characters([_,X2,X3,X4|T],Y):- Y1 is Y+1,has_4unique_characters([X2,X3,X4|T],Y1), Y is 5.

foo(X,Y):- string_chars(X,X_SPLIT), has_4unique_characters(X_SPLIT,Y).
