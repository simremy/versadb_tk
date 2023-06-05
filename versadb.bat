@echo on
@color 0a
@echo		       .------..
@echo		     -          -
@echo		   /              \
@echo		 /                   \
@echo		/    .--._    .---.   i
@echo		i  /      -__-     \   i
@echo		i i                 i  i
@echo		 ii     .     .      ii
@echo		 ii                ii
@echo		 ii      _   i_      ii
@echo		 Ci     (o\_/o)     iO     Uhhh, you have lauched
@echo		  \      _____      /       VersaDB App,
@echo		    \ ( /------\ ) /       Enjoy !
@echo		     \  `------'  /
@echo		      \  -___-  /
@echo		       i       i
@echo		       /-_____-\
@echo		     /           \
@echo	           /               \
@echo	          /__i  AC / DC  i__\
@echo		  i ii           i\ \
@timeout /t 5
@call conda activate versadb_env
@cd "C:\Users\%username%\Desktop\versadb_tk-master\"
python quichante.py
