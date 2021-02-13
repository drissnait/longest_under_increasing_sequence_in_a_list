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
	-/resultat_test : contient les resultat des test ou l'on verifie que les listes de sorties de programmes sont strictement croissante, chaque ligne représente une éxecution, la valeur 1 veut dire que le résultat est bon, la valeur 0 montre le contraire, a priori, les resultats sont tous bon, donc dans chacun des 3 fichiers du répertoire (1 fichier par algorithme), nous avons 50 lignes avec la valeur 1 (parce que on lance 50 fois le programme avec le script bash)
	-/Rapport : contient le rapport du projet 
	- plot.gp : script qui génere les graphes avec la commande citée précédement (gnuplot "plot.gp" > plot.png)
	- plot.png : image .png contenant les graphes 
