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
@echo		 Ci     (o\_/o)     iO     Uhhh, you will 
@echo		  \      _____      /       delete all
@echo		    \ ( /------\ ) /       the VersaDB App...
@echo		     \  `------'  /
@echo		      \  -___-  /
@echo		       i       i
@echo		       /-_____-\
@echo		     /           \
@echo	           /               \
@echo	          /__i  AC / DC  i__\
@echo		  i ii           i\ \
@timeout /t 5
@cd C:\Users\%username%\Desktop\versadb_tk-master\log\
@del *.txt

@cd C:\Users\%username%\Desktop\versadb_tk-master\LOTUS_DB_input\
@del *.txt
@del *.tsv

@cd C:\Users\%username%\Desktop\versadb_tk-master\NMRShift\
@del *predictSdf.bat
@del *.txt

@cd C:\Users\%username%\Desktop\versadb_tk-master\setup\
@del *.txt

@cd C:\Users\%username%\Desktop\versadb_tk-master\sunburst\
@del *.html

@call conda env remove -n versadb_env
@call conda env remove -n my-rdkit-env-lotus

set /p var=<C:\Users\%username%\Desktop\versadb_tk-master\CFM_ID_4\ID_container_cfmid.txt
@echo %var%
@call docker image rm -f wishartlab/cfmid:4.2.6.0
@call docker container rm -f %var%

@cd C:\Users\%username%\Desktop\versadb_tk-master\CFM_ID_4\
@del *.txt

pause

