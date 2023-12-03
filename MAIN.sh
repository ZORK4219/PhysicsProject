


#ma fonction qui contient l'aide pour l'utilisateur
affiche_help() 
{
    echo "Le premier parametre doit etre le chemin d'où se trouve le fichier"
    echo "Le deuxieme parametre doit etre le pas ENTIER d'intervalle de longeur d'onde (c'est plus elegant comme ça :) )"
    echo "Les valeurs à rentrer c'est le debut et fin d'interval "
    echo "CAPEESH?"
}



#Cette section regarde si l'utilisateur a utilisé une option
#Pour afficher que l'option ou l'aide sans afficher le reste !
has_options=false

for arg in "$@"; do
    if [[ $arg == -[a-z] ]]; then
        has_options=true
        break
    fi
done


#La seule option c'est l'aide -help si tout autre option est
#utilisée le programme renvoie une erreur
if $has_options; then

    while getopts ":h" opt; do #t: to add  an argument 
        case $opt in 
          h ) # Si -h est passé, affiche l'aide
                affiche_help
                ;;
          \? ) # Si une option non valide est passée, 
               echo "Option non valide: -$OPTARG" #il faut mettre :ht pour avoir ça (les deux points permettent d'initaliser OPTARG a l'option fausse)
               exit 1
               ;;
        esac
               
    done
    


else

        cheminfichier=$1
        pas=$2
        separateur=$3
    
    
    # Vérification des valeur passées au script

    #Verifie si le chemin vers le fichier est bon et existe
    #Sinon affiche un message d'erreur et quitte l'aventure
    if [ -f  $cheminfichier ]; then
        echo "OK, le fichier existe."
    else
        echo "Le fichier n'existe pas."
        exit
    fi


    if (( $(echo "$pas > 0" | bc -l) )); then
        if [[ $pas =~ ^[0-9]+$ ]]; then
            echo "OK, le pas est bon."
        else
            echo "Le pas doit etre postif, entier, et plus grand que 0"
            exit
        
        fi
        
    else  
            echo "Le pas doit etre postif, entier, et plus grand que 0"
            exit
        
   fi

   echo "Utilisez -h sans les parametres pour afficher le message d'aide si vous n'avez pas compris" 

   

   read -p "Valeur de la premiere bonre (pas en kilo hein)      "  val1 

   #voir si positive
    if (( $(echo "$val1 > 0" | bc -l) )); then
        echo "OK."
    else
        echo "La valeur n'est pas positive ou elle est égale à zéro."
        exit
   fi


   read -p "La deuxieme s'il vous plait :)        "   val2


   if (( $(echo "$val2 > 0" | bc -l) )); then #comparer un reel
        echo "OK."
    else
        echo "La valeur n'est pas positive ou elle est égale à zéro."
        exit
   fi




   partie_entiere1=$(echo "$val1" | awk -F'.' '{print $1}') #pour prendre la partie entiere
   partie_entiere2=$(echo "$val2" | awk -F'.' '{print $1}')






   if [[ $((partie_entiere2-partie_entiere1)) = $pas ]]; then 

        

         v=$(python3 intensite.py $cheminfichier $pas "$separateur")

        echo TADAAAA
        
        python3 recherche_plot.py "$v" "$val1" "$val2"  # il faut le passer comme un sting complet 
        
    else 
        echo "Respectez le pas s'il vous plait, choisissez deux bornes separées par le pas donné"
    fi
fi







#v=$(python3 i.py $1 $2)



# Utiliser la valeur dans votre script Bash

