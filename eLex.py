from plex import *

lexicon = Lexicon ([
        ( Str("Strand"), "declare_an_instruction" ),
        ( Str("if"), "conditional" ),
        ( Str("while"), "iterative" ),
        ( Str("("), "begin_condition"),
        ( Str(")"), "end_condition"),
        ( Str("sync"), "ith_before_i+1th"),
        ( Str("async"), "continuous_pop"),
        ( Str("{"), "begin_statement"),
        ( Str("}"), "end_statement"),
        ( Rep1( Any( " \t\n")), IGNORE)
])
  
filename = "TestCode.gat"
f = open(filename, "r")
scanner = Scanner(lexicon, f, filename)
while 1:
    token = scanner.read()
    print token
    if token[0] is None:
        break

