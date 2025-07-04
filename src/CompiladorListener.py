# Generated from Compilador.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CompiladorParser import CompiladorParser
else:
    from CompiladorParser import CompiladorParser

# This class defines a complete listener for a parse tree produced by CompiladorParser.
class CompiladorListener(ParseTreeListener):

    # Enter a parse tree produced by CompiladorParser#prog.
    def enterProg(self, ctx:CompiladorParser.ProgContext):
        pass

    # Exit a parse tree produced by CompiladorParser#prog.
    def exitProg(self, ctx:CompiladorParser.ProgContext):
        pass


    # Enter a parse tree produced by CompiladorParser#com.
    def enterCom(self, ctx:CompiladorParser.ComContext):
        pass

    # Exit a parse tree produced by CompiladorParser#com.
    def exitCom(self, ctx:CompiladorParser.ComContext):
        pass



del CompiladorParser