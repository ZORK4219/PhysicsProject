


#ma fonction qui contient l'aide pour l'utilisateur
dispaly_help() 
{
    echo "* Fist parameter should indicate where's the file example :'\home\Desktop\file.txt'"
    echo "* Second parameter should be the step between  wavelength inervals "
    echo "   and if you want some good graphs and exact results use a small step (1 is recommanded) "
    echo "* The values to enter are the boundaries of the interval you want to plot"
    echo "* Verify please that your separator doesn't contain any letters, or that it's a comma if you have real values"
    echo "CAPEESH?"
}



is_positive_integer() 
{   re='^[0-9]+$'
    if [[ $1 =~ $re ]] && [ $1 -gt 0 ]; then
        echo "The number is a positive integer greater than zero."
    else
        echo "The input is not a positive integer greater than zero."
        exit
    fi
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
    echo -e "Use the -h option without any parameters if you need help\n"
        filelink=$1
        step=$2
        
    
    # PARAMETER VERIFICATION

    #if the file exists else everthing's done 
    if [ ! -z  $filelink ]; then

        if [ -f  $filelink ]; then

            if [ -s $filelink ]; then
                echo "File exists and it's not empty."
            else 
                echo "File exists but it's empty."
            fi
        else
            echo "File doesn't exist."
            exit
        fi

            is_positive_integer $step
    else
        echo "You didn't give me the link to the file"
        exit
    fi   
  

    read -p "Does you file have more than two columns  "    answer
    case $answer in
    "yes" | "YES" | "Yes" ) 
         
        read -p "First column (x axes) " column1
        is_positive_integer $column1
        read -p "Second column  (y axes)"   column2
        is_positive_integer $column2

           
        
        
        # Add your code here for this condition
        ;;
    "no" | "NO" | "No" ) 
         column1="1"
         column2="2"
        ;;
    *)
        echo "It's a yes no question dummy"
        exit
        ;;
    esac
   


    v=$(python3 Intensity.py "$filelink" $step "$column1" "$column2")
         
          if [[ $v = "error1" ]];then
            echo  "Your separator might be imbigiuous"
            exit

          elif [[ $v = "error2" ]];then
            echo  "Choose one seperator, you're making my code ill"
            exit
          elif [[ $v = "error3" ]];then
            echo  -e "\nOPS! I think you should check your file because the given columns do not exist"
            exit
          fi
          
   

    read -p  "OK now give me the positive non zero Value of the first boundary (not in kilos :])      "  boundary1 

   #See if it's positive
    if (( $(echo "$boundary1 > 0" | bc -l) )); then
    #Using bc command which is like a calculator having some similarities 
    #with C programming language, using -l we can define the standard math library
    #with which we can use some basic math stuff
        echo "OK."
    else
        echo "The value is negative or equals zero"
        exit
   fi


   read -p "Second one please ! :)        "   boundary2


   if (( $(echo "$boundary2 > 0" | bc -l) )); then 
        echo "OK."
    else
        echo "The value is negative or equals zero"
        exit
   fi




   

        if (( $(echo "$boundary1 > $boundary2"| bc -l)));then #in case the user enters the first value bigger than the other second one
            temporary=$boundary1
            boundary1=$boundary2
            boundary2=$temporary
        fi
        
        echo TADAAAA
        
        python3 Search_plot.py "$v" "$boundary1" "$boundary2"  # "$v" to pass it as a whole string
        
    
fi




