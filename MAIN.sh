


#ma fonction qui contient l'aide pour l'utilisateur
dispaly_help() 
{
    echo "Fist parameter should indicate where's the file example :'\home\Desktop\file.txt'"
    echo "Second parameter should be the step between  wavelength inervals"
    echo "The values to enter are the boundaries of the interval you want to plot"
    echo "CAPEESH?"
}



#This section looks if the command contains options
#To display help and not anything else 
has_options=false

for arg in "$@"; do
    if [[ $arg == -[a-z] ]]; then
        has_options=true
        break
    fi
done


#The only option here is the help, if any other option is used
#It dispalys error message
if $has_options; then

    while getopts ":h" opt; do #t: to add  an argument 
        case $opt in 
          h ) # If -h is used it shows the help function
               dispaly_help
                ;;
          \? ) # If any other option is used it will be invalid 
               echo "Option non valide: -$OPTARG" #should use ":h" to work (les points let OPTARG be initialized to wrong option )
               exit 1
               ;;
        esac
               
    done
    


else

        filelink=$1
        step=$2
        separator=$3
    
    echo "$separator"
    # Vérification des valeur passées au script

    #Verifie si le chemin vers le fichier est bon et existe
    #Sinon affiche un message d'erreur et quitte l'aventure
    if [ -f  $filelink ]; then
        echo "OK, file exists."
    else
        echo "File doesn't exist."
        exit
    fi


    if (( $(echo "$step > 0" | bc -l) )); then
        if [[ $step =~ ^[0-9]+$ ]]; then
            echo "Ok, choosen step is clear"
        else
            echo "Step should be integer greater than 0"
            exit
        
        fi
        
    else  
            echo "Step should be integer greater than 0"
            exit
        
   fi

   echo "Use the -h option without any parameters if you need help " 

   

   read -p " The positive non zero Value of the first boundary (not in kilos :])      "  val1 

   #See if it's positive
    if (( $(echo "$val1 > 0" | bc -l) )); then
        echo "OK."
    else
        echo "The value is negative or equals zero"
        exit
   fi


   read -p "Second one please ! :)        "   val2


   if (( $(echo "$val2 > 0" | bc -l) )); then 
        echo "OK."
    else
        echo "The value is negative or equals zero"
        exit
   fi




   partie_entiere1=$(echo "$val1" | awk -F'.' '{print $1}') #to transfom the value into integer
   partie_entiere2=$(echo "$val2" | awk -F'.' '{print $1}')






   if [[ $((partie_entiere2-partie_entiere1)) = $step ]]; then 

        
         v=$(python3 Intensity.py "$filelink" $step "$separator")
         

        echo TADAAAA
        
        python3 Search_plot.py "$v" "$val1" "$val2"  # "$v" to pass it as a whole string
        
    else 
        echo "Please respect the step and choose values such that the step would be the diffrence of the two"
    fi
fi




