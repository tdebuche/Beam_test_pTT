import argparse
from pTTs.Programs.pTTs_to_file import record_all_boards
from S1_Input.Programs.record_text import record_input
from Geometry.Programs.plot import plot_layer




Modules = [{'index':0,'Layer":1, 'type':'Silicon', 'u':4,'v':3},{'index':1,'Layer":1, 'type':'Silicon', 'u':4,'v':2},{'index':2,'Layer":1, 'type':'Silicon', 'u':3,'v':2},{'index':3,'Layer":1, 'type':'Silicon', 'u':4,'v':3},{'index':4,'Layer":1, 'type':'Silicon', 'u':4,'v':2},{'index':5,'Layer":1, 'type':'Silicon', 'u':3,'v':2}]


#record pTTs

parser = argparse.ArgumentParser()

#Scenario
parser.add_argument("--STCs",default = 'yes', help="With (yes) or without STCs (no)")
parser.add_argument("--Edges",default = 'no', help="With (yes) or without edges(no)")

#Build and record pTTs
parser.add_argument("--pTTs",default = 'no', help="build and record the pTTs")
parser.add_argument("--Format",default = 'readable', help="textfile : readable, vhfile: vh")

#Plot a layer 
parser.add_argument("--Plot",default = 'no', help="plot a layer")
parser.add_argument("--Layer", default = 1 ,help="Layer to display",type=int)
parser.add_argument("--UV",default = 'no', help="With or without UV")
parser.add_argument("--Bins",default = 'no', help="With or without bins")

#S1_Input
parser.add_argument("--S1_Input",default = 'no', help="run and record the S1 numbering")


args = parser.parse_args()
  
#Build and record files to build pTTs
if args.pTTs == "yes":
  record_S1_board(args,Modules)


#create and record the S1 numbering
if args.S1_Input == "yes":
  record_input(args,Modules)

#plot Layer
if args.Plot == "yes":
  plot_layer(args,args.Layer,Modules)

