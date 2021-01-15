# Assignment 2 - IN4110 - H20 - UiO
# Exercise 2.2 and 2.3
# Author: Fábio Rodrigues Pereira - fabior@uio.no

function _help() {
    echo ""
    echo "This is a simple function to track activity time."
    echo ""
    echo "option:   --help    # shows this help list"
    echo "option:   --start   # starts a new tracking"
    echo "option:   --stop    # stops a tracking"
    echo "option:   --status  # shows the activity status"
    echo "option:   --log     # shows the time log of a tracking"
    echo ""
}


function _convert_time() {
    START_f=$(date -j -f "%b %d %H:%M:%S %Z %Y" "$START" '+%s')
    END_f=$(date -j -f "%b %d %H:%M:%S %Z %Y" "$END" '+%s')
    diff=$(($END_f - $START_f))
    hour=$((diff/3600))
    min=$(((diff%3600)/60))
    sec=$(((diff%3600)%60))
    echo "Task $LABEL: $hour:$min:$sec"
}


function track() {
    LOGFILE="./LOGFILE.txt"

    if [ ! -f $LOGFILE ]; then
        touch $LOGFILE
    fi

    LOGFILE_last_line=$(tail -1 $LOGFILE)

    # Return help option if no commandline argument is given:
    if [ $# -eq 0 ]; then
        _help

    else

        case "$1" in

            -h|-help|--help)
                _help
                ;;

            -start|--start)
                if [ ${#LOGFILE_last_line} -gt 0 ]; then
                    echo "Error: There is already a task running..."
                    echo "Please, stop the task before start a new one."
                    echo "use track --stop"

                elif [ ${#2} -eq 0 ]; then
                    echo "Starting a new tracking session..."
                    echo "Please, give a LABEL for this tracking session:"
                    read name

                    echo "START $(date)" >> $LOGFILE
                    echo "LABEL This is task $name" >> $LOGFILE
                    echo "Tracking task $name..."

                else
                    echo "Starting a new tracking session..."
                    echo "START $(date)" >> $LOGFILE
                    echo "LABEL This is task $2." >> $LOGFILE
                    echo "Tracking task $2..."
                fi
                ;;

            -stop|--stop)
                if [ ${#LOGFILE_last_line} -eq 0 ]; then
                    echo "Error: There isn't a task running..."
                    echo "Please, start a task before stop."
                    echo "use track --start"

                else
                    echo "Stopping a tracking session..."
                    echo "END $(date)" >> $LOGFILE
                    echo "" >> $LOGFILE
                    echo "Tracking stoped!"
                fi
                ;;

            -s|-status|--status)
                if [ ${#LOGFILE_last_line} -gt 0 ]; then
                    echo ""
                    tail -3 $LOGFILE
                    echo "END: Not ended yet..."
                    echo ""
                else
                    echo ""
                    tail -4 $LOGFILE
                fi
                ;;

            -l|-log|--log)
                length=$(grep -c "START" $LOGFILE)
                for ((i=1;i<=$length;i++)); do

                    START=$(grep -w "START" $LOGFILE | cut -d " " -f 3- | sed -n "$i p")
                    LABEL=$(grep -w "LABEL" $LOGFILE | cut -d " " -f 5 | sed -n "$i p")
                    END=$(grep -w "END" $LOGFILE | cut -d " " -f 3- | sed -n "$i p")

                    if [ ${#END} -gt 0 ]; then
                        _convert_time
                    
                    # Print the session elapse eventhough the last session is still running:
                    else
                        END=$(date +"%b %d %H:%M:%S %Z %Y")
                        _convert_time
                        echo "* This task session is still running..."
                    fi
                done
                ;;
        esac
    fi
}

