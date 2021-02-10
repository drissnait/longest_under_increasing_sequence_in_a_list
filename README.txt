								PROJET AAVP
								
Pour lancer le programme il faut :
	-se déplacer dans le répertoire /src : "cd src/"
	-lancer le script bash qui lance les programmes avec la commande : "bash launch_program.sh"
	-revenir à la racine du projet avec la commande : "cd .."
		-lancer la commande suivante qui permet de génerer les graphes selon les données collectées : "gnuplot "plot.gp" > plot.png"
	-les graphes sont stockés dans l'image "plot.png"
	
Composition des dossiers :
	- /src : contient les différents codes sources
	- /data : contient les différentes données sur le temps d'éxecution et la mémoire utilisée lors du lancement des programmes dans 		src/
	- plot.gp : script qui génere les graphes avec la commande citée précédement (gnuplot "plot.gp" > plot.png)
	- plot.png : image .png contenant les graphes 
