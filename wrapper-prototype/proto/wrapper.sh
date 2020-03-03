#NOTICE

# © 2020 The MITRE Corporation
#This software (or technical data) was produced for the U. S. Government under contract SB-1341-14-CQ-0010, and is subject to the Rights in Data-General Clause 52.227-14, Alt. IV (DEC 2007)
#Released under MITRE PRE #18-4297.

#!/bin/bash

# USE THIS TO TEST THE SCRIPT FOR NOW:
# ./wrapper.sh find tst/ -type f -iname "*tst*.txt"


#==================================================
# CHECKS FOR NO ARGS
NOARGS_ERROR=85
if [ -z "$1" ]
    then
    echo "Usage: <tool> <arguments>"
    exit $NOARGS_ERROR
fi


#==================================================
# META INFO - USER INPUT
echo "Enter your name:"
read Prsn
while [[ ! $Prsn =~ ^[A-Za-z]+[\ \t][A-Za-z]+$ ]]; do
    echo "Use a space and only letters:"
    read Prsn
done
echo ""
echo "Enter evidentiary Media Manufacturer:"
read EMan
echo ""
echo "Enter evidentiary Media Serial#:"
read ESer
while [[ ! $ESer =~ ^[0-9]+$ ]]; do
    echo "Use only numbers:"
    read ESer
done
echo ""
echo "Enter evidentiary Media Notes:"
read ENot
echo ""


#==================================================
# META INFO - SYSTEM GENERATED
User=$USER

LgnM="$(last -R "$USER" | head -1 | awk 'END {print $4}')"  #Note /var/log/wtmp does not track year so current year assumed.
LgnM="$(date --date="$(printf "01 %s" "$LgnM")" +"%Y-%m")"
LgnD="$(last -R "$USER" | head -1 | awk 'END {print $5}')"
LgnT="$(last -R "$USER" | head -1 | awk 'END {print $6}')"
LgnZ="$(date | awk '{print $5}')"
LLgn="$LgnM"-"$LgnD"T"$LgnT":00.Z"$(date +%z)"              #LastLogin

BPid=$$
Tool=$1
TLoc="$(which $1)"
Args=$(($# - 1))


#==================================================
# IMPORT MAPPING FOR TOOL BY SEARCHING IN SCRIPT FOLDER FOR <tool_name>.mapping
echo "========================="
echo "Loading CASE mapping..."
MLoc="$(find . -maxdepth 1 -type f -iname "$Tool.mapping")"
if [ -z "$MLoc" ]; then
    echo ""
    echo "Tool mapping not found!"
    echo "Make sure <tool_name>.mapping is in this script's directory."
    exit
fi
MLoc=${MLoc#"./"}
. $MLoc #Note sourcing mappings should always work; scripts spawn new shells.

touch tmp_out.txt
truncate -s 0 tmp_out.txt
cnt=1
for a in $*
do
    if [[ `echo $a | head -c 1` = "-" ]]; then
        # Removes leading dashes.
        Flag=${a#"-"}
        if [[ `echo $Flag | head -c 1` = "-" ]]; then
            Flag=${Flag#"-"}
        fi
        exec 4<&2 # Redirection of stderr to out_err so that 'command not found' error is hidden.
        exec 2>out_err
        if eval $`echo $Flag`; then
            exec 2<&4
            echo ""
            echo "Mapping for flag not found!"
            echo "Flag:" -$Flag
            echo ""
            exit
        fi 

        Case="${!Flag}"
        Next=$(($cnt + 1))
        Valu="${!Next}"
        echo Flag: $Flag
        echo Case: $Case
        echo Valu: $Valu
        # No value for flag.
        if [[ `echo $Valu | head -c 1` = "-" ]]; then
            echo $Case.item_name=$Flag >> tmp_out.txt
            echo $Case.item_value= >> tmp_out.txt
            echo "" >> tmp_out.txt
            continue
            cnt=$(($cnt+1))
        # Value for flag.
        else
            echo $Case.item_name=$Flag >> tmp_out.txt
            echo $Case.item_value=$Valu >> tmp_out.txt
            echo "" >> tmp_out.txt
        fi
    elif [[ $a = *"="* ]]; then
        Flag="${a%=*}"
        Valu="${a#*=}"
        Case="${!Flag}"
#        echo Flag: $Flag
#        echo Case: $Case
#        echo Valu: $Valu
        echo $Case.item_name=$Flag >> tmp_out.txt
        echo $Case.item_value=$Valu >> tmp_out.txt
        echo "" >> tmp_out.txt
#    else
#        echo "Value arg, skipped tmp_out.txt pipe."
    fi
    cnt=$(($cnt+1))
#    echo ""
done


#==================================================
# RUN TOOL
echo "========================="
Secs=$SECONDS
STim=`date '+%Y-%m-%d %H:%M:%S'`
CmdO="$($*)"
echo "${CmdO}"

# EXPORT ARGS AS KEY:VALUE PAIRS TO A TEMP FILE FOR CASE PYTHON API TO USE.
# A MAPPING FILE COULD BE USED TO THEN DETERMINE HOW KEYS MAP TO CASE GLOSSARY.

#for c=$Args
ETim=`date '+%Y-%m-%d %H:%M:%S'`
echo "========================="


#==================================================
# CALCULATE DURATION
Secs=$(($SECONDS - $Secs))
Days="$(( $Secs / $((24 * 3600)) ))"
Left="$(( $Secs % $((24 * 3600)) ))"
Hour="$(( $Left / 3600 ))"
Left="$(( $Left % 3600 ))"
Mins="$(( $Left / 60 ))"
Left="$(( $Left % 60 ))"
Time="$Days:$Hour:$Mins:$Left"


#==================================================
# OUTPUT SETTINGS
echo -e "Tool:          \t"     $Tool
echo -e "User:          \t"     $User
echo -e "Last Login:    \t"     $LLgn
echo -e "Shell PID:     \t"     $BPid
echo -e "Tool Location: \t"     $TLoc
echo -e "Number Args:   \t"     $Args
echo -e "Start Time:    \t"     $STim
echo -e "End Time:      \t"     $ETim
echo -e "Total Duration:\t"     $Time
echo -e "Media Serial#: \t"     $ESer
echo -e "Manufacturer:  \t"     $EMan
echo -e "Media Notes:   \t"     $ENot


#==================================================
# CALL PYTHON TRANSLATOR
# Tool is first, followed by all other Bash-gathered data.
python conv-and-trans/translator.py "core_Tool.name=$Tool" "propbundle_UNIXAccount.accountLogin=$User" "propbundle_UNIXAccount.lastLoginTime=$LLgn" "core_Tool.location=$TLoc" "core_Action.startTime=$STim" "core_Action.endTime=$ETim" "core_Action.duration=$Time" "propbundle_Device.manufacturer=$EMan" "propbundle_Device.serial=$ESer"
