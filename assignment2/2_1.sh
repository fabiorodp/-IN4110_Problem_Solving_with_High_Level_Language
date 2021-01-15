# Assignment 2 - IN4110 - UiO
# Exercise 2.1 + EXTRAS
# Author: Fábio Rodrigues Pereira - fabior@uio.no

# Assign commandlines to variables:
src=$1
dst=$2
ext=$3
length=$#

function _move () {
    if [ $ext == "all" ]; then
        echo "Question: Move all files and directories? y/n"
        read response

        if [ $response == "y" ]; then
            echo "Moving all files and directories from $src to $dst."
            # Loop through all files and directories in the src directory and move them to dst:
            for file in "$src/*"; do mv -v $file $dst; done

        elif [ $response == "n" ]; then
            echo "Question: Move only files? y: for only files or n: for only directories."
            read response1
            if [ $response1 == "y" ]; then 
                # Loop through all files in the src directory and move them to dst:
                echo "Moving only files from $src to $dst."
                find "$src/" -maxdepth 1 -type f -exec mv {} $dst \;
            
            elif [ $response1 == "n" ]; then 
                echo "Moving only directories from $src to $dst."
                for file in "$src/*/"; do mv -v $file $dst; done
            
            else
                echo "Error: Not correct answer provided."
                exit 1
            fi
        
        else
            echo "Error: Not correct answer provided."
            exit 1
        fi

    else
        echo "Moving files with only $ext extension to $dst."
        # Loop through specific files in the src and move them to dst:
        for file in "$src/*.$ext"; do mv  -v $file $dst; done
    fi
}

function move () {
    # Check that all the commandline arguments are passed:
    if [ ! $length == 3 ]; then
        echo "Error: There are not 3 obligatory commandline arguments: [initial directory name] [destination directory name or new destination directory name] [file extension or all]."

    # Check that src and dst directories exist:
    elif [ -d $src ] && [ -d $dst ]; then
        echo "Attention: 3 commandline arguments [from_directory_name: $src] [to_directory_name: $dst] [file_extension or all: $ext] correctly introduced."

        #Call cond_f_and_d function to move files.
        _move

    # If destination directory not found, then:    
    elif [ -d $src ] && [ ! -d $dst ]; then
        echo "Attention: 3 commandline arguments [from_directory_name: $src] [to_directory_name: $dst] [file_extension or all: $ext] correctly introduced, but the destination directory $dst was not found."
        echo "Question: Would you like to create a directory named $dst? y: for yes or n: for other alternatives."
        read response2

        if [ $response2 == "y" ]; then 
            # Create the directory with the given name:
                mkdir $dst
                
                #Call cond_f_and_d function to move files:
                _move
        
        elif [ $response2 == "n" ]; then 
            # Store dst variable with the date:
            dst=$(date '+%Y-%m-%d-%H-%M')

            echo "Question: Would you like to create a directory named $dst? y/n"
            read response3

            if [ $response3 == "y" ]; then 
                # Create the directory with the given name:
                mkdir $dst
                
                #Call cond_f_and_d function to move files:
                _move

            else
                echo "Error: Not possible to create a destination directory."
                exit 1
            fi
        
        else
            echo "Error: Not correct answer provided."
            exit 1
        fi

    else
        echo "Error: Directory $src does not exist or unspected error. Try again."
        exit 1
    fi
}

move
