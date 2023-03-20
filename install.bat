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
@echo		 Ci     (o\_/o)     iO     Uhhh, you will install
@echo		  \      _____      /       VersaDB App,
@echo		    \ ( /------\ ) /       Be patient and enjoy !
@echo		     \  `------'  /
@echo		      \  -___-  /
@echo		       i       i
@echo		       /-_____-\
@echo		     /           \
@echo	           /               \
@echo	          /__i  AC / DC  i__\
@echo		  i ii           i\ \
@timeout /t 5
@cd C:\Users\%username%\Desktop\versadb_tk-main\setup\
@call conda env create -f C:\Users\%username%\Desktop\versadb_tk-main\setup\environment.yml
@cd C:\Users\%username%\Desktop\versadb_tk-main\
@call conda activate versadb_env
python quichante.py
pause
